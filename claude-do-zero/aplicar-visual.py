"""Poe as telas reais, a foto e os icones na pagina /claude-do-zero.

A copy esta aprovada e NAO muda: este script so insere o que entra em volta dela.
As telas sao prints reais da conta da propria Dani, convertidos para webp em telas/.
Ficaram de fora, de proposito:
  * o print de metricas (99% de alcance entre seguidores, ou seja, post que nao saiu
    da bolha: como prova de venda joga contra);
  * tudo que tem nome de cliente (hub da agencia, design system de cliente).

Os icones sao os oficiais das marcas (simple-icons), monocromaticos, encostados no
texto que fala deles.

Uso: python aplicar-visual.py   (le e reescreve index.html, idempotente)
"""
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ICONES = Path("C:/Users/Micro/AppData/Local/Temp/claude/G--Meu-Drive-DANIELLE---PROJETOS-REDES-SOCIAIS---DANIELLE-LEMOS/2d521f0d-aa7d-472c-a4e3-26eedfd0f682/scratchpad/icones")

MARCAS = [("anthropic", "Claude"), ("canva", "Canva"), ("googledrive", "Google Drive"),
          ("gmail", "Gmail"), ("notion", "Notion"), ("instagram", "Instagram")]


def glifo(arquivo, rotulo):
    """Devolve o SVG oficial da marca, sem o <title>, pronto para entrar inline."""
    svg = (ICONES / f"{arquivo}.svg").read_text(encoding="utf-8")
    corpo = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1)
    corpo = re.sub(r"<title>.*?</title>", "", corpo, flags=re.S)
    return (f'<svg viewBox="0 0 24 24" role="img" aria-label="{rotulo}">'
            f'<title>{rotulo}</title>{corpo}</svg>')


LINHA_MARCAS = '<div class="marcas">' + "".join(glifo(a, r) for a, r in MARCAS) + "</div>"

CSS = """
/* ---------- TELAS REAIS ---------- */
/* print grande, reto e nitido: sem fita, sem inclinacao, sem veu, sem moldura de celular */
.tela{margin:0}
.tela img{display:block;width:100%;height:auto;border-radius:16px;border:1px solid var(--linha);
  background:#fff;box-shadow:0 30px 70px rgba(41,41,41,.16)}
.escuro .tela img{border-color:var(--linha-esc);box-shadow:0 30px 70px rgba(0,0,0,.5)}
.tela figcaption{margin-top:16px;font-size:16px;line-height:1.5;color:var(--suave)}
.escuro .tela figcaption{color:var(--suave-esc)}
.telao{padding-block:clamp(40px,6vw,72px)}
.telao .wrap{max-width:860px;text-align:center}
.telao .eyebrow{margin-bottom:22px}
.telao .tela figcaption{font-size:17px;max-width:34em;margin-inline:auto}

.galeria{display:grid;gap:clamp(22px,3vw,34px);grid-template-columns:1fr;margin-top:44px}
@media (min-width:820px){.galeria{grid-template-columns:1fr 1fr}}
.galeria>figure{min-width:0}

/* icones oficiais das marcas, encostados na tela que fala delas */
.marcas{display:flex;flex-wrap:wrap;align-items:center;gap:16px;margin-top:14px}
.marcas svg{width:22px;height:22px;fill:var(--suave);opacity:.8;flex:0 0 auto}
.escuro .marcas svg{fill:var(--pessego);opacity:.75}

/* ---------- O LEQUE DO TOPO ----------
   Telas reais do Claude trabalhando, em leque, pegando por tras do comecinho da primeira
   linha do titulo. Nenhuma delas e post da Dani nem de cliente: sao pedidos genericos
   feitos na hora (legenda de loja de roupa, semana de uma cafeteria, card de post). */
.palco{position:relative}
.palco .topo-txt{text-align:left;max-width:880px;margin:0;padding-top:clamp(116px,19vw,178px)}
.palco .lead{margin-inline:0}
.palco .cta{align-items:flex-start}
.leque{position:absolute;top:-6px;left:0;z-index:0;display:flex;align-items:flex-start;
  pointer-events:none;user-select:none}
.leque img{width:clamp(112px,17vw,208px);height:auto;display:block;background:#fff;
  border-radius:12px;border:1px solid rgba(252,234,223,.18);box-shadow:0 26px 60px rgba(0,0,0,.62)}
.leque img:nth-child(1){transform:rotate(-11deg)}
.leque img:nth-child(2){transform:rotate(-2deg) translateY(18px);margin-left:clamp(-78px,-6.5vw,-44px)}
.leque img:nth-child(3){transform:rotate(9deg) translateY(2px);margin-left:clamp(-78px,-6.5vw,-44px);
  width:clamp(88px,13vw,162px)}
/* o titulo passa por cima do canto das telas, entao ganha um halo escuro para nao sumir */
.palco h1{position:relative;z-index:1;text-shadow:0 2px 22px rgba(22,14,17,.85),0 0 40px rgba(22,14,17,.6)}
.palco .lead,.palco .cta{position:relative;z-index:1}

/* ---------- SEM BURACO ENTRE AS SECOES ---------- */
.telao{padding-block:clamp(40px,6vw,72px) 0}
#antes{padding-top:clamp(34px,4.5vw,56px)}
"""

