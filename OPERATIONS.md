# OPERATIONS — como o sistema roda

Referência para o Mathews. Um agente que vai escrever aqui deve ler `AGENTS.md` e
`RULES.md`; este arquivo é sobre operar, não sobre compor.

## Onde cada coisa vive

| O quê | Onde | Quem escreve |
|---|---|---|
| Posição do curso | `state/logbook.md` | `daily.py`, e o planejador aos domingos |
| Vocabulário e revisão | `state/lexicon.md` | só o planejador |
| Conteúdo da semana | `state/week.json` | o planejador |
| Notas semanais | `state/checkin_log.md` | o planejador, ao consumir |
| Invariantes | `RULES.md` | Mathews, em conversa |
| Procedimentos | `TASK_PROMPTS.md` | Mathews, em conversa |
| Currículos | `courses/` | em conversa |
| Renderizador | `page/template.html` | em conversa, com commit próprio |
| A página publicada | `docs/index.html` | **ninguém** — é gerada |
<!-- MÓDULO:FALA início -->
| Registro das sessões de fala | `speaking/log.md` | Mathews, aos domingos |
<!-- MÓDULO:FALA fim -->

## A semana, na prática

**Segunda a sábado** você não faz nada. Por volta das 04:40 o GitHub roda `daily.py`,
que atualiza o estado, regera a página e commita. O Pages republica sozinho. Você abre a
mesma URL de sempre e a lição de hoje está lá.

**Domingo** é o único dia com trabalho seu: abrir uma sessão com um agente, dar as três
notas do check-in e deixar ele compor a semana seguinte. O procedimento está em
`TASK_PROMPTS.md`. Sem esse ritual, a semana seguinte não existe — e na segunda o
`daily.py` falha em vez de inventar um dia, o que é o comportamento certo.

## O check-in

Três notas de 1 a 5, uma por trilha, mais as palavras que não vieram. A escala é de
experiência, não de diagnóstico — você não precisa saber qual regra falhou:

| | |
|---|---|
| **1** | não consegui acompanhar |
| **2** | acompanhei com esforço e releitura |
| **3** | acompanhei, sem margem |
| **4** | compreendi sem esforço |
| **5** | fácil demais — pode acelerar |

Elas entram pela conversa de domingo e o agente grava a linha em
`state/checkin_log.md`. Não há formulário: o site é estático e não tem para onde salvar,
e uma máquina para isso só serviria nos domingos em que a semana também não seria
composta.

Semana sem check-in não quebra nada. O planejador mantém o ritmo e a regra conservadora
impede que vocabulário suba sem ter sido testado.

## Quando alguma coisa parecer errada

**A página está com o dia errado, ou desatualizada.** Vá na aba **Actions** do
repositório e veja a última execução de *Morning Packet*. Verde e sem mudanças significa
que o dia de hoje já estava publicado. Vermelha, abra e leia — a mensagem de erro do
`validate.py` diz qual invariante quebrou, em português.

**A página está com uma tarja laranja.** O JSON da semana está quebrado. O conteúdo não
se perdeu: está em `state/week.json` e no histórico do Git. Peça a correção numa conversa.

**A semana não foi composta.** O `daily.py` falha e não altera nada. Rode o planejador
assim que puder; o dia perdido não volta, mas nada foi corrompido.

**Você quer rodar a entrega na mão.** Actions → *Morning Packet* → **Run workflow**.
Funciona a qualquer hora e é inofensivo: se nada mudou, ele não commita.

## Formas de falha já observadas

**Uma execução marcou sucesso e pulou o passo principal** (13/09). Hoje isso não passa:
`validate.py` roda antes e depois, e o CI reprova se `docs/` não corresponder aos dados.

**Uma publicação manual sobrescreveu o progresso real** (13/09). Hoje a página é gerada;
editá-la à mão não corrompe dado nenhum, e o build desfaz.

**Uma execução reescreveu o próprio agendamento** (16/09). Hoje o token do workflow não
tem permissão para isso.

**`probed` pode ser perdido antes de ser consumido.** O campo guarda um dia; o consumo é
semanal. Se o planejador ficar mais de uma semana parado, os testes daquele período se
perdem. Continua aberto — item E4 do `AUDIT.md`.

<!-- MÓDULO:FALA início -->
## Se a trilha de fala parar

Não quebra nada: o módulo de fala não é lido por nenhum script e não entra na entrega
diária. Semana sem linha em `speaking/log.md` é só semana sem prática.

O que **não** se faz é deixá-lo apodrecendo. Se forem menos de doze sessões em seis
semanas, o critério de abandono foi atingido — `speaking/SPEAKING.md` tem o procedimento
de remoção, e ele leva dois minutos.
<!-- MÓDULO:FALA fim -->

## Os dois detalhes chatos do GitHub

**O horário é aproximado.** Workflows agendados entram numa fila e atrasam, às vezes
bastante. Por isso o agendamento é 04:40: com folga antes das 5h, e fora do minuto cheio.

**Workflows agendados são desativados após 60 dias sem atividade no repositório.** Com o
commit diário isso não dispara, mas se o curso parar por dois meses a automação não volta
sozinha: é preciso reativá-la na aba Actions.
