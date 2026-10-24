"""Monta a /diario: o Diario da Dani, com cara de documento e nao de pagina de isca.

Desenho de 24/10, pedido dela: cabecalho de blog com a foto redonda, coluna estreita de leitura,
papel com grao, anotacoes a mao na margem, porta que parece conversa e nao formulario, e
navegacao por capitulos.

O TEXTO DOS CAPITULOS E DELA, PALAVRA POR PALAVRA, do documento
1I6c8fuR7bK0jSWKHFT1dJhllARf_fHSyzxHd7af_F_4. Nao escrever nada por conta: ela ja reprovou isso
uma vez, com razao. O que e meu aqui e so a casca: titulos de navegacao, as linhas de
atualizacao e as anotacoes de margem, que sao marcadas como tal.

DO BANCO, ao vivo: o placar (public.diario_placar, que le dlestudio.metricas_perfil e por isso
nunca fica velho). A navegacao vem dos capitulos escritos aqui.

A PORTA grava em dlestudio.leads pela funcao lead-isca-dlestudio. Dois campos viajam disfarcados,
porque a edge function so repassa campos fixos e nao deu para redeploya-la:
  * profissao  -> a resposta de "qual desses e voce hoje", que a funcao do banco copia para
                  a coluna interesse;
  * origem     -> "diario+sim" ou "diario+nao", e o sufixo vira aceite_whatsapp no banco.
Sem o sim, aceite_whatsapp fica false e a pessoa nao entra em disparo nenhum.

Uso: python montar.py   ->  index.html nesta pasta
"""
import base64
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ASSETS = Path("G:/Meu Drive/DANIELLE   PROJETOS/PRODUTOS DL ESTÚDIO/04 KIT E PLUGINS/_paginas/assets")
ROSTO = Path("C:/Users/Micro/dl-work/daanylemos-plugin/referencias/rosto-selfie-caneca.jpg")

ADV = "data:font/woff2;base64," + base64.b64encode((ASSETS / "Advercase-Regular.woff2").read_bytes()).decode()
FOTO = "data:image/jpeg;base64," + base64.b64encode(ROSTO.read_bytes()).decode()

PIXEL = (
    '<!-- Meta Pixel -->\n<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?'
    'n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";'
    'n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}'
    '(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","2130554737847082");'
    'fbq("track","PageView");</script>\n<noscript><img height="1" width="1" style="display:none" '
    'src="https://www.facebook.com/tr?id=2130554737847082&ev=PageView&noscript=1"/></noscript>\n<!-- /Meta Pixel -->'
)

