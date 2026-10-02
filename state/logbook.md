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
UPDATED: 2026-10-02
DAY: 26
STREAK: 0
LAST_REPORT: 2026-09-27 GR3 IT3 EN3
probed: πονεῖ, ὁ ἀγρός

[GREEK]
phase: 1
lesson: 16 — semana 4, dia 5/7 (texto novo, cresce 3 → 13 frases)
apoio: decaindo por palavra — vários itens já sem glosa (exp ≥5: ἔχει, φέρει, ὁρᾷ,
  χαίρει, λέγει, καλός, ὁ οἶνος, τὸ δῶρον, ὁ καρπός, ὁ βωμός, ὁ ἀγρός, πρός, μικρός,
  ἀγαθός, καί, ἐν τῷ ἀγρῷ, ἐν Ἀχαρναῖς, Κλεισθένης, Μέλιττα, Δᾶος); as 3 palavras novas
  da semana 4 (παίζει, ὁ ἄρτος, ἐσθίει) levam apoio completo
setting: Ἀχαρναί, primavera de 432 a.C.
words: 68 — 3 palavras novas na semana 4 (παίζει, ὁ ἄρτος, ἐσθίει)
unlocked: presente ativo 3sg/3pl (3pl usado pela primeira vez na semana 4, χαίρουσιν);
  artigo; 1ª/2ª decl. nom./ac.; ἐν+dat. como bloco
cast: Κλεισθένης, Μέλιττα, Νικίας, Χλόη, Δᾶος, Σῖμος, Ἄργος
recent: a família celebrou a oferenda e o vinho (semana 3); Argos brinca no campo com
  Nícias e Cloé (semana 4); a casa come pão e vinho e Daos permanece em casa (semana 4)
weak: portão de fase ainda não confirmado — sem registro de 3 leituras seguidas ≥3/4
gate: 3 leituras seguidas com ≥3/4 de compreensão
next: semana 5 continua o texto da semana 4, tecendo os itens vencidos (due 2026-09-30)
  e mantendo o ritmo (nota 3)

[ITALIAN]
phase: 1
lesson: 8 — semana 4: mercato di Testaccio, Roma (seg) / caffè sospeso, Napoli (qua) /
  vaporetto, Venezia (sex)
unlocked: artigos; preposições articuladas (nel/dal/sul/del/al); avere (fame/sete/calor);
  di vs da começando a aparecer nos textos
recent: mercado de Testaccio em Roma; o caffè sospeso napolitano; o vaporetto veneziano.
weak: —
gate: artigos + preposições articuladas sem erro em 2 produções
next: essere/avere completo; presente dos 3 grupos

[ENGLISH]
register_last: public writing
lesson: 9 — semana 4: pricing e scoping (ter) / design tokens (qui) / teste de
  usabilidade (sáb)
topics_done: hierarquia visual; API de componente; acessibilidade; escaneabilidade;
  handoff; estudo de caso; pricing e scoping; design tokens; teste de usabilidade
collocations: 30
weak: —
next: novo tópico async ou client-facing; seguir rotação client/async/public

[SISTEMA]
(sem campos — planner_enabled e planner_must_return_by eram do arranjo de tarefa
agendada anterior e não se aplicam mais; ver "Pendências registradas")
```

## Pendências registradas

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
