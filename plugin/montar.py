"""Monta a pagina da isca PLUGIN (as skills e plugins que a Anthropic deixou abertos).

Padrao oficial da marca: reaproveita o CSS da pagina CEREBRO, que e a primeira no padrao
(PADRAO-DE-PAGINA-DA-MARCA.md, 20/10/2026). Assim o design system tem um lugar so.

Decisao de 20/10 (conversa mestre, gravada em dlestudio.iscas slug plugin): esta isca NAO
entrega a lista de plugins da Dani, porque nove dos onze instalados no Claude dela sao design
systems de cliente e dois sao o Meu Funcionario, que e pago. Ela entrega o passo a passo de
instalar qualquer plugin e a lista dos PUBLICOS que valem a pena.

Tudo que esta escrito aqui foi conferido em 20/10/2026 na documentacao oficial
(code.claude.com/docs/en/plugins/install) e nos repositorios anthropics/skills e
anthropics/claude-plugins-official.

Uso: python montar.py   ->  index.html nesta pasta
"""
import base64
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ASSETS = Path("G:/Meu Drive/DANIELLE   PROJETOS/PRODUTOS DL ESTÚDIO/04 KIT E PLUGINS/_paginas/assets")

ADV = "data:font/woff2;base64," + base64.b64encode((ASSETS / "Advercase-Regular.woff2").read_bytes()).decode()
SELO = "data:image/png;base64," + base64.b64encode((ASSETS / "selo-dourado.png").read_bytes()).decode()

# O CSS vem da pagina CEREBRO, para nao existirem dois design systems.
CEREBRO = (AQUI.parent / "cerebro" / "index.html").read_text(encoding="utf-8")
CSS = re.search(r"<style>(.*?)</style>", CEREBRO, re.S).group(1)
CSS = CSS.replace(re.search(r"src:url\((data:font/woff2;base64,[^)]+)\)", CSS).group(1), ADV)

PIXEL = (
    '<!-- Meta Pixel -->\n<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?'
    'n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";'
    'n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}'
    '(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","2130554737847082");'
    'fbq("track","PageView");</script>\n<noscript><img height="1" width="1" style="display:none" '
    'src="https://www.facebook.com/tr?id=2130554737847082&ev=PageView&noscript=1"/></noscript>\n<!-- /Meta Pixel -->'
)

PASSOS = [
    ("Abra a aba Code no aplicativo do Claude",
     "É a aba onde o Claude trabalha nos seus arquivos. Se você só usa o Claude pelo chat, é essa que você ainda não abriu."),
    ("Clique no sinal de mais, do lado da caixa de escrever",
     "No menu que abre, escolha <b>Adicionar plugins</b>. Se aparecer <b>Plugins</b>, clique nele e depois em <b>Procurar plugins</b>."),
    ("Escolha o que você quer na lista e clique",
     "Antes de confirmar, leia o que ele diz que vai instalar. Plugin é código de outra pessoa rodando no seu Claude, então instale só o que você reconhece."),
    ("Escolha onde ele vale",
     "<b>Para você</b> deixa o plugin disponível em todos os seus projetos. É a opção certa quando você está começando."),
]

