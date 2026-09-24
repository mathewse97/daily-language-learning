# Daily Language Learning

Sistema de estudo diário em três trilhas — grego antigo, italiano e inglês profissional.
Todo dia de manhã uma página é regerada com a lição do dia; todo domingo a semana
seguinte é composta.

**Este é o documento que se lê primeiro.** Ele diz o que existe, o que manda em quê, e
como levar tudo embora.

## Como funciona, em cinco linhas

Um agricultor chamado Κλεισθένης mora em Acarnas, na primavera de 432 a.C. A cada dia o
aluno lê um texto em grego que cresce dentro da semana, mais uma trilha de italiano ou
inglês. O vocabulário grego é um inventário fechado: nada entra num texto que não esteja
no Léxico. A revisão é espaçada e só promove uma palavra que tenha sido efetivamente
testada — aparecer num texto nunca conta. Aos domingos o aluno dá três notas, e o
planejador ajusta o ritmo a partir delas.

## A arquitetura, em uma frase

**Tudo mora nos arquivos; a página lê os arquivos e os traduz em interface.**

```
state/week.json ──► build.py ──► docs/index.html ──► GitHub Pages ──► o telefone
```

`state/week.json` é o conteúdo da semana. `page/template.html` é o renderizador: estilo,
fontes e o código que desenha os cartões, com um `__WEEK_JSON__` onde os dados entram.
`build.py` junta os dois. **`docs/index.html` é gerado e nunca editado à mão** — se
alguém editar, o próximo build desfaz e o CI reprova antes.

O mesmo vale para o resto: estado, léxico e check-ins são arquivos de texto. Não existe
nenhum dado deste sistema que viva só numa tela.

## Quem faz o quê

| | Quando | O que é | Precisa de modelo |
|---|---|---|---|
| **Entrega diária** | todo dia, ~04:40 | `daily.py`, rodado pelo GitHub Actions | não |
| **Planejamento semanal** | domingo | conversa com um agente, seguindo `TASK_PROMPTS.md` | sim, sempre |

A entrega diária é determinística: escolhe o dia de hoje no pacote, atualiza o estado,
regera a página, commita. Seis dias por semana o sistema anda sem nenhum modelo.

O planejamento não é automatizável e não se finge que é: compor grego dentro de um
inventário fechado, conferir acentuação politônica, verificar fato histórico e decidir
promoção de caixa exigem julgamento. É um ritual de domingo, com um agente, numa conversa
— e é nessa conversa que o check-in também entra.

## Ordem de leitura

1. Este README
2. `AGENTS.md` — o essencial para um agente que vai escrever aqui
3. `RULES.md` — as 25 invariantes
4. `OPERATIONS.md` — onde cada coisa vive e o que fazer quando algo falha
5. `TASK_PROMPTS.md` — os dois procedimentos
6. `WEEK_PACKET_SCHEMA.md` — a forma dos dados de uma semana
7. `courses/GREEK_COURSE.md` · `courses/ITALIAN_COURSE.md` · `courses/ENGLISH_COURSE.md`
8. `STATE_SCHEMA.md` · `LEXICON_SCHEMA.md` · `PAGE_TEMPLATE.md`
9. `AUDIT.md` — defeitos conhecidos, ainda abertos
10. `SETUP.md` · `MIGRATION.md` — como isto foi ligado, e como se desliga
<!-- MÓDULO:FALA início -->
11. `speaking/SPEAKING.md` — o módulo de fala, opcional e removível
<!-- MÓDULO:FALA fim -->

## Manifesto

Fonte = alguém escreve nele deliberadamente. Derivado = é regerado a partir de outra
coisa e pode ser apagado sem perda.

