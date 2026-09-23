# MIGRATION — como sair do GitHub sem perder nada

Este documento existe para o dia em que você quiser tirar o projeto do GitHub. Ele não
precisa ser executado nunca, e nada no sistema depende dele. Está aqui porque um sistema
que não sabe explicar como se desmonta não é independente — é só ainda não ter sido
testado.

## O que é seu e o que é do GitHub

**Seu, e suficiente para o sistema inteiro:** todos os arquivos `.md`, `.json`, `.py` e
`.html` do repositório. Baixe a pasta e você tem as regras, os currículos, o vocabulário,
a posição do curso, a semana em curso, o renderizador, o gerador e o validador.

**Do GitHub, e substituível:** o agendamento (`.github/workflows/`), a publicação
(Pages) e o histórico de commits. Nada disso guarda dado — guardam *conveniência*.

O teste é simples: com a pasta na mão e sem conexão nenhuma, você roda
`python3 build.py` e abre `docs/index.html` no navegador. A lição de hoje está lá. Foi
para isso que o conteúdo virou dado.

## Os scripts não dependem de nada

`build.py`, `validate.py` e `daily.py` usam só a biblioteca padrão do Python. Sem `pip`,
sem `requirements.txt`, sem ambiente virtual. Qualquer Python 3.11 ou mais novo roda os
três. Isso foi escolha, não acaso: dependência é a forma mais comum de um projeto parar
de funcionar sozinho três anos depois.

## Como sair, em quatro passos

1. **Baixe a pasta.** No GitHub, botão verde **Code** → **Download ZIP**. Ou, se tiver o
   GitHub Desktop, a pasta já está no seu computador — é a mesma.

2. **Verifique que está tudo lá.** Na pasta, rode `python3 validate.py`. Se passar, o
   repositório está íntegro e completo. É o mesmo teste que o GitHub fazia.

3. **Substitua o agendamento.** O que rodava todo dia era uma linha:
   `python3 daily.py`. As opções, da mais simples à mais robusta:
   - rodar à mão quando abrir a lição — é um comando;
   - `cron` no seu computador, ou o Agendador de Tarefas no Windows;
   - qualquer outro serviço de automação que saiba rodar um script Python.

4. **Substitua a publicação.** `docs/index.html` é um arquivo HTML comum, sem servidor e
   sem dependência externa além das fontes do Google. Ele funciona:
   - aberto direto do disco, com dois cliques;
   - numa pasta sincronizada (Dropbox, iCloud, Drive) que o telefone alcança;
   - em qualquer hospedagem estática — Netlify, Cloudflare Pages, um servidor seu.
   Se privacidade for o motivo da saída, Cloudflare Pages com Access resolve o que o
   GitHub Pages não resolve: lá o site pode exigir login de verdade.

## O que muda de verdade

**O `validate.py` deixa de rodar sozinho.** É a maior perda, e vale saber o tamanho dela:
no GitHub ele roda em todo commit e reprova o que estiver errado. Fora dele, é um comando
que alguém precisa lembrar de rodar. Se você sair, ponha a chamada dentro do mesmo
agendamento que roda o `daily.py` — o script já valida antes e depois.

**O histórico fica para trás,** a menos que você leve a pasta `.git` junto (o Download
ZIP não a inclui; copiar a pasta do GitHub Desktop, sim). Não é dado do curso, mas é o
registro de como ele chegou até aqui.

**A regra 6 volta a ser honra.** No GitHub, uma automação não consegue editar o próprio
agendamento porque não tem permissão. Num `cron` seu, nada impede — volta a depender de
quem escreve respeitar a regra.

## O que não existe

**Não há caminho de volta.** Sair é sair. Se um dia você quiser voltar ao GitHub, é criar
um repositório novo e subir a pasta — o `SETUP.md` continua valendo, e o estado vai junto
porque o estado são os arquivos.
