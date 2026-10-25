"""Desenha as capas das aulas: uma por tema, no design system dela.

A Dani vetou os quadros de video como capa. O que ela quer e um TEMPLATE: cada capa anuncia
o que a aula faz, em frase de acao, do jeito que a pessoa pensa ("que plano do Claude
assinar", "crie o seu clone no Claude").

Molde da capa: papel gelo com grao, pastilha magenta com o numero, titulo grande em
Advercase, filete magenta e o tempo no rodape. Clara de proposito, porque elas aparecem
empilhadas em cima do fundo escuro do topo.

Saida: aulas/capa-1.webp ... capa-8.webp
"""
import io
import random
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

AQUI = Path(__file__).resolve().parent
ASSETS = Path("G:/Meu Drive/DANIELLE   PROJETOS/PRODUTOS DL ESTÚDIO/04 KIT E PLUGINS/_paginas/assets")
DESTINO = AQUI / "aulas"

L, A = 1200, 750
GELO = (244, 242, 238)
PAPEL = (251, 250, 248)
TINTA = (32, 26, 29)
MAGENTA = (139, 8, 63)
ACESA = (226, 48, 122)
SUAVE = (120, 110, 114)

CAPAS = [
    (1, "Conheça a sua\nfuncionária de IA", "2 min"),
    (2, "Que plano do\nClaude assinar", "8 min"),
    (3, "Crie o seu\nclone no Claude", "12 min"),
    (4, "Ligue o Claude no\nseu Gmail e no Drive", "15 min"),
    (5, "Peça uma página\ne receba o link", "12 min"),
    (6, "Coloque o Claude\nno seu WhatsApp", "4 min"),
    (7, "Crie robôs que\ntrabalham sozinhos", "5 min"),
    (8, "Espie a plataforma\nda minha equipe", "6 min"),
]


def fonte_de_woff2(arquivo, tamanho):
    """Pillow nao le woff2, entao a fonte e convertida para ttf na memoria."""
    f = TTFont(ASSETS / arquivo)
    buf = io.BytesIO()
    f.flavor = None
    f.save(buf)
    buf.seek(0)
    return ImageFont.truetype(buf, tamanho)


def poppins(tamanho):
    for nome in ("poppinsb.ttf", "Poppins-SemiBold.ttf", "segoeuib.ttf", "arialbd.ttf"):
        try:
            return ImageFont.truetype(nome, tamanho)
        except OSError:
            continue
    return ImageFont.load_default()


def grao(img, forca=7):
    random.seed(4)
    ruido = Image.effect_noise((img.width, img.height), 24).convert("L")
    return Image.blend(img, Image.merge("RGB", (ruido, ruido, ruido)), forca / 100)


for numero, titulo, tempo in CAPAS:
    capa = Image.new("RGB", (L, A), GELO)
    d = ImageDraw.Draw(capa)

    # uma mancha magenta de canto, bem leve, para o fundo nao ficar cru
    manchinha = Image.new("RGB", (L, A), GELO)
    ImageDraw.Draw(manchinha).ellipse([L - 520, -300, L + 240, 420], fill=(250, 232, 240))
    capa = Image.blend(capa, manchinha, 0.85)
    capa = grao(capa)
    d = ImageDraw.Draw(capa)

    margem = 78

    # pastilha com o numero da aula
    rotulo = "BÔNUS" if numero == 8 else f"AULA {numero}"
    fr = poppins(26)
    larg = d.textlength(rotulo, font=fr)
    d.rounded_rectangle([margem, margem, margem + larg + 56, margem + 56], radius=28, fill=MAGENTA)
    d.text((margem + 28 + larg / 2, margem + 28), rotulo, font=fr, fill=(255, 255, 255), anchor="mm")

    # titulo em Advercase, a estrela da capa
    ft = fonte_de_woff2("Advercase-Regular.woff2", 92)
    d.multiline_text((margem, A - 300), titulo, font=ft, fill=TINTA, spacing=12, anchor="ls")

    # filete magenta e o tempo no rodape
    d.rectangle([margem, A - 132, margem + 86, A - 126], fill=ACESA)
    d.text((margem, A - 96), tempo, font=poppins(28), fill=SUAVE, anchor="la")
    d.text((L - margem, A - 96), "Claude do Zero", font=poppins(26), fill=SUAVE, anchor="ra")

    saida = DESTINO / f"capa-{numero}.webp"
    capa.save(saida, "WEBP", quality=90, method=6)
    print(f"capa-{numero} {saida.stat().st_size // 1024} KB  {titulo.replace(chr(10), ' ')}")
