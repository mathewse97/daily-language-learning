# LOGBOOK — estado vivo do curso

> **Este arquivo é a fonte da verdade do progresso.** Antes de publicar qualquer coisa,
> leia-o e confirme em que lição o sistema está (invariante 1).
>
> Reescrito no lugar, nunca acrescido. Máximo 60 linhas dentro do bloco de dados.
> A artifact *Acharnae Logbook* é um espelho derivado deste arquivo, mantido para
> leitura no telefone. Em caso de divergência, **este arquivo vence**.
>
> **Nunca invente progresso.** Se um campo não for conhecido, escreva `—`.

Campos e contrato em `STATE_SCHEMA.md`.

```
UPDATED: 2026-10-10
DAY: 34
STREAK: 0
LAST_REPORT: 2026-10-04 GR3 IT2 EN3
probed: —

[GREEK]
phase: 1
lesson: 17 — semana 5, dia 6/7 (texto novo, cresce 3 → 13 frases)
apoio: por FORMA desde 04/10 — forma nova de palavra conhecida volta a ter glosa
  ([GR-FORMA] no léxico); exp do lema governa só o teste. Nota de forma, curiosidade
  e "Quem é quem" no cartão (RULES 14)
setting: Ἀχαρναί, primavera de 432 a.C.
words: 72 — 4 palavras novas na semana 5 (ὁ πατήρ, ἡ μήτηρ, τὸ τέκνον, δύο)
unlocked: presente ativo 3sg/3pl (-ουσι(ν) explicado em nota de forma na semana 5);
  artigo; 1ª/2ª decl. nom./ac.; ἐν+dat. como bloco; πατήρ/μήτηρ só nom., como bloco
cast: Κλεισθένης, Μέλιττα, Νικίας, Χλόη, Δᾶος, Σῖμος, Ἄργος
recent: Argos brinca no campo com Nícias e Cloé (semana 4); a casa come pão e vinho
  (semana 4); a família apresentada por inteiro, e Cloé leva a oferenda ao altar (sem. 5)
weak: formas novas de palavras conhecidas (χαίρουσιν, καλή) — agora com apoio e nota;
  portão de fase ainda não confirmado — sem registro de 3 leituras seguidas ≥3/4
gate: 3 leituras seguidas com ≥3/4 de compreensão
next: semana 6 — o sacrifício e o mito de Prometeu em Mecone (anunciado na curiosidade
  de sábado), ritmo mantido (nota 3); tecer ὁ οἶνος, ἀγαθός e λέγει, que ficaram de fora

[ITALIAN]
phase: 1
lesson: 9 — semana 5, mais lenta (nota 2): Colosseo (seg) / Torre di Pisa (qua) /
  Fontana di Trevi e Acqua Vergine (sex)
unlocked: artigos; preposições articuladas (nel/dal/sul/del/al); avere (fame/sete/calor);
  di vs da começando a aparecer nos textos
recent: mercado de Testaccio em Roma; o caffè sospeso napolitano; o vaporetto veneziano.
weak: vocabulário e interesse (nota 2 na semana 4) — textos ~85 palavras, glosa generosa,
  monumentos com história; nenhuma estrutura nova
gate: artigos + preposições articuladas sem erro em 2 produções
next: com nota ≥3, essere/avere completo e presente dos 3 grupos (adiados pela nota 2)

[ENGLISH]
register_last: public writing
lesson: 10 — semana 5: decisão explicada ao cliente (ter) / crítica no Slack (qui) /
  problema no estudo de caso (sáb)
topics_done: hierarquia visual; API de componente; acessibilidade; escaneabilidade;
  handoff; estudo de caso; pricing e scoping; design tokens; teste de usabilidade;
  rationale ao cliente; crítica assíncrona; problema no estudo de caso
collocations: 46
weak: —
next: novo tópico async ou client-facing; seguir rotação client/async/public

[SISTEMA]
(sem campos — planner_enabled e planner_must_return_by eram do arranjo de tarefa
agendada anterior e não se aplicam mais; ver "Pendências registradas")
```

## Pendências registradas

**04/10 · check-in da semana 4 consumido.** Notas GR 3 · IT 2 · EN 3. Misses não
anotados — Mathews não sabia o que eram; a explicação entrou em `OPERATIONS.md` e no
cartão de domingo. Regra conservadora aplicada às promoções (ver `state/lexicon.md`).
Italiano desacelerado pela nota 2. `UPDATED` e `DAY` não foram tocados: são do entregador,
e a entrega de domingo, 04/10, ainda não tinha rodado quando esta rodada foi escrita.

**04/10 · divergência relatada, não corrigida: `daily.py` não confere a data da semana.**
`OPERATIONS.md` e `TASK_PROMPTS.md` dizem que, sem semana nova, o script falha. Ele procura
o dia só pelo dia da semana (`d`), não pelo intervalo `range`; com um pacote velho, a
segunda-feira republicaria a segunda da semana anterior em silêncio. Corrigir é decisão
de Mathews, em conversa (invariante 6).

**04/10 · auditoria mensal (primeiro domingo de outubro).** Só as semanas 3 e 4 estão no
repositório em formato de dados; as semanas 1 e 2 não foram auditadas. Dois erros, nas
notas de som, publicados como correção no cartão de segunda da semana 5.

**27/09 · campos obsoletos de `[SISTEMA]` removidos.** `planner_enabled: NÃO` e
`planner_must_return_by: 2026-09-27` vinham do arranjo em que o planejamento era tarefa
agendada. Desde 22/09 o planejamento é ritual de domingo em conversa (ver
`TASK_PROMPTS.md`), então esses dois campos não significam mais nada — não há "tarefa"
para (des)ativar. Removidos nesta rodada, por instrução de Mathews.

**27/09 · `probed` de 13/09 e da semana 3 inteira, consumidos.** Dois problemas
somados: (1) os cinco itens testados em 13/09 (ὁρᾷ, χαίρει, ὁ οἶνος, φέρει, ἔχει) tinham
ficado pendentes desde 21/09; (2) o campo `probed` do Logbook só guarda um dia, e como
sábado e domingo da semana 3 não têm Ἀνάμνησις, o valor ficou `—` antes de este
planejador rodar — outra instância do defeito E4 do `AUDIT.md`, desta vez apagando a
semana inteira, não só um dia. Como os dados da semana 3 continuam em `state/week.json`
(cada dia publicado carrega seu próprio `recall.probed`), reconstruí o conjunto a partir
de lá em vez de inventar: φέρει, ὁρᾷ, καλός, ὁ καρπός, χαίρει, τὸ δῶρον, ἔχει, λέγει,
ὁ οἶνος, καί — união dos `probed` de segunda a sexta da semana 3 com os cinco de 13/09.
Mathews confirmou nenhum miss nesta semana, então todos os dez foram promovidos para
`recalled`, caixa 2, due 2026-09-30 (ver `state/lexicon.md`). Isto não corrige E4, que
continua aberto; só evita perder mais um ciclo de teste.

**27/09 · semana 2 / semana 3, confirmado.** A semana 2 não foi estudada e sua matéria
foi refeita na semana 3, como já registrado; a semana 4 (composta agora) é matéria nova,
mantendo o formato de texto que cresce. Nenhuma fase avançou: o portão de fase 1 (3
leituras seguidas com ≥3/4 de compreensão) não tem registro que o confirme — as notas de
check-in medem experiência geral, não uma leitura específica testada por compreensão.
