"""Monta a /diario: o Diario da Dani, com cara de documento e leitura que puxa ate o fim.

Desenho de 24/10 (segunda rodada de correcoes dela, em INSTAGRAM/diario-redesenho-24-10.md):

  * topo centralizado, foto do Instagram dela, data de hoje virando sozinha, placar numa
    linha so com seta no numero vivo;
  * navegacao fina que acompanha a rolagem, SO com os capitulos que existem;
  * um capitulo por tela, nunca empilhados, com caixa de proximo capitulo mostrando o
    titulo do seguinte (padrao do Shape Up, a referencia que foi aberta e conferida);
  * cinco marcacoes para a leitura ficar mastigada: frase em marca-texto (uma por tela),
    EXEMPLO, COPIE E COLE (com botao que copia de verdade), passo a passo numerado e a
    caixa vinho O MEU METODO, que e o unico bloco escuro da pagina.

O TEXTO E DELA, do documento 1I6c8fuR7bK0jSWKHFT1dJhllARf_fHSyzxHd7af_F_4. As unicas
mudancas sao as 12 simplificacoes que ela aprovou uma a uma, listadas no .md acima; o resto
e palavra por palavra. O capitulo 1 nao tem titulo porque no documento dela nao tem.

DO BANCO, ao vivo: o placar (public.diario_placar, que le dlestudio.metricas_perfil).

A PORTA grava em dlestudio.leads pela funcao lead-isca-dlestudio. Dois campos viajam
disfarcados, porque a edge function so repassa campos fixos:
  * profissao -> a resposta de "qual desses e voce hoje", que a funcao do banco copia para
    a coluna interesse;
  * origem    -> "diario+sim" ou "diario+nao", e o sufixo vira aceite_whatsapp.
Sem o sim, aceite_whatsapp fica false e a pessoa nao entra em disparo nenhum.

Uso: python montar.py   ->  index.html nesta pasta
"""
import base64
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ASSETS = Path("G:/Meu Drive/DANIELLE   PROJETOS/PRODUTOS DL ESTÚDIO/04 KIT E PLUGINS/_paginas/assets")

ADV = "data:font/woff2;base64," + base64.b64encode((ASSETS / "Advercase-Regular.woff2").read_bytes()).decode()
FOTO = "data:image/jpeg;base64," + base64.b64encode((AQUI / "perfil-instagram.jpg").read_bytes()).decode()

PIXEL = (
    '<!-- Meta Pixel -->\n<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?'
    'n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";'
    'n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}'
    '(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","2130554737847082");'
    'fbq("track","PageView");</script>\n<noscript><img height="1" width="1" style="display:none" '
    'src="https://www.facebook.com/tr?id=2130554737847082&ev=PageView&noscript=1"/></noscript>\n<!-- /Meta Pixel -->'
)