LISTA = [
    {
        "nome": "Documentos de verdade",
        "id": "document-skills",
        "resolve": "Faz o Claude entregar arquivo pronto em Word, Excel, PowerPoint e PDF, em vez de texto na tela para você copiar e formatar na mão.",
        "pra_quem": "Relatório de paciente, proposta para cliente, planilha de controle, apresentação de reunião.",
        "comando": "/plugin marketplace add anthropics/skills\n/plugin install document-skills@anthropic-agent-skills",
    },
    {
        "nome": "Ensinar uma tarefa uma vez",
        "id": "skill-creator",
        "resolve": "Monta com você uma skill nova: você explica uma vez como quer que uma tarefa seja feita e o Claude passa a fazer sempre daquele jeito, sem você repetir.",
        "pra_quem": "Aquela tarefa que você refaz toda semana e sempre corrige do mesmo jeito.",
        "comando": "/plugin install skill-creator@claude-plugins-official",
    },
    {
        "nome": "Os exemplos que a Anthropic publicou",
        "id": "example-skills",
        "resolve": "Um pacote de skills de exemplo, de criação e design até comunicação. Serve para você ver como uma skill é por dentro antes de escrever a sua.",
        "pra_quem": "Quem quer entender o mecanismo, não só usar.",
        "comando": "/plugin marketplace add anthropics/skills\n/plugin install example-skills@anthropic-agent-skills",
    },
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


passos_html = "\n".join(
    f'      <div class="passo"><i>{i}</i><div><b>{t}</b><p>{d}</p></div></div>'
    for i, (t, d) in enumerate(PASSOS, 1)
)

lista_html = "\n".join(
    f"""  <article class="arq">
    <div class="arq-cab">
      <span class="num">{i}</span>
      <div>
        <h3>{p['nome']}</h3>
        <p class="arq-res">{p['resolve']}</p>
      </div>
    </div>
    <div class="arq-corpo">
      <p class="atalho"><b>Serve para:</b> {p['pra_quem']}</p>
      <div class="papel">
        <div class="papel-cab"><span>{p['id']}</span><button class="copiar" type="button" data-alvo="c{i}">Copiar o comando</button></div>
        <pre id="c{i}">{esc(p['comando'])}</pre>
      </div>
    </div>
  </article>"""
    for i, p in enumerate(LISTA, 1)
)

HTML = f"""<!doctype html>
<html lang="pt-BR">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>As skills que a Anthropic deixou abertas | Dani Lemos</title>
<meta name="description" content="O que instalar no seu Claude hoje, o que cada uma resolve e o passo a passo de instalar em 4 passos.">
<meta property="og:title" content="As skills que a Anthropic deixou abertas">
<meta property="og:description" content="O passo a passo de instalar e a lista do que vale a pena ligar no seu Claude.">
{PIXEL}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap">
<style>{CSS}</style>

<header class="topo escuro faixa">
  <div class="wrap topo-txt">
    <span class="pilula"><i></i>Material da Dani</span>
    <h1>As skills que a Anthropic<br><span class="acesa">deixou abertas</span></h1>
    <p class="lead">O seu Claude aceita <b>peça extra</b>, e a maioria das pessoas nunca ligou nenhuma. Aqui estão as que valem a pena, o que cada uma resolve e como instalar em 4 passos.</p>
    <div class="nomes">
      <span>Word, Excel e PowerPoint</span><span>Skill própria</span><span>Exemplos oficiais</span>
    </div>
  </div>
</header>

<section class="cadastro faixa" id="cadastro" style="padding-block:clamp(26px,5vw,72px)">
  <div class="wrap estreito">
    <div class="cartao">
      <h2>Falta pouco para pegar a sua lista</h2>
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
        <label>Qual tarefa você queria que o Claude fizesse sozinho? <span class="opc">(opcional)</span>
          <textarea name="tarefa_chata"></textarea></label>
        <div class="erro" id="erro"></div>
        <button class="botao" type="submit">Quero a lista <span class="seta">→</span></button>
        <p class="lgpd">Ao enviar, você concorda em receber meus conteúdos e novidades por WhatsApp e e-mail. Pode pedir para sair quando quiser.</p>
      </form>
    </div>
  </div>
</section>

<div class="trancado">

<section class="secao faixa">
  <div class="wrap estreito">
    <span class="eyebrow">Antes de tudo</span>
    <h2 class="tit">Plugin é uma <em>peça que você encaixa</em> no Claude.</h2>
    <p class="sub">Ele vem com instruções prontas para um tipo de tarefa. Depois de instalado, você não precisa chamar: o Claude usa sozinho quando a tarefa aparece.</p>
    <p class="sub">A Anthropic publicou várias dessas peças, e elas não custam nada além do que você já paga pelo Claude. O passo a passo é o mesmo para qualquer uma, então aprenda uma vez e instale quantas quiser.</p>
  </div>
</section>

<section class="secao escuro faixa">
  <div class="wrap estreito">
    <span class="eyebrow">O passo a passo</span>
    <h2 class="tit">Instalar leva <em>quatro cliques</em></h2>
    <p class="sub">É assim no aplicativo do Claude no computador, que é onde a maioria usa.</p>
    <div class="passos">
{passos_html}
    </div>
    <p class="sub">Para saber se deu certo: digite uma barra na caixa de escrever e procure o nome do plugin na lista que aparece.</p>
  </div>
</section>

<section class="secao faixa" style="padding-bottom:0">
  <div class="wrap estreito">
    <span class="eyebrow">A lista</span>
    <h2 class="tit">O que vale a pena ligar <em>hoje</em></h2>
    <p class="sub">Se você preferir digitar em vez de clicar, cada uma tem o comando pronto para copiar. Cole na caixa de escrever da aba Code e dê enter.</p>
  </div>
</section>

<section class="secao faixa" style="padding-top:24px">
  <div class="wrap estreito">
{lista_html}
  </div>
</section>

<section class="secao escuro faixa">
  <div class="wrap estreito">
    <span class="eyebrow">Uma coisa que ninguém te fala</span>
    <h2 class="tit">Leia antes de instalar, <em>sempre</em></h2>
    <p class="sub">Plugin é código de outra pessoa rodando dentro do seu Claude, com acesso aos seus arquivos. A própria Anthropic avisa que não controla o que vai dentro de cada um.</p>
    <p class="sub">Antes de confirmar, a tela mostra tudo o que aquele plugin vai acrescentar. Leia. Se tiver coisa que você não entende, não instale. Os três desta página são publicados pela própria Anthropic, e é por isso que eles estão aqui.</p>
  </div>
</section>

<section class="secao faixa fecho" id="claude-do-zero">
  <div class="wrap estreito">
    <span class="eyebrow">Se você quiser ir além da lista</span>
    <h2 class="tit">Instalar é o fácil. O que muda o seu dia é <em>saber o que pedir.</em></h2>
    <p class="sub">No Claude do Zero, para iniciantes, eu começo do absoluto zero e vou até o Claude trabalhando por você, com o pedido pronto em cada aula. Com as peças instaladas, é o passo seguinte natural.</p>
    <a class="botao" href="https://chk.eduzz.com/lniykl57?utm_source=isca&amp;utm_campaign=plugin">Ver o Claude do Zero <span class="seta">→</span></a>
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
const ORIGEM="plugin";
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
 if(!ok&&!PREVIA){{erro.textContent=(r&&r.status===400)?"Confere o WhatsApp (com DDD) e o e-mail.":"Não consegui salvar agora. Tenta de novo em alguns segundos.";bt.disabled=false;bt.innerHTML='Quero a lista <span class="seta">→</span>';return}}
 liberar();
 const alvo=document.querySelector(".trancado");if(alvo)alvo.scrollIntoView({{behavior:"smooth",block:"start"}});
}});
document.addEventListener("click",ev=>{{const b=ev.target.closest(".copiar");if(!b)return;
 const t=document.getElementById(b.dataset.alvo);if(!t)return;
 navigator.clipboard.writeText(t.textContent).then(()=>mostrar("Comando copiado")).catch(()=>mostrar("Selecione e copie o texto"));
}});
</script>
</html>
"""

(AQUI / "index.html").write_text(HTML, encoding="utf-8")
print("ok index.html", len(HTML) // 1024, "KB")
