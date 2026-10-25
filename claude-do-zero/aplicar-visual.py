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

/* ---------- TOPO ----------
   Mecanismo copiado da pagina do Clube Divos da IA, que a Dani mandou estudar: pilula
   pequena, promessa em linguagem de gente, tres pilares em quadradinho e DOIS botoes, o de
   comprar e o de espiar as aulas. A aparencia continua a dela: fundo escuro, Advercase e
   magenta. Print de ferramenta nao entra aqui: nao e o produto e nao gera desejo. */
.pilula{display:inline-block;border:1px solid rgba(226,48,122,.45);border-radius:999px;
  padding:9px 18px;font:600 12px/1 var(--txt);letter-spacing:.13em;text-transform:uppercase;
  color:var(--acesa);background:rgba(226,48,122,.08);margin-bottom:22px}
.pilares{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(10px,1.6vw,18px);
  max-width:760px;margin:clamp(30px,4vw,42px) auto 0}
.pilares>div{background:var(--noite-2);border:1px solid var(--linha-esc);border-radius:18px;
  padding:clamp(16px,2.2vw,24px) clamp(10px,1.6vw,20px);text-align:center;min-width:0}
.pilares i{display:block;font:400 clamp(26px,3.6vw,38px)/1 var(--disp);font-style:normal;color:var(--acesa)}
.pilares b{display:block;font:600 clamp(13px,1.6vw,16px)/1.28 var(--txt);margin-top:10px;color:var(--branco)}
.pilares span{display:block;font-size:clamp(12.5px,1.5vw,14.5px);line-height:1.4;color:var(--suave-esc);margin-top:7px}
.botao.vazado{background:transparent;color:var(--pessego);border:1px solid rgba(252,234,223,.38);box-shadow:none}
.botao.vazado:hover{border-color:var(--acesa);background:rgba(226,48,122,.1)}

/* ---------- AS AULAS POR DENTRO ----------
   E o bloco que vende: o produto vira um produto, com capa, nome, numero e duracao, e da
   para arrastar e espiar. Cada capa e um quadro do proprio video da aula. */
/* o topo entrega direto nas aulas: sem respiro duplo no meio do escuro */
.topo{padding-bottom:clamp(30px,4vw,48px)}
.aulas{padding-block:clamp(30px,4vw,48px) clamp(56px,8vw,92px)}
.aulas .cabeca{text-align:center;max-width:700px;margin:0 auto}
.aulas .arraste{color:var(--suave);font-size:16px;margin-top:14px}
.escuro .aulas .arraste{color:var(--suave-esc)}
.trilho{display:flex;gap:clamp(14px,2vw,22px);overflow-x:auto;scroll-snap-type:x mandatory;
  margin-top:clamp(30px,4vw,44px);padding:4px 0 22px;
  scrollbar-width:thin;scrollbar-color:rgba(226,48,122,.5) transparent}
.trilho::-webkit-scrollbar{height:6px}
.trilho::-webkit-scrollbar-thumb{background:rgba(226,48,122,.5);border-radius:99px}
.aula{flex:0 0 clamp(228px,66vw,286px);scroll-snap-align:start;background:var(--branco);
  border:1px solid var(--linha);border-radius:18px;overflow:hidden;display:flex;flex-direction:column}
.escuro .aula{background:var(--noite-2);border-color:var(--linha-esc)}
.aula img{width:100%;height:auto;display:block;border-bottom:1px solid var(--linha)}
.escuro .aula img{border-bottom-color:var(--linha-esc)}
.aula .corpo{padding:15px 18px 19px}
.aula .num{font:600 11px/1 var(--txt);letter-spacing:.14em;text-transform:uppercase;color:var(--mag)}
.escuro .aula .num{color:var(--acesa)}
.aula h3{font:400 clamp(20px,2.4vw,24px)/1.14 var(--disp);margin-top:9px}
.escuro .aula h3{color:var(--branco)}
.aula p{font-size:15.5px;line-height:1.5;color:var(--suave);margin:0}
.escuro .aula p{color:var(--pessego)}

