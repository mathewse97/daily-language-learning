# RULES — invariantes do sistema

Regras que valem em toda execução, agendada ou não. São regras **do projeto**, não
instruções de interface: continuam valendo se Claude for substituído por outro agente.

> **Este arquivo é a fonte, e agora é a única cópia.**
>
> Enquanto o projeto morou num Claude Project, estas invariantes existiam duas vezes: aqui
> e, integralmente coladas, no campo Instructions — porque o campo era a única coisa
> garantidamente entregue a toda execução agendada, e um ponteiro poderia ser ignorado em
> silêncio.
>
> Num repositório isso deixou de valer. `AGENTS.md`, na raiz, é lido por convenção pelos
> agentes de código antes de qualquer trabalho, e manda ler este arquivo inteiro. A
> entrega diária não lê regra nenhuma porque não julga nada: é um script. A duplicação
> perdeu a razão de existir e foi eliminada.
>
> **Se um dia houver uma segunda cópia em qualquer lugar, ela é derivada desta, e a regra
> de sincronia volta a valer: mudou aqui, muda lá, na mesma volta.**

## Estado e publicação

**1 · Leia o estado antes de publicar.** Antes de escrever qualquer coisa, leia
`state/logbook.md` e confirme em que lição o sistema está. Esta regra existe
porque foi quebrada: em 13/09 uma página foi sobrescrita com conteúdo de uma semana
anterior por falta dessa conferência.

**2 · Os dados moram nos arquivos; a página é gerada a partir deles.** Estado, léxico,
pacote da semana e check-ins são arquivos versionados, em `state/`. `docs/index.html` é
**derivado**: `build.py` o produz a partir de `state/week.json` e de
`page/template.html`. **Nunca componha conteúdo escrevendo HTML de página**, e nunca
edite `docs/` à mão — o próximo build desfaz, e o CI reprova antes disso.

**3 · Uma mudança nos dados e a página que sai dela andam no mesmo commit.** Rode
`python3 validate.py` e `python3 build.py` antes de commitar, e commite `state/` e
`docs/` juntos. Um pacote novo sem o build correspondente é um repositório que mente
sobre o que o aluno vai ler amanhã.

**4 · O Logbook é reescrito no lugar, nunca acrescido.** Máximo 60 linhas de dados.
Se estiver vazio ou inacessível, diga isso no topo do pacote e continue da última fase
conhecida. **Nunca invente progresso.**

**5 · O renderizador é código, não conteúdo.** `page/template.html` — o `<style>`, as
fontes, o script que desenha os cartões e a navegação por dia — não é recomposto a cada
semana. Mudar o desenho da página é uma decisão tomada em conversa, com commit próprio,
separada de qualquer mudança de conteúdo. Contrato em `PAGE_TEMPLATE.md` e
`WEEK_PACKET_SCHEMA.md`.

**6 · Uma execução nunca modifica o sistema que a executa.** Nenhuma automação e nenhum
agente altera `.github/workflows/`, o agendamento, este arquivo ou `AGENTS.md` por
iniciativa própria. Quem notar divergência entre as regras e o que os arquivos fazem
**relata e não conserta**: reconciliar é decisão de Mathews, tomada em conversa, nunca
efeito colateral de uma entrega das 5h. Esta regra existe porque foi quebrada: em 16/09
uma execução reescreveu o próprio agendamento e levou 2h52 para terminar.

No GitHub ela deixou de ser honra: o token do workflow diário tem permissão de conteúdo e
nada mais, e o GitHub recusa por padrão que uma automação edite arquivos de workflow.

## Língua e método

**7 · Metalinguagem.** Português nas trilhas de grego e italiano; inglês na trilha de
inglês. Nunca misturar dentro de uma trilha.

**8 · Inventário fechado.** Textos gregos só usam palavras já no Léxico, mais no máximo 4
novas. Nomes próprios não contam para esse limite, mas não são livres: no máximo 2 novos
por texto, introduzidos deliberadamente, glossados em português na primeira aparição
salvo quando transparentes, e registrados em `[GR-NOM]`. Um nome próprio nunca é a
resposta de uma pergunta de compreensão na primeira vez que aparece, e nunca serve para
contrabandear conteúdo além do inventário.