# ---------------------------------------------------------------- os capitulos
# 'corpo' e o texto DELA. 'margens' sao as anotacoes a mao, que sao minhas e vao na margem.
CAPITULOS = [
    {
        "n": 1, "data": "22 de outubro", "titulo": "O mapa, antes de começar",
        "atualizacao": "escrevi o plano inteiro antes de publicar o primeiro vídeo, para não poder mudar a história depois que os números saírem",
        "margens": [
            (1, "isso aqui é o combinado comigo mesma"),
            (4, "guarda essa ordem, ela é o pulo do gato"),
            (8, "nenhuma isca nasce sem o post pedir"),
        ],
        "corpo": """
<p><b>Isto não é uma promessa de resultado.</b> É o mapa do experimento que eu estou executando no meu próprio perfil. A ideia é documentar o processo, medir o que realmente acontece e ir mudando a estratégia com base em dados, não em opinião.</p>

<h3>1. A mudança principal</h3>
<p>Durante muito tempo eu tratei conteúdo assim: “qual dica eu vou ensinar hoje?”</p>
<p>Só que comecei a estudar perfis que estavam crescendo muito mais rápido e percebi um padrão.</p>
<p>Os conteúdos que mais prendiam não começavam ensinando. Começavam com alguma coisa acontecendo.</p>
<ul><li>Uma meta.</li><li>Um problema.</li><li>Um teste.</li><li>Um número.</li><li>Uma decisão.</li><li>Uma coisa que deu errado.</li><li>Uma coisa que a pessoa construiu.</li><li>Uma história que ainda não terminou.</li></ul>
<p>Então a minha estratégia para estas 16 semanas é simples:</p>
<p class="solta">Parar de criar posts isolados e começar a construir histórias que continuam.</p>
<p>A pergunta que eu quero deixar na cabeça de quem me encontra é: “o que vai acontecer com isso?”</p>

<h3>2. O experimento</h3>
<p>Ponto de partida: <b>3.883 seguidores</b>. Destino: <b>20.000 seguidores</b>. Prazo: <b>16 semanas</b>.</p>
<p>O meu conteúdo vai girar em torno de uma história principal:</p>
<p class="cita">“Eu trabalho com conteúdo todos os dias, ensino IA, tenho clientes e equipe, mas meu próprio perfil ainda está em 3.883 seguidores. Quero descobrir se consigo mudar isso em 16 semanas mostrando o que realmente acontece no meu trabalho.”</p>
<p>Isso cria três coisas ao mesmo tempo: um destino concreto, uma pergunta que ainda não tem resposta, e um motivo para acompanhar o processo.</p>

<h3>3. O que eu vou publicar</h3>
<p>Não vou abandonar conteúdo educativo. Eu só vou mudar a ordem.</p>
<p>Antes: tema, explicação, CTA. Agora: acontecimento, tensão, prova, descoberta, próxima ação.</p>
<p>Os conteúdos vão cair principalmente em quatro grupos.</p>
<p><b>A. O experimento de crescimento.</b> O que eu testei, o que trouxe mais seguidores, o que teve alcance e não converteu, o que eu achei que ia funcionar e morreu, o que eu repeti porque deu sinal de funcionar, placares semanais, e as mudanças que os dados me obrigaram a fazer.</p>
<p><b>B. O que está mudando no meu trabalho com IA.</b> Não é “5 coisas que o Claude faz”. É o que eu fazia manualmente e deixei de fazer, o que eu consegui construir, onde a IA errou, o que precisei ensinar, o que virou sistema, o que virou produto, e o que eu ainda não consegui resolver.</p>
<p><b>C. O que eu estou aplicando nas contas dos clientes.</b> A regra aqui é importante: eu não vou inventar resultado. Vou mostrar decisões reais. Se eu aprender alguma coisa analisando meu próprio perfil e isso mudar um gancho, uma pauta, um formato ou uma escolha numa conta de cliente, eu posso abrir esse raciocínio. A cliente deixa de ver “a Dani estudando Instagram”. Ela vê: “a Dani testa, aprende e aplica”.</p>
<p><b>D. Os bastidores humanos.</b> Nem todo conteúdo precisa ensinar. Também entram dúvidas, decisões, coisas que me irritaram, erros, opiniões, situações da rotina, coisas que eu achava e mudei de ideia, e pequenos bastidores que fazem alguém conhecer a pessoa por trás do trabalho.</p>

<h3>4. A estrutura dos vídeos</h3>
<div class="passos">
  <div><div><b>Cena</b>Quem eu sou ou onde eu estou, de um jeito que a pessoa consiga imaginar.</div></div>
  <div><div><b>Tensão</b>O que estou tentando, o que não está funcionando ou o que aconteceu.</div></div>
  <div><div><b>Destino</b>O que eu quero conseguir, com número, prazo ou consequência concreta.</div></div>
  <div><div><b>Prova</b>Tela, número, arquivo, antes e depois, resultado, comentário, dado, vídeo, processo real.</div></div>
  <div><div><b>Virada</b>O que isso me fez perceber ou mudar.</div></div>
  <div><div><b>CTA</b>Uma próxima ação que faça sentido para a curiosidade que o conteúdo abriu.</div></div>
</div>

<h3>5. Por que eu acho que isso pode funcionar</h3>
<p>Não porque “história funciona melhor”. Porque essa estrutura resolve quatro problemas do conteúdo comum.</p>
<p><b>Problema 1: dica demais e contexto de menos.</b> Quando o conteúdo começa pela história, a pessoa entende por que deveria se importar antes de receber a explicação.</p>
<p><b>Problema 2: todo post parece começar do zero.</b> Quando existe uma série, um conteúdo aumenta o valor do próximo.</p>
<p><b>Problema 3: a pessoa aprende e vai embora.</b> Quando existe uma pergunta aberta, existe mais motivo para seguir.</p>
<p><b>Problema 4: o criador precisa inventar assunto todos os dias.</b> Quando você documenta o que já está vivendo, o próprio trabalho começa a produzir pauta.</p>

<h3>6. O que eu vou medir</h3>
<p>Eu não vou usar curtida como principal sinal de sucesso. Quero acompanhar:</p>
<ul><li>alcance de não seguidores;</li><li>visitas ao perfil;</li><li>seguidores gerados por conteúdo;</li><li>compartilhamentos;</li><li>comentários;</li><li>DMs iniciadas pelas iscas;</li><li>quais conteúdos fazem a pessoa pedir continuação;</li><li>quais mecanismos funcionam mais de uma vez.</li></ul>
<p class="solta">Este conteúdo fez alguém que não me conhecia querer continuar comigo?</p>

<h3>7. Como vou decidir o que repetir</h3>
<p>Quando um conteúdo se destacar, eu não vou abandonar a ideia no dia seguinte. Vou desmontar o que aconteceu: qual foi a promessa, como começou, qual foi a tensão, qual prova apareceu, onde estava a virada, qual foi o CTA, e que comentários se repetiram.</p>
<p>Depois vou manter o mecanismo e trocar a história.</p>
<p>Não repetir: “falar de 22 vídeos de novo”. Repetir: “começar com uma situação concreta, revelar um gargalo invisível, mostrar prova e terminar com uma consequência”.</p>

<h3>8. O papel das iscas</h3>
<p>Durante esse sprint eu quero transformar comentário em conversa. Mas a isca precisa nascer do conteúdo. Nada de “comenta GUIA que eu mando um PDF aleatório”.</p>
<p class="cita">o vídeo abre uma curiosidade → o material entrega exatamente a parte que ficou faltando → a pessoa comenta para receber</p>
<p><b>MAPA</b>, este material que você está lendo. <b>OUTLIER</b>, ficha para analisar um post fora da curva sem copiar o assunto. <b>SPRINT</b>, scorecard para acompanhar um experimento de crescimento. <b>EDITOR</b>, demonstração de como um sistema de edição com Claude funciona. <b>ROTEIRO</b>, estrutura para transformar uma história real em um Yap.</p>

<h3>9. Como adaptar para outros nichos</h3>
<p>A estratégia não depende de falar sobre marketing ou IA. Ela depende de ter:</p>
<p class="solta">uma pessoa + uma situação real + um destino + uma história ainda aberta.</p>
<div class="par"><div class="antes"><span class="rot">Médica · em vez de</span>5 sintomas da menopausa.</div>
<div class="depois"><span class="rot">Pode ser</span>Eu atendo mulheres há X anos e comecei a anotar as dúvidas que mais se repetem no consultório. Quero responder 30 delas em 30 dias usando exatamente as palavras que minhas pacientes usam.</div></div>
<div class="par"><div class="antes"><span class="rot">Social media · em vez de</span>3 dicas para organizar clientes.</div>
<div class="depois"><span class="rot">Pode ser</span>Tenho X clientes e percebi que ainda perco tempo toda semana procurando as mesmas informações. Estou reconstruindo meu processo para parar de depender da minha memória.</div></div>
<div class="par"><div class="antes"><span class="rot">Nutricionista · em vez de</span>como emagrecer com saúde.</div>
<div class="depois"><span class="rot">Pode ser</span>Durante 30 dias eu vou responder as 30 frases que mais escuto de pacientes que acham que precisam comer perfeito para emagrecer.</div></div>
<div class="par"><div class="antes"><span class="rot">Loja · em vez de</span>conheça nossos produtos.</div>
<div class="depois"><span class="rot">Pode ser</span>Temos X peças paradas há meses. Quero descobrir em 30 dias quais delas não vendem por causa do produto e quais não vendem porque estamos mostrando errado.</div></div>
<div class="par"><div class="antes"><span class="rot">Prestador de serviço · em vez de</span>5 motivos para contratar.</div>
<div class="depois"><span class="rot">Pode ser</span>Nos próximos 30 dias eu vou abrir os erros mais caros que eu encontro quando alguém chega até mim, e mostrar como eu resolveria cada um.</div></div>
<div class="par"><div class="antes"><span class="rot">Criador · em vez de</span>dicas de lançamento.</div>
<div class="depois"><span class="rot">Pode ser</span>Quero construir meu próximo produto só a partir do que a audiência pedir durante as próximas semanas.</div></div>

<h3>10. O exercício para criar a sua série</h3>
<div class="ficha">
  <span>Eu sou</span><i>quem você é numa cena concreta</i>
  <span>Hoje estou</span><i>situação real</i>
  <span>O que não está funcionando</span><i>o problema</i>
  <span>Quero</span><i>destino concreto</i>
  <span>Até</span><i>prazo</i>
  <span>Vou mostrar</span><i>provas e acontecimentos que podem virar episódios</i>
  <span>A pergunta que quero deixar aberta</span><i>será que ela consegue o quê?</i>
</div>
<p class="cita">“Sou social media e cuido de 8 clientes. Toda segunda eu ainda começo o dia procurando informação espalhada em WhatsApp, Drive e reunião. Quero passar 30 dias reconstruindo esse processo até abrir a semana sabendo exatamente o que precisa da minha decisão. Vou mostrar o que funcionar e o que continuar me dando trabalho.”</p>

<h3>11. A regra mais importante</h3>
<p class="solta">Não invente uma jornada porque você precisa de conteúdo. Olhe para o que já está acontecendo.</p>
<ul><li>O que você está tentando?</li><li>O que está difícil?</li><li>O que você está construindo?</li><li>Que número você quer mudar?</li><li>Que pergunta ainda não sabe responder?</li><li>O que deu errado esta semana?</li><li>O que alguém pediu para você?</li><li>O que você aprendeu e aplicou?</li></ul>
<p>É daí que nasce a série.</p>

<h3>12. O meu combinado</h3>
<p>Eu vou abrir os testes, os números, as coisas que funcionarem, as coisas que morrerem, as mudanças de rota, os bastidores, e o papel que a IA tiver de verdade nesse processo.</p>
<p>Sem fingir que eu já sei a resposta.</p>
""",
    },
    {
        "n": 2, "data": "24 de outubro", "titulo": "Eu achei que tinha assuntos demais",
        "atualizacao": "passei a semana achando que estava criando quatro perfis dentro de um só, até descobrir que não eram assuntos concorrentes, eram camadas",
        "margens": [
            (1, "quatro perfis dentro de um só, juro"),
            (3, "cada coisa tem uma função, e só"),
            (5, "parei de adivinhar o produto"),
        ],
        "corpo": """
<p>Depois de começar a gravar essa série, eu fiquei confusa.</p>
<p>Meu perfil já estava crescendo em torno de Claude. Eu já tinha criado produto sobre Claude. Eu tinha uns 40 vídeos gravados ensinando Claude. Ao mesmo tempo, comecei a estudar Stella, Meg e Jessica para entender por que os vídeos delas fazem as pessoas acompanharem uma história. E no meio das gravações eu comecei a colocar ideias de livros que estavam influenciando minhas decisões.</p>
<p class="solta">Por alguns dias, pareceu que eu estava criando quatro perfis diferentes dentro de um só.</p>
<p>Até que eu organizei assim:</p>

<div class="camadas">
  <div class="camada"><b>A história principal</b><span>construir uma marca pessoal e tentar sair de 3.883 para 20.000 em 16 semanas</span></div>
  <div class="seta" aria-hidden="true"></div>
  <div class="camada"><b>Claude</b><span>ferramenta real, assunto que já atrai audiência e produto validado</span></div>
  <div class="seta" aria-hidden="true"></div>
  <div class="camada"><b>Livros</b><span>repertório que muda decisões, testes e a forma como eu interpreto dados</span></div>
  <div class="seta" aria-hidden="true"></div>
  <div class="camada"><b>Stella, Meg e Jessica</b><span>referências de estrutura e narrativa</span></div>
  <div class="seta" aria-hidden="true"></div>
  <div class="camada"><b>Clientes</b><span>segundo laboratório: o que funciona aqui também funciona fora daqui?</span></div>
</div>

<p>A conclusão foi simples: eu não preciso escolher entre falar de Claude, marketing, livros ou bastidores.</p>
<p>Eu preciso saber qual função cada coisa cumpre dentro da mesma história.</p>
<p>A partir de agora, minha regra é:</p>
<ul>
  <li><b>Claude</b> me ajuda a ser descoberta.</li>
  <li><b>A série</b> me ajuda a ser acompanhada.</li>
  <li><b>Os livros</b> me ajudam a pensar melhor.</li>
  <li><b>Os clientes</b> me ajudam a testar se o aprendizado sobrevive fora do meu perfil.</li>
  <li><b>Os dados</b> decidem o que merece virar método.</li>
</ul>

<p>E eu também mudei outra coisa.</p>
<p>Eu estava tentando descobrir cedo demais o que deveria vender no final.</p>
<p class="solta">Então eu parei.</p>
<p>Quem pedir acesso a este Diário vai começar a me mostrar o que quer acompanhar comigo:</p>

<div class="marcacoes" id="marcacoes"></div>

<p>Eu vou acompanhar essas respostas junto com comentários, directs, pedidos e padrões que surgirem.</p>
<p>O produto futuro não vai ser escolhido porque eu tive uma ideia boa. Ele vai precisar aparecer como demanda.</p>

<h3>Meu ritmo de conteúdo agora</h3>
<p>Todo dia, em média:</p>
<p><b>Post 1, descoberta e utilidade.</b> Claude, sistemas, automações, casos reais, conteúdos que entregam alguma coisa imediatamente.</p>
<p><b>Post 2, continuidade e marca.</b> Um episódio da série, uma decisão, um insight de livro aplicado, um experimento, um resultado ou um bastidor que faça esta história andar.</p>
<p>Não significa dois posts rígidos para sempre. Significa duas funções diferentes. Uma peça faz uma pessoa nova chegar. A outra dá motivo para ela continuar.</p>
<p>E uma vez por semana eu quero testar a mesma ideia em dois formatos. O primeiro caso já existe: “O Claude fez esse post do zero”. Esse conteúdo já me trouxe 7 seguidores. Agora eu quero testar o mesmo núcleo em outro formato e comparar não só visualização, mas quantas pessoas realmente entraram no perfil e decidiram ficar.</p>
<p class="solta">O que está fazendo este perfil crescer, e o que só parece estar funcionando?</p>
""",
    },
]