/* ---------- A PILHA DO PRODUTO ----------
   Mecanismo da pagina da Maria Wendt: a pessoa ve de uma vez que e muita coisa. A diferenca
   e que aqui nao tem mockup inventado, cada peca e um quadro real de uma aula. */
.pilha{margin:clamp(26px,4vw,40px) auto 0;max-width:720px}
.pilha img{width:100%;height:auto;display:block}

/* soma de valores: cada item com a etiqueta de incluido, como na referencia */
.itens .incluso{display:inline-block;font:600 10px/1 var(--txt);letter-spacing:.1em;
  text-transform:uppercase;color:#1F7A4D;background:#D8F3E3;border-radius:999px;
  padding:5px 9px;margin-left:8px;vertical-align:2px;white-space:nowrap}
.itens s{color:var(--suave-esc);margin-left:8px;font-size:14px;white-space:nowrap}
.ancora{margin-top:14px;font-size:14.5px;color:var(--suave-esc);text-align:center}

/* lista de ganhos com visto, em vez de bolinha */
.saber-lista div::before{content:"✓";color:#fff;background:var(--mag);border-radius:50%;
  width:22px;height:22px;display:grid;place-items:center;font-size:12px;line-height:1;margin-top:3px}

/* ---------- SEM BURACO ENTRE AS SECOES ---------- */
.telao{padding-block:clamp(40px,6vw,72px) 0}
#antes{padding-top:clamp(34px,4.5vw,56px)}
"""

# Cada card e uma ACAO que a pessoa vai conseguir fazer, no jeito que ela pensa:
# "que plano assinar", "crie o seu clone". Nome de aula e categoria nao vendem nada.
# O minuto fica pequeno, so como prova de que e rapido.
AULAS = [
    (1, "Conheça a sua funcionária de IA", "2 min",
     "em dois minutos você vê o que vai ter no fim: alguém respondendo por você no WhatsApp."),
    (2, "Que plano do Claude assinar", "8 min",
     "qual plano vale, qual modelo usar em cada coisa e dois truques para o limite render muito mais."),
    (3, "Crie o seu clone no Claude", "12 min",
     "ele aprende o que você vende, para quem e como você fala. E nunca mais esquece."),
    (4, "Ligue o Claude no seu Gmail e no Drive", "15 min",
     "ele passa a ler e escrever nas ferramentas que você já abre todo dia, sem uma linha de código."),
    (5, "Peça uma página e receba o link", "12 min",
     "proposta, página ou ferramenta pronta para você mandar para a cliente no mesmo dia."),
    (6, "Coloque o Claude no seu WhatsApp", "4 min",
     "dez passos e ele começa a te responder no seu próprio número."),
    (7, "Crie robôs que trabalham sozinhos", "5 min",
     "bom dia, plantão, fechamento e arrumação acontecendo no horário que você escolher."),
    (8, "Espie a plataforma da minha equipe", "6 min",
     "o tour por dentro do que eu construí com o Claude, para você copiar a ideia."),
]

CARTOES = "\n".join(
    f"""      <article class="aula">
        <img src="aulas/capa-{n}.webp" width="1080" height="1350" loading="lazy" decoding="async"
             alt="Capa da aula {n}: {titulo}">
        <div class="corpo">
          <p>{frase}</p>
        </div>
      </article>""" for n, titulo, tempo, frase in AULAS)

BLOCO_AULAS = f"""
<!-- O QUE VOCE SAI SABENDO -->
<section class="secao aulas escuro brilho faixa" id="aulas">
  <div class="wrap">
    <div class="cabeca">
      <p class="eyebrow">O que você sai sabendo</p>
      <h2 class="tit">Domine o Claude <em>em menos de um dia</em></h2>
      <p class="arraste">A aula mais longa tem 15 minutos. Dá para fazer todas numa tarde.</p>
    </div>
    <div class="trilho">
{CARTOES}
    </div>
  </div>
</section>
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

