# STATE_SCHEMA — como ler e escrever o Logbook

O Logbook (`state/logbook.md`) guarda a posição do curso: em que lição, em que
fase, com que apoio, o que foi testado e o que ainda não foi consumido. É o arquivo que
responde "onde o sistema parou" quando tudo o mais falha.

**Contrato.** Só valores, uma linha por campo. Sem prosa e sem histórico dentro do bloco
de dados — a prosa vai abaixo dele, em "Pendências registradas". Máximo 60 linhas de
dados. Reescrito no lugar, nunca acrescido.

## Campos globais

| Campo | O que é |
|---|---|
| `UPDATED` | data da última escrita, ISO |
| `DAY` | dia corrido desde o início do curso |
| `STREAK` | dias seguidos com lição lida; `0` quando quebrou |
| `LAST_REPORT` | data e três notas do último check-in **já consumido** pelo planejador |
| `probed` | os itens do Léxico que o Ἀνάμνησις de hoje testou, separados por vírgula; `—` quando não houve |

**`probed` é a única ponte entre o que foi testado e o que pode ser promovido.** O
entregador escreve; o planejador consome e limpa. Se for sobrescrito antes de consumido,
o teste daquele dia se perde — foi o que aconteceu em 13/09 e está registrado no próprio
Logbook.

## Blocos por trilha

`[GREEK]`, `[ITALIAN]`, `[ENGLISH]`. Campos comuns:

| Campo | O que é |
|---|---|
| `phase` | fase do currículo daquela trilha |
| `lesson` | número da lição e onde ela está na semana |
| `unlocked` | o que já foi liberado gramaticalmente |
| `recent` | no máximo os três últimos episódios, uma oração cada |
| `weak` | no máximo três pontos fracos ativos; o quarto empurra o mais antigo |
| `gate` | a condição de passagem para a fase seguinte, dita por extenso |
| `next` | o que vem a seguir, em uma linha |

Só no grego: `apoio` (o estágio do apoio interlinear em vigor — decai por palavra pelo
`exp` do Léxico, nunca por calendário), `setting`, `words`, `cast`.
Só no inglês: `register_last`, `topics_done`, `collocations`.

## Bloco `[SISTEMA]`

Estado operacional que não é de nenhuma trilha: se o planejador está ativo, até quando,
e qualquer coisa que uma execução precise saber antes de agir. Campos livres, uma linha
cada, sempre com data quando forem temporários.

## Regras

- **Nunca invente progresso.** Campo desconhecido é `—`.
- Se o arquivo estiver vazio ou inacessível, diga isso no topo do pacote e continue da
  última fase conhecida, dizendo qual é.
- A artifact *Acharnae Logbook* é espelho derivado. Escreva no arquivo primeiro; a
  artifact depois. Em divergência, o arquivo vence.
