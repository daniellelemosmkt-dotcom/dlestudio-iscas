# dlestudio-iscas: ler antes de escrever qualquer coisa

Este repositório é servido pelo GitHub Pages em **dlestudio.com.br**. Cada pasta
é um endereço no ar, e vários já foram mandados para clientes e alunas por
WhatsApp, e-mail e Eduzz. **Sobrescrever a página de uma pasta quebra um link
que já está na mão de alguém.**

Mais de uma sessão do Claude mexe aqui ao mesmo tempo. Em 22/10/2026 duas
sessões publicaram páginas diferentes em `/biblioteca/` no mesmo dia, e o link
que tinha acabado de ser mandado para 14 alunas passou a cair na página errada.

## A regra

Antes de escrever em `<pasta>/index.html`:

```bash
git log --oneline -5 -- <pasta>/index.html
```

Se a página de cima for de outra sessão e for de outro assunto, **não
sobrescreva**. Crie uma pasta nova com o endereço do seu assunto. Quem decide
qual página fica num endereço disputado é a Dani, não a sessão.

Vale o mesmo para `montar.py`: se a pasta tem um gerador, ele vai reescrever o
`index.html` na próxima execução. Não ponha conteúdo de outro assunto numa pasta
que tem gerador de outra pessoa.

## Quem é quem hoje

| Endereço | O que é | Para quem |
|---|---|---|
| `/` | DL Estúdio, a porta da frente | público |
| `/turma-fundadora/` | Biblioteca da Turma Fundadora, 12 partes | alunas do Modo Automático, R$ 552 |
| `/materiais/` | Materiais da Imersão Modo Automático | quem fez a imersão |
| `/biblioteca/` | A biblioteca, uma porta por material, com gerador `montar.py` | público |
| `/imersao/` | Claude do Zero, para iniciantes | público |
| `/claude-do-zero/` `/criar-robos/` `/social-media/` | Páginas de venda do Claude do Zero, variações A, B e C do teste de anúncio (mesmo checkout, `utm_content` A, B, C) | público, tráfego pago |
| `/diario/` | MAPA 20K, a edição viva | público |
| `/mapa/` | aviso de que o Diário mudou de endereço | público |
| `/grade/` | Grade viva, @daanylemos | interno |
| `/agenda/` `/cerebro/` `/codigos/` `/drive/` `/pauta/` `/plugin/` `/prompt/` `/reuniao/` `/skill/` | páginas de isca, uma por material grátis | público |

Pasta nova que entrar aqui, acrescente uma linha nesta tabela no mesmo commit.

## Antes de mandar um link para alguém

Confira que ele responde e que é a página certa:

```bash
curl -s https://dlestudio.com.br/<pasta>/ | grep -o '<title>[^<]*</title>'
```

O GitHub Pages leva de um a três minutos para publicar depois do push. Um `404`
logo após o push é normal; espere e confira de novo antes de mandar o link.

## Imagens e arquivos

As páginas de produto reaproveitam o que já existe, em vez de duplicar: os
ícones ficam em `materiais/img/` e os downloads em `biblioteca/arquivos/`. Uma
página dentro de uma pasta chega neles com `../materiais/img/...` e
`../biblioteca/arquivos/...`.
