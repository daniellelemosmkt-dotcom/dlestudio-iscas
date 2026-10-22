"""Monta a pagina do MAPA: o Diario Vivo do laboratorio de 16 semanas.

Diferente das outras iscas, esta pagina NAO tem o conteudo escrito dentro dela. Ela LE o banco
ao vivo, pelas views publicas public.mapa_placar e public.mapa_testes, com a chave publicavel
(a mesma que a pagina da grade ja usa). Assim o Diario Vivo se atualiza sozinho: a atualizacao
semanal e uma escrita no banco, nao uma edicao de HTML.

O schema dlestudio NAO esta exposto na API. Só as duas views estao, e elas so trazem coluna que
pode ser lida por qualquer pessoa. Conferido em 21/10: leads nao e alcancavel pela chave publica.

Padrao visual: o oficial da marca, reaproveitando o CSS da pagina CEREBRO.

Uso: python montar.py   ->  index.html nesta pasta
"""
import base64
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ASSETS = Path("G:/Meu Drive/DANIELLE   PROJETOS/PRODUTOS DL ESTÚDIO/04 KIT E PLUGINS/_paginas/assets")

ADV = "data:font/woff2;base64," + base64.b64encode((ASSETS / "Advercase-Regular.woff2").read_bytes()).decode()
SELO = "data:image/png;base64," + base64.b64encode((ASSETS / "selo-dourado.png").read_bytes()).decode()

CEREBRO = (AQUI.parent / "cerebro" / "index.html").read_text(encoding="utf-8")
CSS_BASE = re.search(r"<style>(.*?)</style>", CEREBRO, re.S).group(1)
CSS_BASE = CSS_BASE.replace(re.search(r"src:url\((data:font/woff2;base64,[^)]+)\)", CSS_BASE).group(1), ADV)

CSS_EXTRA = """
/* placar */
.placar{background:var(--noite-2);border:1px solid var(--linha-esc);border-radius:22px;padding:clamp(22px,4vw,34px);margin-top:26px}
.placar-topo{display:flex;flex-wrap:wrap;gap:18px;align-items:flex-end;justify-content:space-between}
.numerao{font:400 clamp(54px,13vw,104px)/1 var(--disp);color:var(--branco);letter-spacing:-.02em}
.numerao small{display:block;font:600 12px/1.2 var(--txt);letter-spacing:.16em;text-transform:uppercase;color:var(--acesa);margin-bottom:10px}
.delta{font:600 17px/1.2 var(--txt);color:var(--pessego)}
.delta b{color:var(--acesa)}
.trilho{height:12px;border-radius:999px;background:rgba(252,234,223,.10);margin-top:22px;overflow:hidden}
.trilho i{display:block;height:100%;border-radius:999px;background:var(--acesa);width:0;transition:width .9s ease}
.reguas{display:flex;justify-content:space-between;margin-top:9px;font:500 13px/1 var(--txt);color:var(--suave-esc)}
.placar-nota{color:var(--suave-esc);font-size:15px;margin-top:18px}
.carregando{color:var(--suave-esc);font-size:16px}

/* testes */
.grupo{margin-top:38px}
.grupo-tit{display:flex;align-items:center;gap:10px;font:600 13px/1 var(--txt);letter-spacing:.14em;text-transform:uppercase}
.bolinha{width:11px;height:11px;border-radius:50%;flex:0 0 auto}
.g-funcionou .bolinha{background:#1F9D55}.g-funcionou .grupo-tit{color:#1F9D55}
.g-morreu .bolinha{background:var(--mag)}.g-morreu .grupo-tit{color:var(--mag)}
.g-cedo .bolinha{background:#9A7B18}.g-cedo .grupo-tit{color:#9A7B18}
.teste{background:var(--branco);border:1px solid var(--linha);border-radius:20px;padding:clamp(20px,3vw,30px);margin-top:16px;box-shadow:0 10px 30px rgba(41,41,41,.05)}
.teste h3{font:400 clamp(22px,3vw,30px)/1.15 var(--disp);color:var(--graf)}
.teste .semana{font:600 12px/1 var(--txt);letter-spacing:.12em;text-transform:uppercase;color:var(--suave)}
.teste p{margin-top:12px}
.numero{background:var(--noite);color:var(--pessego);border-radius:14px;padding:15px 17px;margin-top:14px;font-size:16px}
.numero b{color:var(--acesa)}
.adaptar{background:var(--pessego);border-radius:14px;padding:15px 17px;margin-top:14px;font-size:16px;color:var(--vinho)}
.adaptar b{color:var(--mag);display:block;margin-bottom:4px}
.vazio{color:var(--suave);font-size:16px;margin-top:14px}
"""

