"""Monta a /biblioteca: as seis familias de isca numa pagina so, uma aba por familia.

Desenho de 21 e 22/10 (DESENHO-BIBLIOTECA-E-DIARIO.md e CALENDARIO-16-SEMANAS.md secao 6):
quem comenta uma palavra recebe o link da aba dela; as outras aparecem fechadas, de proposito,
porque ver que existe mais e o que faz a pessoa comentar de novo.

AS SEIS: DIARIO (a serie de videos, muda toda semana), ROTEIRO, OUTLIER, SPRINT, EDITOR e ZERO.

LIMITE HONESTO DA TRANCA, escrito aqui para ninguem se enganar depois: a aba aberta vem do
parametro ?m= da URL, guardado no navegador. Isso segura quem esta de boa-fe e cria o desejo,
mas NAO e seguranca: quem mexer na URL abre outra aba. Para material de isca isso basta, e foi
decidido assim. Se algum dia uma aba levar material que nao pode vazar, a tranca tem que passar
a ser conferida na funcao do Supabase, contra o contato do ManyChat, nao no navegador.

Cadastro uma vez so, no mesmo contrato das outras (dl_cadastro).

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
.biblio{display:grid;gap:26px;align-items:start}
@media(min-width:900px){.biblio{grid-template-columns:270px 1fr;gap:38px}}
.estante{display:grid;gap:8px}
@media(min-width:900px){.estante{position:sticky;top:18px}}
.aba{display:flex;gap:12px;align-items:center;width:100%;text-align:left;cursor:pointer;
  background:var(--branco);border:1px solid var(--linha);border-radius:14px;padding:14px 16px;font:600 15px/1.2 var(--txt);color:var(--graf)}
.aba small{display:block;font:400 13px/1.3 var(--txt);color:var(--suave);margin-top:3px}
.aba .ico{flex:0 0 auto;width:30px;height:30px;border-radius:9px;background:var(--pessego);color:var(--mag);
  display:grid;place-items:center;font:600 13px/1 var(--txt)}
.aba[aria-selected="true"]{border-color:var(--mag);box-shadow:0 10px 26px rgba(139,8,63,.14)}
.aba[aria-selected="true"] .ico{background:var(--mag);color:#fff}
.aba.fechada{opacity:.72}
.aba.fechada .ico{background:#EFE9E4;color:var(--suave)}
.painel{background:var(--branco);border:1px solid var(--linha);border-radius:20px;padding:clamp(22px,4vw,38px);box-shadow:0 12px 34px rgba(41,41,41,.06)}
.painel h2{font:400 clamp(26px,3.8vw,40px)/1.08 var(--disp)}
.painel .quando{font:600 12px/1 var(--txt);letter-spacing:.14em;text-transform:uppercase;color:var(--mag)}
.painel p{margin-top:14px}
.campo{border:1px solid var(--linha);border-radius:14px;padding:16px 18px;margin-top:14px;background:#fff}
.campo b{display:block;font:600 12px/1 var(--txt);letter-spacing:.12em;text-transform:uppercase;color:var(--mag);margin-bottom:8px}
.campo .linha{border-bottom:1px dashed var(--linha);height:26px;margin-top:8px}
.marcar{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.marcar span{border:1px solid var(--linha);border-radius:8px;padding:7px 11px;font-size:14px;color:var(--suave)}
.tranca{text-align:center;padding:clamp(28px,5vw,50px) 0}
.tranca .cad{font-size:34px}
.tranca h3{font:400 clamp(22px,3.2vw,30px)/1.15 var(--disp);margin-top:12px}
.tranca p{color:var(--suave);margin-top:12px;max-width:34em;margin-left:auto;margin-right:auto}
.vid{border-radius:14px;overflow:hidden;background:var(--noite);aspect-ratio:9/16}
.vid video,.vid img{width:100%;height:100%;object-fit:cover;display:block}
.dupla{display:grid;gap:12px;margin-top:16px}
@media(min-width:560px){.dupla{grid-template-columns:1fr 1fr}}
.dupla figure{margin:0}
.dupla figcaption{font:600 12px/1.3 var(--txt);letter-spacing:.1em;text-transform:uppercase;color:var(--suave);margin-top:9px;text-align:center}
.dupla .depois figcaption{color:var(--mag)}
.parede{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:12px;margin-top:16px}
.parede figure{margin:0}
.parede .vid{border-radius:10px}
.parede figcaption{font:500 12px/1.3 var(--txt);color:var(--suave);margin-top:6px;text-align:center}
.amostra{display:inline-block;width:12px;height:12px;border-radius:3px;vertical-align:-1px;margin-right:4px}
.tranca .palavra{display:inline-block;margin-top:16px;background:var(--mag);color:#fff;border-radius:999px;padding:11px 20px;font:600 15px/1 var(--txt);letter-spacing:.06em}
"""