CAP1 = """
<p><b>Isto não é uma promessa de resultado.</b> É o mapa do experimento que eu estou executando no meu próprio perfil. A ideia é documentar o processo, medir o que realmente acontece e ir mudando a estratégia com base em dados, não em opinião.</p>

<h3>1. A mudança principal</h3>
<p>Durante muito tempo eu tratei conteúdo assim: <mark>qual dica eu vou ensinar hoje?</mark></p>
<p>Só que comecei a estudar perfis que estavam crescendo muito mais rápido e percebi um padrão.</p>
<p class="solta">Os conteúdos que mais prendiam não começavam ensinando. Começavam com alguma coisa acontecendo.</p>
<ul><li>Uma meta.</li><li>Um problema.</li><li>Um teste.</li><li>Um número.</li><li>Uma decisão.</li><li>Uma coisa que deu errado.</li><li>Uma coisa que a pessoa construiu.</li><li>Uma história que ainda não terminou.</li></ul>
<p>Então a minha estratégia para estas 16 semanas é simples:</p>
<div class="metodo"><span>O meu método</span>
  <p>Parar de criar posts isolados e começar a construir histórias que continuam.</p>
  <p class="pequeno">A pergunta que eu quero deixar na cabeça de quem me encontra é: “o que vai acontecer com isso?”</p>
</div>

<h3>2. O experimento</h3>
<p>Ponto de partida: <b>3.883 seguidores</b>. Destino: <b>20.000 seguidores</b>. Prazo: <b>16 semanas</b>.</p>
<p>O meu conteúdo vai girar em torno de uma história principal:</p>
<div class="bloco"><span>A história que eu vou contar</span>
  <p>“Eu trabalho com conteúdo todos os dias, ensino IA, tenho clientes e equipe, mas meu próprio perfil ainda está em 3.883 seguidores. Quero descobrir se consigo mudar isso em 16 semanas mostrando o que realmente acontece no meu trabalho.”</p>
</div>
<p>Isso cria três coisas ao mesmo tempo: um destino concreto, uma pergunta que ainda não tem resposta, e um motivo para acompanhar o processo.</p>

<h3>3. O que eu vou publicar</h3>
<p>Não vou abandonar conteúdo educativo. <mark>Eu só vou mudar a ordem.</mark></p>
<p>Antes eu escolhia o assunto, explicava e pedia para a pessoa fazer alguma coisa. Agora eu começo contando o que aconteceu, mostro o problema, mostro a prova, conto o que descobri e só então digo o que fazer.</p>
<p>Os conteúdos vão cair principalmente em quatro grupos.</p>
<div class="grupos">
  <div><b>A</b><div><h4>O experimento de crescimento</h4><p>O que eu testei, o que trouxe mais seguidores, o que teve alcance e não converteu, o que eu achei que ia funcionar e morreu, o que eu repeti porque deu sinal de funcionar, placares semanais, e as mudanças que os dados me obrigaram a fazer.</p></div></div>
  <div><b>B</b><div><h4>O que está mudando no meu trabalho com IA</h4><p>Não é “5 coisas que o Claude faz”. É o que eu fazia manualmente e deixei de fazer, o que eu consegui construir, onde a IA errou, o que precisei ensinar, o que virou sistema, o que virou produto, e o que eu ainda não consegui resolver.</p></div></div>
  <div><b>C</b><div><h4>O que eu estou aplicando nas contas dos clientes</h4><p>A regra aqui é importante: eu não vou inventar resultado. Vou mostrar decisões reais. Se eu aprender alguma coisa analisando meu próprio perfil e isso mudar um gancho, uma pauta, um formato ou uma escolha numa conta de cliente, eu posso abrir esse raciocínio. A cliente deixa de ver “a Dani estudando Instagram”. Ela vê: “a Dani testa, aprende e aplica”.</p></div></div>
  <div><b>D</b><div><h4>Os bastidores humanos</h4><p>Nem todo conteúdo precisa ensinar. Também entram dúvidas, decisões, coisas que me irritaram, erros, opiniões, situações da rotina, coisas que eu achava e mudei de ideia, e pequenos bastidores que fazem alguém conhecer a pessoa por trás do trabalho.</p></div></div>
</div>

<h3>4. A estrutura dos vídeos</h3>
<p>A estrutura que eu estou usando como base é esta:</p>
<div class="passos">
  <div><div><b>Cena</b>Quem eu sou ou onde eu estou, de um jeito que a pessoa consiga imaginar.</div></div>
  <div><div><b>O problema</b>O que eu estou tentando fazer, o que não está dando certo ou o que aconteceu.</div></div>
  <div><div><b>Onde eu quero chegar</b>O que eu quero conseguir, com número e prazo.</div></div>
  <div><div><b>Prova</b>Tela, número, arquivo, antes e depois, resultado, comentário, dado, vídeo, processo real.</div></div>
  <div><div><b>O que mudou</b>O que eu percebi ou passei a fazer diferente.</div></div>
  <div><div><b>O convite</b>O que a pessoa pode fazer agora, ligado à curiosidade que o vídeo abriu.</div></div>
</div>

<h3>5. Por que eu acho que isso pode funcionar</h3>
<p>Não porque “história funciona melhor”. Porque essa estrutura resolve quatro problemas do conteúdo comum.</p>
<p><b>Problema 1: muita dica e pouca explicação de por que aquilo importa.</b> Quando o conteúdo começa pela história, a pessoa entende por que deveria se importar antes de receber a explicação.</p>
<p><b>Problema 2: todo post parece começar do zero.</b> Quando existe uma série, um conteúdo aumenta o valor do próximo.</p>
<p><b>Problema 3: a pessoa aprende e vai embora.</b> Quando existe uma pergunta aberta, existe mais motivo para seguir.</p>
<p><b>Problema 4: o criador precisa inventar assunto todos os dias.</b> <mark>Quando você documenta o que já está vivendo, o próprio trabalho começa a produzir pauta.</mark></p>

<h3>6. O que eu vou medir</h3>
<p>Eu não vou usar curtida como principal sinal de sucesso. Quero acompanhar:</p>
<ul><li>quantas pessoas que ainda não me seguem viram o conteúdo;</li><li>visitas ao perfil;</li><li>seguidores gerados por conteúdo;</li><li>compartilhamentos;</li><li>comentários;</li><li>conversas no direct que começaram por causa dos materiais;</li><li>quais conteúdos fazem a pessoa pedir continuação;</li><li>quais jeitos de fazer o vídeo deram certo mais de uma vez.</li></ul>
<div class="metodo"><span>O meu método</span>
  <p>Este conteúdo fez alguém que não me conhecia querer continuar comigo?</p>
  <p class="pequeno">É essa pergunta que decide se um conteúdo valeu, não o número de curtidas.</p>
</div>

<h3>7. Como vou decidir o que repetir</h3>
<p>Quando um conteúdo se destacar, eu não vou abandonar a ideia no dia seguinte. Vou olhar por partes o que aconteceu: o que o vídeo prometeu, como começou, qual foi o problema, qual prova apareceu, onde estava a virada, qual foi o convite, e que comentários se repetiram.</p>
<p><mark>Depois eu mantenho o jeito de fazer e troco a história que eu conto.</mark></p>
<div class="bloco"><span>Exemplo</span>
  <p><b>Não repetir</b> o assunto, como falar dos 22 vídeos outra vez.</p>
  <p><b>Repetir</b> “começar com uma situação do dia a dia, mostrar o problema escondido que trava tudo, provar que ele existe e terminar dizendo o que isso causa”.</p>
</div>

<h3>8. O papel das iscas</h3>
<p>Nessas 16 semanas eu quero que quem comenta passe a conversar comigo no direct. Mas o material que eu ofereço tem que ser a continuação do vídeo.</p>
<div class="bloco"><span>Exemplo do que eu não quero fazer</span>
  <p>“Comenta GUIA que eu mando um PDF aleatório.”</p>
</div>
<div class="passos curto">
  <div><div>O vídeo abre uma curiosidade.</div></div>
  <div><div>O material entrega exatamente a parte que ficou faltando.</div></div>
  <div><div>A pessoa comenta para receber.</div></div>
</div>
<p><b>MAPA</b>, este material que você está lendo. <b>OUTLIER</b>, uma ficha para estudar um post que bombou muito mais que o normal, sem copiar o tema dele. <b>SPRINT</b>, uma tabela para você acompanhar o seu próprio experimento de crescimento. <b>EDITOR</b>, demonstração de como um sistema de edição com Claude funciona. <b>ROTEIRO</b>, um passo a passo para transformar uma história sua em vídeo falado, daqueles em que você só conversa com a câmera.</p>

<h3>9. Como adaptar para outros nichos</h3>
<p>A estratégia não depende de falar sobre marketing ou IA. Ela só precisa de:</p>
<div class="metodo"><span>O meu método</span>
  <p>Uma pessoa + uma situação real + um destino + uma história ainda aberta.</p>
</div>
<div class="bloco"><span>Exemplos em seis áreas</span>
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
</div>

<h3>10. Estrutura para você gravar o seu primeiro conteúdo nesse estilo</h3>
<p>Preencha estas sete linhas. O que sair daqui já é o roteiro do seu primeiro vídeo da série.</p>
<div class="ficha">
  <div><b>Eu sou</b><i></i><em>quem você é, numa cena concreta</em></div>
  <div><b>Hoje estou</b><i></i><em>a situação real</em></div>
  <div><b>O que não está funcionando</b><i></i><em>o problema</em></div>
  <div><b>Quero</b><i></i><em>um destino concreto</em></div>
  <div><b>Até</b><i></i><em>o prazo</em></div>
  <div><b>Vou mostrar</b><i></i><em>as provas que podem virar episódio</em></div>
  <div><b>A pergunta que eu deixo aberta</b><i></i><em>será que ela consegue o quê?</em></div>
</div>
<div class="copiar"><span>Copie e cole no seu</span>
<pre>Eu sou [quem você é, numa cena concreta].
Hoje estou [situação real].
O que não está funcionando é [o problema].
Quero [destino concreto] até [prazo].
Vou mostrar [as provas que viram episódio].
A pergunta que eu deixo aberta é [será que ela consegue o quê?].</pre>
<button type="button" class="bt-copia">copiar</button></div>
<div class="bloco"><span>Exemplo preenchido</span>
  <p>“Sou social media e cuido de 8 clientes. Toda segunda eu ainda começo o dia procurando informação espalhada em WhatsApp, Drive e reunião. Quero passar 30 dias reconstruindo esse processo até abrir a semana sabendo exatamente o que precisa da minha decisão. Vou mostrar o que funcionar e o que continuar me dando trabalho.”</p>
</div>

<h3>11. A regra mais importante</h3>
<p><mark>Não invente uma jornada porque você precisa de conteúdo.</mark> Olhe para o que já está acontecendo.</p>
<ul><li>O que você está tentando?</li><li>O que está difícil?</li><li>O que você está construindo?</li><li>Que número você quer mudar?</li><li>Que pergunta ainda não sabe responder?</li><li>O que deu errado esta semana?</li><li>O que alguém pediu para você?</li><li>O que você aprendeu e aplicou?</li></ul>
<p>É daí que nasce a série.</p>

<h3>12. O meu combinado</h3>
<p>Eu vou abrir os testes, os números, as coisas que funcionarem, as coisas que morrerem, as mudanças de rota, os bastidores, e o papel que a IA tiver de verdade nesse processo.</p>
<p class="solta">Sem fingir que eu já sei a resposta.</p>
"""

