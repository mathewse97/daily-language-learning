# TASK_PROMPTS — os dois procedimentos

O sistema tem dois procedimentos, e eles são de naturezas diferentes. Tratar os dois como
"tarefa agendada" foi um erro do arranjo anterior, e é o que este arquivo corrige.

| | Quando | O que é | Precisa de modelo |
|---|---|---|---|
| **Entrega diária** | todo dia, ~04:40 | `daily.py`, rodado pelo Actions | não |
| **Planejamento semanal** | domingo | conversa com um agente | sim, sempre |

---

## 1 · Entrega diária — é código, não prompt

Não há prompt. O procedimento está em `daily.py` e o agendamento em
`.github/workflows/daily.yml`. O que ele faz, na ordem:

1. valida o repositório (`validate.py`) **antes** de tocar em qualquer coisa;
2. acha em `state/week.json` o dia da semana de hoje;
3. atualiza `state/logbook.md`: `UPDATED`, `DAY`, `probed` e o `dia N/7` da lição;
4. roda `build.py`, que regera `docs/index.html`;
5. valida de novo, **depois** de mexer;
6. commita `state/` e `docs/` — e só commita se algo mudou.

Se o pacote da semana não tiver o dia de hoje, o script **falha e não altera nada**. Isso
é o comportamento certo: significa que o planejador não compôs a semana, e inventar um
dia seria pior que não entregar.

Isso só é possível porque o conteúdo é dado. Enquanto a lição era HTML escrito à mão, a
entrega diária precisava de um modelo — e um modelo que escreve HTML todo dia é um modelo
que um dia reescreve o desenho da página por engano.

---

## 2 · Planejamento semanal — é conversa

Domingo. Abra uma sessão com um agente que tenha acesso ao repositório e use o texto
abaixo. Ele é a fonte do procedimento: se o jeito de planejar mudar, muda aqui.