EDITOR_HTML = """<p>Eu gravo no celular, mando o arquivo e vou fazer outra coisa. O corte, a legenda, a manchete e o efeito saem prontos, na minha identidade. A decisão do que entra continua minha: o que mudou é que eu parei de perder a madrugada arrastando bloquinho na timeline.</p>

      <h3 style="font:600 12px/1 var(--txt);letter-spacing:.14em;text-transform:uppercase;color:var(--mag);margin-top:26px">O mesmo vídeo, antes e depois</h3>
      <div class="dupla">
        <figure><div class="vid"><video src="moldes/real-bruto.mp4" poster="moldes/real-bruto.jpg" muted loop playsinline preload="none" controls></video></div><figcaption>o que eu gravei</figcaption></figure>
        <figure class="depois"><div class="vid"><video src="moldes/real-editado.mp4" poster="moldes/real-editado.jpg" muted loop playsinline preload="none" controls></video></div><figcaption>o que voltou pronto</figcaption></figure>
      </div>

      <h3 style="font:600 12px/1 var(--txt);letter-spacing:.14em;text-transform:uppercase;color:var(--mag);margin-top:30px">Mesmo efeito, identidade diferente</h3>
      <p>Esta é a parte que eu não sabia que importava tanto: o sistema lê a sua marca em vez de devolver molde igual para todo mundo. O efeito é o mesmo nos dois, as cores e a tipografia não.</p>
      <div class="dupla">
        <figure><div class="vid"><video src="moldes/pull-back-reveal.mp4" poster="moldes/pull-back-reveal.jpg" muted loop playsinline preload="none"></video></div><figcaption><span class="amostra" style="background:#4A63C8"></span>padrão</figcaption></figure>
        <figure class="depois"><div class="vid"><video src="moldes/marca-pull-back-reveal.mp4" poster="moldes/marca-pull-back-reveal.jpg" muted loop playsinline preload="none"></video></div><figcaption><span class="amostra" style="background:#8B083F"></span>com a minha marca</figcaption></figure>
      </div>

      <h3 style="font:600 12px/1 var(--txt);letter-spacing:.14em;text-transform:uppercase;color:var(--mag);margin-top:30px">Um efeito para cada tipo de vídeo</h3>
      <p>Todos estes já estão com a minha identidade aplicada: as cores, a tipografia, o jeito. Cada um serve a um tipo de conteúdo, de lista a prova de tela, manchete, dado e conversa.</p>
      <div class="parede">__PAREDE__</div>

      <div class="atalho" style="margin-top:22px"><b>Para ser justa com você:</b> isso não edita sozinho e não substitui quem sabe o que está fazendo. Quando eu joguei um bruto cru, sem dizer nada, a manchete saiu no lugar errado. Quem decide o que o vídeo precisa continua sendo você: o sistema executa.</div>

      <p style="margin-top:20px">O Kit inteiro, com todos os efeitos e a instalação guiada, eu mostro no direct de quem pede. É só me chamar lá.</p>"""

# A parede e montada a partir dos arquivos que existem DE VERDADE em moldes/,
# para a pagina nunca prometer efeito que nao esta la.
PAREDE = sorted(q.stem for q in (AQUI / "previas").glob("*.mp4"))
assert PAREDE, "nenhuma previa em previas/: a aba EDITOR ficaria sem a parede"
EDITOR_HTML = EDITOR_HTML.replace("__PAREDE__", "".join(
    f'<figure><div class="vid"><video src="previas/{n}.mp4" poster="previas/{n}.jpg" '
    f'muted loop playsinline preload="none"></video></div><figcaption>{n.replace("-", " ")}</figcaption></figure>'
    for n in PAREDE))

