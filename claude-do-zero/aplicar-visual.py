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

/* ---------- FOTO NO TOPO ---------- */
.topo-grid{display:grid;gap:clamp(26px,4vw,52px);grid-template-columns:1fr;align-items:center}
@media (min-width:900px){.topo-grid{grid-template-columns:1.15fr .85fr}}
@media (min-width:900px){
  .topo-grid .topo-txt{text-align:left;margin:0}
  .topo-grid .lead{margin-inline:0}
  .topo-grid .cta{align-items:flex-start}
}
.topo-foto{position:relative;width:100%;max-width:420px;margin:0 auto;aspect-ratio:4/5;
  border-radius:24px;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.45);background:var(--noite-2)}
.topo-foto img{width:100%;height:100%;object-fit:cover;object-position:50% 20%;display:block}
/* no celular o rosto vem antes do titulo: e a primeira coisa que a pessoa ve */
@media (max-width:899px){
  .topo-grid{display:flex;flex-direction:column}
  .topo-foto{order:-1;max-width:208px;aspect-ratio:1/1;border-radius:50%;
    box-shadow:0 18px 44px rgba(0,0,0,.5),0 0 0 4px rgba(226,48,122,.25)}
  .topo-grid .topo-txt{margin-top:26px}
}
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

# 2. foto dela no topo, ao lado do titulo
antes_topo = '  <div class="wrap">\n    <div class="topo-txt">'
depois_topo = '  <div class="wrap topo-grid">\n    <div class="topo-txt">'
assert antes_topo in html, "nao achei a abertura do topo"
html = html.replace(antes_topo, depois_topo, 1)

fecha_topo = """    </div>
  </div>
</header>"""
novo_fecha = """    </div>
    <div class="topo-foto">
      <img src="dani-topo.jpg" width="787" height="1400" fetchpriority="high" decoding="async"
           alt="Danielle Lemos olhando para a câmera, em casa, na frente da estante de livros">
    </div>
  </div>
</header>"""
assert fecha_topo in html, "nao achei o fechamento do topo"
html = html.replace(fecha_topo, novo_fecha, 1)

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