**9 · Exposição não é aprendizado.** Encontrar uma palavra num texto nunca a promove. Só
um teste que ele não reportou como falho promove. O campo `exp` conta aparições e governa
apenas o apoio de leitura (17); a promoção entre caixas é outra coisa. Regra completa em
`TASK_PROMPTS.md`, passo 4 do planejador; campos em `LEXICON_SCHEMA.md`.

**10 · Rótulos de registro.** Todo texto grego é marcado `[composto]`, `[adaptado]` ou
`[autêntico]`. Sem exceção — ele nunca deve confundir grego pedagógico com grego atestado.

**11 · Dialeto.** O grego é ático. Koiné só a partir da fase 3, sempre rotulada como
janela. Homero e Heródoto são recontados em ático até a fase 5.

**12 · O texto cresce dentro da semana, e isso não é opcional.** Segunda tem 3 frases
curtas. De terça a sábado, cada dia repete **palavra por palavra** todas as frases
anteriores e acrescenta exatamente 2. Domingo relê tudo e não acrescenta nada. Na segunda
seguinte começa um texto novo, carregando o vocabulário acumulado. **Na forma dos dados
isso é estrutural:** as frases ficam uma vez só em `greek.sentences` e cada dia declara
`upTo`. Não existe onde escrever uma variação — e é assim que deve continuar.

**13 · Conteúdo culturalmente sofisticado, língua simples.** Deuses, heróis, templos,
escudos, festivais. Nunca "conteúdo simples porque o grego é simples" — o que ele já
conhece é o que torna a língua desconhecida compreensível.

## Forma da lição

**14 · A forma do cartão de grego é fixa e curta.** Quatro partes, nesta ordem, e nada
mais: o Ἀνάμνησις com a chave recolhida; o texto interlinear; o português corrido,
recolhido, logo abaixo do texto; a nota de som. Depois disso o cartão termina, com a
tabela do alfabeto recolhida e a linha do check-in. **Nenhum exercício depois do texto** —
sem Ἐρωτήσεις, sem Σκόπει, sem observação gramatical, sem etimologia, sem Θησαυρός. A
leitura é a lição. Isto foi decidido em 17/09 depois de duas semanas de uso: o único
exercício que ajudava era o Ἀνάμνησις.

**15 · Recuperação, não reconhecimento.** O Ἀνάμνησις são 2 a 5 prompts respondíveis de
memória sem olhar para trás, metade deles português → grego, no máximo um de múltipla
escolha, nenhum respondível pelo texto do próprio dia. Testa **apenas itens com `exp` ≥ 5**
— essa é a única janela; não há semana de estreia. Os itens testados são exatamente o que
vai para `probed` no Logbook.

**16 · A chave do Ἀνάμνησις fica logo abaixo dele, recolhida.** Recuperação sem
verificação imediata não consolida, e resposta visível na mesma tela transforma
recuperação de volta em leitura. Nas trilhas de italiano e inglês, que ainda têm
exercícios, as respostas vão no fim do cartão. O cartão de grego não tem gabarito porque
não tem exercício além do Ἀνάμνησις.

**17 · O apoio de leitura é interlinear, generoso e nunca é retirado como teste.** Todo
texto grego é montado palavra a palavra: a glosa portuguesa acima, o grego no meio, a
transliteração abaixo. A glosa é palavra por palavra, não tradução corrida — `ἐν τῷ ἀγρῷ`
lê-se "em / o / campo", e é isso que se quer. O apoio some **por palavra, nunca por data**:
uma palavra carrega glosa e transliteração enquanto seu `exp` no Léxico for menor que 5;
ao chegar a 5 perde as duas e não as recupera. Enquanto o planejador não tiver contado ao
menos uma semana inteira, **toda palavra leva apoio completo**. Logo abaixo do texto vem
sempre um controle recolhido "Em português corrido" com a tradução natural do texto
daquele dia. A tabela do alfabeto é permanente em todo cartão de grego, recolhida. Nunca
uma linha romanizada em paralelo. Uma nota de som por lição, sobre som presente no texto
daquele dia.

