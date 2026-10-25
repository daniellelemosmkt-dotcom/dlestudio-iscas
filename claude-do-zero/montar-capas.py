"""Desenha as capas das aulas: cheias de cor, do jeito que ela pediu.

Historico das correcoes dela, para nao repetir erro:
  1. titulo nao e nome de aula, e uma acao que a pessoa imagina fazendo;
  2. a capa nao pode ser so texto;
  3. a capa NAO e um print da aula dentro de um cartao branco;
  4. e a capa tambem NAO e foto dela de papel de parede, nem em outro formato, nem com
     letra preta. O que ela pediu: "capas visuais, preenchidas, coloridas que chamem
     atencao".

Entao: fundo cheio de cor da marca, com brilho e grao para nao ficar cru, numero gigante
em marca d'agua, titulo grande em letra clara (Poppins em cima, Advercase embaixo) e, nas
aulas de ferramenta, os icones reais recortados da tela de conectores dela.

Formato 1200x750, o mesmo de antes.

Saida: aulas/capa-1.webp ... capa-8.webp
"""
import io
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = Path(__file__).resolve().parent
ASSETS = Path("G:/Meu Drive/DANIELLE   PROJETOS/PRODUTOS DL ESTÚDIO/04 KIT E PLUGINS/_paginas/assets")
DESTINO = AQUI / "aulas"

L, A = 1200, 750
CREME = (252, 246, 240)
PESSEGO = (252, 234, 223)
MAGENTA = (139, 8, 63)
ACESA = (226, 48, 122)
VINHO = (58, 20, 36)
NOITE = (22, 14, 17)

# numero, linha em Poppins, linha em Advercase, tempo, cor do fundo, cor do brilho
CAPAS = [
    (1, "conheça a sua", "funcionária de IA", "2 min", (139, 8, 63), (255, 132, 178)),
    (2, "que plano do Claude", "assinar?", "8 min", (165, 11, 75), (252, 214, 196)),
    (3, "crie o seu", "clone no Claude", "12 min", (110, 10, 51), (226, 48, 122)),
    (4, "ligue o Claude no seu", "Gmail e no Drive", "15 min", (139, 8, 63), (252, 200, 172)),
    (5, "peça uma página", "e receba o link", "12 min", (165, 11, 75), (255, 132, 178)),
    (6, "coloque o Claude", "no seu WhatsApp", "4 min", (110, 10, 51), (252, 214, 196)),
    (7, "crie robôs que", "trabalham sozinhos", "5 min", (139, 8, 63), (226, 48, 122)),
    (8, "espie a plataforma", "da minha equipe", "6 min", (165, 11, 75), (252, 200, 172)),
]

ICONES = [(238, 182), (636, 182), (238, 299), (636, 299), (636, 416)]
LADO_ICONE = 48


def advercase(tamanho):
    f = TTFont(ASSETS / "Advercase-Regular.woff2")
    buf = io.BytesIO()
    f.flavor = None
    f.save(buf)
    buf.seek(0)
    return ImageFont.truetype(buf, tamanho)


def poppins(tamanho):
    for nome in ("poppinsb.ttf", "Poppins-Bold.ttf", "Poppins-SemiBold.ttf", "segoeuib.ttf"):
        try:
            return ImageFont.truetype(nome, tamanho)
        except OSError:
            continue
    return ImageFont.load_default()


def fundo_cheio(cor, brilho):
    """Cor cheia com um brilho no canto e grao por cima: nunca chapada."""
    base = Image.new("RGB", (L, A), cor)

    luz = Image.new("RGB", (L, A), cor)
    d = ImageDraw.Draw(luz)
    for raio, peso in ((560, 0.55), (380, 0.75), (220, 1.0)):
        mistura = tuple(round(c + (b - c) * 0.42 * peso) for c, b in zip(cor, brilho))
        d.ellipse([L - 300 - raio, -raio // 2, L - 300 + raio, raio], fill=mistura)
    luz = luz.filter(ImageFilter.GaussianBlur(120))
    base = Image.blend(base, luz, 0.85)

    ruido = Image.effect_noise((L, A), 20).convert("L")
    return Image.blend(base, Image.merge("RGB", (ruido, ruido, ruido)), 0.05)


def cabe(texto, fonte, largura, d):
    return d.textlength(texto, font=fonte) <= largura


def maior_que_cabe(texto, criar, limite, d, teto):
    t = teto
    while t > 30 and not cabe(texto, criar(t), limite, d):
        t -= 2
    return criar(t)


def icones_reais():
    fonte = Image.open(AQUI / "telas" / "descobrir.webp").convert("RGBA")
    return [fonte.crop((x, y, x + LADO_ICONE, y + LADO_ICONE)) for x, y in ICONES]


for numero, linha_sans, linha_serif, tempo, cor, brilho in CAPAS:
    capa = fundo_cheio(cor, brilho).convert("RGBA")
    d = ImageDraw.Draw(capa)

    # o numero gigante, em marca d'agua, enche a capa sem atrapalhar a leitura
    marca = Image.new("RGBA", (L, A), (0, 0, 0, 0))
    ImageDraw.Draw(marca).text((L - 60, A + 70), "0" + str(numero) if numero < 10 else str(numero),
                               font=advercase(460), fill=(255, 255, 255, 34), anchor="rs")
    capa.alpha_composite(marca)

    d = ImageDraw.Draw(capa)
    margem = 74
    limite = L - margem * 2 - 60
    f_sans = maior_que_cabe(linha_sans, poppins, limite, d, 76)
    f_serif = maior_que_cabe(linha_serif, advercase, limite, d, 104)

    rotulo = "bônus" if numero == 8 else f"aula {numero}"
    d.text((margem, 92), f"{rotulo}  ·  {tempo}", font=poppins(27), fill=PESSEGO, anchor="la")

    y = 268
    d.text((margem, y), linha_sans, font=f_sans, fill=CREME, anchor="la")
    d.text((margem, y + f_sans.size + 20), linha_serif, font=f_serif, fill=CREME, anchor="la")

    d.rectangle([margem, A - 148, margem + 92, A - 142], fill=ACESA)

    if numero == 4:
        x = margem
        for icone in icones_reais():
            capa.alpha_composite(icone, (x, A - 116))
            x += LADO_ICONE + 16
    else:
        d.text((margem, A - 104), "Claude do Zero", font=poppins(26),
               fill=(252, 234, 223, 170), anchor="la")

    saida = DESTINO / f"capa-{numero}.webp"
    capa.convert("RGB").save(saida, "WEBP", quality=88, method=6)
    print(f"capa-{numero} {saida.stat().st_size // 1024} KB  {linha_sans} {linha_serif}")