CAP2 = """
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
<p><mark>Eu preciso saber qual função cada coisa cumpre dentro da mesma história.</mark></p>
<p>A partir de agora, minha regra é:</p>
<div class="metodo"><span>O meu método</span>
  <ul>
    <li><b>Claude</b> me ajuda a ser descoberta.</li>
    <li><b>A série</b> me ajuda a ser acompanhada.</li>
    <li><b>Os livros</b> me ajudam a pensar melhor.</li>
    <li><b>Os clientes</b> me ajudam a testar se o aprendizado sobrevive fora do meu perfil.</li>
    <li><b>Os dados</b> decidem o que merece virar método.</li>
  </ul>
</div>

<p>E eu também mudei outra coisa.</p>
<p>Eu estava tentando descobrir cedo demais o que deveria vender no final.</p>
<p class="solta">Então eu parei.</p>
<p>Quem pedir acesso a este Diário vai começar a me mostrar o que quer acompanhar comigo:</p>

<div class="marcacoes" id="marcacoes"></div>

<p>Eu vou acompanhar essas respostas junto com comentários, directs, pedidos e padrões que surgirem.</p>
<p>O produto futuro não vai ser escolhido porque eu tive uma ideia boa. Ele vai precisar aparecer como demanda.</p>

<h3>Meu ritmo de conteúdo agora</h3>
<p>Todo dia, em média:</p>
<div class="passos curto">
  <div><div><b>Descoberta e utilidade</b>Claude, sistemas, automações, casos reais, conteúdos que entregam alguma coisa imediatamente.</div></div>
  <div><div><b>Continuidade e marca</b>Um episódio da série, uma decisão, um insight de livro aplicado, um experimento, um resultado ou um bastidor que faça esta história andar.</div></div>
</div>
<p>Não significa dois posts rígidos para sempre. Significa duas funções diferentes. Uma peça faz uma pessoa nova chegar. A outra dá motivo para ela continuar.</p>
<p>E uma vez por semana eu quero testar a mesma ideia em dois formatos. O primeiro caso já existe: “O Claude fez esse post do zero”. Esse conteúdo já me trouxe 7 seguidores. Agora eu quero testar o mesmo núcleo em outro formato e comparar não só visualização, mas quantas pessoas realmente entraram no perfil e decidiram ficar.</p>
<p class="solta">O que está fazendo este perfil crescer, e o que só parece estar funcionando?</p>
"""