PIXEL = (
    '<!-- Meta Pixel -->\n<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?'
    'n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";'
    'n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}'
    '(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","2130554737847082");'
    'fbq("track","PageView");</script>\n<noscript><img height="1" width="1" style="display:none" '
    'src="https://www.facebook.com/tr?id=2130554737847082&ev=PageView&noscript=1"/></noscript>\n<!-- /Meta Pixel -->'
)

HTML = f"""<!doctype html>
<html lang="pt-BR">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>O Diário Vivo: de 3.884 a 20 mil seguidores à vista de todo mundo | Dani Lemos</title>
<meta name="description" content="O placar da semana, o que eu testei, o que funcionou, o que morreu, e como adaptar cada teste para o seu nicho. Atualizado toda terça.">
<meta property="og:title" content="O Diário Vivo">
<meta property="og:description" content="De 3.884 a 20 mil seguidores em 16 semanas, com os números abertos toda semana.">
{PIXEL}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap">
<style>{CSS_BASE}{CSS_EXTRA}</style>

<header class="topo escuro faixa">
  <div class="wrap topo-txt">
    <span class="pilula"><i></i>Diário Vivo</span>
    <h1>De 3.884 a 20 mil,<br><span class="acesa">à vista de todo mundo</span></h1>
    <p class="lead">Eu apostei que consigo levar este perfil a <b>20 mil seguidores em 16 semanas</b>, publicando todo dia. Aqui ficam os números, o que eu testei e o que deu errado. Sem recorte bonito.</p>
    <div class="nomes">
      <span>Começa 22 de outubro</span><span>Termina 11 de fevereiro</span><span>112 dias</span>
    </div>
  </div>
</header>

<section class="cadastro faixa" id="cadastro" style="padding-block:clamp(26px,5vw,72px)">
  <div class="wrap estreito">
    <div class="cartao">
      <h2>Falta pouco para você acompanhar</h2>
      <p class="ajuda">Você preenche uma vez só e depois acessa qualquer material. O Diário muda toda terça, e você pode voltar aqui quando quiser.</p>
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
        <label>Quantos seguidores você tem hoje? <span class="opc">(opcional, é só para eu saber com quem eu estou falando)</span>
          <textarea name="tarefa_chata"></textarea></label>
        <div class="erro" id="erro"></div>
        <button class="botao" type="submit">Quero acompanhar <span class="seta">→</span></button>
        <p class="lgpd">Ao enviar, você concorda em receber meus conteúdos e novidades por WhatsApp e e-mail. Pode pedir para sair quando quiser.</p>
      </form>
    </div>
  </div>
</section>

<div class="trancado">

<section class="secao escuro faixa" id="placar">
  <div class="wrap estreito">
    <span class="eyebrow">O placar de agora</span>
    <h2 class="tit">Onde eu estou <em>hoje</em></h2>
    <div class="placar" id="cx-placar">
      <p class="carregando">Buscando o número mais recente...</p>
    </div>
  </div>
</section>

<section class="secao faixa">
  <div class="wrap estreito">
    <span class="eyebrow">O que eu já testei</span>
    <h2 class="tit">Cada teste com o número <em>e o que fazer com ele</em></h2>
    <p class="sub">Os que deram certo vêm primeiro. Os que morreram ficam aqui também, porque é neles que está a parte útil.</p>
    <div id="cx-testes"><p class="carregando">Carregando os testes...</p></div>
  </div>
</section>

<section class="secao escuro faixa">
  <div class="wrap estreito">
    <span class="eyebrow">Como isto funciona</span>
    <h2 class="tit">Toda terça esta página <em>muda sozinha</em></h2>
    <p class="sub">Depois de fechar os números da semana, eu atualizo o placar e acrescento os testes novos. Você não precisa baixar nada de novo: é a mesma página, com o conteúdo de hoje.</p>
    <p class="sub">Se uma semana for ruim, ela aparece aqui do mesmo jeito. Um laboratório que só mostra o que deu certo não é laboratório, é propaganda.</p>
  </div>
</section>

<section class="secao faixa fecho" id="claude-do-zero">
  <div class="wrap estreito">
    <span class="eyebrow">Se você quiser fazer junto</span>
    <h2 class="tit">Quase tudo que eu testo aqui <em>é o Claude fazendo por mim.</em></h2>
    <p class="sub">No Claude do Zero, para iniciantes, eu começo do absoluto zero e vou até ele trabalhando por você, com o pedido pronto em cada aula. É o mesmo que eu uso para dar conta de publicar todo dia.</p>
    <a class="botao" href="https://chk.eduzz.com/lniykl57?utm_source=isca&amp;utm_campaign=mapa">Ver o Claude do Zero <span class="seta">→</span></a>
  </div>
</section>

</div>

<footer>
  <img src="{SELO}" alt="Selo DL">
  <p>Siga <a href="https://instagram.com/daanylemos">@daanylemos</a> no Instagram para acompanhar o laboratório todo dia.</p>
  <p>Dani Lemos, DL Estúdio</p>
</footer>

<div class="aviso" role="status" aria-live="polite"></div>
<script>
const ORIGEM="mapa";
const FN="https://veogbuoxtbpaxoqvuakr.supabase.co/functions/v1/lead-isca-dlestudio";
const API="https://veogbuoxtbpaxoqvuakr.supabase.co/rest/v1";
const CHAVE="sb_publishable_2j7Vv_Ifmmu8Dtozr8F44w_HyZlH4xX";
const META=20000, PARTIDA=3884;
const MC=new URLSearchParams(location.search).get("mc")||"";
const aviso=document.querySelector(".aviso"),f=document.getElementById("fcad"),erro=document.getElementById("erro");
const esc=s=>String(s??"").replace(/[&<>"]/g,c=>(({{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}})[c]));
const mil=n=>Number(n).toLocaleString("pt-BR");
function liberar(){{document.body.classList.add("liberado");try{{localStorage.setItem("dl_cadastro","1")}}catch(e){{}}carregar()}}
try{{if(localStorage.getItem("dl_cadastro")==="1")liberar()}}catch(e){{}}
if(!document.body.classList.contains("liberado")&&MC){{fetch(FN+"?mc="+encodeURIComponent(MC)).then(r=>r.json()).then(d=>{{if(d.existe)liberar()}}).catch(()=>{{}})}}

async function buscar(tabela,ordem){{
  const r=await fetch(API+"/"+tabela+"?select=*&order="+ordem,{{headers:{{apikey:CHAVE}}}});
  if(!r.ok)throw new Error(r.status);
  return r.json();
}}
let carregado=false;
async function carregar(){{
  if(carregado)return; carregado=true;
  const cxP=document.getElementById("cx-placar"), cxT=document.getElementById("cx-testes");
  try{{
    const [placar,testes]=await Promise.all([buscar("mapa_placar","semana.desc"),buscar("mapa_testes","semana.desc,ordem.asc")]);
    const hoje=placar[0];
    if(!hoje){{cxP.innerHTML='<p class="carregando">O primeiro placar entra na terça que vem.</p>';}}
    else{{
      const ganho=hoje.seguidores-PARTIDA;
      const pct=Math.max(0,Math.min(100,((hoje.seguidores-PARTIDA)/(META-PARTIDA))*100));
      const dia=hoje.data_fim?hoje.data_fim.split("-").reverse().join("/"):"";
      cxP.innerHTML=
        '<div class="placar-topo"><div class="numerao"><small>Seguidores em '+esc(dia)+'</small>'+mil(hoje.seguidores)+'</div>'+
        '<div class="delta">Semana '+esc(hoje.semana)+' de 16<br><b>'+(ganho>=0?"+":"")+mil(ganho)+'</b> desde o começo</div></div>'+
        '<div class="trilho"><i style="width:'+pct.toFixed(1)+'%"></i></div>'+
        '<div class="reguas"><span>'+mil(PARTIDA)+'</span><span>'+mil(META)+'</span></div>'+
        (hoje.nota?'<p class="placar-nota">'+esc(hoje.nota)+'</p>':'');
    }}
    const ordem=[["funcionou","O que funcionou"],["cedo","Ainda é cedo para dizer"],["morreu","O que morreu"]];
    let html="";
    for(const [chave,rotulo] of ordem){{
      const lista=testes.filter(t=>t.resultado===chave);
      if(!lista.length)continue;
      html+='<div class="grupo g-'+chave+'"><div class="grupo-tit"><span class="bolinha"></span>'+rotulo+'</div>';
      for(const t of lista){{
        html+='<article class="teste"><span class="semana">Semana '+esc(t.semana)+'</span><h3>'+esc(t.titulo)+'</h3>'+
          '<p>'+esc(t.o_que_testei)+'</p>'+
          (t.numero?'<div class="numero"><b>O número:</b> '+esc(t.numero)+'</div>':'')+
          (t.aprendizado?'<p>'+esc(t.aprendizado)+'</p>':'')+
          '<div class="adaptar"><b>Como adaptar isso para o seu nicho</b>'+esc(t.como_adaptar)+'</div></article>';
      }}
      html+='</div>';
    }}
    cxT.innerHTML=html||'<p class="vazio">Os primeiros testes entram na terça que vem.</p>';
  }}catch(e){{
    cxP.innerHTML='<p class="carregando">Não consegui buscar o placar agora. Atualize a página em alguns segundos.</p>';
    cxT.innerHTML='';
  }}
}}

f.addEventListener("submit",async ev=>{{ev.preventDefault();erro.textContent="";
 const d=Object.fromEntries(new FormData(f));d.origem=ORIGEM;d.mc=MC;
 if(!d.nome||!d.email||!d.whatsapp||!d.instagram||!d.profissao){{erro.textContent="Preencha todos os campos (só a última pergunta é opcional).";return}}
 const bt=f.querySelector("[type=submit]");bt.disabled=true;bt.textContent="Liberando...";
 const PREVIA=!/dlestudio\\.com\\.br$/.test(location.hostname);
 let r=null;try{{r=await fetch(FN,{{method:"POST",headers:{{"content-type":"application/json"}},body:JSON.stringify(d)}})}}catch(e){{}}
 const ok=r&&r.ok;
 if(!ok&&!PREVIA){{erro.textContent=(r&&r.status===400)?"Confere o WhatsApp (com DDD) e o e-mail.":"Não consegui salvar agora. Tenta de novo em alguns segundos.";bt.disabled=false;bt.innerHTML='Quero acompanhar <span class="seta">→</span>';return}}
 liberar();
 const alvo=document.getElementById("placar");if(alvo)alvo.scrollIntoView({{behavior:"smooth",block:"start"}});
}});
</script>
</html>
"""

(AQUI / "index.html").write_text(HTML, encoding="utf-8")
print("ok index.html", len(HTML) // 1024, "KB")