# As cinco respostas da porta. Sao as mesmas do capitulo 2, e e de proposito:
# a pessoa le no capitulo exatamente o que ela acabou de responder.
CAMINHOS = [
    ("claude_automacao", "Quero colocar a IA para trabalhar por mim", "Claude + automação"),
    ("crescimento_marca", "Quero fazer o meu perfil crescer", "crescimento + marca pessoal"),
    ("conteudo_vende", "Quero que o meu conteúdo venda", "conteúdo que vende"),
    ("operacao_social", "Sou social media e quero organizar a operação", "operação / social media"),
    ("acompanhar", "Por enquanto só quero acompanhar", "outra coisa"),
]

PERIODOS = ["22 a 28 de outubro", "29 de outubro a 4 de novembro", "5 a 11 de novembro",
            "12 a 18 de novembro", "19 a 25 de novembro", "26 de novembro a 2 de dezembro",
            "3 a 9 de dezembro", "10 a 16 de dezembro", "17 a 23 de dezembro",
            "24 a 30 de dezembro", "31 de dezembro a 6 de janeiro", "7 a 13 de janeiro",
            "14 a 20 de janeiro", "21 a 27 de janeiro", "28 de janeiro a 3 de fevereiro",
            "4 a 11 de fevereiro"]

escritos = {c["n"]: c for c in CAPITULOS}
ultimo = max(escritos)