# As seis familias. 'conteudo' None = aba existe mas ainda nao tem material escrito.
ABAS = [
    {"id": "diario", "nome": "DIARIO", "resumo": "O capítulo da semana e o placar",
     "quando": "Muda toda terça",
     "conteudo": """<p>O Diário Vivo tem página própria, porque ele muda toda semana e é feito para ser lido do começo ao fim.</p>
<p>Lá está o mapa inteiro do experimento, o placar de hoje e um capítulo por semana, com o que funcionou, o que morreu e como adaptar para o seu nicho.</p>
<p><a class="botao" href="/diario">Abrir o Diário Vivo <span class="seta">→</span></a></p>"""},
    {"id": "roteiro", "nome": "ROTEIRO", "resumo": "Transformar uma dica em história",
     "quando": "Material pronto",
     "conteudo": None},  # montado abaixo, porque e longo
    {"id": "outlier", "nome": "OUTLIER", "resumo": "Desmontar um post fora da curva",
     "quando": "Abre quando o carrossel de análise sair", "conteudo": None},
    {"id": "sprint", "nome": "SPRINT", "resumo": "Acompanhar um experimento de crescimento",
     "quando": "Abre quando o carrossel de medição sair", "conteudo": None},
    {"id": "editor", "nome": "EDITOR", "resumo": "O sistema de edição funcionando",
     "quando": "Material pronto", "conteudo": EDITOR_HTML},
    {"id": "zero", "nome": "ZERO", "resumo": "Por onde começar no Claude",
     "quando": "Abre quando a audiência pedir base", "conteudo": None},
]

ROTEIRO_CAMPOS = [
    ("1. O tema educativo", "Qual é a dica, assunto ou conhecimento que você queria ensinar?", None),
    ("2. A cena real", "Onde esse assunto está acontecendo de verdade na sua vida, no seu trabalho ou no seu cliente?", None),
    ("3. A tensão", "O que está difícil, travado, dando errado, surpreendendo ou ainda sem resposta?", None),
    ("4. O destino", "O que você quer conseguir, provar, mudar ou descobrir? Se puder, use número, prazo ou consequência concreta.", None),
    ("5. A prova", "O que a pessoa pode ver? Marque o que você tem:",
     ["número", "print", "tela", "comentário", "antes e depois", "arquivo", "gravação", "resultado", "erro"]),
    ("6. A virada", "O que você percebeu, decidiu ou mudou por causa disso?", None),
    ("7. A pergunta aberta", "Qual pergunta real continua sem resposta depois deste conteúdo? Não vale “amanhã eu conto uma dica”. Vale “será que isso funciona de novo?”, “quanto trabalho isso realmente reduz?”, “esse formato traz seguidores ou só alcance?”.", None),
    ("8. O CTA", "Depois de assistir, o que a pessoa ficou querendo ver, receber ou aplicar? E qual material entrega exatamente isso?", None),
    ("9. O próximo capítulo possível", "Se alguma coisa relevante acontecer depois deste post, qual continuação pode nascer naturalmente?", None),
]

campos_html = "\n".join(
    f'      <div class="campo"><b>{t}</b><p>{d}</p>' +
    ('<div class="marcar">' + "".join(f"<span>{m}</span>" for m in marcar) + '</div>' if marcar
     else '<div class="linha"></div><div class="linha"></div>') +
    '</div>'
    for t, d, marcar in ROTEIRO_CAMPOS
)

FICHA_TXT = """FICHA ROTEIRO: transforme uma dica em história

1. O TEMA EDUCATIVO
Qual é a dica que você queria ensinar?


2. A CENA REAL
Onde isso acontece de verdade na sua vida, no seu trabalho ou no seu cliente?


3. A TENSÃO
O que está difícil, travado, dando errado ou ainda sem resposta?


4. O DESTINO
O que você quer conseguir, provar, mudar ou descobrir? Use número, prazo ou consequência.


5. A PROVA
O que a pessoa pode ver? (número, print, tela, comentário, antes e depois, arquivo, gravação, resultado, erro)


6. A VIRADA
O que você percebeu, decidiu ou mudou por causa disso?


7. A PERGUNTA ABERTA
Qual pergunta real continua sem resposta depois deste conteúdo?


8. O CTA
O que a pessoa ficou querendo? Qual material entrega exatamente isso?
Palavra-chave:


9. O PRÓXIMO CAPÍTULO POSSÍVEL
Se algo acontecer depois deste post, qual continuação nasce naturalmente?
"""

ABAS[1]["conteudo"] = f"""<p>Use esta ficha antes de gravar um conteúdo que hoje está com cara de aula. Ela não troca o que você sabe: ela troca a ordem em que você conta.</p>
<div class="papel" style="margin-top:18px">
  <div class="papel-cab"><span>ficha-roteiro.txt</span><button class="copiar" type="button" data-alvo="ficha">Copiar a ficha em branco</button></div>
  <pre id="ficha">{FICHA_TXT.replace("&", "&amp;").replace("<", "&lt;")}</pre>
</div>
{campos_html}
      <div class="atalho" style="margin-top:18px"><b>O modelo rápido:</b> em vez de “5 dicas para organizar clientes”, fica “eu cuido de vários clientes e ainda perco tempo toda segunda procurando as mesmas informações. Estou reconstruindo meu processo para começar a semana sabendo o que precisa da minha decisão”.</div>
      <p class="sub" style="margin-top:18px">A regra final: não invente uma jornada para ter conteúdo. Comece por alguma coisa que já está acontecendo. A história é a embalagem, o conhecimento continua lá dentro.</p>"""

