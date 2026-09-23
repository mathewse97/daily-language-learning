# PAGE_TEMPLATE — a página Morning Packet é um renderizador

A página TODAY **não guarda conteúdo**. Ela contém um bloco de dados e o código que o
transforma em interface. O conteúdo da semana vive em `state/week.json`;
o contrato dos campos está em `WEEK_PACKET_SCHEMA.md`.

Isso é o oposto do arranjo anterior, em que o pacote da semana era o próprio HTML: a
página era ao mesmo tempo dado de entrada e renderização de saída, e uma edição manual
descuidada apagava dados. Era o item B3 da auditoria, e a causa estrutural do incidente
de 13/09.

## A regra

**Publicar é rodar `build.py`.** Ele lê `state/week.json`, lê `page/template.html`,
troca o marcador `__WEEK_JSON__` pelos dados e escreve `docs/index.html`.

```
state/week.json  +  page/template.html  ──build.py──►  docs/index.html
```

`docs/index.html` é **derivado**. Não se edita, não se revisa, não se corrige ali. O
próximo build desfaz, e o CI reprova antes: há um passo no `validate.yml` que regera a
página e falha se o resultado for diferente do que está commitado.

`page/template.html` — `<style>`, fontes, o renderizador, a navegação por dia — é
**código**, não conteúdo. Nenhuma automação o reescreve. Se o desenho precisar mudar,
isso é uma decisão tomada em conversa, com commit próprio, separada de conteúdo.

Consequências que vale dizer por extenso:

- **Ninguém escreve HTML de lição.** Não há como uma execução inventar markup, cor ou
  classe: ela só produz dados. A invariante 4 deixa de depender de disciplina.
- **A tabela do alfabeto, a linha do check-in e os rótulos de seção são do
  renderizador.** Não aparecem nos dados e não podem faltar num dia.
- **Se o JSON não abrir, a página diz isso** em vez de aparecer em branco, e aponta o
  arquivo-fonte. Um pacote quebrado é visível, não silencioso.
- A página nunca é reduzida a um único dia: os sete estão sempre lá, e o script abre o de
  hoje pelo `getDay()` do navegador.

## Vocabulário de classes

Para quem for mexer no renderizador — não para quem compõe.

| Classe | Uso |
|---|---|
| `.ph` | cabeçalho: `.eyebrow` → `h1` → `.sub` |
| `dl.stats` | faixa de números: `dt` rótulo mono, `dd` número em serifa |
| `nav.days` | pílulas de dia; `data-d` é 1–6 = segunda a sábado, 0 = domingo |
| `section.day` | um dia; `hidden` em todos menos o visível |
| `article.card` | um bloco de língua |
| `.b.gr` `.b.it` `.b.en` | etiqueta da língua |
| `.b.tag` | etiqueta neutra: registro, `composto`, `adaptado`, `autêntico` |
| `.min` | duração, alinhada à direita |
| `.setting` | a linha de contexto |
| `.il` + `.w` (`.pt` `.gr` `.tr`) | o texto interlinear, uma pilha por palavra |
| `.w.known` | palavra com `exp` ≥ 5: glosa e transliteração escondidas |
| `.w.new` | palavra de uma frase acrescentada hoje |
| `.br` | quebra entre frases |
| `.rec` | o Ἀνάμνησις / Ripasso |
| `.ita` `.eng` | texto italiano e inglês |
| `.glosses` | glosas: `<b>` termo — texto |
| `.sound` | a nota de pronúncia |
| `.note` | a observação (italiano) |
| `.sect` | rótulo de subseção |
| `details` + `.dz` | chave, português corrido, alfabeto, gabarito — recolhidos |
| `.ans` | respostas: `<i>` rótulo · conteúdo |
| `.letters` | a tabela do alfabeto |
| `.err` | a mensagem de pacote ilegível |

## Marcação inline nos dados

Os campos de texto aceitam, e só, `<b> <i> <em> <code> <a> <span class="gi">`. Tudo o
mais é escapado. `.gi` é grego dentro de texto português.

## Tema

Escuro por padrão. O claro existe apenas em `:root[data-theme="light"]` e só aparece se o
leitor escolher. Nunca inverta isso: a página é lida às 5h da manhã.
