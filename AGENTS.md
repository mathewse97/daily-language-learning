# AGENTS.md — leia isto antes de mexer em qualquer coisa

Você é um agente trabalhando neste repositório. Ele é um sistema de estudo diário que
roda há semanas e tem estado real dentro dele. Não é um projeto novo.

## As três regras que, quebradas, estragam o sistema

**1 · Os dados moram nos arquivos. A página é derivada.**
O conteúdo da semana é `state/week.json`. A página `docs/index.html` é **gerada** por
`build.py` e nunca editada à mão. Se você editar a página, o próximo build apaga o que
você fez — e a validação no CI vai reprovar antes disso.

**2 · Exposição não é aprendizado.**
Uma palavra aparecer num texto **nunca** a promove na revisão espaçada. Só promove um
teste que o aluno não reportou como falho. São duas contagens separadas (`exp` e `box`)
e confundi-las corrompe o sistema inteiro.

**3 · Você não modifica o que te executa.**
Não altere `.github/workflows/`, não reescreva `RULES.md` nem este arquivo por iniciativa
própria, não mude o agendamento. Se notar divergência entre as regras e o que os arquivos
fazem, **relate** e não conserte sozinho. Reconciliar é decisão do Mathews, tomada em
conversa. Esta regra existe porque foi quebrada: uma execução já reescreveu o próprio
agendamento.

## Antes de escrever

Leia `RULES.md` inteiro — são 25 invariantes e elas são o contrato. Depois leia
`state/logbook.md`, que diz onde o curso parou. **Nunca invente progresso:** campo
desconhecido é `—`.

Para compor uma semana, leia também `WEEK_PACKET_SCHEMA.md` e o currículo da trilha em
`courses/`. Você escreve JSON, nunca HTML de lição.

## Antes de commitar

```
python3 validate.py     # tem de passar
python3 build.py        # regera docs/index.html
```

Commite `state/` e `docs/` juntos. Uma mudança em `state/week.json` sem o build
correspondente reprova no CI.

## O que o validador não pega

Ele confere estrutura, não conteúdo: não sabe se o português corresponde ao grego, não
confere acentuação, aumento, aspecto ou concordância, e não verifica fato histórico.
Isso continua sendo seu, e `courses/GREEK_COURSE.md` diz como.

## Ordem de leitura completa

`README.md` → `RULES.md` → `OPERATIONS.md` → `TASK_PROMPTS.md` →
`WEEK_PACKET_SCHEMA.md` → `courses/` → `STATE_SCHEMA.md` e `LEXICON_SCHEMA.md` →
`state/logbook.md` → `AUDIT.md`.
