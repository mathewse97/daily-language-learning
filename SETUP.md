# SETUP — como ligar isto no GitHub, do zero

Escrito para quem nunca usou GitHub. Não pressupõe nada: nem conta, nem terminal, nem
saber o que é um commit. São umas vinte a trinta minutos, uma vez só.

Se algum passo não bater com o que você vê na tela, o GitHub mudou o nome de um botão.
A lógica continua: **uma pasta de arquivos, uma cópia dela na nuvem, e duas automações
que leem essa cópia.**

---

## Antes de começar: público ou privado?

É a única decisão real deste documento, e ela tem consequência de dinheiro.

Na conta gratuita do GitHub, o Pages — a publicação da página — **só funciona em
repositório público**. Publicar a partir de um repositório privado exige um plano pago.
E, em qualquer plano abaixo do Enterprise, **a página publicada é pública de todo jeito**:
não existe site do Pages que peça login.

Então:

| | O repositório | A página | Custo |
|---|---|---|---|
| **Público** | qualquer um lê seus arquivos | pública | grátis |
| **Privado + plano pago** | só você | pública mesmo assim | mensalidade |

**Recomendo público.** O que está aqui é um curso de grego que você escreveu para si
mesmo — não há nada a proteger, e a página seria aberta nos dois casos. Repositório
público também tem Actions sem limite de minutos, enquanto o privado tem cota mensal.

Se mesmo assim quiser tudo fechado, a saída não é o GitHub: é hospedar a página no
Cloudflare Pages com Access, que pede login de verdade. Está descrito em `MIGRATION.md`.

---

## Vocabulário mínimo

Quatro palavras, e você não precisa de mais nenhuma:

- **Repositório** — uma pasta de arquivos com histórico. É o projeto inteiro.
- **Commit** — salvar uma mudança, com uma frase dizendo o que mudou.
- **Actions** — as automações que rodam sozinhas na nuvem.
- **Workflow** — uma dessas automações. Você tem duas: a entrega diária e o validador.

---

## Passo 1 · Conta no GitHub

Se já tem, pule. Senão, vá em **github.com**, clique em **Sign up** e siga. Use um e-mail
que você vá manter — é por ele que chegam os avisos de automação quebrada.

Guarde o **nome de usuário** que você escolher; ele aparece no endereço da sua página
depois.

---

## Passo 2 · Crie o repositório

Em **github.com**, clique no **+** no canto superior direito → **New repository**.

- **Repository name:** `daily-language-learning`
- Deixe **Public** marcado (ver a decisão lá em cima)
- **Não** marque "Add a README file" — já existe um
- O resto, em branco

Clique **Create repository**.

---

## Passo 3 · Prepare a pasta no seu computador

Descompacte o `.zip`. Dentro dele há uma pasta com o projeto inteiro: cinco pastas
(`.github`, `courses`, `docs`, `page`, `state`) e dezesseis arquivos soltos.

**Mostre os arquivos ocultos**, senão a pasta `.github` não aparece para ser arrastada —
e sem ela nada roda sozinho:

- **Mac:** `Cmd + Shift + .` no Finder
- **Windows:** aba **Exibir** → marque **Itens ocultos**

---

## Passo 4 · Envie tudo pelo navegador

Na tela que apareceu depois de criar o repositório, clique no link
**uploading an existing file**, no meio do texto.

Abra a pasta descompactada, selecione **tudo** (`Cmd+A` ou `Ctrl+A`) e arraste para a
área de upload.

> **O detalhe que estraga isto:** arraste as **pastas**, não o conteúdo delas. Se você
> entrar em `state/`, selecionar os quatro arquivos e arrastar, eles vão parar na raiz do
> repositório e o sistema não funciona. Selecione no nível de cima, onde as pastas
> aparecem como pastas.

A tela lista **arquivos, não pastas** — isso é normal. O que importa é o caminho: os
arquivos de dentro de pastas devem aparecer como `state/week.json`,
`.github/workflows/daily.yml`, com as barras. Se aparecerem só como `week.json` e
`daily.yml`, o upload achatou e você vai precisar refazer.

---

## Passo 5 · Commit

Embaixo, no campo de mensagem, escreva qualquer coisa que descreva o que você fez —
`primeiro commit` serve. É um bilhete para você mesmo daqui a um ano, não um comando.

Clique **Commit changes**.

**Confira agora**, antes de seguir. A página inicial do repositório tem de mostrar cinco
pastas — `.github`, `courses`, `docs`, `page`, `state` — e os arquivos soltos ao lado. Se
mostrar trinta e três arquivos soltos e nenhuma pasta, o upload achatou: apague o
repositório em **Settings → Danger Zone → Delete this repository** e refaça o passo 4,
arrastando as pastas inteiras.

