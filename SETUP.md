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
- **Push** — mandar seus commits para a cópia na nuvem.
- **Actions** — as automações que rodam sozinhas na nuvem.

---

## Passo 1 · Conta no GitHub

Se já tem, pule. Senão, vá em **github.com**, clique em **Sign up** e siga. Use um e-mail
que você vá manter — é por ele que chegam os avisos de automação quebrada.

Guarde o **nome de usuário** que você escolher; ele aparece no endereço da sua página
depois.

---

## Passo 2 · Instale o GitHub Desktop

**desktop.github.com** → baixe → instale → abra → **Sign in to GitHub.com** e entre com a
conta do passo 1.

O GitHub Desktop é um programa com botões. Ele faz tudo o que você vai precisar sem uma
única linha de comando. Não instale mais nada.

> Existe um jeito de fazer tudo pelo site, arrastando arquivos. Não recomendo: a pasta
> `.github`, que guarda as automações, começa com ponto, e o Finder e o Explorer escondem
> pastas assim — você arrastaria o projeto sem as automações e não entenderia por quê.

---

## Passo 3 · Crie o repositório

No GitHub Desktop: **File → New repository**.

- **Name:** `daily-language-learning`
- **Local path:** onde você quiser no seu computador. Anote o caminho.
- **Initialize with a README:** deixe **desmarcado** — já existe um.
- O resto, em branco.

Clique **Create repository**. Agora existe uma pasta vazia no seu computador, com
histórico ligado.

---

## Passo 4 · Ponha os arquivos na pasta

Descompacte o `.zip` que eu te mandei. Dentro dele há uma pasta com todo o projeto.

**Copie o *conteúdo* dessa pasta para dentro da pasta que o GitHub Desktop criou** — não
a pasta inteira, o conteúdo dela. No fim, dentro de `daily-language-learning` você deve
ver `README.md`, `build.py`, `courses`, `state`, `page`, `docs` e as outras.

**Confira que a pasta `.github` veio junto.** Ela é invisível por padrão:
- no Mac, aperte `Cmd + Shift + .` no Finder para mostrar arquivos ocultos;
- no Windows, aba **Exibir** → marque **Itens ocultos**.

Se `.github` não estiver lá, as automações não existem e nada vai rodar sozinho.

---

## Passo 5 · Primeiro commit

Volte ao GitHub Desktop. Ele agora lista dezenas de arquivos novos.

- No campo **Summary**, embaixo à esquerda, escreva: `Sistema completo, vindo do Claude Project`
- Clique **Commit to main**
- Clique **Publish repository** no topo

Uma caixa aparece com **Keep this code private** marcado. **Desmarque**, se você escolheu
público no começo. Clique **Publish repository**.

Pronto — seus arquivos estão na nuvem. Dá para ver em
`github.com/SEU-USUARIO/daily-language-learning`.

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

**Segunda a sábado, sozinho.** Por volta das 05:20 o GitHub roda a entrega, regera a
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