# 2. a pilula e um titulo que fala do ganho, nao do formato.
#    "Aprenda a usar a ferramenta" descreve o curso; "coloque ele para fazer a parte chata"
#    e o que a pessoa quer. A dor ja esta na frase de baixo, entao o titulo fica no desejo.
H1_VELHO = ('      <h1>Aprenda do zero a usar o Claude para '
            '<span class="acesa">criar conteúdos</span></h1>')
H1_NOVO = ('      <p class="pilula">Para quem nunca abriu o Claude</p>\n'
           '      <h1>Coloque o Claude para fazer a '
           '<span class="acesa">parte chata</span> do seu dia</h1>')
assert H1_VELHO in html, "nao achei o titulo"
html = html.replace(H1_VELHO, H1_NOVO, 1)

# 3. a pilha do produto, os tres pilares e o segundo botao, logo abaixo da promessa
PILARES = """      <div class="pilha">
        <img src="telas/pilha.png" width="1400" height="860" fetchpriority="high" decoding="async"
             alt="As capas das oito aulas do minicurso, empilhadas">
      </div>
      <div class="pilares">
        <div><i>01</i><b>Ensine o Claude quem você é</b></div>
        <div><i>02</i><b>Peça para ele escrever os seus conteúdos</b></div>
        <div><i>03</i><b>Crie robôs que fazem o trabalho</b></div>
      </div>
"""
marca_cta = '      <div class="cta">\n'
assert marca_cta in html, "nao achei o bloco de botoes do topo"
html = html.replace(marca_cta, PILARES + marca_cta, 1)

antes_nota = '        <span class="nota-cta">'
novo_nota = ('        <a class="botao vazado" href="#aulas">Ver as aulas por dentro</a>\n'
             '        <span class="nota-cta">')
assert antes_nota in html, "nao achei a nota do botao"
html = html.replace(antes_nota, novo_nota, 1)

# 3b. a soma de valores no bloco da oferta: cada item marcado como incluido.
#     O unico preco avulso que existe de verdade e o da imersao, que foi vendida a R$ 97.
#     Nao invento preco para os outros itens: numero inventado numa pagina de venda queima.
INCLUSO = '<em class="incluso">incluído</em>'
TROCAS = [
    ("<b>O Minicurso Modo Automático</b>, com 8 aulas.</div>",
     f"<b>O Minicurso Modo Automático</b>, com 8 aulas. {INCLUSO}</div>"),
    ("A gravação da imersão do dia 10 de outubro, uma tarde inteira montando do zero.</div>",
     "A gravação da imersão do dia 10 de outubro, uma tarde inteira montando do zero. "
     f"<s>R$ 97</s>{INCLUSO}</div>"),
    ("Os prompts e materiais prontos.</div>", f"Os prompts e materiais prontos. {INCLUSO}</div>"),
    ("Tudo que eu gravar durante o seu ano de acesso.</div>",
     f"Tudo que eu gravar durante o seu ano de acesso. {INCLUSO}</div>"),
    ("A aula de agendar posts, de 8 minutos.</div>",
     f"A aula de agendar posts, de 8 minutos. {INCLUSO}</div>"),
]
for velho, novo in TROCAS:
    assert velho in html, f"nao achei o item da oferta: {velho[:40]}"
    html = html.replace(velho, novo, 1)

ANCORA = ('        <span class="parc">ou R$ 193 à vista. <span class="parc-mes">'
          'Menos de R$ 20 por mês.</span></span>')
assert ANCORA in html, "nao achei a linha de parcela"
html = html.replace(ANCORA, ANCORA + '\n        <p class="ancora">Só a imersão de quatro horas '
                    'foi vendida sozinha por R$ 97. Aqui ela vem junto com todo o resto.</p>', 1)

# 4. as aulas por dentro logo depois do topo, e so entao a tela grande, como prova
html = html.replace("</header>\n", "</header>\n" + BLOCO_AULAS + HERO, 1)

# 5. a galeria de telas dentro de "o que voce vai saber fazer"
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
