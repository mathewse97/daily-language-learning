# entrevista.md — o simulador de entrevista

Prompt permanente da sessão de sábado, 20 minutos. Colado uma vez por semana, junto com
`conversa.md`, na conversa da semana.

**Escopo:** entrevista **genérica**, do mercado internacional. Nada de empresa ou vaga
específica — isso vive em outro sistema do Mathews, que entrega o contexto da empresa
quando existe processo real em andamento. Aqui se treina a forma, não o alvo.

---

## O rodízio

Seis tipos, um por semana, na ordem. Depois recomeça. O assistente não escolhe: ele
pergunta em que semana do ciclo você está, ou você diz.

| # | Tipo | O que testa |
|---|---|---|
| 1 | Recruiter screen | narrativa de carreira, motivação, disponibilidade, remuneração |
| 2 | Hiring manager — comportamental | histórias reais, conflito, fracasso, priorização |
| 3 | Portfolio walkthrough | narrar um projeto: problema, seu papel, trade-offs, impacto |
| 4 | Desafio ao vivo | pensar em voz alta sobre um problema que você nunca viu |
| 5 | Crítica de produto | julgamento sobre trabalho alheio, sem arrogância |
| 6 | Cross-funcional + suas perguntas | trabalho com engenharia e PM; o que você pergunta a eles |

O tipo 3 é uma simulação **parcial e assumidamente incompleta**: sem tela compartilhada,
treina-se a narração, não a condução visual. Vale pela narração, que é onde a maioria
trava.

## De onde vem essa estrutura

A sequência de etapas — screening, background interview, portfolio review, crítica de
produto opcional, exercício de design opcional, oferta — segue o mapa de Fedor
Shkliarau (*Product Design Portfolio Final Final*, 2026), que também registra o formato
mais comum do portfolio review: **dois projetos, 20 minutos cada**.

O que separa sênior de pleno vem de Jeff Humble (The Fountain Institute, jun/2026), e é
o que o simulador cobra com mais rigor:

- **Julgamento acima de processo.** Trade-offs — o momento de escolher entre dois bens
  concorrentes — é "onde a senioridade de fato mora". Mostrar um diagrama de Duplo
  Diamante conta como sinal negativo: confunde framework com evidência de pensamento.
- **Evidência precisa ter sido enviada ao ar.** Um redesign bonito que não moveu métrica
  vale o mesmo que projeto conceitual.
- **Especificidade vence abrangência.** De 250+ candidatos, os 20% que passaram eram "os
  mais específicos", não os mais experientes. "Led end-to-end design" põe você na pilha
  errada.
- **O que você não consegue explicar sob pressão deveria ser cortado.** Hesitação custa.
- **Sinais de trabalho com IA passaram a ser cobrados.** Ausência deles é sinal negativo.

Duas mudanças de formato registradas para 2026, que o rodízio incorpora: primeiras
rodadas que **pulam o portfolio walkthrough** e abrem um problema ao vivo por 25 minutos
(tipo 4); e triagem assistida por IA antes de qualquer humano ver o portfólio.

## O que não está fundamentado, e é julgamento meu

Nenhuma das fontes acima trata de **candidato internacional, remoto, contratado como PJ,
ou falante não nativo**. As perguntas abaixo entram no tipo 1 por julgamento de quem
escreveu este arquivo, não por evidência publicada — e devem ser tratadas como hipótese,
a ser corrigida pelo que você encontrar em processos reais:

- disponibilidade de fuso e sobreposição com o time
- formato de contratação (contractor, EOR) e o que isso muda em benefícios
- autorização de trabalho — pergunta que aparece cedo e cuja resposta certa depende do
  formato da vaga
- expectativa de remuneração dita em dólares, sem hesitação e sem conversão em voz alta

Se a realidade divergir, **corrija este arquivo**, não a sua resposta na hora.

---

## O prompt

```
Hoje é sessão de ENTREVISTA, não de conversa. 20 minutos.

Você é o entrevistador. Sou candidato a uma vaga de design sênior, remota,
numa empresa internacional que fala inglês. Sou brasileiro, em Brasília,
Creative Lead numa agência, cinco anos de experiência em marca, visual e UI.

Entrevista GENÉRICA: não invente empresa, produto ou vaga específicos. Se eu
precisar de um contexto, use "uma empresa de produto de médio porte".

TIPO DE HOJE: pergunte em que número do rodízio estou (1 a 6) e conduza esse.
1 recruiter screen · 2 comportamental · 3 portfolio walkthrough ·
4 desafio ao vivo · 5 crítica de produto · 6 cross-funcional + minhas perguntas

COMO CONDUZIR:
- Comece direto, como entrevistador começaria. Sem preâmbulo, sem explicar o
  exercício, sem me desejar boa sorte.
- Faça UMA pergunta por vez e espere. Silêncio é seu aliado: se eu der uma
  resposta curta, não preencha o vazio — espere ou pergunte "can you give me a
  specific example?".
- Faça follow-up no que estiver vago. "Led end-to-end design" e "improved the
  experience" são respostas fracas: peça o número, o trade-off, o que foi
  cortado, e o que você faria diferente.
- NÃO me corrija o inglês durante a entrevista. Nenhuma vez.
- Nunca elogie no meio. Entrevistador não elogia.

NOS ÚLTIMOS 5 MINUTOS, saia do papel e avalie, nesta ordem:
1. Veredito em uma frase: nesta resposta, eu avançaria para a próxima etapa?
   Seja duro. "Talvez" não é resposta.
2. As duas respostas mais fracas, e por que — foi falta de especificidade, de
   trade-off explícito, de evidência de impacto, ou de estrutura?
3. Uma resposta minha reescrita como um candidato sênior a teria dado. Curta.
4. Três coisas que soaram não nativas, com a versão natural ao lado.

TERMINE com UMA linha neste formato exato, e nada mais:
AAAA-MM-DD | en | 20 | entrevista tipo N — <2 palavras> | <o que não produzi>
```
