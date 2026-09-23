# AUDIT — independência de agente

Critério: o projeto pode ser entregue a outro agente competente, hoje, sem aviso?
Material só é canônico se for **exportável**, **autoexplicativo** e **nomeado** por um
manifesto do próprio projeto.

**Última revisão: 22/09/2026, na mudança para repositório Git.** Nenhum item continua esperando resposta de Mathews.

**Teste de substituição de agente: passa.** Desde 14/09. Em 21/09 passou a passar por um
motivo mais forte: além dos documentos, o **estado** também é arquivo. Outro agente
recebe a pasta e tem a posição do curso, o vocabulário com revisão, o conteúdo da semana
e o histórico de notas — não só o currículo.

---

## Fechados

**A1 · O Léxico não tinha esquema nem cópia** — FECHADO 14/09, reforçado 21/09
O esquema existe desde 14/09. Em 21/09 a relação inverteu: o arquivo
`state/lexicon.md` é a **fonte**, e a artifact é o espelho. O snapshot semanal
deixou de existir porque não há mais de que tirar snapshot.

**A2 · Os prompts deixaram de ser exportáveis** — FECHADO 14/09
`TASK_PROMPTS.md` restaurado, declarado como fonte, com a tarefa como deploy e uma
regra de sincronia explícita.

**B1 · Não existia README nem manifesto** — FECHADO 14/09
Manifesto no README, agora com 24 linhas cobrindo documentos, estado, artifacts e tarefas.

**B2 · As invariantes viviam só no campo Instructions** — FECHADO 14/09
`RULES.md` é a fonte; o campo é o deploy, com marcadores delimitando exatamente o
trecho a colar.

**B3 · A página Morning Packet era fonte e derivada ao mesmo tempo** — **FECHADO 21/09**
Era a maior pendência e a que eliminava uma classe inteira de erro. O pacote da semana
saiu do HTML e virou dados em `state/week.json`; a página passou a ser um
renderizador que não guarda conteúdo. Uma edição manual na página agora estraga no máximo
a renderização, nunca o dado. De quebra, a invariante 12 (o texto cresce dentro da
semana) deixou de depender de disciplina: as frases ficam numa lista só e cada dia
declara `upTo`, de modo que não existe onde escrever uma variação.

**C2 · Publicação manual sem ler o estado** — FECHADO 14/09 como regra
Virou a invariante 1. É regra, não guarda.

**C3 · Caminhos inconsistentes** — **FECHADO 21/09**
Os currículos foram para `courses/`; o estado, para `state/`. A raiz do
projeto ficou vazia. A estrutura agora é a mesma que a pasta local teria.

**D1 · As seções italianas tinham um campo a menos** — **FECHADO 22/09**
Perguntado, Mathews não tinha o registro e delegou. Adotada a leitura de que o campo
ausente era `status`; as linhas de `[IT-FALSI]` e `[IT-INTERF]` foram normalizadas com
`status: seen`. É decisão, não dado recuperado, e está marcada assim em
`LEXICON_SCHEMA.md`. Nada foi apagado e nenhum estado de revisão mudou.

**D2 · A coluna `data` das colocações inglesas** — **FECHADO 22/09, por evidência**
É data de **entrega**, e a coluna passou a se chamar assim. As datas futuras eram terça,
quinta e sábado — os dias da trilha — e agrupavam por registro exatamente como os pacotes
da semana 2. Uma colocação cuja entrega não passou ainda não foi encontrada e não entra
na fila de recuperação.

**D3 · A contagem de exposições não era um campo** — FECHADO 17/09
`exp` existe em todas as linhas gregas. A dívida que fica é que a semana 1 não tem
registro e não foi reconstruída.

---

**C1 · Uma execução podia marcar sucesso e pular o passo principal** — **FECHADO 22/09**
Era parcial havia uma semana: a notificação tornava a falha visível, não detectável.
No repositório o `validate.py` roda antes e depois da entrega, e o CI reprova qualquer
commit em que `docs/` não corresponda a `state/week.json`. A falha deixou de depender de
alguém ler um aviso.

**E1 · O arranjo dependia de a execução conseguir escrever** — **FECHADO 22/09**
Era a dependência mais frágil do sistema enquanto o estado morava num Claude Project: uma
escrita que falhasse em silêncio deixava o espelho mais novo que a fonte. Um commit não
falha em silêncio — ou entra no histórico, ou o workflow fica vermelho.

**E2 · Os prompts das tarefas divergiam do arquivo** — **FECHADO 22/09**
Deixou de existir junto com a duplicação. A entrega diária virou código, e código não
diverge da sua documentação sem que o validador ou o CI percebam. O planejador continua
sendo um texto, mas agora há um só, e é o do repositório.

**E3 · O planejador estava desativado** — **FECHADO 22/09**
Deixou de ser tarefa agendada. Passou a ser ritual de domingo, que não tem como ficar
"desativado" sem que você perceba: se não acontecer, a semana não existe e a entrega de
segunda falha em vez de inventar.

**E5 · As duas invariantes do campo Instructions foram aposentadas** — 22/09
A duplicação das regras existia porque o campo era a única entrega garantida a uma
execução agendada. Num repositório, `AGENTS.md` cumpre esse papel por convenção e a
entrega diária não lê regra nenhuma, porque não julga nada. Uma fonte a menos para
divergir.

---

## Abertos

**E4 · `probed` pode ser perdido antes de ser consumido** — ABERTO
Aconteceu: os cinco itens testados em 13/09 foram sobrescritos antes de o planejador os
consumir, porque ele não rodou no intervalo. O campo guarda um dia; o consumo é semanal.
Enquanto o planejador rodar toda semana, não há perda. Quando ele falha, há.
Correção: `probed` virar lista acumulada que o planejador limpa. Custa uma mudança em
`STATE_SCHEMA.md`, em `daily.py` e no passo 7 do planejador.

**E6 · O validador confere estrutura, não conteúdo** — ABERTO por natureza
Ele garante sete dias, texto que nunca encolhe, nada testado antes de cinco encontros e
manifesto honesto. Não sabe se o português corresponde ao grego, nem confere acentuação,
aspecto ou fato histórico. Parte disso é automatizável com esforço — conferir que toda
palavra do texto está no léxico exigiria um lematizador de grego antigo. Parte não é.
Está declarado no fim do próprio `validate.py`, que é onde alguém vai procurar.

**E7 · O GitHub Pages é público** — ABERTO, aceito
Controle de acesso em Pages só existe no Enterprise Cloud. O repositório pode ser
privado; a página publicada, não. O dano é pequeno — só a lição vai para lá — mas quem
tiver o endereço lê. Saída, se um dia incomodar: Cloudflare Pages com Access, em
`MIGRATION.md`.

## Prioridade sugerida

1. E4 — `probed` acumulado em vez de diário; é a única perda de dado que resta
2. E6 — mais conferência automática, até onde valer o esforço
3. E7 — decidir se a página pública incomoda, e só então mudar de hospedagem
