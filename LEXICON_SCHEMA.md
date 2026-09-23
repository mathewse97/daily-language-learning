# LEXICON_SCHEMA — como ler e escrever o Léxico

O Léxico é o bem mais valioso do sistema: o vocabulário acumulado com o estado de
revisão de cada item. Ele governa a composição do grego (inventário fechado) e a
repetição espaçada.

**Onde vive:** `state/lexicon.md`, no bloco de código. **Esse arquivo é a fonte.**
A artifact *Acharnae Lexicon* é um espelho derivado, para leitura no telefone; em
divergência, o arquivo vence. Quem escreve é o planejador, aos domingos, e só ele.

> Até 21/09/2026 a fonte era a artifact e o arquivo era um backup semanal
> (`state/lexicon.md`). Inverteu-se: o dado mora no arquivo, e a página é a
> renderização. O backup virou redirecionamento.

Este documento existe para que o Léxico seja legível sem a página: um agente que receba
só os arquivos precisa saber o que `seen | 1 | — | 0` significa.

## Vocabulário

**status** — o que se sabe sobre o item, nunca o que se leu.

| | |
|---|---|
| `seen` | introduzido, nunca testado |
| `recalled` | testado e recordado |
| `missed` | testado e não recordado |

**box** — a caixa de Leitner, que define o intervalo até a próxima revisão.

| caixa | intervalo |
|---|---|
| 1 | +1 dia |
| 2 | +3 dias |
| 3 | +7 dias |
| 4 | +21 dias |
| 5 | +60 dias |

**due** — data da próxima revisão. `—` quando o item nunca foi testado.

**exp** — quantas vezes o item já apareceu num texto publicado. Governa duas coisas e só
duas: abaixo de 5, a palavra leva glosa e transliteração no texto interlinear e **não
pode ser testada**; a partir de 5, perde as duas para sempre e passa a ser elegível para
recuperação. **`exp` nunca promove entre caixas** — essa é a distinção central do
sistema.

A contagem começou na semana 2 (17/09/2026). A semana 1 não tem registro e não é
reconstruída; itens que só apareceram nela ficam em 0. Quem mantém o campo é o
planejador, no passo 4a, somando as aparições da semana que acabou.

## Regras de movimentação

- **Aparecer num texto nunca promove.** Só um teste promove. Esta é a regra central: é
  fácil confundir exposição com aprendizado, e o sistema foi desenhado para não confundir.
- Só itens listados em `probed` no Logbook podem se mover, e só o planejador os move.
- Dos testados: nomeados em `misses` no check-in → `missed`, caixa 1. Não nomeados →
  `recalled`, caixa +1.
- São necessários **dois** `recalled` distintos antes de um item entrar na caixa 4.
- Sem check-in utilizável: só a caixa 1 avança para a 2; da 2 para cima, tudo segura.
- Trilha com nota 1–2 na semana: nada promove, e o quarto mais recente cai para a caixa 1.
- **Nunca se apaga um termo.** O Léxico é append-only; itens se movem entre caixas.
- Itens vencidos são **restrição de geração**: têm de aparecer tecidos nos textos da
  semana. A revisão chega como história, não como lista.

## Formato das linhas

O arquivo não tem uma forma única. Cada seção tem a sua, e é preciso declarar isso:

| Seção | Forma | O que é |
|---|---|---|
| `[GR]` | `termo \| glosa \| fase \| status \| caixa \| due \| exp` | vocabulário grego |
| `[GR-INTERROG]` | idem | interrogativas, semeadas antes do uso |
| `[GR-BLOCO]` | idem | expressões memorizadas inteiras, não analisadas na fase 1 |
| `[GR-NOM]` | idem | nomes próprios; a glosa carrega restrições de caso |
| `[IT-CORE]` | idem | vocabulário italiano (vazio até agora) |
| `[IT-FALSI]` | idem, sem `exp` | falsos amigos com o português |
| `[IT-INTERF]` | idem, sem `exp`; a glosa é `—` | interferências estruturais |
| `[EN-COLLOC]` | `frase \| registro \| entrega` | colocações profissionais em inglês |

`exp` só existe nas seções gregas. As seções italianas ficam sem ele de propósito: o
apoio de leitura interlinear, que é o que `exp` governa, não existe no italiano.

Em `[IT-INTERF]` o termo já é a descrição inteira, então a glosa é `—`. É a única seção
em que isso acontece.

## Inconsistências conhecidas

**1 · As seções italianas tinham um campo a menos do que o cabeçalho declara.**
— **RESOLVIDO em 22/09/2026, por decisão de Mathews.**
As linhas traziam `burro | manteiga (não asno) | 1 | 1 | —`: três valores onde o `FORMAT`
pede quatro. Duas leituras eram possíveis e nada no arquivo desempatava. Perguntado,
Mathews não tinha o registro e delegou a decisão. Adotada a leitura mais provável — o
campo ausente era `status` — e todas as linhas de `[IT-FALSI]` e `[IT-INTERF]` foram
normalizadas para a forma completa, com `status: seen`.

**Isto é uma decisão, não um dado recuperado.** Nenhum termo foi apagado e nenhuma caixa,
data ou fase foi alterada: só um campo ausente foi preenchido, com o valor que todo item
nunca testado tem. Se algum dia aparecer registro de que a leitura era outra, o conserto
é trocar uma coluna — os números originais estão preservados.

**2 · A coluna `data` de `[EN-COLLOC]` trazia datas futuras.**
— **RESOLVIDO em 22/09/2026, por evidência interna.** A coluna chama-se `entrega`.
As datas em questão eram 15, 17 e 19/09/2026 — terça, quinta e sábado, exatamente os dias
da trilha de inglês — e as entradas agrupam-se por registro em blocos que correspondem um
a um aos pacotes daquela semana: seis `client-facing` em 15/09, cinco `async team` em
17/09, quatro `public writing` em 19/09. Isso é a distribuição dos pacotes, não o rastro
de alguém encontrando expressões avulsas.

Consequência para a revisão: uma colocação cuja `entrega` ainda não passou **não foi
encontrada** e não pode ser tratada como conhecida nem entrar na fila de recuperação.

Mathews foi consultado e não tinha o registro; a conclusão é inferência apoiada no
próprio dado, e está marcada como tal.

**3 · A contagem de exposições não aparecia nas linhas.** — **RESOLVIDO em 17/09/2026.**
O campo `exp` foi acrescentado a todas as linhas gregas, com os valores apurados dos sete
textos da semana 2. O que resta de dívida é isso: os primeiros sete dias de exposição
estão perdidos, e nenhum número no arquivo os inclui.
