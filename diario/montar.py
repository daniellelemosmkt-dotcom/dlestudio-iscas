"""Monta a pagina do DIARIO: MAPA 20K, a edicao viva.

O TEXTO e o do documento canonico da Dani (MAPA 20K, doze secoes) e o visual e o de diario
desenhado pela coordenacao no artefato E5s5MS97jcJhbSJ3BVoL5a: papel com grao, numero da secao
a mao, frases fortes soltas, assinatura no fim. Nao reescrever o texto: ela pediu literal.

O QUE E LIDO DO BANCO, ao vivo, pela chave publicavel:
- public.diario_placar  -> os quatro numeros do topo. O "hoje" vem de dlestudio.metricas_perfil,
  que a rotina alimenta todo dia, entao nunca fica velho mesmo que a terca passe em branco.
- public.diario_capitulos -> os 16 capitulos. Os sem titulo aparecem como "a escrever".

O schema dlestudio nao esta exposto na API: so as views de public estao.

Uso: python montar.py   ->  index.html nesta pasta
"""
import base64
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ASSETS = Path("G:/Meu Drive/DANIELLE   PROJETOS/PRODUTOS DL ESTÚDIO/04 KIT E PLUGINS/_paginas/assets")
ADV = "data:font/woff2;base64," + base64.b64encode((ASSETS / "Advercase-Regular.woff2").read_bytes()).decode()

PIXEL = (
    '<!-- Meta Pixel -->\n<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?'
    'n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";'
    'n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}'
    '(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","2130554737847082");'
    'fbq("track","PageView");</script>\n<noscript><img height="1" width="1" style="display:none" '
    'src="https://www.facebook.com/tr?id=2130554737847082&ev=PageView&noscript=1"/></noscript>\n<!-- /Meta Pixel -->'
)