estante = "\n".join(
    f'      <button class="aba" role="tab" id="t-{a["id"]}" data-aba="{a["id"]}" aria-selected="false">'
    f'<span class="ico">{"✦" if a["conteudo"] else "✕"}</span>'
    f'<span>{a["nome"]}<small>{a["resumo"]}</small></span></button>'
    for a in ABAS
)

paineis = []
for a in ABAS:
    if a["conteudo"]:
        corpo = a["conteudo"]
    else:
        corpo = f"""<div class="tranca">
        <div class="cad">🔒</div>
        <h3>Esta porta ainda não abriu</h3>
        <p>{a['quando']}. Quando abrir, a palavra aparece no post e você entra por aqui mesmo, sem se cadastrar de novo.</p>
        <span class="palavra">{a['nome']}</span>
      </div>"""
    paineis.append(
        f'    <section class="painel" id="p-{a["id"]}" role="tabpanel" hidden>\n'
        f'      <span class="quando">{a["quando"]}</span>\n'
        f'      <h2>{a["nome"]}</h2>\n'
        f'      <p class="sub" style="margin-top:6px">{a["resumo"]}</p>\n{corpo}\n    </section>'
    )
paineis_html = "\n".join(paineis)

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
<title>A biblioteca | Dani Lemos</title>
<meta name="description" content="Os materiais do laboratório, um por palavra. Você abre a porta que comentou.">
<meta property="og:title" content="A biblioteca da Dani">
<meta property="og:description" content="Uma porta por material. Comente a palavra do post e a sua abre.">
{PIXEL}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap">
<style>{CSS_BASE}{CSS_EXTRA}</style>

<header class="topo escuro faixa">
  <div class="wrap topo-txt">
    <span class="pilula"><i></i>A biblioteca</span>
    <h1>Uma porta<br><span class="acesa">por material</span></h1>
    <p class="lead">Cada post meu entrega uma coisa diferente. Aqui elas ficam todas no mesmo lugar, e <b>você abre a que comentou</b>. As outras ficam à vista de propósito.</p>
  </div>
</header>

<section class="cadastro faixa" id="cadastro" style="padding-block:clamp(26px,5vw,72px)">
  <div class="wrap estreito">
    <div class="cartao">
      <h2>Falta pouco para abrir a sua porta</h2>
      <p class="ajuda">Você preenche uma vez só. Nas próximas, entra direto.</p>
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
        <label>O que você queria resolver primeiro? <span class="opc">(opcional)</span>
          <textarea name="tarefa_chata"></textarea></label>
        <div class="erro" id="erro"></div>
        <button class="botao" type="submit">Abrir a biblioteca <span class="seta">→</span></button>
        <p class="lgpd">Ao enviar, você concorda em receber meus conteúdos e novidades por WhatsApp e e-mail. Pode pedir para sair quando quiser.</p>
      </form>
    </div>
  </div>
</section>

<div class="trancado">
<section class="secao faixa">
  <div class="wrap biblio">
    <div class="estante" role="tablist" aria-label="Materiais">
{estante}
    </div>
    <div>
{paineis_html}
    </div>
  </div>
</section>

<section class="secao escuro faixa fecho" id="claude-do-zero">
  <div class="wrap estreito">
    <span class="eyebrow">Para abrir todas de uma vez</span>
    <h2 class="tit">Quem entra no Claude do Zero <em>recebe a chave da biblioteca inteira.</em></h2>
    <p class="sub">No Claude do Zero, para iniciantes, eu começo do absoluto zero e vou até ele trabalhando por você, com o pedido pronto em cada aula. Quem entra recebe o link que abre todas as portas daqui, inclusive as que ainda vão nascer.</p>
    <a class="botao" href="https://chk.eduzz.com/lniykl57?utm_source=isca&amp;utm_campaign=biblioteca">Ver o Claude do Zero <span class="seta">→</span></a>
  </div>
</section>
</div>

<footer>
  <img src="{SELO}" alt="Selo DL">
  <p>Siga <a href="https://instagram.com/daanylemos">@daanylemos</a> no Instagram para saber qual porta abre em cada post.</p>
  <p>Dani Lemos, DL Estúdio</p>
</footer>

