# MÓDULO FALA — o que é, no que se apoia, e como arrancar

> **Este módulo é opcional e removível.** O sistema de leitura funciona inteiro sem ele.
> Se você é um agente lendo este repositório pela primeira vez: tudo que pertence a este
> módulo está nesta pasta `speaking/` ou dentro de blocos marcados
> `MÓDULO:FALA início` … `MÓDULO:FALA fim` em cinco arquivos do núcleo. A seção
> "Como remover" no fim deste documento lista os cinco, com precisão.
>
> **Acrescentado em 24/09/2026.** A revisão de continuidade é seis semanas depois da
> **ativação**, não do acréscimo — ver "Estado" logo abaixo.

## Estado

```
ESTADO: dormente
desde: 2026-10-04
ativado_em: —
rodizio_semana_1: —
revisao: —
```

**Dormente** quer dizer: pronto, documentado, e desligado por decisão de Mathews
(04/10/2026: "quero deixar pronto, mas não farei por agora"). Enquanto dormente:

- o planejador de domingo **pula o passo 9a inteiro** — não lê `log.md`, não gera
  briefing — e diz numa linha só, no relatório final, que o módulo está dormente;
- `log.md` vazio não é falha nem conta para o critério de abandono: o relógio das seis
  semanas só começa na ativação;
- nada mais muda. Nenhum script lê este bloco; ele é para o agente e para você.

## Como ativar

Para ativar, basta Mathews dizer numa conversa com um agente que tenha acesso ao
repositório — esta ou qualquer outra — algo como **"ative o módulo de fala"**. Não
precisa repetir nada desta seção; o agente que receber o pedido faz, nesta ordem:

1. Lê este arquivo inteiro, `conversa.md`, `entrevista.md` e `log.md`.
2. Define a **segunda-feira de início**: a próxima segunda, ou a desta semana se
   Mathews disser que quer começar já. Reescreve o bloco "Estado" acima:
   `ESTADO: ativo`, `ativado_em:` a data de hoje, `rodizio_semana_1:` a segunda de
   início, `revisao:` a segunda de início + 42 dias. Atualiza a linha de revisão em
   `AUDIT.md` (item F1) para a mesma data.
3. Compõe o **briefing da semana** a partir de `state/week.json` — o da semana que
   começa na segunda de início; se ela ainda não foi composta, compõe o planejamento
   primeiro. Mesmo formato do passo 9a de `TASK_PROMPTS.md`: no máximo dez linhas, só
   inglês, com as colocações da semana e o registro de cada uma, `rodízio: 1`, e
   "pendências: nenhuma (primeira semana)".
4. Entrega a Mathews **três blocos prontos para colar**, um depois do outro: o prompt de
   `conversa.md`, o prompt de `entrevista.md` e o briefing. E a agenda em quatro
   linhas: segunda abre a conversa e cola; terça e quinta "sessão de hoje"; sábado
   "entrevista de hoje"; domingo "me dá as linhas do log da semana".
5. Roda `python3 validate.py`, commita `speaking/` e `AUDIT.md` com a mensagem
   "Ativa o módulo de fala" e diz o que escreveu.

A partir daí, o passo 9a do planejador de domingo roda normalmente.

O número do rodízio de entrevista é **derivado da data**, não guardado: semanas
inteiras desde `rodizio_semana_1`, módulo 6, mais 1. Isso evita mais um contador que
precise ser lembrado — e se uma semana for pulada, o rodízio segue andando, o que é
aceitável: os seis tipos voltam a cada seis semanas de qualquer jeito.

**Para pôr de volta em dormência**, o mesmo: Mathews diz, o agente reescreve
`ESTADO: dormente` com a data, e anota em `log.md` uma linha de texto fora do bloco de
dados. As linhas já registradas ficam. Ao reativar, o relógio das seis semanas
recomeça.

## O problema que ele resolve

O curso entrega input diário e recuperação espaçada, e faz isso bem. O que ele não faz:
nenhum áudio, nenhuma fala, nenhuma produção com retorno. A trilha de inglês termina em
composição mental com um modelo para comparar — o que treina reconhecimento e
planejamento, não produção em tempo real.

Isso importa porque o inglês tem prazo atrelado: Mathews busca vagas remotas
internacionais, e entrevista é fala ao vivo, não roteirizada, sob pressão.

O `courses/ITALIAN_COURSE.md` já registrava o mesmo buraco com todas as letras: *"Sem
escrita, a correção real desaparece deste percurso — e produção é justamente o gargalo
dele."*

## No que ele se apoia, e no que não se apoia

**Sustentado por evidência.** Duas meta-análises recentes encontram efeito médio para
prática de língua com chatbots: ES 0,576 · IC 95% [0,385–0,768] em 41 estudos e 3.515
participantes (Li et al., 2025, *J. Computer Assisted Learning*); g = 0,608 em 31 estudos
(Lyu et al., *Int. J. Applied Linguistics*). Numa revisão sistemática de 24 estudos sobre
fala especificamente (Du & Daniel, 2024, *Computers and Education: AI*), o achado mais
repetido é **redução de ansiedade de fala** — 11 dos 24 —, seguido de pronúncia (7),
fluência (6) e confiança (6).

**Não sustentado, e é importante dizer.** Nos mesmos 24 estudos, "aumento da disposição
real de se comunicar" aparece em apenas 3 — e é o construto mais próximo de
"transferiu para a vida real". **Nenhum dos trabalhos que consultei mede transferência
para conversa com humanos.** Também não existe curva de dose: ninguém testou o mínimo.