---

> **Alternativa: GitHub Desktop.** Se preferir um programa a arrastar arquivos no
> navegador, **desktop.github.com** faz os passos 2 a 5 com botões: *File → New
> repository*, copie o conteúdo do ZIP para a pasta criada, escreva a mensagem, *Commit
> to main*, *Publish repository*. Ele resolve a pasta oculta sozinho. Daí em diante os
> passos são os mesmos.

---

## Passo 6 · Dê permissão de escrita às automações

Esse passo é o que mais gente esquece, e sem ele a entrega diária roda e falha no fim.

No site do repositório: **Settings** (a engrenagem, na barra de cima do repositório, não a
do seu perfil) → menu da esquerda, **Actions** → **General** → role até
**Workflow permissions** → marque **Read and write permissions** → **Save**.

Isso deixa a automação commitar a lição do dia. Ela continua sem poder editar as próprias
automações — o GitHub recusa isso por padrão, e é exatamente o que a invariante 6 pede.

---

## Passo 7 · Ligue a página

**Settings** → menu da esquerda, **Pages**.

- Em **Source**, escolha **Deploy from a branch**
- Em **Branch**, escolha **main**, e na caixa ao lado escolha **`/docs`**
- **Save**

Espere um ou dois minutos e recarregue a página de Settings → Pages. Vai aparecer o
endereço, mais ou menos assim:

```
https://SEU-USUARIO.github.io/daily-language-learning/
```

Abra. Se você vir a lição de hoje, está tudo funcionando.

> Se **Deploy from a branch** estiver cinza, o repositório é privado numa conta gratuita.
> Volte à decisão do começo: ou torne o repositório público em **Settings → General →
> Danger Zone → Change visibility**, ou assine um plano pago.

---

## Passo 8 · Teste a automação agora, sem esperar amanhã

Aba **Actions**, no topo do repositório → na lista da esquerda, **Morning Packet** → botão
**Run workflow** → **Run workflow** de novo, no menu que abre.

Recarregue. Em menos de um minuto aparece a execução. Clique nela para ver os passos.

- **Verde** — funcionou. Se não commitou nada, é porque o dia de hoje já estava publicado;
  isso é normal e correto.
- **Vermelho** — clique no passo vermelho e leia. As mensagens do `validate.py` são em
  português e dizem qual invariante quebrou.

---

## Passo 9 · O telefone

Abra o endereço do passo 7 no celular e adicione à tela de início:

- **iPhone (Safari):** botão de compartilhar → **Adicionar à Tela de Início**
- **Android (Chrome):** menu de três pontos → **Adicionar à tela inicial**

Vira um ícone. Abre como aplicativo. É a mesma URL para sempre — ela nunca muda, por mais
que o conteúdo mude todo dia.

---

## Pronto. O que acontece a partir de agora

**Segunda a sábado, sozinho.** Por volta das 04:40 o GitHub roda a entrega, regera a
página e commita. Você abre o ícone e a lição está lá. Não há nada a fazer.

**Domingo, com você.** Abra uma conversa com um agente que tenha acesso ao repositório,
dê as três notas do check-in e deixe ele compor a semana. O procedimento inteiro está em
`TASK_PROMPTS.md` — o agente lê de lá, você não precisa decorar nada.

Sem esse ritual de domingo, a semana seguinte não existe e a entrega de segunda falha de
propósito, em vez de inventar uma lição.

---

## Como mudar alguma coisa, depois

**O jeito normal:** peça em conversa. "Tire essa palavra da revisão", "conserta o
espaçamento do cartão de grego", "acrescenta uma frase ao texto de quinta". O agente lê as
regras, muda o arquivo certo, roda o validador e commita.

**Uma correção pequena, na mão:** no site do repositório, abra o arquivo, clique no lápis,
edite, e em **Commit changes** escreva o que mudou. Se você quebrar alguma coisa, o
validador reprova e o GitHub te avisa por e-mail — e o histórico guarda a versão anterior
de qualquer jeito.

**Nunca edite `docs/index.html`.** É gerado. O próximo build apaga o que você fizer.

---

## Quando algo der errado

O lugar é sempre a aba **Actions**. Toda execução fica registrada, com o que rodou e o que
falhou, e as mensagens de erro foram escritas para serem lidas por você, não por um
programador. `OPERATIONS.md` tem a lista das falhas já vistas e o que fazer com cada uma.

E o essencial: **nada aqui se perde.** Todo commit fica no histórico, e qualquer versão
anterior de qualquer arquivo pode voltar. Foi para isso que o projeto veio para cá.
