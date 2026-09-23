# WEEK_PACKET_SCHEMA — o contrato dos dados da semana

`state/week.json` guarda um bloco JSON com a semana inteira. A página
*Morning Packet* é a renderização dele e não contém nenhum conteúdo que não esteja aqui.

Quem compõe escreve **dados**, nunca HTML de página. Só três campos aceitam marcação
inline, e só esta: `<b> <i> <em> <code> <a> <span class="gi">`.

## Topo

| Campo | O que é |
|---|---|
| `schema` | `acharnae-week/1`. Mudou a forma, sobe o número e este arquivo muda junto |
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

Cada frase é uma lista de palavras; cada palavra é `[glosa, grego, transliteração]`.
A pontuação pertence ao grego da palavra que ela segue — `"οἰκεῖ."` — nunca a um
elemento próprio.

**Apoio de leitura.** Quando o `exp` da palavra no Léxico chegar a 5, quem compõe escreve
`null` em glosa e transliteração: `[null, "φέρει.", null]`. O renderizador esconde as
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

Quatro partes e nada mais (invariante 13). Campos, nesta ordem de renderização:

| Campo | Obrigatório | O que é |
|---|---|---|
| `min` | sim | duração estimada |
| `setting` | não | uma frase, só quando o cenário não for dedutível |
| `recall` | não | `{prompts, key, probed}` — o Ἀνάμνησις |
| `upTo` | sim | quantas frases de `greek.sentences` este dia lê |
| `pt` | sim | o português corrido do texto **daquele dia** |
| `sound` | sim | a nota de som, sobre som presente no texto do dia |

`recall.probed` nomeia os itens do Léxico que os prompts testam, exatamente como estão
escritos lá. É o que o entregador copia para `probed` no Logbook. Sem Ἀνάμνησις naquele
dia, o campo `recall` simplesmente não existe — não se escreve um vazio.

A tabela do alfabeto e a linha do check-in são do renderizador, não dos dados: aparecem
em todo cartão de grego sem que ninguém as escreva.

### Cartão de italiano — `lang: "it"`

`min`, `setting`, `recall` (`{prompts, key}`), `text`, `glosses` (pares
`[termo, glosa]`), `questions`, `note`, `produce`, `answers` (pares `[rótulo, texto]`),
`compare`. Todos opcionais menos `min`; o domingo usa só `min` e `text`.

### Cartão de inglês — `lang: "en"`

`tag` (o registro), `min`, `title`, `body` (um item por parágrafo), `inContext` (pares),
`check`, `sayit`, `answers`, `compare`, `expression`.

### Cartão neutro — `lang: "tag"`

`label` e `body`. Serve para o check-in de domingo e para qualquer aviso.

## Verificação antes de publicar

1. O JSON abre (`json.load`) — um pacote que não abre deixa a página em branco.
2. Há 7 dias, `d` de 1 a 6 mais 0.
3. `upTo` nunca diminui de segunda a sábado.
4. Todo `pt` corresponde às frases até o `upTo` daquele dia.
5. Todo cartão de grego tem `sound`; todo `register` está preenchido.