```
Planeje e componha a semana que vem neste repositório, e audite a que acabou.

VOCÊ NÃO MODIFICA O QUE TE EXECUTA. Não altere .github/workflows/, o agendamento,
RULES.md ou AGENTS.md. Se notar divergência entre as regras e o que os arquivos
fazem, relate e não conserte.

1. Leia RULES.md, state/logbook.md, state/lexicon.md, state/week.json (ainda a
   semana que acabou) e state/checkin_log.md.

2. Pergunte a Mathews as três notas da semana, de 1 a 5, uma por trilha, e quais
   palavras não vieram. Acrescente uma linha a state/checkin_log.md no formato
   `data | gr | it | en | misses`. Se ele não quiser dar as notas, siga sem elas
   e use a regra conservadora do passo 4.

   1-2  desacelere — sem avanço de fase, metade dos itens novos, repita estruturas
   3    mantenha o ritmo
   4    progressão normal
   5    acelere — itens novos no topo da faixa da fase, antecipe o portão

3. Calcule o que vence: todo item do léxico com `due` até o sábado que vem. São
   restrição de geração, não lista — têm de aparecer tecidos nos textos.

4. Atualize state/lexicon.md. EXPOSIÇÃO NÃO É APRENDIZADO:
   - palavra nova entra como `seen`, caixa 1, exp 0;
   - só itens nomeados em `probed` no logbook podem se mover;
   - nomeados em `misses` → `missed`, caixa 1. Não nomeados → `recalled`, caixa +1;
   - dois `recalled` distintos antes de entrar na caixa 4;
   - sem check-in: só a caixa 1 avança para a 2, o resto segura;
   - trilha com nota 1-2: nada promove, e o quarto mais recente cai para a caixa 1.
   Caixas: 1=+1d 2=+3d 3=+7d 4=+21d 5=+60d.

4a. Atualize a coluna `exp`. Para cada palavra grega da semana que acabou, conte as
   aparições nos dias que de fato a leram — uma frase dentro do `upTo` de cinco dias
   conta cinco vezes — somando sob o lema; o artigo não é item de léxico. `exp`
   governa apoio de leitura e elegibilidade para teste, nunca promoção de caixa.

5. Componha a semana como DADOS e escreva em state/week.json, seguindo
   WEEK_PACKET_SCHEMA.md. Você escreve JSON, nunca HTML.
   Grego todo dia · italiano seg/qua/sex · inglês ter/qui/sáb · domingo só revisão.
   Siga os currículos em courses/.

   As frases gregas da semana vão UMA VEZ SÓ em greek.sentences, e cada dia declara
   só `upTo`: 3, 5, 7, 9, 11, 13, 13. Não existe outro lugar onde escrever texto
   grego, e é isso que torna a invariante 12 impossível de violar. Palavra com
   exp ≥ 5 leva null no lugar da glosa e da transliteração.

   O CARTÃO DE GREGO TEM QUATRO PARTES E NADA MAIS: Ἀνάμνησις, texto interlinear,
   português corrido recolhido, nota de som. Sem Ἐρωτήσεις, sem Σκόπει, sem
   observação, sem Θησαυρός, sem etimologia, sem gabarito. Não reintroduza nada
   disso: foi retirado de propósito, depois de duas semanas de uso.

   O Ἀνάμνησις testa SÓ itens com exp ≥ 5. Se nenhum qualificar, omita `recall`
   naquele dia. Nomeie os itens testados em `recall.probed`, escritos exatamente
   como estão no léxico.

6. Confira o seu próprio grego antes de commitar: toda palavra no léxico ou entre as
   ≤4 novas; no máximo 2 nomes próprios novos, glossados; acentuação politônica
   completa; aumento correto inclusive em compostos; aspecto deliberado; nada além
   da fase atual; Κλεισθένης, Ἡρακλῆς e Ζεύς só em nominativo ou vocativo até a
   fase 2. Na dúvida sobre uma forma, troque a palavra.
   Depois confira os fatos ANTES de compor, não depois. Nada posterior a 432 a.C.
   Onde a bibliografia diverge, diga em uma linha ou omita.

7. Atualize state/logbook.md: avance de fase só se o portão do currículo tiver sido
   cumprido — diga qual portão e por quê. Limpe `probed`. Escreva LAST_REPORT com a
   data e as três notas que você consumiu.

8. Rode `python3 validate.py` e `python3 build.py`. Se o validador reprovar,
   conserte antes de commitar — ele confere estrutura, e estrutura errada quebra a
   página do aluno amanhã de manhã.

9. Commite state/ e docs/ juntos, com uma mensagem que diga a semana e o arco.

<!-- MÓDULO:FALA início -->
9a. SE a pasta speaking/ existir — ela é um módulo opcional e pode ter sido
    removida; se não existir, pule este passo inteiro sem comentar:

    Leia speaking/log.md. Trate a coluna `não produzi` das linhas da semana que
    acabou como entrada adicional de `misses` no passo 4: o que ele tentou dizer
    e não conseguiu é evidência de item não recordado, tão boa quanto o check-in.
    Vale para as colocações inglesas; não mexa no grego por causa disso.

    Depois componha o BRIEFING DA SEMANA e entregue a Mathews no fim, em bloco
    separado, pronto para ele colar no assistente de voz na segunda. No máximo
    dez linhas:
      - as colocações de inglês da semana, com o registro de cada uma;
      - o que ficou pendente do log da semana anterior;
      - o número do rodízio de entrevista desta semana (1 a 6, ciclando).
    Nada de grego e nada de italiano nesse bloco — ele é só para a fala em inglês.
<!-- MÓDULO:FALA fim -->

10. Diga a Mathews, explicitamente, o que você escreveu, arquivo por arquivo, e o
    arco da semana em uma linha. Um passo que você pulou tem de aparecer aqui.

11. No primeiro domingo de cada mês, releia o grego do mês procurando acento errado,
    aumento falso, erro de aspecto, concordância e sintaxe portuguesa vestida de
    grego, e os fatos, procurando o que foi inventado ou é anacrônico. Ponha as
    correções no topo do cartão de segunda, cada uma com a forma certa e o porquê em
    uma linha.
```

---

## Histórico

**22/09/2026** — o sistema mudou para um repositório Git. A entrega diária deixou de ser
um prompt e virou `daily.py`: com a lição em dados, não há nada nela que exija julgamento.
O planejador continuou sendo conversa, e o check-in passou a entrar por ela — a página de
check-in que salvava a si mesma não tem equivalente em site estático, e construir uma
máquina para substituí-la só ajudaria nos domingos em que a semana também não seria
composta.

**21/09/2026** — o estado saiu das páginas e foi para arquivos; a página virou
renderizador. O pacote da semana deixou de ser HTML e virou JSON.

**17/09/2026** — o cartão de grego foi reduzido a quatro partes; o texto grego passou a
ser interlinear; o campo `exp` foi criado. Motivo da primeira: o único exercício que
ajudava era o Ἀνάμνησις. Motivo da segunda: a transliteração em bloco obrigava a sair do
texto e voltar, e o resultado foi uma semana inteira não estudada.

**16/09/2026** — uma execução reescreveu o próprio agendamento, numa rodada de 2h52. É a
origem da invariante 6.

**13/09/2026** — uma execução marcou sucesso sem publicar o pacote, e uma publicação
manual sobrescreveu a semana com conteúdo antigo. São a origem das invariantes 1 e 3.
