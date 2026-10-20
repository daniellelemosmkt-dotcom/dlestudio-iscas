"""Monta a pagina da isca CEREBRO (os 5 arquivos do cerebro da marca).

Padrao oficial da marca (PADRAO-DE-PAGINA-DA-MARCA.md, 20/10/2026): faixas escuras e gelo
alternadas, Advercase no display, Poppins no texto, magenta aceso no botao.
Cadastro obrigatorio antes do conteudo, no mesmo contrato das outras iscas.

Uso: python montar.py   ->  index.html nesta pasta
"""
import base64
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ASSETS = Path("G:/Meu Drive/DANIELLE   PROJETOS/PRODUTOS DL ESTÚDIO/04 KIT E PLUGINS/_paginas/assets")

ADV = "data:font/woff2;base64," + base64.b64encode((ASSETS / "Advercase-Regular.woff2").read_bytes()).decode()
SELO = "data:image/png;base64," + base64.b64encode((ASSETS / "selo-dourado.png").read_bytes()).decode()

PIXEL = (
    '<!-- Meta Pixel -->\n<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?'
    'n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";'
    'n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}'
    '(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","2130554737847082");'
    'fbq("track","PageView");</script>\n<noscript><img height="1" width="1" style="display:none" '
    'src="https://www.facebook.com/tr?id=2130554737847082&ev=PageView&noscript=1"/></noscript>\n<!-- /Meta Pixel -->'
)

