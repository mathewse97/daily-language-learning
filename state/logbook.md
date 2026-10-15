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
UPDATED: 2026-10-15
DAY: 39
STREAK: 0
LAST_REPORT: 2026-10-11 GR3 IT3 EN2
probed: ἐν τῷ ἀγρῷ, πρός (+ac), πονεῖ

[GREEK]
phase: 1
lesson: 18 — semana 6, dia 4/7 (texto novo, cresce 3 → 13 frases)
apoio: por FORMA desde 04/10 — forma nova de palavra conhecida volta a ter glosa
  ([GR-FORMA] no léxico); exp do lema governa só o teste. Nota de forma, curiosidade
  e "Quem é quem" no cartão (RULES 14)
setting: Ἀχαρναί, primavera de 432 a.C.
words: 76 — 4 palavras novas na semana 6 (θύει, τὸ κρέας, τὸ ὀστοῦν, ὁ δημός)
unlocked: presente ativo 3sg/3pl (-ουσι(ν) explicado na semana 5 e retomado na 6);
  artigo; 1ª/2ª decl. nom./ac.; plural nom. masc. (οἱ θεοί) e neutro em -α (τὰ ὀστᾶ),
  explicados em nota de forma; ἐν+dat. como bloco; πατήρ/μήτηρ só nom., como bloco
cast: Κλεισθένης, Μέλιττα, Νικίας, Χλόη, Δᾶος, Σῖμος, Ἄργος; no mito: Προμηθεύς, Ζεύς
recent: a casa come pão e vinho (semana 4); a família apresentada por inteiro (semana 5);
  Melita conta o mito de Prometeu em Mecone, e a família leva vinho e oferenda ao altar
  (semana 6)
weak: portão de fase ainda não confirmado — sem registro de 3 leituras seguidas ≥3/4
gate: 3 leituras seguidas com ≥3/4 de compreensão
next: semana 7 — ritmo mantido (nota 3); tecer πονεῖ, μικρός, ἀγαθός e παίζει, vencidos
  e fora do texto da semana 6 (só testados no Ἀνάμνησις); o currículo vai até a
  semana 8 na fase 1, mas o portão ainda não foi confirmado

[ITALIAN]
phase: 1
lesson: 10 — semana 6: Pompei (seg) / Pantheon (qua) / Paestum (sex)
unlocked: artigos; preposições articuladas (nel/dal/sul/del/al); essere e avere completos;
  presente dos verbos em -are (qua) e -ere/-ire (sex)
recent: Coliseu, Torre de Pisa e Fontana di Trevi (semana 5); Pompeia, Panteão e Paestum
  (semana 6)
weak: vocabulário e interesse (nota 2 na semana 4, recuperada para 3 na 5) — textos
  de ~90 palavras, glosa generosa, monumentos com história
gate: artigos + preposições articuladas sem erro em 2 produções
next: com nota ≥3, passato prossimo é fase 2; antes, presente irregular (andare, fare,
  venire) e c'è / ci sono em texto contínuo

[ENGLISH]
register_last: public writing
lesson: 11 — semana 6, mais leve (nota 2): rodada de revisões (ter) / pedir feedback
  (qui) / bio de portfólio (sáb)
topics_done: hierarquia visual; API de componente; acessibilidade; escaneabilidade;
  handoff; estudo de caso; pricing e scoping; design tokens; teste de usabilidade;
  rationale ao cliente; crítica assíncrona; problema no estudo de caso; rodada de revisões;
  pedir feedback; bio de portfólio
collocations: 55
weak: nota 2 na semana 5 — motivo não informado; semana 6 com 3 colocações novas por
  texto, em vez de 6, e as anteriores (walk through, tie back to, up front) de volta
next: com nota ≥3, volta a 5–6 colocações; seguir rotação client/async/public

[SISTEMA]
(sem campos — planner_enabled e planner_must_return_by eram do arranjo de tarefa
agendada anterior e não se aplicam mais; ver "Pendências registradas")
```

## Pendências registradas

**11/10 · check-in da semana 5 consumido.** Notas GR 3 · IT 3 · EN 2, **sem misses**
(Mathews disse explicitamente). Promoções normais, uma caixa por item testado (ver
`state/lexicon.md`). Inglês com nota 2: metade das colocações novas; o motivo da nota
não foi perguntado e fica registrado como desconhecido. Italiano voltou ao ritmo normal e
ganhou essere/avere completos e o presente dos três grupos.

**11/10 · módulo de fala segue dormente.** Mathews não disse o contrário; o passo 9a foi
pulado e não houve briefing.

**11/10 · itens vencidos que ficaram fora do texto da semana 6:** πονεῖ, μικρός, ἀγαθός,
παίζει. A restrição "tecidos nos textos" não coube em 13 frases com no máximo 4 palavras
novas; os quatro entram no Ἀνάμνησις (dias diferentes) e voltam ao texto na semana 7.

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