CSS = """
@font-face{font-family:"Advercase";src:url(__ADV__) format("woff2");font-weight:400;font-display:swap}
:root{
  --papel:#F7F4EE; --papel-2:#FFFDF8; --tinta:#2B2522; --tinta-2:#5C534E; --margem:#E6DCCD;
  --mag:#8B083F; --acesa:#E2307A; --noite:#160E11; --pessego:#FCEADF;
  --disp:"Advercase","Playfair Display",Georgia,serif; --txt:"Poppins","Segoe UI",Arial,sans-serif;
  --mao:"Homemade Apple",cursive;
  color-scheme:light;
}
*{box-sizing:border-box}
html{background:var(--papel);scroll-behavior:smooth}
body{margin:0;background:var(--papel);color:var(--tinta);font:400 17px/1.75 var(--txt);-webkit-font-smoothing:antialiased;overflow-x:hidden}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:50;opacity:.5;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='g'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/><feColorMatrix type='saturate' values='0'/></filter><rect width='180' height='180' filter='url(%23g)' opacity='.055'/></svg>")}
.faixa{padding-left:max(20px,env(safe-area-inset-left,0px));padding-right:max(20px,env(safe-area-inset-right,0px))}
.wrap{max-width:720px;margin:0 auto}
h1,h2,h3{text-wrap:balance;margin:0}
p{margin:0}
a{color:var(--mag)}
:focus-visible{outline:3px solid var(--acesa);outline-offset:3px;border-radius:6px}

.capa{padding-block:clamp(56px,9vw,110px) clamp(40px,6vw,70px);position:relative}
.capa::before{content:"";position:absolute;left:0;right:0;top:0;height:7px;background:linear-gradient(90deg,var(--mag),var(--acesa))}
.selo{font:400 20px/1 var(--mao);color:var(--mag);transform:rotate(-3deg);display:inline-block}
h1{font:400 clamp(46px,11vw,112px)/.88 var(--disp);letter-spacing:-.03em;margin-top:18px}
.sub{font:400 clamp(18px,2.4vw,23px)/1.4 var(--disp);color:var(--tinta-2);margin-top:20px;max-width:24em}
.autor{font:600 12px/1 var(--txt);letter-spacing:.18em;text-transform:uppercase;color:var(--tinta-2);margin-top:28px}
.aviso{margin-top:34px;background:var(--papel-2);border:1px solid var(--margem);border-left:4px solid var(--mag);
  border-radius:4px;padding:20px 22px;font-size:16px;color:var(--tinta-2)}
.aviso b{color:var(--tinta);font-weight:600;display:block;font:600 11px/1 var(--txt);letter-spacing:.16em;text-transform:uppercase;margin-bottom:10px}

.placar{display:flex;flex-wrap:wrap;gap:0;border:1px solid var(--margem);border-radius:4px;overflow:hidden;margin-top:30px;background:var(--papel-2)}
.placar div{flex:1 1 120px;padding:18px 16px;border-right:1px solid var(--margem)}
.placar div:last-child{border-right:0}
.placar .n{font:400 clamp(26px,4vw,38px)/1 var(--disp)}
.placar .n.viva{color:var(--mag)}
.placar .r{font:600 10px/1.3 var(--txt);letter-spacing:.14em;text-transform:uppercase;color:var(--tinta-2);margin-top:6px}
.placar-data{font-size:13px;color:var(--tinta-2);margin-top:10px}

.entrada{padding-block:clamp(34px,5vw,54px);border-top:1px solid var(--margem);position:relative}
.entrada .n-sec{font:400 13px/1 var(--mao);color:var(--acesa);display:block;margin-bottom:10px}
.entrada h2{font:400 clamp(26px,4.2vw,40px)/1.08 var(--disp);letter-spacing:-.01em}
.entrada p{margin-top:16px;max-width:38em}
.entrada p+p{margin-top:14px}
.solta{font:400 clamp(21px,3.2vw,30px)/1.3 var(--disp);color:var(--mag);margin-top:22px;max-width:26em}
.cita{border-left:3px solid var(--acesa);padding:4px 0 4px 18px;margin-top:20px;font-style:italic;color:var(--tinta-2);max-width:34em}
ul{margin:16px 0 0;padding-left:20px;max-width:38em}
li{margin-bottom:7px}
.bloco{background:var(--papel-2);border:1px solid var(--margem);border-radius:4px;padding:20px 22px;margin-top:20px}
.bloco h3{font:600 12px/1 var(--txt);letter-spacing:.14em;text-transform:uppercase;color:var(--mag);margin-bottom:12px}
.bloco p{margin-top:0}
.par{display:grid;gap:14px;margin-top:18px}
@media(min-width:720px){.par{grid-template-columns:1fr 1fr}}
.par div{background:var(--papel-2);border:1px solid var(--margem);border-radius:4px;padding:16px 18px}
.par .rot{font:600 10px/1 var(--txt);letter-spacing:.14em;text-transform:uppercase;color:var(--tinta-2);margin-bottom:8px;display:block}
.par .depois{border-color:rgba(139,8,63,.35)}
.par .depois .rot{color:var(--mag)}
.passos{counter-reset:p;margin-top:22px;display:grid;gap:12px}
.passos div{counter-increment:p;display:grid;grid-template-columns:34px 1fr;gap:14px;align-items:start}
.passos div::before{content:counter(p);font:400 20px/1.1 var(--disp);color:var(--mag);border-bottom:2px solid var(--acesa);text-align:center;padding-bottom:2px}
.passos b{display:block;font:600 11px/1 var(--txt);letter-spacing:.13em;text-transform:uppercase;margin-bottom:5px}
.ficha{background:var(--noite);color:var(--pessego);border-radius:6px;padding:24px;margin-top:22px;font-size:16px;line-height:2.1}
.ficha span{display:block;font:600 11px/1 var(--txt);letter-spacing:.13em;text-transform:uppercase;margin-top:14px;color:var(--acesa)}
.ficha span:first-child{margin-top:0}
.ficha i{font-style:normal;border-bottom:1px dashed rgba(252,234,223,.4);display:inline-block;min-width:200px}

.caps{background:var(--noite);color:#FBFAF8;padding-block:clamp(48px,7vw,84px)}
.caps .n-sec{color:var(--acesa);font:400 13px/1 var(--mao);display:block;margin-bottom:10px}
.caps h2{font:400 clamp(28px,4.4vw,44px)/1.06 var(--disp)}
.caps .intro{color:#BFAEB4;margin-top:16px;max-width:38em}
.lista-cap{margin-top:32px;display:grid;gap:2px;background:rgba(252,234,223,.14);border:1px solid rgba(252,234,223,.14);border-radius:6px;overflow:hidden}
.lista-cap article{background:var(--noite);padding:16px 18px;display:flex;gap:14px;align-items:baseline;flex-wrap:wrap}
.lista-cap .s{font:600 11px/1 var(--txt);letter-spacing:.12em;text-transform:uppercase;color:var(--acesa);min-width:84px}
.lista-cap .t{color:#FBFAF8;font-weight:500}
.lista-cap .d{color:#BFAEB4;flex-basis:100%;font-size:15px;margin-top:6px}
.lista-cap .e{margin-left:auto;font:600 10px/1 var(--txt);letter-spacing:.1em;text-transform:uppercase;color:#BFAEB4;border:1px solid rgba(252,234,223,.2);padding:5px 9px;border-radius:999px;white-space:nowrap}
.lista-cap .agora .e{color:var(--acesa);border-color:rgba(226,48,122,.5)}

/* cadastro, no mesmo papel */
.cadastro{border-top:1px solid var(--margem);padding-block:clamp(40px,6vw,66px)}
.cartao{background:var(--papel-2);border:1px solid var(--margem);border-radius:4px;padding:clamp(22px,4vw,34px)}
.cartao h2{font:400 clamp(24px,3.4vw,34px)/1.1 var(--disp)}
.cartao .ajuda{color:var(--tinta-2);font-size:15px;margin-top:10px}
label{display:block;margin-top:16px;font:500 14px/1.4 var(--txt)}
label .opc{color:var(--tinta-2);font-weight:400}
input,select,textarea{width:100%;margin-top:6px;font:400 16px/1.5 var(--txt);color:var(--tinta);background:#fff;border:1px solid var(--margem);border-radius:4px;padding:12px 13px}
textarea{min-height:76px;resize:vertical}
.botao{display:inline-flex;align-items:center;justify-content:center;gap:10px;background:var(--mag);color:#fff;text-decoration:none;border:0;cursor:pointer;
  font:600 17px/1 var(--txt);padding:18px 26px;border-radius:999px;width:100%;margin-top:22px}
.botao[disabled]{opacity:.6;cursor:default}
.lgpd{font-size:13px;color:var(--tinta-2);margin-top:12px;text-align:center}
.erro{color:var(--mag);font-size:14px;margin-top:10px;min-height:1em}
.trancado{display:none}
body.liberado .trancado{display:block}
body.liberado .cadastro{display:none}

.fim{padding-block:clamp(50px,8vw,90px);text-align:center}
.fim .numero{font:400 clamp(40px,8vw,84px)/1 var(--disp);color:var(--mag)}
.fim .agora{font:400 clamp(22px,3.4vw,32px)/1.2 var(--disp);margin-top:14px}
.assina{font:400 clamp(26px,4vw,38px)/1 var(--mao);color:var(--tinta);margin-top:30px}
.psilva{border-top:1px solid var(--margem);padding-block:clamp(38px,6vw,64px)}
.psilva .n-sec{font:400 13px/1 var(--mao);color:var(--acesa);display:block;margin-bottom:10px}
.psilva h2{font:400 clamp(24px,3.6vw,36px)/1.1 var(--disp)}
.psilva p{margin-top:16px;max-width:38em;color:var(--tinta-2)}
.psilva a.botao{width:auto;margin-top:22px}
footer{border-top:1px solid var(--margem);font-size:13px;color:var(--tinta-2)}
footer .wrap{padding-block:20px 44px;display:flex;flex-wrap:wrap;gap:8px 20px;justify-content:space-between}
.carregando{color:var(--tinta-2);font-size:15px}
""".replace("__ADV__", ADV)

