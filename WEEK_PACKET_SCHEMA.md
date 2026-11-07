# WEEK_PACKET_SCHEMA — o contrato dos dados da semana

`state/week.json` guarda um bloco JSON com a semana inteira. A página
*Morning Packet* é a renderização dele e não contém nenhum conteúdo que não esteja aqui.

Quem compõe escreve **dados**, nunca HTML de página. Só três campos aceitam marcação
inline, e só esta: `<b> <i> <em> <code> <a> <span class="gi">`.

## Topo

| Campo | O que é |
|---|---|
| `schema` | `acharnae-week/1`. Mudou a forma, sobe o número e este arquivo muda junto (ver o fim do arquivo) |
| `week`, `phase`, `range` | número da semana, fase do grego, intervalo ISO `início/fim` |
| `composed` | quando e como o pacote foi composto — útil quando não foi o planejador |
| `header` | `eyebrow`, `title`, `sub` — o cabeçalho da página |
| `stats` | 2 a 4 objetos `{dt, dd, small}` — a faixa de números |
| `foot` | linhas de rodapé, uma por parágrafo |

## `greek`

| Campo | O que é |
|---|---|
| `register` | `composto`, `adaptado` ou `autêntico` — invariante 9, obrigatório |
| `setting` | a linha de contexto da semana, se houver |
| `sentences` | **as frases da semana, na ordem, uma vez só** |
| `cast` | o elenco: pares `[nome, quem é]`, recolhido como "Quem é quem" em todo cartão |

Cada frase é uma lista de palavras; cada palavra é `[glosa, grego, transliteração]`.
A pontuação pertence ao grego da palavra que ela segue — `"οἰκεῖ."` — nunca a um
elemento próprio.

**Apoio de leitura.** Quando o `exp` **da forma** da palavra chegar a 5 (regra em
`LEXICON_SCHEMA.md`), quem compõe escreve `null` em glosa e transliteração:
`[null, "φέρει.", null]`. O renderizador esconde as
duas. A decisão é de quem compõe, que tem o Léxico à mão; o renderizador não decide nada.

**Por que as frases ficam num lugar só.** Cada dia declara apenas `upTo`: quantas das
frases ele lê. Segunda `upTo: 3`, terça `5`, e assim por diante até `13` no sábado e no
domingo. A invariante 11 — cada dia repete o anterior palavra por palavra — deixa de
depender de disciplina e passa a ser impossível de violar: não existe onde escrever uma
variação. As frases acrescentadas hoje são as que o renderizador marca como novas,
comparando com o `upTo` do dia anterior.

## `days`

Sete objetos, segunda primeiro: `d` (1–6 = segunda a sábado, 0 = domingo), `label`, `n`
(o dia do mês), e `cards`.

### Cartão de grego — `lang: "gr"`

Quatro partes, mais três acréscimos opcionais (invariante 14). Campos, nesta ordem de
renderização:

| Campo | Obrigatório | O que é |
|---|---|---|
| `min` | sim | duração estimada |
| `fix` | não | lista de correções da auditoria mensal — só no cartão de segunda |
| `setting` | não | uma frase, só quando o cenário não for dedutível |
| `recall` | não | `{prompts, key, probed}` — o Ἀνάμνησις |
| `upTo` | sim | quantas frases de `greek.sentences` este dia lê |
| `pt` | sim | o português corrido do texto **daquele dia** |
| `form` | não | a nota de forma: até três linhas, com a causa, só no dia em que uma forma nova aparece |
| `sound` | sim | a nota de som, sobre som presente no texto do dia |
| `curio` | não | a curiosidade: 2–3 linhas, só em dia com gancho, terminando com a fonte |

`recall.probed` nomeia os itens do Léxico que os prompts testam, exatamente como estão
escritos lá. É o que o entregador copia para `probed` no Logbook. Sem Ἀνάμνησις naquele
dia, o campo `recall` simplesmente não existe — não se escreve um vazio.

A tabela do alfabeto e a linha do check-in são do renderizador, não dos dados: aparecem
em todo cartão de grego sem que ninguém as escreva.

### Cartão de italiano — `lang: "it"`

`min`, `setting`, `recall` (`{prompts, key}`), `text`, `glosses` (pares
`[termo, glosa]`), `questions`, `note`, `produce`, `answers` (pares `[rótulo, texto]`),
`curio` (a curiosidade, em português, com fonte). Todos opcionais menos `min`;
o domingo usa só `min` e `text`.

### Cartão de inglês — `lang: "en"`

