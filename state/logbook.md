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
UPDATED: 2026-10-31
DAY: 55
STREAK: 0
LAST_REPORT: 2026-11-01 GR4 IT3 EN4
probed: —

[GREEK]
phase: 1
lesson: 20 — semana 8, dia 1/7 (texto novo, cresce 3 → 13 frases)
apoio: por FORMA desde 04/10 — forma nova de palavra conhecida volta a ter glosa
  ([GR-FORMA] no léxico); exp do lema governa só o teste. Nota de forma, curiosidade
  e "Quem é quem" no cartão (RULES 14)
setting: Ἀχαρναί, primavera de 432 a.C.
words: 80 — 2 palavras novas na semana 8 (ὁ δεσπότης e παλαιός) e o nome Ὀδυσσεύς
unlocked: presente ativo 3sg/3pl (-ουσι(ν) explicado na semana 5 e retomado na 6);
  artigo; 1ª/2ª decl. nom./ac.; plural nom. masc. (οἱ θεοί) e neutro em -α (τὰ ὀστᾶ),
  explicados em nota de forma; ἐν+dat. como bloco; πατήρ/μήτηρ só nom., como bloco;
  εἰς+ac (εἰς τὴν οἰκίαν); masc. em -ης da 1ª decl. (ὁ δεσπότης → τὸν δεσπότην)
cast: Κλεισθένης, Μέλιττα, Νικίας, Χλόη, Δᾶος, Σῖμος, Ἄργος; reais ou míticos, só em cena
  pontual: Ὀδυσσεύς (semana 8), Σωκράτης (semana 7), Προμηθεύς e Ζεύς (semana 6)
recent: Melita conta o mito de Prometeu em Mecone (semana 6); Simo encontra Sócrates na
  ágora e não sabe dizer o que é o bem (semana 7); Melita conta o mito de Odisseu e do cão
  Argos, o único que o reconhece (semana 8)
weak: — (os seis misses de 18/10 voltaram a `recalled`, caixa 2, due 04/11; sem misses em 01/11)
gate: 3 sábados seguidos com ≥10 das 13 frases entendidas, com o apoio escondido (coluna
  `frases` do checkin_log). 1 de 3 cumprido: 13/13 em 31/10; próxima medição, sábado 07/11
next: semana 9 com ritmo normal (nota 4); a fase 1 só fecha com os 3 sábados; pedir o número
  de frases do sábado 07/11 e as palavras que não vieram

[ITALIAN]
phase: 1
lesson: 12 — semana 8: Colosseo (seg) / Torre di Pisa (qua) / Fontana di Trevi (sex)
unlocked: artigos; preposições articuladas (nel/dal/sul/del/al); essere e avere completos;
  presente regular (-are, -ere, -ire); andare, venire, fare, potere, volere, dovere; in/a/di + artigo
  (nel, nella, nei, alla, della, al)
recent: Via Ápia, Ponte Vecchio e a cúpula de Brunelleschi (semana 7); Colosseo, Torre di
  Pisa e Fontana di Trevi (semana 8)
weak: vocabulário e interesse (nota 2 na semana 4, recuperada para 3 na 5) — textos
  de ~90 palavras, glosa generosa, monumentos com história
gate: artigos + preposições articuladas sem erro em 2 produções
next: fechar a fase 1 com o gate (artigos + preposições articuladas sem erro em 2
  produções); passato prossimo é fase 2

[ENGLISH]
register_last: public writing
lesson: 13 — semana 8, ritmo normal (nota 4): layout fluido para o cliente (ter) / comentário
  útil sobre um layout responsivo (qui) / 320 pixels e acessibilidade (sáb)
topics_done: hierarquia visual; API de componente; acessibilidade; escaneabilidade;
  handoff; estudo de caso; pricing e scoping; design tokens; teste de usabilidade;
  rationale ao cliente; crítica assíncrona; problema no estudo de caso; rodada de revisões;
  pedir feedback; bio de portfólio; dizer não ao cliente; propor componente; resultados;
  layout fluido (cliente, time, texto público)