| Material | O que guarda | Fonte/derivado | Na entrega |
|---|---|---|---|
| `README.md` | este documento, com o manifesto | fonte | sim |
| `AGENTS.md` | o briefing de entrada para agentes | fonte | sim |
| `RULES.md` | as 25 invariantes | fonte | sim |
| `OPERATIONS.md` | operação e formas de falha | fonte | sim |
| `SETUP.md` | como o repositório foi ligado, passo a passo | fonte | sim |
| `MIGRATION.md` | como sair do GitHub sem perder nada | fonte | sim |
| `TASK_PROMPTS.md` | os dois procedimentos | fonte | sim |
| `PAGE_TEMPLATE.md` | o contrato do renderizador | fonte | sim |
| `WEEK_PACKET_SCHEMA.md` | a forma dos dados da semana | fonte | sim |
| `STATE_SCHEMA.md` | os campos do Logbook | fonte | sim |
| `LEXICON_SCHEMA.md` | os campos do Léxico | fonte | sim |
| `AUDIT.md` | defeitos, abertos e fechados | fonte | sim |
| `courses/GREEK_COURSE.md` | método, fases, semente, exatidão | fonte | sim |
| `courses/ITALIAN_COURSE.md` | método e fases do italiano | fonte | sim |
| `courses/ENGLISH_COURSE.md` | rotação de registros e temas | fonte | sim |
| `state/logbook.md` | **a posição do curso** | fonte | sim — sem ele não se sabe onde parou |
| `state/lexicon.md` | **o vocabulário com estado de revisão** | fonte | sim — é o bem mais valioso |
| `state/week.json` | o conteúdo da semana em curso | fonte | sim |
| `state/checkin_log.md` | histórico das notas semanais | fonte | sim |
| `page/template.html` | o renderizador | fonte | sim |
| `build.py` | gera a página a partir dos dados | fonte | sim |
| `validate.py` | confere as invariantes verificáveis | fonte | sim |
| `daily.py` | a entrega diária | fonte | sim |
| `docs/index.html` | a página publicada | **derivado** de `state/week.json` | não · regerar |
| `.github/workflows/` | agendamento e CI | fonte, mas específico do GitHub | sim, como referência |
<!-- MÓDULO:FALA início -->
| `speaking/SPEAKING.md` | o módulo de fala: razão, evidência, dose, remoção | fonte · **módulo removível** | sim |
| `speaking/conversa.md` | o prompt das sessões de conversa | fonte · **módulo removível** | sim |
| `speaking/entrevista.md` | o simulador de entrevista e seu rodízio | fonte · **módulo removível** | sim |
| `speaking/log.md` | registro das sessões de fala | fonte · **módulo removível** | sim |
<!-- MÓDULO:FALA fim -->

`docs/` e `.github/` ficam fora da conferência automática do manifesto: o primeiro é
gerado, o segundo é o andaime da plataforma.

<!-- MÓDULO:FALA início -->
As quatro últimas linhas pertencem a um **módulo opcional**. O sistema de leitura roda
inteiro sem elas. `speaking/SPEAKING.md` explica o que é e traz o procedimento exato de
remoção; apagar a pasta não quebra a validação.
<!-- MÓDULO:FALA fim -->

## Estado atual

Não está neste arquivo de propósito — estaria velho em um dia. A posição real vive em
`state/logbook.md`.

## Limitações conhecidas

**O validador confere estrutura, não conteúdo.** Ele garante que há sete dias, que o
texto nunca encolhe, que nada com menos de cinco encontros é testado e que o manifesto
não mente. Ele não sabe se o português corresponde ao grego, nem confere acentuação,
aspecto ou fato histórico. Isso continua sendo de quem compõe.

**O GitHub Pages é público.** Sites com controle de acesso só existem no GitHub
Enterprise Cloud. O repositório pode ser privado — e então o léxico, o estado e os
currículos são só seus — mas a página publicada é aberta a quem tiver o endereço.

**Workflows agendados atrasam e são desativados após 60 dias sem atividade no
repositório.** O horário de 04:40 é aproximado. E se o curso parar por dois meses, a
automação não volta sozinha: é preciso reativá-la na aba Actions.

**Não existe caminho de volta definido.** `MIGRATION.md` diz como sair do GitHub; sair é
sair, não sincronizar.