HTML = f"""<!doctype html>
<html lang="pt-BR">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>MAPA 20K, a edição viva | Dani Lemos</title>
<meta name="description" content="Como eu vou tentar sair de 3.883 para 20.000 seguidores em 16 semanas, e como adaptar a estratégia para qualquer nicho. Atualizado toda terça.">
<meta property="og:title" content="MAPA 20K">
<meta property="og:description" content="O mapa do experimento, com o placar de hoje e um capítulo por semana.">
{PIXEL}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Homemade+Apple&display=swap">
<style>{CSS}</style>

<header class="capa faixa"><div class="wrap">
  <span class="selo">edição viva</span>
  <h1>MAPA 20K</h1>
  <p class="sub">Como eu vou tentar sair de 3.883 para 20.000 seguidores em 16 semanas, e como adaptar a estratégia para qualquer nicho.</p>
  <p class="autor">Por Danielle Lemos</p>

  <div class="aviso"><b>Importante</b>Isto não é uma promessa de resultado. É o mapa do experimento que eu estou executando no meu próprio perfil. A ideia é documentar o processo, medir o que realmente acontece e ir mudando a estratégia com base em dados, não em opinião.</div>

  <div class="placar" id="placar">
    <div><div class="n">3.883</div><div class="r">no começo</div></div>
    <div><div class="n viva" id="n-hoje">...</div><div class="r">hoje</div></div>
    <div><div class="n">20.000</div><div class="r">o destino</div></div>
    <div><div class="n">16</div><div class="r">semanas</div></div>
  </div>
  <p class="placar-data" id="placar-data"></p>
</div></header>

<main class="faixa"><div class="wrap">

<section class="entrada">
  <span class="n-sec">um</span>
  <h2>A mudança principal</h2>
  <p>Durante muito tempo eu tratei conteúdo assim: <em>qual dica eu vou ensinar hoje?</em></p>
  <p>Só que comecei a estudar perfis que estavam crescendo muito mais rápido e percebi um padrão. Os conteúdos que mais prendiam não começavam ensinando. Começavam com alguma coisa acontecendo.</p>
  <ul>
    <li>Uma meta.</li><li>Um problema.</li><li>Um teste.</li><li>Um número.</li><li>Uma decisão.</li>
    <li>Uma coisa que deu errado.</li><li>Uma coisa que a pessoa construiu.</li><li>Uma história que ainda não terminou.</li>
  </ul>
  <p class="solta">Parar de criar posts isolados e começar a construir histórias que continuam.</p>
  <p>A pergunta que eu quero deixar na cabeça de quem me encontra é: <b>o que vai acontecer com isso?</b></p>
</section>

<section class="entrada">
  <span class="n-sec">dois</span>
  <h2>O experimento</h2>
  <p>Ponto de partida: <b>3.883 seguidores</b>. Destino: <b>20.000 seguidores</b>. Prazo: <b>16 semanas</b>.</p>
  <p>O meu conteúdo vai girar em torno de uma história principal:</p>
  <p class="cita">Eu trabalho com conteúdo todos os dias, ensino IA, tenho clientes e equipe, mas meu próprio perfil ainda está em 3.883 seguidores. Quero descobrir se consigo mudar isso em 16 semanas mostrando o que realmente acontece no meu trabalho.</p>
  <p>Isso cria três coisas ao mesmo tempo: um destino concreto, uma pergunta que ainda não tem resposta, e um motivo para acompanhar o processo.</p>
</section>

<section class="entrada">
  <span class="n-sec">três</span>
  <h2>O que eu vou publicar</h2>
  <p>Não vou abandonar conteúdo educativo. Eu só vou mudar a ordem.</p>
  <div class="par">
    <div class="antes"><span class="rot">Antes</span>tema → explicação → CTA</div>
    <div class="depois"><span class="rot">Agora</span>acontecimento → tensão → prova → descoberta → próxima ação</div>
  </div>
  <div class="bloco"><h3>A. O experimento de crescimento</h3>
    <p>O que eu testei, o que trouxe mais seguidores, o que teve alcance e não converteu, o que eu achei que ia funcionar e morreu, o que eu repeti porque deu sinal de funcionar, os placares semanais e as mudanças que os dados me obrigaram a fazer.</p></div>
  <div class="bloco"><h3>B. O que está mudando no meu trabalho com IA</h3>
    <p>Não é "5 coisas que o Claude faz". É o que eu fazia manualmente e deixei de fazer, o que eu consegui construir, onde a IA errou, o que precisei ensinar, o que virou sistema, o que virou produto e o que eu ainda não consegui resolver.</p></div>
  <div class="bloco"><h3>C. O que eu estou aplicando nas contas dos clientes</h3>
    <p>A regra aqui é importante: eu não vou inventar resultado. Vou mostrar decisões reais. Se eu aprender alguma coisa analisando meu próprio perfil e isso mudar um gancho, uma pauta, um formato ou uma escolha numa conta de cliente, eu posso abrir esse raciocínio.</p>
    <p style="margin-top:12px">A cliente deixa de ver "a Dani estudando Instagram". Ela vê: a Dani testa, aprende e aplica.</p></div>
  <div class="bloco"><h3>D. Os bastidores humanos</h3>
    <p>Nem todo conteúdo precisa ensinar. Também entram dúvidas, decisões, coisas que me irritaram, erros, opiniões, situações da rotina, coisas que eu achava e mudei de ideia, e pequenos bastidores que fazem alguém conhecer a pessoa por trás do trabalho.</p></div>
</section>

<section class="entrada">
  <span class="n-sec">quatro</span>
  <h2>A estrutura dos vídeos</h2>
  <div class="passos">
    <div><div><b>Cena</b>Quem eu sou ou onde eu estou, de um jeito que a pessoa consiga imaginar.</div></div>
    <div><div><b>Tensão</b>O que estou tentando, o que não está funcionando ou o que aconteceu.</div></div>
    <div><div><b>Destino</b>O que eu quero conseguir, com número, prazo ou consequência concreta.</div></div>
    <div><div><b>Prova</b>Tela, número, arquivo, antes e depois, resultado, comentário, dado, vídeo, processo real.</div></div>
    <div><div><b>Virada</b>O que isso me fez perceber ou mudar.</div></div>
    <div><div><b>CTA</b>Uma próxima ação que faça sentido para a curiosidade que o conteúdo abriu.</div></div>
  </div>
</section>

<section class="entrada">
  <span class="n-sec">cinco</span>
  <h2>Por que eu acho que isso pode funcionar</h2>
  <p>Não porque "história funciona melhor". Porque essa estrutura resolve quatro problemas do conteúdo comum.</p>
  <div class="bloco"><h3>Problema 1 · dica demais e contexto de menos</h3><p>Quando o conteúdo começa pela história, a pessoa entende por que deveria se importar antes de receber a explicação.</p></div>
  <div class="bloco"><h3>Problema 2 · todo post parece começar do zero</h3><p>Quando existe uma série, um conteúdo aumenta o valor do próximo.</p></div>
  <div class="bloco"><h3>Problema 3 · a pessoa aprende e vai embora</h3><p>Quando existe uma pergunta aberta, existe mais motivo para seguir.</p></div>
  <div class="bloco"><h3>Problema 4 · o criador precisa inventar assunto todos os dias</h3><p>Quando você documenta o que já está vivendo, o próprio trabalho começa a produzir pauta.</p></div>
</section>

<section class="entrada">
  <span class="n-sec">seis</span>
  <h2>O que eu vou medir</h2>
  <p>Eu não vou usar curtida como principal sinal de sucesso. Quero acompanhar:</p>
  <ul>
    <li>alcance de não seguidores;</li><li>visitas ao perfil;</li><li>seguidores gerados por conteúdo;</li>
    <li>compartilhamentos;</li><li>comentários;</li><li>DMs iniciadas pelas iscas;</li>
    <li>quais conteúdos fazem a pessoa pedir continuação;</li><li>quais mecanismos funcionam mais de uma vez.</li>
  </ul>
  <p class="solta">Este conteúdo fez alguém que não me conhecia querer continuar comigo?</p>
</section>

<section class="entrada">
  <span class="n-sec">sete</span>
  <h2>Como vou decidir o que repetir</h2>
  <p>Quando um conteúdo se destacar, eu não vou abandonar a ideia no dia seguinte. Vou desmontar o que aconteceu: qual foi a promessa, como começou, qual foi a tensão, qual prova apareceu, onde estava a virada, qual foi o CTA e que comentários se repetiram.</p>
  <p>Depois vou manter o mecanismo e trocar a história.</p>
  <div class="par">
    <div class="antes"><span class="rot">Não repetir</span>falar de 22 vídeos de novo</div>
    <div class="depois"><span class="rot">Repetir</span>começar com uma situação concreta, revelar um gargalo invisível, mostrar prova e terminar com uma consequência</div>
  </div>
</section>

<section class="entrada">
  <span class="n-sec">oito</span>
  <h2>O papel das iscas</h2>
  <p>Durante esse sprint eu quero transformar comentário em conversa. Mas a isca precisa nascer do conteúdo. Nada de "comenta GUIA que eu mando um PDF aleatório".</p>
  <p class="cita">o vídeo abre uma curiosidade → o material entrega exatamente a parte que ficou faltando → a pessoa comenta para receber</p>
  <div class="bloco"><h3>As iscas</h3>
    <p><b>MAPA</b> · este material que você está lendo.</p>
    <p style="margin-top:10px"><b>OUTLIER</b> · ficha para analisar um post fora da curva sem copiar o assunto.</p>
    <p style="margin-top:10px"><b>SPRINT</b> · scorecard para acompanhar um experimento de crescimento.</p>
    <p style="margin-top:10px"><b>EDITOR</b> · demonstração de como um sistema de edição com Claude funciona.</p>
    <p style="margin-top:10px"><b>ROTEIRO</b> · estrutura para transformar uma história real em um Yap.</p></div>
</section>

<section class="entrada">
  <span class="n-sec">nove</span>
  <h2>Como adaptar para outros nichos</h2>
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
</section>

<section class="entrada">
  <span class="n-sec">dez</span>
  <h2>O exercício para criar a sua série</h2>
  <div class="ficha">
    <span>Eu sou</span><i>quem você é numa cena concreta</i>
    <span>Hoje estou</span><i>situação real</i>
    <span>O que não está funcionando</span><i>o problema</i>
    <span>Quero</span><i>destino concreto</i>
    <span>Até</span><i>prazo</i>
    <span>Vou mostrar</span><i>provas e acontecimentos que podem virar episódios</i>
    <span>A pergunta que quero deixar aberta</span><i>será que ela consegue o quê?</i>
  </div>
  <p class="cita">Sou social media e cuido de 8 clientes. Toda segunda eu ainda começo o dia procurando informação espalhada em WhatsApp, Drive e reunião. Quero passar 30 dias reconstruindo esse processo até abrir a semana sabendo exatamente o que precisa da minha decisão. Vou mostrar o que funcionar e o que continuar me dando trabalho.</p>
</section>

<section class="entrada">
  <span class="n-sec">onze</span>
  <h2>A regra mais importante</h2>
  <p class="solta">Não invente uma jornada porque você precisa de conteúdo. Olhe para o que já está acontecendo.</p>
  <ul>
    <li>O que você está tentando?</li><li>O que está difícil?</li><li>O que você está construindo?</li>
    <li>Que número você quer mudar?</li><li>Que pergunta ainda não sabe responder?</li>
    <li>O que deu errado esta semana?</li><li>O que alguém pediu para você?</li><li>O que você aprendeu e aplicou?</li>
  </ul>
  <p>É daí que nasce a série.</p>
</section>

<section class="entrada">
  <span class="n-sec">doze</span>
  <h2>O meu combinado</h2>
  <p>Eu vou abrir os testes, os números, as coisas que funcionarem, as coisas que morrerem, as mudanças de rota, os bastidores, e o papel que a IA tiver de verdade nesse processo.</p>
  <p>Sem fingir que eu já sei a resposta.</p>
</section>

</div></main>

<section class="cadastro faixa" id="cadastro"><div class="wrap">
  <div class="cartao">
    <h2>Para acompanhar os capítulos</h2>
    <p class="ajuda">O mapa acima é aberto. Os capítulos de cada semana, com o placar e o que funcionou, ficam logo abaixo. Você preenche uma vez só e depois acessa qualquer material meu.</p>
    <form id="fcad" novalidate>
      <label>Seu nome<input name="nome" autocomplete="name" required></label>
      <label>WhatsApp com DDD<input name="whatsapp" inputmode="tel" autocomplete="tel" required></label>
      <label>E-mail<input name="email" type="email" autocomplete="email" required></label>
      <label>Seu @ do Instagram<input name="instagram" required></label>
      <label>Você trabalha com
        <select name="profissao" required>
          <option value="">Escolha uma opção</option>
          <option>Social media ou marketing</option>
          <option>Saúde (medicina, odontologia, psicologia e afins)</option>
          <option>Outra profissão liberal (advocacia, arquitetura, contabilidade)</option>
          <option>Negócio próprio, loja ou serviço</option>
          <option>Ainda estou começando</option>
        </select>
      </label>
      <label>Quantos seguidores você tem hoje? <span class="opc">(opcional)</span>
        <textarea name="tarefa_chata"></textarea></label>
      <div class="erro" id="erro"></div>
      <button class="botao" type="submit">Quero acompanhar</button>
      <p class="lgpd">Ao enviar, você concorda em receber meus conteúdos e novidades por WhatsApp e e-mail. Pode pedir para sair quando quiser.</p>
    </form>
  </div>
</div></section>

<div class="trancado">
<section class="caps faixa"><div class="wrap">
  <span class="n-sec">os capítulos</span>
  <h2>Dezesseis semanas, uma por capítulo</h2>
  <p class="intro">Cada semana ganha o seu capítulo aqui, com o placar, os posts, o que funcionou, o que não funcionou, o que ficou inconclusivo e como aplicar em outro nicho. Os capítulos futuros estão em branco de propósito: o que vai ser testado depende do que os números mostrarem antes.</p>
  <div class="lista-cap" id="lista-cap"><article><span class="t carregando">Carregando os capítulos...</span></article></div>
</div></section>
</div>

<section class="fim faixa"><div class="wrap">
  <div class="numero" id="fim-numero">3.883 → 20.000</div>
  <div class="agora">Agora começou.</div>
  <div class="assina">Danielle Lemos</div>
</div></section>

<section class="psilva faixa"><div class="wrap">
  <span class="n-sec">uma nota de rodapé</span>
  <h2>Quase tudo que eu testo aqui é o Claude fazendo por mim</h2>
  <p>Publicar todo dia durante 16 semanas, medir cada post e escrever este diário não caberia no meu dia sem isso. No Claude do Zero, para iniciantes, eu começo do absoluto zero e vou até ele trabalhando por você, com o pedido pronto em cada aula.</p>
  <p><a class="botao" href="https://chk.eduzz.com/lniykl57?utm_source=isca&amp;utm_campaign=diario">Ver o Claude do Zero</a></p>
</div></section>

<footer class="faixa"><div class="wrap"><span>Dani Lemos // Marketing &amp; IA</span><span>Edição viva · atualizada toda terça</span></div></footer>

<script>
const ORIGEM="diario";
const FN="https://veogbuoxtbpaxoqvuakr.supabase.co/functions/v1/lead-isca-dlestudio";
const API="https://veogbuoxtbpaxoqvuakr.supabase.co/rest/v1";
const CHAVE="sb_publishable_2j7Vv_Ifmmu8Dtozr8F44w_HyZlH4xX";
const MC=new URLSearchParams(location.search).get("mc")||"";
const f=document.getElementById("fcad"),erro=document.getElementById("erro");
const esc=s=>String(s??"").replace(/[&<>"]/g,c=>(({{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}})[c]));
const mil=n=>Number(n).toLocaleString("pt-BR");
function liberar(){{document.body.classList.add("liberado");try{{localStorage.setItem("dl_cadastro","1")}}catch(e){{}}capitulos()}}
try{{if(localStorage.getItem("dl_cadastro")==="1")liberar()}}catch(e){{}}
if(!document.body.classList.contains("liberado")&&MC){{fetch(FN+"?mc="+encodeURIComponent(MC)).then(r=>r.json()).then(d=>{{if(d.existe)liberar()}}).catch(()=>{{}})}}

async function buscar(v){{const r=await fetch(API+"/"+v,{{headers:{{apikey:CHAVE}}}});if(!r.ok)throw 0;return r.json()}}

// o placar do topo e publico: aparece para todo mundo, cadastrado ou nao
buscar("diario_placar?select=*").then(l=>{{
  const p=l[0]; if(!p)return;
  document.getElementById("n-hoje").textContent=mil(p.hoje);
  document.getElementById("fim-numero").textContent=mil(p.inicio)+" → "+mil(p.meta);
  const d=p.data_hoje?p.data_hoje.split("-").reverse().join("/"):"";
  document.getElementById("placar-data").textContent="Número de "+d+", semana "+p.semana_atual+" de "+p.semanas+". O Instagram fecha o dia com atraso, então o de hoje aparece amanhã.";
}}).catch(()=>{{document.getElementById("n-hoje").textContent="3.884"}});

let feitos=false;
async function capitulos(){{
  if(feitos)return; feitos=true;
  const cx=document.getElementById("lista-cap");
  try{{
    const [caps,placar]=await Promise.all([buscar("diario_capitulos?select=*&order=semana.asc"),buscar("diario_placar?select=semana_atual")]);
    const atual=(placar[0]||{{}}).semana_atual||1;
    cx.innerHTML=caps.map(c=>{{
      const escrito=c.titulo&&c.publicado;
      const estado=escrito?"escrito":(c.semana===atual?"em andamento":"a escrever");
      return '<article class="'+(c.semana===atual?"agora":"")+'">'+
        '<span class="s">Semana '+c.semana+'</span>'+
        '<span class="t">'+esc(escrito?c.titulo:c.periodo)+'</span>'+
        '<span class="e">'+estado+'</span>'+
        (escrito&&c.resumo?'<span class="d">'+esc(c.resumo)+'</span>':'')+
      '</article>';
    }}).join("");
  }}catch(e){{cx.innerHTML='<article><span class="t carregando">Não consegui buscar os capítulos agora. Atualize a página em alguns segundos.</span></article>'}}
}}

f.addEventListener("submit",async ev=>{{ev.preventDefault();erro.textContent="";
 const d=Object.fromEntries(new FormData(f));d.origem=ORIGEM;d.mc=MC;
 if(!d.nome||!d.email||!d.whatsapp||!d.instagram||!d.profissao){{erro.textContent="Preencha todos os campos (só a última pergunta é opcional).";return}}
 const bt=f.querySelector("[type=submit]");bt.disabled=true;bt.textContent="Liberando...";
 const PREVIA=!/dlestudio\\.com\\.br$/.test(location.hostname);
 let r=null;try{{r=await fetch(FN,{{method:"POST",headers:{{"content-type":"application/json"}},body:JSON.stringify(d)}})}}catch(e){{}}
 if(!(r&&r.ok)&&!PREVIA){{erro.textContent=(r&&r.status===400)?"Confere o WhatsApp (com DDD) e o e-mail.":"Não consegui salvar agora. Tenta de novo em alguns segundos.";bt.disabled=false;bt.textContent="Quero acompanhar";return}}
 liberar();
 const alvo=document.querySelector(".trancado");if(alvo)alvo.scrollIntoView({{behavior:"smooth",block:"start"}});
}});
</script>
</html>
"""

(AQUI / "index.html").write_text(HTML, encoding="utf-8")
print("ok index.html", len(HTML) // 1024, "KB")