CAPITULOS = [
    {"n": 1, "data": "22 de outubro", "titulo": "", "corpo": CAP1,
     "margens": [(2, "isso aqui é o combinado comigo mesma"),
                 (26, "nenhuma isca nasce sem o post pedir")]},
    {"n": 2, "data": "24 de outubro",
     "titulo": "Eu achei que tinha assuntos demais. Na verdade, eu tinha camadas diferentes.",
     "corpo": CAP2,
     "margens": [(3, "quatro perfis dentro de um só, juro"),
                 (9, "parei de adivinhar o produto")]},
]

CAMINHOS = [
    ("Quero colocar a IA para trabalhar por mim", "Claude + automação"),
    ("Quero fazer o meu perfil crescer", "crescimento + marca pessoal"),
    ("Quero que o meu conteúdo venda", "conteúdo que vende"),
    ("Sou social media e quero organizar a operação", "operação / social media"),
    ("Por enquanto só quero acompanhar", "outra coisa"),
]


def minutos(html):
    """Tempo de leitura a 200 palavras por minuto, arredondado para cima."""
    palavras = len(re.sub(r"<[^>]+>", " ", html).split())
    return max(1, int(palavras / 200 + 0.5))


def monta_capitulo(c, proximo):
    corpo, p, saida = c["corpo"].strip(), 0, []
    margens = dict(c["margens"])
    for linha in corpo.split("\n"):
        saida.append(linha)
        if linha.startswith("<p>") or linha.startswith('<p class="solta">'):
            p += 1
            if p in margens:
                saida.append(f'<aside class="margem">{margens[p]}</aside>')
    titulo = f'<h2>{c["titulo"]}</h2>' if c["titulo"] else ""
    if proximo:
        fim = (f'<a class="proximo" href="#cap{proximo["n"]}" data-ir="{proximo["n"]}">'
               f'<span>Próximo capítulo</span><b>{proximo["titulo"]}</b>'
               f'<i>Ler o capítulo {proximo["n"]} &rarr;</i></a>')
    else:
        fim = '<p class="aguarde">capítulo novo toda terça</p>'
    return f"""  <article class="capitulo" id="cap{c['n']}" data-cap="{c['n']}">
    <p class="cap-linha">Capítulo {c['n']} <span>·</span> {c['data']} <span>·</span> {minutos(corpo)} min de leitura</p>
    {titulo}
{chr(10).join(saida)}
    {fim}
  </article>"""


NAV = "\n      ".join(
    f'<a href="#cap{c["n"]}" data-ir="{c["n"]}">Capítulo {c["n"]}</a>' for c in CAPITULOS)
CAPS_HTML = "\n".join(
    monta_capitulo(c, CAPITULOS[i + 1] if i + 1 < len(CAPITULOS) else None)
    for i, c in enumerate(CAPITULOS))
PASSOS_PORTA = "\n".join(
    f'      <button class="caminho" type="button" data-v="{rot}">{rot}</button>' for rot, _ in CAMINHOS)