`tag` (o registro), `min`, `title`, `body` (um item por parágrafo), `inContext` (pares),
`check`, `sayit`, `answers`, `expression`.

### Cartão neutro — `lang: "tag"`

`label` e `body`. Serve para o check-in de domingo e para qualquer aviso.

## Card ao toque, áudio, fotos e mapas — campos opcionais (desde 01/11/2026)

Tudo abaixo é opcional: um pacote sem eles continua válido e a página só não oferece o
recurso. As mídias são **arquivos** em `docs/audio/` e `docs/media/`, citados por nome.

**`media.photos`** — as fotos da semana, uma vez cada: `{chave: {file, alt, expl, cred,
page?}}`. `file` está em `docs/media/`; `alt` descreve a imagem; `expl` diz **o que é o
objeto e por que está ali** (se for de outra época ou lugar, diz isso); `cred` é o crédito
com autor e licença; `page` é o link da página da foto. Foto sem `cred` e sem `expl` não
entra (invariante 23): o validador reprova.

**`greek.glossary`** — `{forma: [glosa, transliteração]}` de **toda** palavra do texto, até
as que já perderam o apoio (`null` nas frases). É o que o card ao toque mostra. O validador
reprova palavra sem apoio que falte aqui.
**`greek.notes`** — `{forma: [dica, ver mais]}`: a dica é uma linha em português simples;
"ver mais" abre só se o aluno pedir. Nunca repita a glosa na dica.
**`greek.family`** — `{forma: [palavra, explicação]}`: uma palavra que o aluno já conhece
ou do português que vem da mesma raiz, **com a fonte consultada** (invariante 23).
**`greek.photos`** — `{forma: chave}`: a foto que aparece no card daquela palavra.
**`greek.cast`** aceita um terceiro item por par — `fam`, `casa`, `fora` ou `mito` — que
agrupa o "Quem é quem".
**`audio.greek`** — `{file, sent, t, words}`: a faixa com as frases do texto, `sent` os
tempos `[início, fim]` de cada frase, `t` o início de cada palavra (uma lista por frase) e
`words` os arquivos das palavras soltas. Gerado por `tools/audio.py`.

**No cartão de italiano e de inglês:**
`audio` — `{file, t}`: a faixa do texto e o início de cada palavra (o texto separado por
espaços, na ordem). Com áudio ou `tap`, o texto é **puro, sem HTML**.
`tap` — o que abre ao tocar: `w` `{palavra: [português, nota]}` (a nota pode ser `""`),
`p` `{"expressão ou nome inteiro": [português, nota, chave de foto?]}` — tocar em qualquer
palavra dela abre o mesmo card — e `f` `{palavra: chave de foto}`. **Toda palavra do texto precisa de glosa** (em `w`, ou dentro de uma `p`): o aluno toca
em qualquer uma e o validador reprova a que faltar. Palavras comuns levam nota `""`. Com `tap`, a lista de
glosas do cartão (italiano) e o "In context" (inglês) saem da página: o card os substitui.
Como no resto do pacote, número em algarismos vem seguido do extenso.

**No cartão de grego e no de italiano — `viz`**: lista de mapas e linhas do tempo, **dados,
não desenho** (`viz.py` desenha). Mapa: `{kind: "map", base: "atica"|"italia", title, cap,
points: [{n, lat, lon, hl?, dx?, dy?, a?}], route?, hills?, labels?}`. Linha do tempo:
`{kind: "timeline", title, cap, scale?: [de, até], items: [{yr|x, y, t, lvl?, hl?}]}`.
Sem `scale` a linha só mostra a ordem e cada item traz `x` de 0 a 1.

## Verificação antes de publicar

1. O JSON abre (`json.load`) — um pacote que não abre deixa a página em branco.
2. Há 7 dias, `d` de 1 a 6 mais 0.
3. `upTo` nunca diminui de segunda a sábado.
4. Todo `pt` corresponde às frases até o `upTo` daquele dia.
5. Todo cartão de grego tem `sound`; todo `register` está preenchido.
6. `form` é curta; `curio` termina com a fonte; `fix` só na segunda.
7. No italiano, todo número em algarismos é seguido do extenso entre parênteses.
8. Toda mídia citada existe em `docs/` e toda foto tem `cred` e `expl`.
9. Toda palavra sem apoio tem entrada em `greek.glossary` (se ele existir).

Campos novos e opcionais não mudam o número do `schema`: um pacote antigo continua
válido. O número sobe quando um campo muda de sentido ou passa a ser obrigatório.