HERO = """
<!-- A TELA QUE PROVA -->
<section class="secao telao faixa">
  <div class="wrap">
    <p class="eyebrow">Uma conversa de verdade</p>
    <figure class="tela">
      <picture>
        <!-- no celular a conversa inteira fica ilegivel, entao vai so o pedaco que prova -->
        <source media="(max-width:700px)" srcset="telas/carrossel-celular.webp" width="660" height="265">
        <img src="telas/carrossel.webp" width="892" height="710" loading="eager" decoding="async"
             alt="Conversa real no Claude: ele executa os comandos, monta os nove cards do carrossel e sobe para a grade">
      </picture>
      <figcaption>Eu pedi o post do dia. Ele montou os nove cards, escreveu a legenda e subiu tudo para a grade.</figcaption>
    </figure>
  </div>
</section>
"""

GALERIA = f"""
    <div class="galeria">
      <figure class="tela">
        <img src="telas/aba-nova.webp" width="853" height="412" loading="lazy" decoding="async"
             alt="Menu de mais dentro da conversa do Claude, com habilidades, conectores, sistema de design e plugins">
        <figcaption>Tudo começa aqui dentro, no botão de mais da conversa.</figcaption>
      </figure>
      <figure class="tela">
        <img src="telas/descobrir.webp" width="1049" height="823" loading="lazy" decoding="async"
             alt="Lista de conectores que o Claude oferece: Google Drive, Gmail, Google Agenda, Canva, Notion, Figma, Slack e outros">
        <figcaption>As ferramentas que dá para ligar nele, sem código nenhum.</figcaption>
      </figure>
      <figure class="tela">
        <img src="telas/conectores.webp" width="1069" height="840" loading="lazy" decoding="async"
             alt="Tela de conectores do Claude com Canva, Gmail, Google Drive, Google Agenda e Notion ligados na conta da Dani">
        <figcaption>As minhas, ligadas. Ele lê e escreve nelas quando eu peço.
        {LINHA_MARCAS}</figcaption>
      </figure>
      <figure class="tela">
        <img src="telas/plugins.webp" width="1074" height="859" loading="lazy" decoding="async"
             alt="Tela de plugins e habilidades salvas no Claude">
        <figcaption>O que funcionou uma vez fica salvo e você reusa quando quiser.</figcaption>
      </figure>
    </div>
"""

html = (AQUI / "index.html").read_text(encoding="utf-8")
if "telas/carrossel.webp" in html:
    raise SystemExit("as telas ja estao na pagina: nada a fazer")

# 1. o CSS novo, antes de fechar o style
html = html.replace("</style>", CSS + "</style>", 1)

# 2. o leque de telas atras do titulo
antes_topo = '  <div class="wrap">\n    <div class="topo-txt">'
depois_topo = """  <div class="wrap palco">
    <div class="leque" aria-hidden="true">
      <img src="telas/leque-1.webp" alt="" fetchpriority="high" decoding="async">
      <img src="telas/leque-2.webp" alt="" fetchpriority="high" decoding="async">
      <img src="telas/leque-3.webp" alt="" fetchpriority="high" decoding="async">
    </div>
    <div class="topo-txt">"""
assert antes_topo in html, "nao achei a abertura do topo"
html = html.replace(antes_topo, depois_topo, 1)

# 3. a tela grande logo depois do topo
html = html.replace("</header>\n", "</header>\n" + HERO, 1)

# 4. a galeria de telas dentro de "o que voce vai saber fazer"
marca = """      <div>Deixar tarefas rodando sozinhas no horário que você escolher.</div>
    </div>
  </div>
</section>"""
nova = """      <div>Deixar tarefas rodando sozinhas no horário que você escolher.</div>
    </div>
  </div>
""" + GALERIA + """</section>"""
assert marca in html, "nao achei o fim da lista do saber fazer"
html = html.replace(marca, nova, 1)

(AQUI / "index.html").write_text(html, encoding="utf-8")
print("ok index.html", len(html) // 1024, "KB")