nav = []
for i in range(1, 17):
    c = escritos.get(i)
    if c:
        marca = '<span class="novo">novo</span>' if i == ultimo else ""
        nav.append(f'<a class="cap-link" href="#cap{i}"><span class="cap-n">Capítulo {i}</span>'
                   f'<span class="cap-t">{c["titulo"]}</span>{marca}</a>')
    else:
        nav.append(f'<span class="cap-link vazio"><span class="cap-n">Capítulo {i}</span>'
                   f'<span class="cap-t">{PERIODOS[i-1]}</span><span class="depois">a escrever</span></span>')
NAV = "\n      ".join(nav)


def monta_capitulo(c):
    corpo = c["corpo"].strip()
    # as anotacoes de margem entram depois do n-esimo paragrafo de primeiro nivel
    pedacos = corpo.split("\n")
    saida, p = [], 0
    usadas = {pos: txt for pos, txt in c["margens"]}
    for linha in pedacos:
        saida.append(linha)
        if linha.startswith("<p>") or linha.startswith('<p class="solta">'):
            p += 1
            if p in usadas:
                saida.append(f'<aside class="margem">{usadas[p]}</aside>')
    return f"""  <article class="capitulo" id="cap{c['n']}">
    <div class="cap-cab">
      <span class="cap-sel">Capítulo {c['n']}</span>
      <h2>{c['titulo']}</h2>
      <p class="atualizacao"><b>Atualização · {c['data']}</b> · {c['atualizacao']}</p>
    </div>
{chr(10).join(saida)}
  </article>"""


CAPS_HTML = "\n".join(monta_capitulo(c) for c in CAPITULOS)

PASSOS_PORTA = "\n".join(
    f'      <button class="caminho" type="button" data-v="{rot}">{rot}</button>'
    for _id, rot, _eco in CAMINHOS)

MARCACOES = "".join(f'<span class="marca" data-eco="{eco}"><i></i>{eco}</span>' for _i, _r, eco in CAMINHOS)