# Os cinco arquivos. Cada um: numero, nome, o que escrever (paragrafos), atalho, arquivo em branco.
ARQUIVOS = [
    {
        "nome": "quem-eu-sou",
        "resumo": "O que você faz, para quem, e com que nome você chama cada coisa.",
        "paras": [
            "Escreva o que você vende, para quem, onde você atende e quanto custa.",
            "Escreva também o nome que você dá para cada serviço, do jeito que você fala com o cliente. "
            "Se você chama de consulta estendida, ele passa a chamar de consulta estendida.",
            "Quanto mais específico você for aqui, menos ele inventa.",
        ],
        "atalho": "Se travar, copie a descrição que já está na sua bio e vá acrescentando o que falta.",
        "branco": """# Quem eu sou

O que eu vendo:
Para quem é:
Onde eu atendo:
Quanto custa:

Como eu chamo cada serviço (o nome que eu uso com o cliente):
-
-
-
""",
    },
    {
        "nome": "como-eu-falo",
        "resumo": "Cinco textos seus, para ele parar de escrever como robô.",
        "paras": [
            "Cole cinco textos seus: legendas, e-mails, mensagens de direct. Escolha os que você escreveria "
            "de novo do mesmo jeito.",
            "Embaixo, escreva as palavras e os emojis que você nunca usa.",
        ],
        "atalho": "Se travar na hora de explicar o seu estilo (acontece com todo mundo), mande a transcrição "
                  "de uma reunião sua e peça para ele descrever como você fala.",
        "branco": """# Como eu falo

Cinco textos meus, colados inteiros:

1.

2.

3.

4.

5.

Palavras que eu nunca uso:
Emojis que eu nunca uso:
""",
    },
    {
        "nome": "quem-compra",
        "resumo": "Três clientes de verdade, e quem não é cliente seu.",
        "paras": [
            "Escreva três clientes de verdade, com o nome trocado. De cada um: o que a pessoa procurava, "
            "o que fez ela pensar duas vezes antes de fechar e a frase que fez ela decidir.",
            "Escreva também quem não é seu cliente, para ele não escrever para quem você não quer atender.",
        ],
        "atalho": "Abra as três últimas conversas de venda do seu direct e cole ali dentro.",
        "branco": """# Quem compra

Cliente 1 (nome trocado)
O que procurava:
O que fez pensar duas vezes:
A frase que fez decidir:

Cliente 2 (nome trocado)
O que procurava:
O que fez pensar duas vezes:
A frase que fez decidir:

Cliente 3 (nome trocado)
O que procurava:
O que fez pensar duas vezes:
A frase que fez decidir:

Quem não é meu cliente:
""",
    },
    {
        "nome": "o-que-eu-vendo",
        "resumo": "Preço, prazo e, principalmente, o que não está incluído.",
        "paras": [
            "Escreva cada serviço com o preço, o prazo e a forma de pagamento.",
            "Escreva o que está incluído e, principalmente, o que não está. É a parte que todo mundo pula e "
            "que depois vira mal-entendido no direct.",
            "Se o seu preço muda de caso para caso, escreva o que faz o valor subir e o que faz descer.",
        ],
        "atalho": "Se você nunca escreveu isso em lugar nenhum, comece pelo serviço que você mais vende e "
                  "deixe os outros para depois.",
        "branco": """# O que eu vendo

Serviço:
Preço:
Prazo:
Forma de pagamento:
Está incluído:
Não está incluído:

(repita o bloco acima para cada serviço)

O que faz o valor subir:
O que faz o valor descer:
""",
    },
    {
        "nome": "o-que-nunca-fazer",
        "resumo": "As suas regras, uma por linha. O arquivo que mais cresce.",
        "paras": [
            "Escreva as suas regras, uma por linha: o que não pode ser prometido, as palavras proibidas e o "
            "que precisa da sua aprovação antes de ser enviado ou publicado.",
            "Toda vez que você corrigir o Claude, escreva a correção aqui. Em uma semana esse arquivo já "
            "está completo.",
        ],
        "atalho": "Comece com três linhas. Ele vai crescer sozinho, cada vez que você disser “não é assim”.",
        "branco": """# O que nunca fazer

Nunca prometer:
-
-

Palavras proibidas:
-
-

Precisa da minha aprovação antes de enviar ou publicar:
-
-

Correções (toda vez que eu corrigir, escrevo aqui):
-
""",
    },
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


blocos = []
for i, a in enumerate(ARQUIVOS, 1):
    paras = "\n".join(f"      <p>{p}</p>" for p in a["paras"])
    blocos.append(f"""  <article class="arq">
    <div class="arq-cab">
      <span class="num">{i}</span>
      <div>
        <h3>{a['nome']}<span class="ext">.md</span></h3>
        <p class="arq-res">{a['resumo']}</p>
      </div>
    </div>
    <div class="arq-corpo">
{paras}
      <p class="atalho"><b>Se você travar:</b> {a['atalho']}</p>
      <div class="papel">
        <div class="papel-cab"><span>{a['nome']}.md</span><button class="copiar" type="button" data-alvo="t{i}">Copiar em branco</button></div>
        <pre id="t{i}">{esc(a['branco']).rstrip()}</pre>
      </div>
    </div>
  </article>""")

BLOCOS = "\n".join(blocos)

HTML = f"""<!doctype html>
<html lang="pt-BR">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Os 5 arquivos que ensinam o Claude a ser você | Dani Lemos</title>
<meta name="description" content="Os cinco arquivos do cérebro da sua marca, prontos para preencher e subir dentro de um Projeto do Claude.">
<meta property="og:title" content="Os 5 arquivos que ensinam o Claude a ser você">
<meta property="og:description" content="Preencha os cinco, suba em Contexto, e ele para de errar quem você é.">
{PIXEL}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap">
<style>
@font-face{{font-family:"Advercase";src:url({ADV}) format("woff2");font-weight:400;font-display:swap}}
:root{{
  --noite:#160E11; --noite-2:#22151A; --vinho:#3A1424; --mag:#8B083F; --acesa:#E2307A; --pessego:#FCEADF;
  --gelo:#F4F2EE; --branco:#FBFAF8; --graf:#292929; --linha:#E2DAD3; --linha-esc:rgba(252,234,223,.14);
  --suave:#6B6266; --suave-esc:#BFAEB4;
  --disp:"Advercase","Playfair Display",Georgia,serif; --txt:"Poppins","Segoe UI",Arial,sans-serif;
  color-scheme:light;
}}
*{{box-sizing:border-box}}
html{{background:var(--noite)}}
body{{margin:0;background:var(--gelo);color:var(--graf);font:400 17px/1.6 var(--txt);-webkit-font-smoothing:antialiased;overflow-x:hidden}}
.faixa{{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.wrap{{max-width:1120px;margin:0 auto}}
.estreito{{max-width:760px;margin:0 auto}}
a{{color:inherit}}
:focus-visible{{outline:3px solid var(--acesa);outline-offset:3px;border-radius:6px}}
h1,h2,h3{{text-wrap:balance;margin:0}}
p{{margin:0}}
.escuro{{background:var(--noite);color:var(--branco)}}
.eyebrow{{font:600 13px/1.2 var(--txt);letter-spacing:.16em;text-transform:uppercase;color:var(--mag)}}
.escuro .eyebrow{{color:var(--acesa)}}
.tit{{font:400 clamp(32px,5.2vw,58px)/1.02 var(--disp);margin-top:12px;letter-spacing:-.01em}}
.tit em{{font-style:normal;color:var(--mag)}}
.escuro .tit em{{color:var(--acesa)}}
.sub{{color:var(--suave);margin-top:16px;max-width:38em;font-size:18px}}
.escuro .sub{{color:var(--suave-esc)}}
.secao{{padding-block:clamp(60px,8vw,104px)}}
.botao{{display:inline-flex;align-items:center;justify-content:center;gap:12px;background:var(--acesa);color:#fff;text-decoration:none;border:0;cursor:pointer;
  font:600 18px/1 var(--txt);padding:20px 30px;border-radius:999px;box-shadow:0 12px 34px rgba(226,48,122,.38);transition:transform .2s,box-shadow .2s}}
.botao:hover{{transform:translateY(-2px);box-shadow:0 16px 40px rgba(226,48,122,.5)}}
.botao[disabled]{{opacity:.6;cursor:default;transform:none}}
.botao .seta{{transition:transform .2s}}
.botao:hover .seta{{transform:translateX(4px)}}

/* topo */
.topo{{position:relative;overflow:hidden;padding-block:clamp(30px,5vw,64px) clamp(34px,6vw,80px);
  background:radial-gradient(60% 50% at 50% 62%,rgba(226,48,122,.30),transparent 70%),radial-gradient(40% 40% at 12% 10%,rgba(139,8,63,.35),transparent 70%),var(--noite)}}
.topo-txt{{text-align:center;max-width:880px;margin:0 auto}}
.pilula{{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--linha-esc);background:rgba(252,234,223,.06);border-radius:999px;padding:8px 14px;font-size:14px;color:var(--pessego)}}
.pilula i{{width:8px;height:8px;border-radius:50%;background:var(--acesa);box-shadow:0 0 0 4px rgba(226,48,122,.25)}}
h1{{font:400 clamp(34px,6.2vw,78px)/1 var(--disp);letter-spacing:-.015em;margin-top:16px}}
h1 .acesa{{color:var(--acesa)}}
.topo .lead{{font-size:clamp(16px,2.1vw,21px);line-height:1.5;color:var(--suave-esc);max-width:32em;margin:16px auto 0}}
.topo .lead b{{color:var(--branco);font-weight:500}}
.nomes{{display:flex;flex-wrap:wrap;gap:7px;justify-content:center;margin-top:18px}}
.nomes span{{font:500 13px/1 var(--txt);color:var(--pessego);border:1px solid var(--linha-esc);background:rgba(252,234,223,.06);border-radius:8px;padding:9px 12px}}

/* cadastro */
.cadastro{{background:var(--gelo)}}
.cartao{{background:var(--branco);border:1px solid var(--linha);border-radius:20px;padding:clamp(22px,4vw,38px);box-shadow:0 18px 50px rgba(41,41,41,.08)}}
.cartao h2{{font:400 clamp(26px,3.6vw,36px)/1.1 var(--disp)}}
.cartao .ajuda{{color:var(--suave);font-size:15px;margin-top:10px}}
label{{display:block;margin-top:18px;font:500 14px/1.4 var(--txt);color:var(--graf)}}
label .opc{{color:var(--suave);font-weight:400}}
input,select,textarea{{width:100%;margin-top:7px;font:400 16px/1.5 var(--txt);color:var(--graf);background:#fff;border:1px solid var(--linha);border-radius:12px;padding:13px 14px}}
textarea{{min-height:84px;resize:vertical}}
.cartao .botao{{width:100%;margin-top:24px}}
.lgpd{{font-size:13px;color:var(--suave);margin-top:14px;text-align:center}}
.erro{{color:var(--mag);font-size:14px;margin-top:12px;min-height:1em}}

/* conteudo travado */
.trancado{{display:none}}
body.liberado .trancado{{display:block}}
body.liberado .cadastro{{display:none}}

/* arquivos */
.arq{{background:var(--branco);border:1px solid var(--linha);border-radius:20px;padding:clamp(20px,3vw,32px);margin-top:20px;box-shadow:0 10px 30px rgba(41,41,41,.05)}}
.arq-cab{{display:flex;gap:16px;align-items:flex-start}}
.num{{flex:0 0 auto;width:44px;height:44px;border-radius:50%;background:var(--mag);color:#fff;font:600 19px/44px var(--txt);text-align:center}}
.arq h3{{font:400 clamp(24px,3.2vw,34px)/1.1 var(--disp);color:var(--graf)}}
.arq h3 .ext{{color:var(--mag)}}
.arq-res{{color:var(--suave);font-size:15px;margin-top:6px}}
.arq-corpo{{margin-top:18px;display:grid;gap:14px}}
.atalho{{background:var(--pessego);border-radius:12px;padding:14px 16px;font-size:16px;color:var(--vinho)}}
.atalho b{{color:var(--mag)}}
.papel{{border:1px solid var(--linha);border-radius:14px;overflow:hidden;margin-top:4px}}
.papel-cab{{display:flex;gap:10px;flex-wrap:wrap;align-items:center;justify-content:space-between;background:var(--noite);color:var(--pessego);padding:11px 14px;font:500 13px/1 var(--txt)}}
.papel-cab span{{white-space:nowrap}}
.copiar{{border:0;cursor:pointer;white-space:nowrap;background:var(--acesa);color:#fff;font:600 13px/1 var(--txt);padding:10px 14px;border-radius:999px}}
pre{{margin:0;padding:16px;background:#fff;color:var(--graf);font:400 14px/1.7 ui-monospace,"Cascadia Mono",Consolas,monospace;white-space:pre-wrap;word-break:break-word}}

/* passos de onde sobe */
.passos{{display:grid;gap:14px;margin-top:26px;counter-reset:p}}
.passo{{display:flex;gap:14px;align-items:flex-start;background:var(--noite-2);border:1px solid var(--linha-esc);border-radius:16px;padding:18px}}
.passo i{{flex:0 0 auto;width:30px;height:30px;border-radius:50%;background:var(--acesa);color:#fff;font:600 15px/30px var(--txt);text-align:center;font-style:normal}}
.passo b{{display:block;color:var(--branco);font-weight:600}}
.passo p{{color:var(--suave-esc);font-size:16px;margin-top:4px}}

/* fecho */
.fecho{{text-align:center}}
.fecho .tit{{margin-top:12px}}
.fecho .sub{{margin-left:auto;margin-right:auto}}
.fecho .botao{{margin-top:28px}}

footer{{background:var(--noite);color:var(--suave-esc);text-align:center;padding:40px 16px 56px;font-size:14px}}
footer img{{width:62px;height:auto;opacity:.9}}
footer p{{margin-top:12px}}
footer a{{color:var(--pessego)}}

.aviso{{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(12px);background:var(--noite);color:var(--pessego);
  padding:13px 20px;border-radius:999px;font:500 15px/1 var(--txt);opacity:0;pointer-events:none;transition:.2s;z-index:9}}
.aviso.ver{{opacity:1;transform:translateX(-50%)}}
</style>

<header class="topo escuro faixa">
  <div class="wrap topo-txt">
    <span class="pilula"><i></i>Material da Dani</span>
    <h1>Os 5 arquivos que ensinam<br><span class="acesa">o Claude a ser você</span></h1>
    <p class="lead">Preencha uma vez, suba dentro do seu Projeto, e ele <b>para de errar quem você é</b>. Cada arquivo com o que escrever dentro e o modelo em branco.</p>
    <div class="nomes">
      <span>quem-eu-sou.md</span><span>como-eu-falo.md</span><span>quem-compra.md</span><span>o-que-eu-vendo.md</span><span>o-que-nunca-fazer.md</span>
    </div>
  </div>
</header>

<section class="cadastro faixa" id="cadastro" style="padding-block:clamp(26px,5vw,72px)">
  <div class="wrap estreito">
    <div class="cartao">
      <h2>Falta pouco para pegar os seus cinco arquivos</h2>
      <p class="ajuda">Você preenche uma vez só e depois acessa qualquer material.</p>
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
        <label>O que o Claude mais erra quando escreve por você? <span class="opc">(opcional)</span>
          <textarea name="tarefa_chata"></textarea></label>
        <div class="erro" id="erro"></div>
        <button class="botao" type="submit">Quero os 5 arquivos <span class="seta">→</span></button>
        <p class="lgpd">Ao enviar, você concorda em receber meus conteúdos e novidades por WhatsApp e e-mail. Pode pedir para sair quando quiser.</p>
      </form>
    </div>
  </div>
</section>

<div class="trancado">

<section class="secao faixa">
  <div class="wrap estreito">
    <span class="eyebrow">Antes de tudo</span>
    <h2 class="tit">O problema não é o seu pedido. <em>É que ele não sabe quem você é.</em></h2>
    <p class="sub">Você pede um texto e ele volta genérico. Você explica melhor e ele volta quase bom. No dia seguinte, em outra conversa, tudo de novo do zero.</p>
    <p class="sub">Os cinco arquivos abaixo resolvem isso de uma vez. Preencha na ordem, do jeito que você fala, sem se preocupar em escrever bonito: quem vai ler é ele.</p>
  </div>
</section>

<section class="secao faixa" style="padding-top:0">
  <div class="wrap estreito">
{BLOCOS}
  </div>
</section>

<section class="secao escuro faixa">
  <div class="wrap estreito">
    <span class="eyebrow">A parte que quase todo mundo erra</span>
    <h2 class="tit">Onde esses cinco <em>ficam guardados</em></h2>
    <p class="sub">Não cole esses textos no meio de uma conversa. Colado numa conversa, vale só naquela conversa, e na próxima ele esquece.</p>
    <div class="passos">
      <div class="passo"><i>1</i><div><b>Abra o Claude e crie um Projeto</b><p>No menu da esquerda, em Projetos, clique em Novo projeto e dê o nome do seu negócio.</p></div></div>
      <div class="passo"><i>2</i><div><b>Abra o Contexto do projeto</b><p>Dentro do projeto, no canto direito, procure Contexto. É ali que os arquivos moram.</p></div></div>
      <div class="passo"><i>3</i><div><b>Suba os cinco arquivos</b><p>Um por um, com o nome que está aqui. Pode ser arquivo de texto mesmo.</p></div></div>
      <div class="passo"><i>4</i><div><b>Peça qualquer coisa dentro desse projeto</b><p>Em Contexto ele lê os cinco toda vez que responde, sem você precisar lembrar. É isso que faz a resposta sair certa mesmo quando o seu pedido é curto.</p></div></div>
    </div>
  </div>
</section>

<section class="secao faixa fecho" id="claude-do-zero">
  <div class="wrap estreito">
    <span class="eyebrow">Se você quiser ir além dos cinco</span>
    <h2 class="tit">Montar esses arquivos é a <em>primeira coisa</em> que eu ensino para quem está começando do zero.</h2>
    <p class="sub">No Claude do Zero, para iniciantes, eu começo do absoluto zero e vou até o Claude trabalhando por você, com o pedido pronto em cada aula. Se o seu cérebro de marca já está montado, é o passo seguinte natural.</p>
    <a class="botao" href="https://chk.eduzz.com/lniykl57?utm_source=isca&amp;utm_campaign=cerebro">Ver o Claude do Zero <span class="seta">→</span></a>
  </div>
</section>

</div>

<footer>
  <img src="{SELO}" alt="Selo DL">
  <p>Siga <a href="https://instagram.com/daanylemos">@daanylemos</a> no Instagram para aprender a colocar a IA para trabalhar por você.</p>
  <p>Dani Lemos, DL Estúdio</p>
</footer>

<div class="aviso" role="status" aria-live="polite"></div>
<script>
const ORIGEM="cerebro";
const FN="https://veogbuoxtbpaxoqvuakr.supabase.co/functions/v1/lead-isca-dlestudio";
const MC=new URLSearchParams(location.search).get("mc")||"";
const aviso=document.querySelector(".aviso"),f=document.getElementById("fcad"),erro=document.getElementById("erro");
function mostrar(t){{aviso.textContent=t;aviso.classList.add("ver");setTimeout(()=>aviso.classList.remove("ver"),1800)}}
function liberar(){{document.body.classList.add("liberado");try{{localStorage.setItem("dl_cadastro","1")}}catch(e){{}}}}
try{{if(localStorage.getItem("dl_cadastro")==="1")liberar()}}catch(e){{}}
if(!document.body.classList.contains("liberado")&&MC){{fetch(FN+"?mc="+encodeURIComponent(MC)).then(r=>r.json()).then(d=>{{if(d.existe)liberar()}}).catch(()=>{{}})}}
f.addEventListener("submit",async ev=>{{ev.preventDefault();erro.textContent="";
 const d=Object.fromEntries(new FormData(f));d.origem=ORIGEM;d.mc=MC;
 if(!d.nome||!d.email||!d.whatsapp||!d.instagram||!d.profissao){{erro.textContent="Preencha todos os campos (só a última pergunta é opcional).";return}}
 const bt=f.querySelector("[type=submit]");bt.disabled=true;bt.textContent="Liberando...";
 const PREVIA=!/dlestudio\\.com\\.br$/.test(location.hostname);
 let r=null;try{{r=await fetch(FN,{{method:"POST",headers:{{"content-type":"application/json"}},body:JSON.stringify(d)}})}}catch(e){{}}
 const ok=r&&r.ok;
 if(!ok&&!PREVIA){{erro.textContent=(r&&r.status===400)?"Confere o WhatsApp (com DDD) e o e-mail.":"Não consegui salvar agora. Tenta de novo em alguns segundos.";bt.disabled=false;bt.innerHTML='Quero os 5 arquivos <span class="seta">→</span>';return}}
 liberar();
 const alvo=document.querySelector(".trancado");if(alvo)alvo.scrollIntoView({{behavior:"smooth",block:"start"}});
}});
document.addEventListener("click",ev=>{{const b=ev.target.closest(".copiar");if(!b)return;
 const t=document.getElementById(b.dataset.alvo);if(!t)return;
 navigator.clipboard.writeText(t.textContent).then(()=>mostrar("Arquivo copiado")).catch(()=>mostrar("Selecione e copie o texto"));
}});
</script>
</html>
"""

(AQUI / "index.html").write_text(HTML, encoding="utf-8")
print("ok index.html", len(HTML) // 1024, "KB")