MARCACOES = "".join(f'<span class="marca" data-eco="{eco}"><i></i>{eco}</span>' for _, eco in CAMINHOS)

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
  --margem:#E6DCCD; --mag:#8B083F; --acesa:#E2307A; --vinho:#2E0A1A; --pessego:#FCEADF;
  --caneta:rgba(226,48,122,.24);
  --disp:"Advercase","Playfair Display",Georgia,serif; --txt:"Poppins","Segoe UI",Arial,sans-serif;
  --mao:"Homemade Apple",cursive;
  color-scheme:light;
}}
*{{box-sizing:border-box}}
html{{background:var(--papel)}}
body{{margin:0;background:var(--papel);color:var(--tinta);font:400 17.5px/1.85 var(--txt);-webkit-font-smoothing:antialiased;overflow-x:hidden}}
body::after{{content:"";position:fixed;inset:0;pointer-events:none;z-index:60;opacity:.5;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='g'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/><feColorMatrix type='saturate' values='0'/></filter><rect width='180' height='180' filter='url(%23g)' opacity='.055'/></svg>")}}
.faixa{{padding-left:max(20px,env(safe-area-inset-left,0px));padding-right:max(20px,env(safe-area-inset-right,0px))}}
.wrap{{max-width:680px;margin:0 auto}}
h1,h2,h3,h4{{text-wrap:balance;margin:0}}
p{{margin:0}}
a{{color:var(--mag)}}
:focus-visible{{outline:3px solid var(--acesa);outline-offset:3px;border-radius:6px}}

/* ---------- topo, centralizado ---------- */
.topo{{padding-block:clamp(34px,6vw,58px) clamp(18px,3vw,26px);text-align:center}}
.topo img{{width:92px;height:92px;border-radius:50%;object-fit:cover;border:3px solid var(--papel-2);box-shadow:0 3px 16px rgba(43,37,34,.16)}}
.nome{{font:600 18px/1.2 var(--txt);margin-top:14px}}
.sub{{font:400 14px/1.4 var(--txt);color:var(--tinta-3);margin-top:4px}}
h1{{font:400 clamp(29px,5.4vw,46px)/1.1 var(--disp);letter-spacing:-.015em;margin-top:22px}}
.mao{{font:400 clamp(15.5px,2.3vw,19px)/1.7 var(--mao);color:var(--tinta-3);margin:18px auto 0;max-width:27em}}

.placar{{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--margem);border-bottom:1px solid var(--margem);margin-top:28px}}
.placar>div{{padding:14px 4px;position:relative}}
.placar>div+div::before{{content:"";position:absolute;left:0;top:18%;height:64%;width:1px;background:var(--margem)}}
.placar .n{{font:400 clamp(19px,4.4vw,28px)/1 var(--disp);white-space:nowrap}}
.placar .n u{{font-size:.42em;text-decoration:none;letter-spacing:.01em}}
.placar .viva .n{{color:var(--mag)}}
.placar .viva .n s{{text-decoration:none;font-size:.6em;vertical-align:.14em;margin-left:1px}}
.placar .r{{font:600 9.5px/1.3 var(--txt);letter-spacing:.12em;text-transform:uppercase;color:var(--tinta-3);margin-top:7px}}

/* ---------- porta ---------- */
.porta{{padding-block:clamp(26px,4vw,44px)}}
.pergunta{{display:none}}
.pergunta.ativa{{display:block;animation:sobe .35s ease}}
@keyframes sobe{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
.pergunta h2{{font:400 clamp(24px,3.8vw,34px)/1.2 var(--disp)}}
.pergunta .ajuda{{color:var(--tinta-3);margin-top:10px;font-size:16px}}
.pergunta input{{width:100%;margin-top:18px;font:400 20px/1.5 var(--txt);color:var(--tinta);background:transparent;border:0;border-bottom:2px solid var(--margem);padding:8px 2px}}
.pergunta input:focus{{outline:0;border-bottom-color:var(--mag)}}
.caminho{{display:block;width:100%;text-align:left;margin-top:10px;cursor:pointer;background:var(--papel-2);border:1px solid var(--margem);border-radius:14px;padding:17px 18px;font:500 16.5px/1.35 var(--txt);color:var(--tinta)}}
.caminho:hover,.caminho:focus-visible{{border-color:var(--mag);background:#fff}}
.sim-nao{{display:flex;gap:10px;margin-top:18px;flex-wrap:wrap}}
.sim-nao button{{flex:1 1 130px;cursor:pointer;border-radius:999px;padding:16px 20px;font:600 16px/1 var(--txt)}}
.sim{{background:var(--mag);color:#fff;border:0}}
.nao{{background:transparent;color:var(--tinta-2);border:1px solid var(--margem)}}
.avancar{{margin-top:20px;cursor:pointer;background:var(--mag);color:#fff;border:0;border-radius:999px;padding:16px 30px;font:600 16px/1 var(--txt)}}
.erro{{color:var(--mag);font-size:14.5px;margin-top:10px;min-height:1em}}
.passo-conta{{font:600 11px/1 var(--txt);letter-spacing:.14em;text-transform:uppercase;color:var(--tinta-3);margin-bottom:14px}}

/* ---------- navegação ---------- */
.trancado{{display:none}}
body.liberado .trancado{{display:block}}
body.liberado .porta{{display:none}}
.nav{{position:sticky;top:0;z-index:40;background:rgba(247,244,238,.95);backdrop-filter:blur(8px);
  border-top:1px solid var(--margem);border-bottom:1px solid var(--margem)}}
.nav .wrap{{display:flex;gap:4px;justify-content:center;flex-wrap:wrap}}
.nav a{{padding:13px 16px;font:600 13px/1 var(--txt);letter-spacing:.04em;color:var(--tinta-3);text-decoration:none;border-bottom:2px solid transparent;margin-bottom:-1px}}
.nav a:hover{{color:var(--tinta)}}
.nav a.aqui{{color:var(--mag);border-bottom-color:var(--mag)}}

/* ---------- capítulo ---------- */
.capitulo{{display:none;position:relative;scroll-margin-top:60px;padding-block:clamp(30px,5vw,52px) clamp(20px,3vw,30px)}}
.capitulo.aberto{{display:block}}
.cap-linha{{font:600 11px/1.5 var(--txt);letter-spacing:.11em;text-transform:uppercase;color:var(--tinta-3)}}
.cap-linha span{{color:var(--margem);margin:0 4px}}
.capitulo h2{{font:400 clamp(26px,4.2vw,38px)/1.12 var(--disp);letter-spacing:-.01em;margin-top:12px}}
.capitulo h3{{font:400 clamp(21px,3vw,27px)/1.2 var(--disp);margin-top:38px}}
.capitulo h4{{font:600 15px/1.35 var(--txt);margin-bottom:4px}}
.capitulo p{{margin-top:16px}}
.capitulo ul{{margin:14px 0 0;padding-left:20px}}
.capitulo li{{margin-bottom:6px}}
mark{{background:linear-gradient(transparent 14%,var(--caneta) 14%,var(--caneta) 93%,transparent 93%);color:inherit;padding:0 2px}}
.solta{{font:400 clamp(20px,3vw,27px)/1.35 var(--disp);color:var(--mag);margin-top:26px!important}}
.pequeno{{font-size:15.5px}}
.margem{{font:400 15px/1.6 var(--mao);color:var(--tinta-3);margin-top:14px;padding-left:16px;border-left:2px solid var(--margem)}}
@media(min-width:1120px){{.margem{{position:absolute;left:calc(50% + 365px);width:205px;margin-top:-54px;border-left:0;padding-left:0;transform:rotate(-1.2deg)}}}}

.bloco{{margin-top:22px;background:var(--papel-2);border:1px solid var(--margem);border-radius:8px;padding:18px 20px}}
.bloco>span{{display:block;font:600 10px/1 var(--txt);letter-spacing:.15em;text-transform:uppercase;color:var(--tinta-3)}}
.bloco p:first-of-type{{margin-top:10px}}

.copiar{{margin-top:20px;border:1.5px dashed rgba(139,8,63,.45);border-radius:8px;padding:18px 20px;background:var(--papel-2)}}
.copiar>span{{display:block;font:600 10px/1 var(--txt);letter-spacing:.15em;text-transform:uppercase;color:var(--mag);margin-bottom:12px}}
.copiar pre{{margin:0;white-space:pre-wrap;font:400 15.5px/1.75 var(--txt);color:var(--tinta-2)}}
.bt-copia{{margin-top:14px;cursor:pointer;background:transparent;border:1px solid var(--mag);color:var(--mag);border-radius:999px;padding:9px 20px;font:600 13px/1 var(--txt)}}
.bt-copia.ok{{background:var(--mag);color:#fff}}

.passos{{counter-reset:p;margin-top:22px;display:grid;gap:14px}}
.passos>div{{counter-increment:p;display:grid;grid-template-columns:38px 1fr;gap:14px;align-items:start}}
.passos>div::before{{content:counter(p);font:400 26px/1 var(--disp);color:var(--mag);text-align:center}}
.passos b{{display:block;font:600 11px/1 var(--txt);letter-spacing:.13em;text-transform:uppercase;margin-bottom:5px}}
.passos.curto>div{{align-items:center}}

.grupos{{margin-top:20px;display:grid;gap:16px}}
.grupos>div{{display:grid;grid-template-columns:34px 1fr;gap:14px;align-items:start}}
.grupos>div>b{{font:400 26px/1 var(--disp);color:var(--acesa);text-align:center}}
.grupos p{{margin-top:0;font-size:16.5px;color:var(--tinta-2)}}

.metodo{{margin-top:24px;background:var(--vinho);color:var(--pessego);border-radius:10px;padding:24px 24px 26px}}
.metodo>span{{display:block;font:600 10px/1 var(--txt);letter-spacing:.17em;text-transform:uppercase;color:var(--acesa);margin-bottom:14px}}
.metodo p{{margin:0;font:400 clamp(20px,2.9vw,26px)/1.3 var(--disp)}}
.metodo p.pequeno{{font:400 15.5px/1.7 var(--txt);color:rgba(252,234,223,.8);margin-top:14px}}
.metodo ul{{margin:0;padding-left:18px;font-size:16.5px}}
.metodo li{{margin-bottom:7px}}
.metodo b{{color:#fff}}

.ficha{{margin-top:22px}}
.ficha>div{{display:grid;grid-template-columns:auto 1fr;gap:3px 10px;align-items:baseline;padding:11px 0;border-bottom:1px solid var(--margem)}}
.ficha b{{font:600 11px/1.4 var(--txt);letter-spacing:.1em;text-transform:uppercase;color:var(--mag)}}
.ficha i{{display:block;border-bottom:1px solid var(--tinta-3);height:1.4em}}
.ficha em{{grid-column:1/-1;font-style:normal;font-size:14px;color:var(--tinta-3)}}

.par{{display:grid;gap:10px;margin-top:14px}}
@media(min-width:620px){{.par{{grid-template-columns:1fr 1fr}}}}
.par>div{{background:var(--papel);border:1px solid var(--margem);border-radius:6px;padding:14px 16px;font-size:16px}}
.par .rot{{display:block;font:600 10px/1 var(--txt);letter-spacing:.13em;text-transform:uppercase;color:var(--tinta-3);margin-bottom:7px}}
.par .depois{{border-color:rgba(139,8,63,.3)}}
.par .depois .rot{{color:var(--mag)}}

.camadas{{margin-top:22px;display:grid;justify-items:center}}
.camada{{width:100%;background:var(--papel-2);border:1px solid var(--margem);border-radius:6px;padding:15px 18px}}
.camada b{{display:block;font:600 11px/1 var(--txt);letter-spacing:.14em;text-transform:uppercase;color:var(--mag);margin-bottom:7px}}
.camada span{{font-size:16px;color:var(--tinta-2)}}
.seta{{width:2px;height:22px;background:var(--margem);position:relative}}
.seta::after{{content:"";position:absolute;left:-4px;bottom:0;border-left:5px solid transparent;border-right:5px solid transparent;border-top:7px solid var(--margem)}}
.marcacoes{{margin-top:18px;display:grid;gap:8px}}
.marca{{display:flex;gap:11px;align-items:center;font-size:16.5px;color:var(--tinta-2)}}
.marca i{{flex:0 0 auto;width:19px;height:19px;border:1.5px solid var(--tinta-3);border-radius:4px}}
.marca.sua i{{background:var(--mag);border-color:var(--mag);position:relative}}
.marca.sua i::after{{content:"";position:absolute;left:5.5px;top:1.5px;width:5px;height:10px;border:solid #fff;border-width:0 2px 2px 0;transform:rotate(42deg)}}
.marca.sua{{color:var(--tinta);font-weight:500}}
.marca em{{font-style:normal;font:400 14px/1 var(--mao);color:var(--acesa);margin-left:4px}}

.proximo{{display:block;margin-top:46px;text-decoration:none;color:var(--tinta);background:var(--papel-2);
  border:1px solid var(--margem);border-left:4px solid var(--mag);border-radius:10px;padding:22px 24px 20px}}
.proximo:hover{{background:#fff;border-left-color:var(--acesa)}}
.proximo>span{{display:block;font:600 10px/1 var(--txt);letter-spacing:.17em;text-transform:uppercase;color:var(--tinta-3)}}
.proximo b{{display:block;font:400 clamp(21px,3.2vw,28px)/1.22 var(--disp);margin-top:10px}}
.proximo i{{display:block;font-style:normal;font:600 14px/1 var(--txt);color:var(--mag);margin-top:16px}}
.aguarde{{margin-top:46px;text-align:center;font:400 18px/1.6 var(--mao);color:var(--tinta-3)}}

.rodape-nota{{border-top:1px solid var(--margem);padding-block:clamp(28px,5vw,46px);color:var(--tinta-2);font-size:16px}}
.rodape-nota a{{font-weight:600}}
footer{{border-top:1px solid var(--margem);font-size:13px;color:var(--tinta-3)}}
footer .wrap{{padding-block:18px 42px;display:flex;flex-wrap:wrap;gap:8px 20px;justify-content:space-between}}
</style>

<header class="topo faixa"><div class="wrap">
  <img src="{FOTO}" alt="Danielle Lemos">
  <div class="nome">Danielle Lemos</div>
  <div class="sub">@daanylemos <span id="hoje-data"></span></div>
  <h1>Como vou sair dos 3K para os 20K?</h1>
  <p class="mao">não sei se vou bater a meta, mas vou registrar aqui tudo que eu testei, o que funcionou e o que não funcionou</p>

  <div class="placar">
    <div><div class="n">3.883</div><div class="r">dia 1</div></div>
    <div class="viva"><div class="n" id="n-hoje">&middot;&middot;&middot;</div><div class="r">hoje</div></div>
    <div><div class="n">20K</div><div class="r">a meta</div></div>
    <div><div class="n">16<u> semanas</u></div><div class="r">o prazo</div></div>
  </div>
</div></header>

<section class="porta faixa" id="porta"><div class="wrap">
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
</div></section>

<div class="trancado">
<nav class="nav faixa"><div class="wrap">
      {NAV}
</div></nav>

<main class="faixa"><div class="wrap">
{CAPS_HTML}
</div></main>

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

document.getElementById("hoje-data").textContent="· "+new Date().toLocaleDateString("pt-BR",
  {{weekday:"long",day:"numeric",month:"long"}});

fetch(API+"/diario_placar?select=*",{{headers:{{apikey:CHAVE}}}}).then(r=>r.json()).then(l=>{{
  const p=l[0]; if(!p)return;
  document.getElementById("n-hoje").innerHTML=mil(p.hoje)+(p.hoje>p.inicio?"<s>&#8593;</s>":"");
}}).catch(()=>{{document.getElementById("n-hoje").textContent="3.884"}});

function marcarEco(){{
  const eco=resp.eco; if(!eco)return;
  document.querySelectorAll(".marca").forEach(m=>{{
    if(m.dataset.eco===eco){{m.classList.add("sua");if(!m.querySelector("em")){{const e=document.createElement("em");e.textContent="você";m.appendChild(e)}}}}
  }});
}}

const caps=[...document.querySelectorAll(".capitulo")];
function abrir(n,rolar){{
  caps.forEach(c=>c.classList.toggle("aberto",c.dataset.cap===String(n)));
  document.querySelectorAll(".nav a").forEach(a=>a.classList.toggle("aqui",a.dataset.ir===String(n)));
  history.replaceState(null,"","#cap"+n);
  // salto instantaneo: com rolagem suave o navegador se perde, porque o documento encolhe
  // no meio da animacao quando o capitulo anterior some
  if(rolar)requestAnimationFrame(()=>window.scrollTo(0,document.querySelector(".nav").offsetTop));
}}
document.querySelectorAll("[data-ir]").forEach(a=>a.addEventListener("click",ev=>{{
  ev.preventDefault(); abrir(a.dataset.ir,true);
}}));
const pedido=(location.hash.match(/^#cap(\\d+)$/)||[])[1];
abrir(caps.some(c=>c.dataset.cap===pedido)?pedido:caps[0].dataset.cap,false);

document.querySelectorAll(".bt-copia").forEach(b=>b.addEventListener("click",async ()=>{{
  const t=b.parentElement.querySelector("pre").innerText;
  try{{await navigator.clipboard.writeText(t)}}catch(e){{
    const a=document.createElement("textarea");a.value=t;document.body.appendChild(a);a.select();
    try{{document.execCommand("copy")}}catch(e2){{}} a.remove();
  }}
  b.textContent="copiado"; b.classList.add("ok");
  setTimeout(()=>{{b.textContent="copiar";b.classList.remove("ok")}},2200);
}}));

function liberar(){{
  document.body.classList.add("liberado");
  try{{localStorage.setItem("dl_cadastro","1");const e=localStorage.getItem("dl_diario_eco");if(e)resp.eco=e}}catch(e){{}}
  marcarEco();
}}
try{{if(localStorage.getItem("dl_cadastro")==="1")liberar()}}catch(e){{}}
if(!document.body.classList.contains("liberado")&&MC){{fetch(FN+"?mc="+encodeURIComponent(MC)).then(r=>r.json()).then(d=>{{if(d.existe)liberar()}}).catch(()=>{{}})}}

const passos=[...document.querySelectorAll(".pergunta")];
function mostrar(n){{
  passos.forEach((p,k)=>p.classList.toggle("ativa",k===n));
  document.getElementById("conta").textContent="Pergunta "+(n+1)+" de "+passos.length;
  const inp=passos[n].querySelector("input"); if(inp)setTimeout(()=>inp.focus(),80);
}}
function erro(n,t){{passos[n].querySelector(".erro").textContent=t||""}}
passos.forEach((p,n)=>{{
  const bt=p.querySelector(".avancar");
  if(bt)bt.addEventListener("click",()=>{{
    erro(n,"");
    if(n===0){{const v=document.getElementById("q-nome").value.trim();
      if(v.length<2)return erro(n,"Me diz como você se chama."); resp.nome=v;}}
    if(n===1){{const v=document.getElementById("q-insta").value.trim().replace(/^@/,"");
      if(v.length<2)return erro(n,"Falta o seu @."); resp.instagram=v;}}
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
  const aceite=b.dataset.aceite==="sim"; erro(4,"");
  b.disabled=true; const antes=b.textContent; b.textContent="Abrindo...";
  const ECO={{{", ".join(f'"{rot}":"{eco}"' for rot, eco in CAMINHOS)}}};
  const d={{nome:resp.nome,email:resp.email,whatsapp:resp.whatsapp,instagram:resp.instagram,
    profissao:resp.caminho||"",origem:"diario+"+(aceite?"sim":"nao"),mc:MC,tarefa_chata:""}};
  const PREVIA=!/dlestudio\\.com\\.br$/.test(location.hostname);
  let r=null;try{{r=await fetch(FN,{{method:"POST",headers:{{"content-type":"application/json"}},body:JSON.stringify(d)}})}}catch(e){{}}
  if(!(r&&r.ok)&&!PREVIA){{b.disabled=false;b.textContent=antes;return erro(4,"Não consegui salvar agora. Tenta de novo em alguns segundos.")}}
  resp.eco=ECO[resp.caminho]||"";
  try{{localStorage.setItem("dl_diario_eco",resp.eco)}}catch(e){{}}
  document.querySelector("#porta .wrap").innerHTML='<h2 style="font:400 clamp(24px,3.8vw,34px)/1.2 var(--disp)">pronto, agora é só ler</h2>';
  setTimeout(()=>{{liberar();const t=document.querySelector(".nav").offsetTop;window.scrollTo({{top:t,behavior:"smooth"}})}},700);
}}));

document.getElementById("marcacoes").innerHTML='{MARCACOES}';
marcarEco();
</script>
</html>
"""

(AQUI / "index.html").write_text(HTML, encoding="utf-8")
print("ok index.html", len(HTML) // 1024, "KB ·",
      " · ".join(f"cap {c['n']}: {minutos(c['corpo'])} min" for c in CAPITULOS))