collocations: 85
weak: —
next: novo tópico; seguir rotação client/async/public; 5 colocações por texto

[SISTEMA]
(sem campos — planner_enabled e planner_must_return_by eram do arranjo de tarefa
agendada anterior e não se aplicam mais; ver "Pendências registradas")
```

## Pendências registradas

**01/11 · check-in da semana 7 (repetida) consumido; semana 8 composta e página nova.** Notas GR 4
· IT 3 · EN 4, **sem misses** (ditos explicitamente) e **13 das 13 frases** no teste de sábado
31/10: primeira medição do portão, 1 de 3. Promoções em `state/lexicon.md` (os sete dias
supostamente lidos, como nas rodadas anteriores). A página ganhou card ao toque, áudio, fotos,
mapas e abas por idioma — mudança de renderizador em commit próprio (invariante 5). Áudio e fotos
saem do `tools/audio.py` e do `tools/foto.py`, rodados pelo planejador no domingo. **Divergência
relatada, não corrigida (invariante 6):** `RULES.md` 14 fala em "quatro partes" e na invariante 19
em "nada abaixo do texto além de…"; a página nova junta Forma, Som, Curiosidade, mapa e elenco em
abas dentro do mesmo cartão e acrescenta botões de áudio — a forma continua a mesma, mas a
redação da invariante 14 não mencionava os botões. **Resolvida em 01/11:** Mathews aprovou a nova
redação, aplicada em `RULES.md` (reconciliação de 01/11/2026).

**25/10 · FEITO:** a semana 7 foi reemitida para 26/10–01/11, sem consumir nada (ver
`state/lexicon.md`). A pendência abaixo fica como registro.

**23/10 · semana 7 não lida; será repetida de 26/10 a 01/11 (decisão de Mathews).** Ele não
leu nenhum dia. No domingo 25/10, em vez de compor a semana 8: (1) **não** consumir nenhum
`probed` da semana 7 e **não** somar `exp` — nada foi lido nem testado, então não há promoção
nem miss novo; (2) reemitir o mesmo `state/week.json` com `range` 2026-10-26/2026-11-01, os
dias `n` 26 a 1, o cabeçalho avisando que a semana repete a anterior, e a `composed`
atualizada; (3) mover as datas de entrega das 15 colocações inglesas da semana 7 em
`state/lexicon.md` para 27/10, 29/10 e 31/10 (ainda não foram encontradas); (4) a primeira
medição do portão passa de 24/10 para o sábado **31/10**; (5) o número da lição continua 19.
Pedir as notas só se ele quiser dá-las; não há leitura para avaliar. Até lá, nada mudou:
mesmo sem a reedição, a entrega de segunda mostraria o mesmo conteúdo, só com os números dos
dias errados.

**18/10 · check-in da semana 6 consumido.** Notas GR 3 · IT 3 · EN 3. Seis palavras
nomeadas "com um pouco de dificuldade", tratadas como misses (ver `state/lexicon.md`); todas
voltam no texto da semana 7 e no Ἀνάμνησις de segunda. Mathews perguntou o que `+ac` quer
dizer: a sigla estava visível na chave do Ἀνάμνησις. Corrigido, e regra nova na invariante 19.

**18/10 · módulo de fala segue dormente.** Mathews não disse o contrário; passo 9a pulado.

**18/10 · portão da fase 1, combinado com Mathews.** Teste no sábado: lê as 13 frases com o
apoio escondido e diz quantas entendeu; 10 ou mais passa; três sábados seguidos cumprem.
A primeira medição é o sábado 31/10 (era 24/10; a semana 7 foi repetida). A nota abaixo, sobre o problema, fica como histórico.

**18/10 · sobre o portão de fase.** Três semanas seguidas de nota 3 em grego, mas o portão
da fase 1 pede 3 leituras com ≥3/4 de compreensão, e a nota mede experiência, não isso.
Para fechar a fase 1 na semana 8 é preciso perguntar a ele, em conversa, quanto do texto
entendeu em cada leitura.

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
