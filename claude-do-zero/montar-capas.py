"""Desenha as capas das aulas: uma por tema, no design system dela, com imagem real.

A Dani vetou duas coisas antes: o nome de aula como titulo (tem que ser uma acao que a
pessoa imagina fazendo) e a capa sendo so texto (tem que ser visual). Entao cada capa tem:

  * pastilha magenta com o numero da aula;
  * a acao em Advercase grande, do lado esquerdo;
  * UMA TELA DE VERDADE da propria aula, encaixada do lado direito, torta e com sombra;
  * nas aulas de ferramenta, os icones reais recortados da propria tela de conectores dela;
  * filete magenta, tempo e assinatura no rodape.

Entradas: os quadros em frames/ (tirados dos videos das aulas) e telas/descobrir.webp,
de onde saem os icones de verdade do Google Drive, Gmail, Canva e Notion.

Saida: aulas/capa-1.webp ... capa-8.webp
"""
import io
import random
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = Path(__file__).resolve().parent
ASSETS = Path("G:/Meu Drive/DANIELLE   PROJETOS/PRODUTOS DL ESTÚDIO/04 KIT E PLUGINS/_paginas/assets")
FRAMES = Path("C:/Users/Micro/AppData/Local/Temp/claude/G--Meu-Drive-DANIELLE---PROJETOS-REDES-SOCIAIS---DANIELLE-LEMOS/2d521f0d-aa7d-472c-a4e3-26eedfd0f682/scratchpad/frames")
DESTINO = AQUI / "aulas"

L, A = 1200, 750
GELO = (244, 242, 238)
TINTA = (32, 26, 29)
MAGENTA = (139, 8, 63)
ACESA = (226, 48, 122)
SUAVE = (120, 110, 114)

# (numero, titulo, tempo, quadro da aula, mostra os icones das ferramentas?)
CAPAS = [
    (1, "Conheça a sua\nfuncionária\nde IA", "2 min", "a1.jpg", False),
    (2, "Que plano\ndo Claude\nassinar", "8 min", "a2.jpg", False),
    (3, "Crie o seu\nclone no\nClaude", "12 min", "a3.jpg", False),
    (4, "Ligue o Claude\nno seu Gmail\ne no Drive", "15 min", "a4.jpg", True),
    (5, "Peça uma\npágina e\nreceba o link", "12 min", "a5.jpg", False),
    (6, "Coloque o\nClaude no seu\nWhatsApp", "4 min", "a6.jpg", False),
    (7, "Crie robôs que\ntrabalham\nsozinhos", "5 min", "a7.jpg", False),
    (8, "Espie a\nplataforma da\nminha equipe", "6 min", "a8.jpg", False),
]

# recortes dos icones reais dentro de telas/descobrir.webp (1049x823)
ICONES = [(238, 182), (636, 182), (238, 299), (636, 299), (636, 416)]
LADO_ICONE = 48


def fonte_advercase(tamanho):
    """Pillow nao le woff2, entao a fonte e convertida para ttf na memoria."""
    f = TTFont(ASSETS / "Advercase-Regular.woff2")
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


def cantos(img, raio):
    mascara = Image.new("L", img.size, 0)
    ImageDraw.Draw(mascara).rounded_rectangle([0, 0, img.width - 1, img.height - 1],
                                              radius=raio, fill=255)
    img.putalpha(mascara)
    return img


def tela_inclinada(caminho, largura, giro):
    """O quadro da aula com moldura branca, canto arredondado e sombra."""
    img = Image.open(caminho).convert("RGB")
    altura = round(largura * img.height / img.width)
    img = img.resize((largura, altura), Image.LANCZOS)

    m = 9
    com_moldura = Image.new("RGBA", (largura + m * 2, altura + m * 2), (255, 255, 255, 255))
    com_moldura.paste(img, (m, m))
    com_moldura = cantos(com_moldura, 16)

    girada = com_moldura.rotate(giro, expand=True, resample=Image.BICUBIC)
    folga = 40
    tela = Image.new("RGBA", (girada.width + folga * 2, girada.height + folga * 2), (0, 0, 0, 0))
    sombra = Image.new("RGBA", tela.size, (0, 0, 0, 0))
    sombra.paste(Image.new("RGBA", girada.size, (40, 24, 32, 120)), (folga, folga + 12), girada)
    tela.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(14)))
    tela.alpha_composite(girada, (folga, folga))
    return tela


def icones_reais():
    """Os icones das ferramentas, recortados da tela de conectores de verdade dela."""
    fonte = Image.open(AQUI / "telas" / "descobrir.webp").convert("RGBA")
    return [fonte.crop((x, y, x + LADO_ICONE, y + LADO_ICONE)) for x, y in ICONES]


for numero, titulo, tempo, quadro, com_icones in CAPAS:
    capa = Image.new("RGB", (L, A), GELO)
    manchinha = Image.new("RGB", (L, A), GELO)
    ImageDraw.Draw(manchinha).ellipse([L - 560, -320, L + 260, 400], fill=(250, 232, 240))
    capa = Image.blend(capa, manchinha, 0.85)

    random.seed(4)
    ruido = Image.effect_noise((L, A), 24).convert("L")
    capa = Image.blend(capa, Image.merge("RGB", (ruido, ruido, ruido)), 0.07).convert("RGBA")

    # a tela da aula entra primeiro, do lado direito
    giro = -4 if numero % 2 else 4
    tela = tela_inclinada(FRAMES / quadro, 470, giro)
    capa.alpha_composite(tela, (L - tela.width + 54, (A - tela.height) // 2 - 10))

    d = ImageDraw.Draw(capa)
    margem = 74

    rotulo = "BÔNUS" if numero == 8 else f"AULA {numero}"
    fr = poppins(26)
    larg = d.textlength(rotulo, font=fr)
    d.rounded_rectangle([margem, margem, margem + larg + 56, margem + 56], radius=28, fill=MAGENTA)
    d.text((margem + 28 + larg / 2, margem + 28), rotulo, font=fr, fill=(255, 255, 255), anchor="mm")

    ft = fonte_advercase(72)
    d.multiline_text((margem, 262), titulo, font=ft, fill=TINTA, spacing=12, anchor="la")

    if com_icones:
        x = margem
        for icone in icones_reais():
            capa.alpha_composite(icone, (x, A - 232))
            x += LADO_ICONE + 16

    d.rectangle([margem, A - 136, margem + 86, A - 130], fill=ACESA)
    d.text((margem, A - 100), tempo, font=poppins(28), fill=SUAVE, anchor="la")
    d.text((L - margem, A - 100), "Claude do Zero", font=poppins(26), fill=SUAVE, anchor="ra")

    saida = DESTINO / f"capa-{numero}.webp"
    capa.convert("RGB").save(saida, "WEBP", quality=88, method=6)
    print(f"capa-{numero} {saida.stat().st_size // 1024} KB  {titulo.replace(chr(10), ' ')}")