<div class="aviso" role="status" aria-live="polite"></div>
<script>
const ORIGEM="biblioteca";
const FN="https://veogbuoxtbpaxoqvuakr.supabase.co/functions/v1/lead-isca-dlestudio";
const ABAS=["diario","roteiro","outlier","sprint","editor","zero"];
const COM_MATERIAL=["diario","roteiro","editor"];
const q=new URLSearchParams(location.search);
const MC=q.get("mc")||"";
const aviso=document.querySelector(".aviso"),f=document.getElementById("fcad"),erro=document.getElementById("erro");
function mostrar(t){{aviso.textContent=t;aviso.classList.add("ver");setTimeout(()=>aviso.classList.remove("ver"),1800)}}

// quais portas esta pessoa ja abriu. vem do ?m= e fica guardado no navegador.
function abertas(){{
  let l=[]; try{{l=JSON.parse(localStorage.getItem("dl_biblioteca")||"[]")}}catch(e){{}}
  const m=(q.get("m")||"").toLowerCase();
  if(m==="tudo"){{l=ABAS.slice()}} else if(ABAS.includes(m)&&!l.includes(m)){{l.push(m)}}
  if(!l.includes("diario"))l.push("diario");   // o Diario e publico
  try{{localStorage.setItem("dl_biblioteca",JSON.stringify(l))}}catch(e){{}}
  return l;
}}
function pintar(){{
  const abs=abertas();
  const alvo=(q.get("m")||"").toLowerCase();
  const inicial=ABAS.includes(alvo)?alvo:(abs.find(a=>COM_MATERIAL.includes(a))||"diario");
  ABAS.forEach(id=>{{
    const bt=document.getElementById("t-"+id), pn=document.getElementById("p-"+id);
    if(!bt||!pn)return;
    const temMaterial=COM_MATERIAL.includes(id), aberta=abs.includes(id)&&temMaterial;
    bt.classList.toggle("fechada",!aberta);
    bt.querySelector(".ico").textContent=aberta?"✦":"🔒";
    bt.onclick=()=>selecionar(id);
    pn.hidden=true; bt.setAttribute("aria-selected","false");
  }});
  selecionar(inicial);
}}
function selecionar(id){{
  ABAS.forEach(o=>{{
    const bt=document.getElementById("t-"+o), pn=document.getElementById("p-"+o);
    if(!bt||!pn)return;
    const on=(o===id);
    pn.hidden=!on; bt.setAttribute("aria-selected",on?"true":"false");
  }});
}}
function liberar(){{document.body.classList.add("liberado");try{{localStorage.setItem("dl_cadastro","1")}}catch(e){{}}pintar()}}
try{{if(localStorage.getItem("dl_cadastro")==="1")liberar()}}catch(e){{}}
if(!document.body.classList.contains("liberado")&&MC){{fetch(FN+"?mc="+encodeURIComponent(MC)).then(r=>r.json()).then(d=>{{if(d.existe)liberar()}}).catch(()=>{{}})}}

f.addEventListener("submit",async ev=>{{ev.preventDefault();erro.textContent="";
 const d=Object.fromEntries(new FormData(f));d.origem=ORIGEM+((q.get("m"))?("_"+q.get("m")):"");d.mc=MC;
 if(!d.nome||!d.email||!d.whatsapp||!d.instagram||!d.profissao){{erro.textContent="Preencha todos os campos (só a última pergunta é opcional).";return}}
 const bt=f.querySelector("[type=submit]");bt.disabled=true;bt.textContent="Abrindo...";
 const PREVIA=!/dlestudio\\.com\\.br$/.test(location.hostname);
 let r=null;try{{r=await fetch(FN,{{method:"POST",headers:{{"content-type":"application/json"}},body:JSON.stringify(d)}})}}catch(e){{}}
 if(!(r&&r.ok)&&!PREVIA){{erro.textContent=(r&&r.status===400)?"Confere o WhatsApp (com DDD) e o e-mail.":"Não consegui salvar agora. Tenta de novo em alguns segundos.";bt.disabled=false;bt.innerHTML='Abrir a biblioteca <span class="seta">→</span>';return}}
 liberar();
 const alvo=document.querySelector(".biblio");if(alvo)alvo.scrollIntoView({{behavior:"smooth",block:"start"}});
}});
document.addEventListener("click",ev=>{{const b=ev.target.closest(".copiar");if(!b)return;
 const t=document.getElementById(b.dataset.alvo);if(!t)return;
 navigator.clipboard.writeText(t.textContent).then(()=>mostrar("Ficha copiada")).catch(()=>mostrar("Selecione e copie o texto"));
}});
</script>
</html>
"""

(AQUI / "index.html").write_text(HTML, encoding="utf-8")
print("ok index.html", len(HTML) // 1024, "KB")