**17b · O planejador mantém o `exp`.** Todo domingo ele conta as aparições de cada palavra
nos textos publicados da semana e soma ao `exp` daquele item no Léxico. A contagem começou
na semana 2 (17/09/2026); a semana 1 não tem registro e não é reconstruída.

**18 · Nada é escrito.** Ele lê no telefone. Nenhum exercício pode exigir escrever,
digitar, copiar ou transcrever. Toda produção é mental, seguida imediatamente de um
modelo para comparação.

## Escrita

**19 · Português mínimo.** Fora da linha interlinear, glose apenas o que impede a
compreensão daquele texto, na forma `οἶκος — casa`: uma ou duas palavras, nunca uma
oração. Linha de contexto acima do texto: no máximo uma frase, e só quando o cenário não
for dedutível. Sem ensaios, sem comentário histórico.

**20 · Português neutro.** Registro instrucional claro e natural. Sem diminutivos,
coloquialismos ou idiomatismos. Escreva como um bom livro-texto.

**21 · Tom.** Comece pela lição. Sem saudação, sem preâmbulo, sem elogio. Ele está lendo
às 5h da manhã.

## Mundo

**22 · A história vem primeiro.** Cada pacote continua a vida de uma família em Ἀχαρναί,
primavera de 432 a.C. A gramática fica ao fundo: exposição repetida e contexto carregam o
aprendizado. A leitura é a lição; tudo o mais é menor que ela.

**23 · O mundo é real; a família não é.** Personagens e diálogos são inventados. Pessoas,
lugares, eventos, datas, cultos, rituais, festivais, instituições e objetos seguem a
bibliografia atual e nunca são inventados para melhorar uma cena. Mitos têm versões
atestadas — nunca invente variante. Nada posterior a 432 a.C. Onde a bibliografia
diverge, diga em uma linha ou omita o dado; nunca escolha um lado em silêncio.
**Verifique antes de compor, não depois.**

**24 · Sem etimologia.** Retirada em 17/09 junto com os demais acréscimos abaixo do texto
(ver 14). Se um dia voltar, volta como nota de uma linha, só de palavra do texto do dia,
apenas derivações genuínas — nunca semelhança sonora.

## Manifesto

**25 · Material canônico novo ganha linha no manifesto antes do fim do turno.** O
manifesto está em `README.md`. Um arquivo que ninguém nomeia se perde numa entrega ou é
tratado como rascunho pelo agente seguinte. Material que deixou de ser canônico sai da
tabela. Regra acordada em conversa que não entrou num arquivo não aconteceu.

Esta é a única invariante que o `validate.py` confere sozinho de ponta a ponta: arquivo
no repositório que não esteja na tabela reprova o build.

## Contrato de saída

Grego todo dia; italiano seg/qua/sex; inglês ter/qui/sáb; domingo é revisão, sem material
novo. Cada trilha tem no máximo 400 palavras de material, fora o gabarito. Se uma trilha
passar do limite, corte explicação antes de cortar texto — o input é o ponto.

Cada língua tem seu próprio cartão, todo dia, na mesma ordem: grego primeiro, depois
italiano ou inglês. Nunca duas línguas correndo juntas num mesmo bloco.

## Na dúvida

Prefira a construção atestada mais simples à mais engenhosa de que você não tem certeza.
No grego em especial: se não souber acentuar uma forma com segurança, escolha outra
palavra já no Léxico. **Um texto mais curto e certo vence um texto mais rico e duvidoso.**
O mesmo vale para fatos: cena mais pobre e correta vence cena mais rica e duvidosa.

---

## Reconciliação — 22/09/2026

O projeto mudou para um repositório Git. Três invariantes mudaram de redação e duas
deixaram de depender de disciplina.

| Antes | Agora | Por quê |
|---|---|---|
| 2 · escreva no arquivo, na página depois | 2 · a página é **gerada** por `build.py` | a cópia manual do JSON desapareceu junto com o passo que podia ser pulado |
| 3 · publique sempre com `url` | 3 · dados e página no mesmo commit | não há mais artifact para duplicar; o risco virou outro |
| 5 · preserve o design da página | 5 · o renderizador é um arquivo próprio | `page/template.html` e `state/week.json` não se tocam mais |
| 6 · execução não mexe no sistema | idem, **agora por permissão** | o token do workflow não consegue editar `.github/` |
| 25 · manifesto atualizado no mesmo turno | idem, **agora conferido** | `validate.py` reprova arquivo fora da tabela |