**Três ressalvas que mudam a leitura dos números.** O moderador mais forte na
meta-análise de Li foram as intervenções de 1 a 7 dias, que é a assinatura de efeito de
novidade. O reconhecimento de fala erra com sotaque não nativo — um estudo citado reporta
~50% de acurácia. E aprendizes de nível mais alto ganharam mais que iniciantes, o que
inverte a intuição de que a ferramenta serve para quem está começando.

**Conclusão honesta:** isto é uma aposta com evidência média a favor e lacunas
conhecidas, não um método comprovado. O critério de abandono no fim deste arquivo existe
por isso.

## A dose

O único protocolo com resultado positivo que encontrei foi 3 × 30 min por semana durante
6 semanas (n=60, atribuição não randomizada). Este módulo roda **metade disso**:

| Sessão | Quando | Minutos |
|---|---|---|
| Conversa | terça e quinta | 15 |
| Entrevista | sábado | 20 |
| **Total** | | **50 min/semana** |

Sobre os ~25 min/dia de leitura já existentes, são **7 minutos a mais por dia**, em média.
Se em seis semanas nada tiver mudado, a primeira hipótese a testar é **dose**, não método.

O italiano fica **fora por enquanto**, deliberadamente: fase 1, e a literatura diz que
iniciante ganha menos. Entra na fase 2, se entrar.

O grego fica fora **por enquanto, não permanentemente**. A meta de Mathews é ler grego
antigo em geral — qualquer obra, não só Xenofonte: a lista da fase 5 do currículo
(Xenofonte → Platão → Lísias) é um caminho de exemplo, nunca o objetivo em si. Ele também
quer aprender a falar ático, só que não é prioridade agora, e conversar hoje seria custo
de oportunidade frente à leitura. Se um assistente de voz um dia sustentar conversa em
grego antigo com qualidade aceitável, o módulo pode ser estendido para o grego — decisão
a tomar em conversa, quando isso acontecer. Até lá, a única prática oral é ler o texto do
dia em voz alta, dois minutos, e isso não precisa de módulo nenhum.

> Corrigido em 27/09/2026: a redação anterior ("permanentemente", "o objetivo é ler
> Xenofonte") era uma leitura estreita demais de quem compôs este arquivo, nunca algo que
> Mathews tivesse dito. Ele apontou o erro na mesma conversa.

## Como opera

Nada disto roda sozinho. São três conversas por semana, conduzidas por você, num
assistente com modo de voz.

**Domingo, no planejamento.** O planejador gera um bloco curto — o briefing da semana —
e lê `speaking/log.md` como entrada de `misses`. É esse segundo ponto que faz o módulo
ser parte do sistema e não um app paralelo: o que você não conseguiu dizer na terça vira
restrição de geração do texto da semana seguinte.

**Segunda, uma vez.** Abra **uma conversa para a semana inteira** no assistente de voz.
Cole `speaking/conversa.md` e o briefing. Nomeie "Fala — semana N".

**Terça e quinta.** Mesma conversa, microfone, "sessão de hoje". 15 minutos.

**Sábado.** Mesma conversa, mas diga "entrevista de hoje". O assistente usa
`speaking/entrevista.md`, que está nesse mesmo fio desde segunda. 20 minutos.

**Domingo.** "Me dá as linhas do log da semana." Ele devolve três. Você cola em
`speaking/log.md`. É a **única** escrita no repositório durante a semana inteira.

Uma conversa por semana, e não uma por sessão, é o detalhe que faz isso funcionar sem
depender de memória entre chats — recurso que varia por plano e por produto.

## Critério de abandono

Definido enquanto a ideia é nova, para não depender de força de vontade depois:

- **Menos de 12 sessões em seis semanas** — o hábito não pegou. Remova o módulo, não o
  mantenha como arquivo morto mentindo que o sistema tem trilha de fala.
- **O reconhecimento de fala irritar mais do que ajudar** — abandone a ambição de
  pontuação de pronúncia e fique só com a conversa. O dado dos ~50% com sotaque não
  nativo diz que isso é provável.
- **As entrevistas simuladas ficarem confortáveis** — é sinal de que o simulador parou
  de ser útil, não de que você está pronto. Troque por humano.

## O que este módulo não substitui

**Uma sessão de entrevista simulada com um humano a cada duas semanas vale mais que
qualquer quantidade de bot**, para o objetivo específico de passar em processo
internacional. Um assistente não sabe o que é uma resposta fraca para um hiring manager
americano, não interrompe, não fica em silêncio esperando você continuar, e não diz que
você respondeu com confiança à pergunta errada. Custa US$25–40/hora em plataformas de
tutoria. Este módulo é volume entre essas sessões, não substituto delas.

## Como remover

Removido assim, o repositório volta exatamente ao estado anterior e o `validate.py`
continua passando — isso foi testado, não suposto.

1. Apague a pasta `speaking/` inteira.
2. Corte os blocos entre os marcadores `MÓDULO:FALA início` e `MÓDULO:FALA fim`,
   inclusive os marcadores, nestes cinco arquivos:
   - `README.md` — linhas do manifesto e da ordem de leitura
   - `TASK_PROMPTS.md` — passos do planejador de domingo
   - `OPERATIONS.md` — linha da tabela e da solução de problemas
   - `AUDIT.md` — o registro da decisão
   - `validate.py` — a conferência condicional
3. Rode `python3 validate.py`. Tem de passar.

O passo 3 do `validate.py` já é condicional: se a pasta `speaking/` não existir, ele pula
a conferência em silêncio. Ou seja, **apagar só a pasta não quebra o CI** — os blocos
marcados são limpeza, não obrigação.