HTML = f"""<!doctype html>
<html lang="pt-BR">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Como vou sair dos 3K para os 20K? | Danielle Lemos</title>
<meta name="description" content="O diário aberto de um experimento de 16 semanas: o que eu testei, o que funcionou, o que não funcionou e como adaptar para qualquer nicho.">
<meta property="og:title" content="Como vou sair dos 3K para os 20K?">
<meta property="og:description" content="Não sei se vou bater a meta, mas vou registrar aqui tudo que eu testei.">
{PIXEL}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Homemade+Apple&display=swap">
<style>
@font-face{{font-family:"Advercase";src:url({ADV}) format("woff2");font-weight:400;font-display:swap}}
:root{{
  --papel:#F7F4EE; --papel-2:#FFFDF8; --tinta:#2B2522; --tinta-2:#5C534E; --tinta-3:#8A8078;
  --margem:#E6DCCD; --mag:#8B083F; --acesa:#E2307A; --noite:#160E11; --pessego:#FCEADF;
  --disp:"Advercase","Playfair Display",Georgia,serif; --txt:"Poppins","Segoe UI",Arial,sans-serif;
  --mao:"Homemade Apple",cursive;
  color-scheme:light;
}}
*{{box-sizing:border-box}}
html{{background:var(--papel);scroll-behavior:smooth}}
body{{margin:0;background:var(--papel);color:var(--tinta);font:400 17.5px/1.85 var(--txt);-webkit-font-smoothing:antialiased;overflow-x:hidden}}
body::after{{content:"";position:fixed;inset:0;pointer-events:none;z-index:50;opacity:.5;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='g'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/><feColorMatrix type='saturate' values='0'/></filter><rect width='180' height='180' filter='url(%23g)' opacity='.055'/></svg>")}}
.faixa{{padding-left:max(20px,env(safe-area-inset-left,0px));padding-right:max(20px,env(safe-area-inset-right,0px))}}
.wrap{{max-width:680px;margin:0 auto}}
h1,h2,h3{{text-wrap:balance;margin:0}}
p{{margin:0}}
a{{color:var(--mag)}}
:focus-visible{{outline:3px solid var(--acesa);outline-offset:3px;border-radius:6px}}

/* cabecalho de blog */
.topo{{padding-block:clamp(36px,6vw,64px) clamp(22px,3vw,34px)}}
.perfil{{display:flex;gap:14px;align-items:center}}
.perfil img{{width:58px;height:58px;border-radius:50%;object-fit:cover;object-position:50% 22%;border:2px solid var(--papel-2);box-shadow:0 2px 10px rgba(43,37,34,.14)}}
.perfil b{{display:block;font:600 16px/1.2 var(--txt)}}
.perfil span{{display:block;font:400 14px/1.3 var(--txt);color:var(--tinta-3)}}
h1{{font:400 clamp(34px,6.6vw,58px)/1.06 var(--disp);letter-spacing:-.02em;margin-top:26px}}
.mao{{font:400 clamp(17px,2.6vw,21px)/1.65 var(--mao);color:var(--tinta-3);margin-top:20px;max-width:30em}}

/* placar, discreto, como linha de documento */
.placar{{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--margem);border-bottom:1px solid var(--margem);margin-top:30px}}
@media(min-width:560px){{.placar{{grid-template-columns:repeat(4,1fr)}}}}
.placar div{{padding:14px 10px 14px 0}}
.placar div:nth-child(-n+2){{border-bottom:1px solid var(--margem)}}
@media(min-width:560px){{.placar div:nth-child(-n+2){{border-bottom:0}}}}
.placar .n{{font:400 clamp(22px,3.4vw,30px)/1 var(--disp)}}
.placar .n.viva{{color:var(--mag)}}
.placar .r{{font:600 10px/1.3 var(--txt);letter-spacing:.14em;text-transform:uppercase;color:var(--tinta-3);margin-top:5px}}
.placar-data{{font-size:13.5px;color:var(--tinta-3);margin-top:10px}}

/* a porta: uma pergunta por vez */
.porta{{padding-block:clamp(30px,5vw,54px)}}
.conversa{{border-top:1px solid var(--margem);padding-top:clamp(26px,4vw,40px)}}
.pergunta{{display:none}}
.pergunta.ativa{{display:block;animation:sobe .35s ease}}
@keyframes sobe{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
.pergunta h2{{font:400 clamp(24px,3.8vw,34px)/1.2 var(--disp)}}
.pergunta .ajuda{{color:var(--tinta-3);margin-top:10px;font-size:16px}}
.pergunta input{{width:100%;margin-top:18px;font:400 20px/1.5 var(--txt);color:var(--tinta);
  background:transparent;border:0;border-bottom:2px solid var(--margem);padding:8px 2px}}
.pergunta input:focus{{outline:0;border-bottom-color:var(--mag)}}
.caminho{{display:block;width:100%;text-align:left;margin-top:10px;cursor:pointer;
  background:var(--papel-2);border:1px solid var(--margem);border-radius:14px;
  padding:17px 18px;font:500 16.5px/1.35 var(--txt);color:var(--tinta)}}
.caminho:hover,.caminho:focus-visible{{border-color:var(--mag);background:#fff}}
.sim-nao{{display:flex;gap:10px;margin-top:18px;flex-wrap:wrap}}
.sim-nao button{{flex:1 1 130px;cursor:pointer;border-radius:999px;padding:16px 20px;font:600 16px/1 var(--txt)}}
.sim{{background:var(--mag);color:#fff;border:0}}
.nao{{background:transparent;color:var(--tinta-2);border:1px solid var(--margem)}}
.avancar{{margin-top:20px;cursor:pointer;background:var(--mag);color:#fff;border:0;border-radius:999px;padding:16px 30px;font:600 16px/1 var(--txt)}}
.avancar[disabled]{{opacity:.45;cursor:default}}
.erro{{color:var(--mag);font-size:14.5px;margin-top:10px;min-height:1em}}
.passo-conta{{font:600 11px/1 var(--txt);letter-spacing:.14em;text-transform:uppercase;color:var(--tinta-3);margin-bottom:14px}}

/* o diario */
.trancado{{display:none}}
body.liberado .trancado{{display:block}}
body.liberado .porta{{display:none}}

.indice{{border-top:1px solid var(--margem);padding-block:clamp(28px,4vw,44px)}}
.indice h2{{font:400 clamp(22px,3.2vw,28px)/1.15 var(--disp)}}
.indice p{{color:var(--tinta-3);font-size:15.5px;margin-top:8px}}
.lista-cap{{margin-top:18px;display:grid;gap:1px;background:var(--margem);border:1px solid var(--margem);border-radius:8px;overflow:hidden}}
.cap-link{{background:var(--papel-2);padding:13px 15px;display:flex;gap:12px;align-items:baseline;flex-wrap:wrap;text-decoration:none;color:var(--tinta)}}
a.cap-link:hover{{background:#fff}}
.cap-n{{font:600 11px/1.3 var(--txt);letter-spacing:.1em;text-transform:uppercase;color:var(--mag);min-width:84px}}
.cap-t{{font-weight:500}}
.cap-link.vazio{{color:var(--tinta-3)}}
.cap-link.vazio .cap-n{{color:var(--tinta-3)}}
.cap-link .depois,.cap-link .novo{{margin-left:auto;font:600 10px/1 var(--txt);letter-spacing:.1em;text-transform:uppercase;padding:5px 9px;border-radius:999px;white-space:nowrap}}
.cap-link .depois{{color:var(--tinta-3);border:1px solid var(--margem)}}
.cap-link .novo{{color:#fff;background:var(--mag)}}

.capitulo{{border-top:1px solid var(--margem);padding-block:clamp(36px,5.5vw,62px);position:relative}}
.cap-sel{{font:400 15px/1 var(--mao);color:var(--acesa)}}
.capitulo h2{{font:400 clamp(27px,4.4vw,40px)/1.1 var(--disp);letter-spacing:-.01em;margin-top:10px}}
.atualizacao{{margin-top:16px;padding:13px 16px;background:var(--papel-2);border:1px solid var(--margem);border-left:3px solid var(--mag);border-radius:4px;font-size:15.5px;color:var(--tinta-2)}}
.atualizacao b{{color:var(--mag);font-weight:600}}
.capitulo h3{{font:400 clamp(21px,3vw,27px)/1.2 var(--disp);margin-top:34px}}
.capitulo p{{margin-top:16px}}
.capitulo ul{{margin:14px 0 0;padding-left:20px}}
.capitulo li{{margin-bottom:6px}}
.solta{{font:400 clamp(20px,3vw,27px)/1.35 var(--disp);color:var(--mag);margin-top:24px!important}}
.cita{{border-left:3px solid var(--acesa);padding:2px 0 2px 18px;font-style:italic;color:var(--tinta-2)}}
.margem{{font:400 15px/1.6 var(--mao);color:var(--tinta-3);margin-top:14px;padding-left:16px;border-left:2px solid var(--margem)}}
@media(min-width:1100px){{
  .margem{{position:absolute;left:calc(50% + 360px);width:210px;margin-top:-54px;border-left:0;padding-left:0;transform:rotate(-1.2deg)}}
}}
.passos{{counter-reset:p;margin-top:22px;display:grid;gap:12px}}
.passos>div{{counter-increment:p;display:grid;grid-template-columns:34px 1fr;gap:14px;align-items:start}}
.passos>div::before{{content:counter(p);font:400 20px/1.1 var(--disp);color:var(--mag);border-bottom:2px solid var(--acesa);text-align:center;padding-bottom:2px}}
.passos b{{display:block;font:600 11px/1 var(--txt);letter-spacing:.13em;text-transform:uppercase;margin-bottom:5px}}
.par{{display:grid;gap:12px;margin-top:16px}}
@media(min-width:620px){{.par{{grid-template-columns:1fr 1fr}}}}
.par>div{{background:var(--papel-2);border:1px solid var(--margem);border-radius:4px;padding:15px 17px;font-size:16px}}
.par .rot{{display:block;font:600 10px/1 var(--txt);letter-spacing:.13em;text-transform:uppercase;color:var(--tinta-3);margin-bottom:7px}}
.par .depois{{border-color:rgba(139,8,63,.3)}}
.par .depois .rot{{color:var(--mag)}}
.ficha{{background:var(--noite);color:var(--pessego);border-radius:6px;padding:24px;margin-top:22px;font-size:16px;line-height:2.1}}
.ficha span{{display:block;font:600 11px/1 var(--txt);letter-spacing:.13em;text-transform:uppercase;margin-top:14px;color:var(--acesa)}}
.ficha span:first-child{{margin-top:0}}
.ficha i{{font-style:normal;border-bottom:1px dashed rgba(252,234,223,.4);display:inline-block;min-width:190px}}

/* o diagrama das camadas */
.camadas{{margin-top:22px;display:grid;justify-items:center}}
.camada{{width:100%;background:var(--papel-2);border:1px solid var(--margem);border-radius:6px;padding:15px 18px}}
.camada b{{display:block;font:600 11px/1 var(--txt);letter-spacing:.14em;text-transform:uppercase;color:var(--mag);margin-bottom:7px}}
.camada span{{font-size:16px;color:var(--tinta-2)}}
.seta{{width:2px;height:22px;background:var(--margem);position:relative}}
.seta::after{{content:"";position:absolute;left:-4px;bottom:0;border-left:5px solid transparent;border-right:5px solid transparent;border-top:7px solid var(--margem)}}

/* as marcacoes do capitulo 2, que sao a mesma pergunta da porta */
.marcacoes{{margin-top:18px;display:grid;gap:8px}}
.marca{{display:flex;gap:11px;align-items:center;font-size:16.5px;color:var(--tinta-2)}}
.marca i{{flex:0 0 auto;width:19px;height:19px;border:1.5px solid var(--tinta-3);border-radius:4px}}
.marca.sua i{{background:var(--mag);border-color:var(--mag);position:relative}}
.marca.sua i::after{{content:"";position:absolute;left:5.5px;top:1.5px;width:5px;height:10px;border:solid #fff;border-width:0 2px 2px 0;transform:rotate(42deg)}}
.marca.sua{{color:var(--tinta);font-weight:500}}
.marca em{{font-style:normal;font:400 14px/1 var(--mao);color:var(--acesa);margin-left:4px}}

.fim{{border-top:1px solid var(--margem);padding-block:clamp(44px,7vw,78px);text-align:center}}
.fim .numero{{font:400 clamp(32px,6.4vw,58px)/1 var(--disp);color:var(--mag)}}
.fim .agora{{font:400 clamp(19px,3vw,26px)/1.2 var(--disp);margin-top:12px}}
.assina{{font:400 clamp(24px,3.8vw,34px)/1 var(--mao);margin-top:26px}}
.rodape-nota{{border-top:1px solid var(--margem);padding-block:clamp(30px,5vw,50px);color:var(--tinta-2);font-size:16px}}
.rodape-nota a{{font-weight:600}}
footer{{border-top:1px solid var(--margem);font-size:13px;color:var(--tinta-3)}}
footer .wrap{{padding-block:18px 42px;display:flex;flex-wrap:wrap;gap:8px 20px;justify-content:space-between}}
</style>

<header class="topo faixa"><div class="wrap">
  <div class="perfil">
    <img src="{FOTO}" alt="Danielle Lemos">
    <div><b>Danielle Lemos</b><span>@daanylemos</span></div>
  </div>
  <h1>Como vou sair dos 3K para os 20K?</h1>
  <p class="mao">não sei se vou bater a meta, mas vou registrar aqui tudo que eu testei, o que funcionou e o que não funcionou</p>

  <div class="placar">
    <div><div class="n">3.883</div><div class="r">no começo</div></div>
    <div><div class="n viva" id="n-hoje">...</div><div class="r">hoje</div></div>
    <div><div class="n">20.000</div><div class="r">o destino</div></div>
    <div><div class="n">16</div><div class="r">semanas</div></div>
  </div>
  <p class="placar-data" id="placar-data"></p>
</div></header>

<section class="porta faixa" id="porta"><div class="wrap">
  <div class="conversa">
    <p class="passo-conta" id="conta">Pergunta 1 de 5</p>

    <div class="pergunta ativa" data-passo="1">
      <h2>Como você se chama?</h2>
      <p class="ajuda">É rápido: cinco perguntas e o diário abre. Você preenche uma vez e nunca mais.</p>
      <input id="q-nome" autocomplete="name" placeholder="seu nome">
      <div class="erro"></div>
      <button class="avancar" type="button">Continuar</button>
    </div>

    <div class="pergunta" data-passo="2">
      <h2>Qual o seu @ do Instagram?</h2>
      <p class="ajuda">Para eu saber quem está do outro lado quando você comentar por lá.</p>
      <input id="q-insta" placeholder="@seuperfil">
      <div class="erro"></div>
      <button class="avancar" type="button">Continuar</button>
    </div>

    <div class="pergunta" data-passo="3">
      <h2>Qual o seu melhor WhatsApp?</h2>
      <p class="ajuda">Com DDD. Eu também vou precisar de um e-mail, logo ali embaixo.</p>
      <input id="q-whats" inputmode="tel" autocomplete="tel" placeholder="(00) 00000-0000">
      <input id="q-email" type="email" autocomplete="email" placeholder="seu@email.com" style="margin-top:14px">
      <div class="erro"></div>
      <button class="avancar" type="button">Continuar</button>
    </div>

    <div class="pergunta" data-passo="4">
      <h2>E me conta: qual desses é você hoje?</h2>
      <p class="ajuda">Escolhe o que estiver mais perto. É isso que vai me dizer o que construir depois.</p>
{PASSOS_PORTA}
      <div class="erro"></div>
    </div>

    <div class="pergunta" data-passo="5">
      <h2>Quer que eu te avise no WhatsApp quando sair um capítulo novo?</h2>
      <p class="ajuda">Um aviso por semana, quando o capítulo entrar. Se você disser não, eu não mando nada.</p>
      <div class="sim-nao">
        <button class="sim" type="button" data-aceite="sim">Sim, pode avisar</button>
        <button class="nao" type="button" data-aceite="nao">Não, eu volto aqui</button>
      </div>
      <div class="erro"></div>
    </div>
  </div>
</div></section>

<div class="trancado">
<section class="indice faixa"><div class="wrap">
  <h2>Os capítulos</h2>
  <p>Um por semana, até fevereiro. Os que ainda não existem estão apagados de propósito: o que vai ser testado depende do que os números mostrarem antes.</p>
  <div class="lista-cap">
      {NAV}
  </div>
</div></section>

<main class="faixa"><div class="wrap">
{CAPS_HTML}
</div></main>

<section class="fim faixa"><div class="wrap">
  <div class="numero">3.883 → 20.000</div>
  <div class="agora">Agora começou.</div>
  <div class="assina">Danielle Lemos</div>
</div></section>

<section class="rodape-nota faixa"><div class="wrap">
  <p>Quase tudo que eu testo aqui é o Claude fazendo por mim. Publicar todo dia durante 16 semanas, medir cada post e escrever este diário não caberia no meu dia sem isso. No <a href="https://chk.eduzz.com/lniykl57?utm_source=isca&amp;utm_campaign=diario">Claude do Zero, para iniciantes</a>, eu começo do absoluto zero e vou até ele trabalhando por você, com o pedido pronto em cada aula.</p>
</div></section>
</div>

<footer class="faixa"><div class="wrap"><span>Dani Lemos // Marketing &amp; IA</span><span>Edição viva · atualizada toda semana</span></div></footer>

<script>
const FN="https://veogbuoxtbpaxoqvuakr.supabase.co/functions/v1/lead-isca-dlestudio";
const API="https://veogbuoxtbpaxoqvuakr.supabase.co/rest/v1";
const CHAVE="sb_publishable_2j7Vv_Ifmmu8Dtozr8F44w_HyZlH4xX";
const MC=new URLSearchParams(location.search).get("mc")||"";
const mil=n=>Number(n).toLocaleString("pt-BR");
const resp={{}};

// o placar do topo e publico: aparece para quem ainda nao entrou
fetch(API+"/diario_placar?select=*",{{headers:{{apikey:CHAVE}}}}).then(r=>r.json()).then(l=>{{
  const p=l[0]; if(!p)return;
  document.getElementById("n-hoje").textContent=mil(p.hoje);
  const d=p.data_hoje?p.data_hoje.split("-").reverse().join("/"):"";
  document.getElementById("placar-data").textContent="Número de "+d+", semana "+p.semana_atual+" de "+p.semanas+". O Instagram fecha o dia com atraso, então o de hoje aparece amanhã.";
}}).catch(()=>{{document.getElementById("n-hoje").textContent="3.884"}});

function marcarEco(){{
  const eco=resp.eco; if(!eco)return;
  document.querySelectorAll(".marca").forEach(m=>{{
    if(m.dataset.eco===eco){{m.classList.add("sua");if(!m.querySelector("em")){{const e=document.createElement("em");e.textContent="você";m.appendChild(e)}}}}
  }});
}}
function liberar(){{
  document.body.classList.add("liberado");
  try{{localStorage.setItem("dl_cadastro","1");const e=localStorage.getItem("dl_diario_eco");if(e)resp.eco=e}}catch(e){{}}
  marcarEco();
}}
try{{if(localStorage.getItem("dl_cadastro")==="1")liberar()}}catch(e){{}}
if(!document.body.classList.contains("liberado")&&MC){{fetch(FN+"?mc="+encodeURIComponent(MC)).then(r=>r.json()).then(d=>{{if(d.existe)liberar()}}).catch(()=>{{}})}}

const passos=[...document.querySelectorAll(".pergunta")];
let i=0;
function mostrar(n){{
  i=n; passos.forEach((p,k)=>p.classList.toggle("ativa",k===n));
  document.getElementById("conta").textContent="Pergunta "+(n+1)+" de "+passos.length;
  const inp=passos[n].querySelector("input"); if(inp)setTimeout(()=>inp.focus(),80);
}}
function erro(n,t){{passos[n].querySelector(".erro").textContent=t||""}}

passos.forEach((p,n)=>{{
  const bt=p.querySelector(".avancar");
  if(bt)bt.addEventListener("click",()=>{{
    erro(n,"");
    if(n===0){{const v=document.getElementById("q-nome").value.trim();
      if(v.length<2)return erro(n,"Me diz como você se chama.");
      resp.nome=v;}}
    if(n===1){{const v=document.getElementById("q-insta").value.trim().replace(/^@/,"");
      if(v.length<2)return erro(n,"Falta o seu @.");
      resp.instagram=v;}}
    if(n===2){{const w=document.getElementById("q-whats").value.replace(/[^0-9+]/g,"");
      const e=document.getElementById("q-email").value.trim();
      if(w.length<10)return erro(n,"O WhatsApp precisa do DDD.");
      if(!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(e))return erro(n,"Confere o e-mail.");
      resp.whatsapp=w; resp.email=e;}}
    mostrar(n+1);
  }});
}});
document.querySelectorAll(".caminho").forEach(b=>b.addEventListener("click",()=>{{
  resp.caminho=b.dataset.v; mostrar(4);
}}));
document.querySelectorAll("[data-aceite]").forEach(b=>b.addEventListener("click",async ()=>{{
  const aceite=b.dataset.aceite==="sim";
  erro(4,"");
  b.disabled=true; const antes=b.textContent; b.textContent="Abrindo...";
  const ECO={{{", ".join(f'"{rot}":"{eco}"' for _i, rot, eco in CAMINHOS)}}};
  const d={{nome:resp.nome,email:resp.email,whatsapp:resp.whatsapp,instagram:resp.instagram,
    profissao:resp.caminho||"",origem:"diario+"+(aceite?"sim":"nao"),mc:MC,
    tarefa_chata:""}};
  const PREVIA=!/dlestudio\\.com\\.br$/.test(location.hostname);
  let r=null;try{{r=await fetch(FN,{{method:"POST",headers:{{"content-type":"application/json"}},body:JSON.stringify(d)}})}}catch(e){{}}
  if(!(r&&r.ok)&&!PREVIA){{b.disabled=false;b.textContent=antes;return erro(4,"Não consegui salvar agora. Tenta de novo em alguns segundos.")}}
  resp.eco=ECO[resp.caminho]||"";
  try{{localStorage.setItem("dl_diario_eco",resp.eco)}}catch(e){{}}
  document.querySelector(".conversa").innerHTML='<h2 style="font:400 clamp(24px,3.8vw,34px)/1.2 var(--disp)">pronto, agora é só ler</h2>';
  setTimeout(()=>{{liberar();document.querySelector(".indice").scrollIntoView({{behavior:"smooth",block:"start"}})}},700);
}}));

document.getElementById("marcacoes").innerHTML='{MARCACOES}';
marcarEco();
</script>
</html>
"""

(AQUI / "index.html").write_text(HTML, encoding="utf-8")
print("ok index.html", len(HTML) // 1024, "KB")