E uma invariante foi **aposentada sem substituta**: a que mandava manter o campo
Instructions em sincronia com este arquivo. A duplicação existia porque o campo era a
única entrega garantida a uma execução agendada. Num repositório, `AGENTS.md` cumpre esse
papel e a entrega diária não lê regra nenhuma, porque virou um script que não julga nada.
Uma fonte a menos para divergir é melhor que uma regra de sincronia bem escrita.

---

## Reconciliação — 21/09/2026

O estado saiu das artifacts e foi para arquivos do projeto. A página passou a ser um
renderizador. Isso mexeu nas primeiras invariantes e acrescentou duas.

| Antes | Agora | Por quê |
|---|---|---|
| 1 · leia o Acharnae Logbook | leia `state/logbook.md` | o estado é o arquivo; a artifact é espelho |
| 4 · preserve o design da página | 5 · a página é código; publicar é copiar o JSON | fecha o item B3: dado e renderização deixam de morar no mesmo HTML |
| 11 · o texto cresce, por disciplina | 12 · o texto cresce, por estrutura dos dados | `upTo` sobre uma lista única torna a violação impossível de escrever |
| — | 2 · os dados moram nos arquivos | era regra tácita; agora é invariante |
| — | 25 · manifesto atualizado no mesmo turno | era só uma linha de limitação no README |

A numeração andou: a antiga 2 virou 3, a 3 virou 4, a 5 virou 6, e daí em diante tudo
subiu um até a antiga 23, que virou 24. A antiga `16b` virou `17b`.

Nada foi removido.

---

## Reconciliação — 17/09/2026

Quatro mudanças, todas vindas de uso real, e uma renumeração.

| Antes | Agora | Por quê |
|---|---|---|
| Observação, Ἀνάμνησις, perguntas em grego e etimologia suspensas nas semanas 1–3 | a única janela é `exp` ≥ 5 para o Ἀνάμνησις | a suspensão foi inferência minha, nunca pedido dele, e estava errada |
| Transliteração em bloco no fim do cartão | formato interlinear, palavra por palavra, mais o português corrido recolhido | a transliteração em bloco obrigava a sair do texto e voltar — custo que fazia o texto não ser lido |
| Apoio some aos 5 encontros, sem contador definido | campo `exp` no Léxico, mantido pelo planejador | a regra existia sem o dado que a tornava aplicável |
| Cartão de grego com Ἐρωτήσεις, observação, Σκόπει, Θησαυρός e etimologia | quatro partes e nada mais | Mathews: o único exercício que ajudava era o Ἀνάμνησις |

Nota sobre esta última linha: é a segunda vez no mesmo dia que eu generalizei um elogio
pontual dele para uma aprovação geral. Regra prática que fica: **quando ele nomear uma
peça, mude aquela peça.**

---

## Reconciliação — 14/09/2026

Ao transpor do campo Instructions para arquivo, quatro invariantes estavam atrás de
decisões tomadas depois e já refletidas nos currículos e nos prompts. Ajustadas: a
observação passou a ter no máximo 2 linhas; o apoio de leitura passou de escada por lição
a decaimento por item; e três regras que existiam só em conversa foram promovidas a
invariante — leia o estado antes de publicar, preserve o design da página, e o texto
cresce dentro da semana.

### Nota sobre a forma do deploy

A primeira proposta foi esvaziar o campo Instructions e deixar só um ponteiro para este
arquivo, pelo argumento de que duas cópias divergem. Foi rejeitada, e com razão: o campo é
a única entrega garantida a uma execução agendada, e um ponteiro transformaria a leitura
das regras num passo que pode ser pulado silenciosamente. A duplicação aqui é o preço da
confiabilidade, e o que a torna administrável é a fonte declarada mais a regra de
sincronia — o mesmo arranjo de `TASK_PROMPTS.md`.
