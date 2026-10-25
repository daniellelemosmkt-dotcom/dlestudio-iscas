"""Monta a pilha do produto: tudo que a pessoa leva, numa imagem so.

E o mecanismo da pagina da Maria Wendt que a Dani mandou adaptar: um monte de material
empilhado, numerado, para a pessoa ver de uma vez que e MUITA coisa. A diferenca e que aqui
nao tem mockup inventado: cada peca da pilha e a capa de uma aula de verdade,
a mesma que aparece nos cards mais abaixo.

Saida: telas/pilha.png (fundo transparente, para cair em qualquer cor de secao).
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = Path(__file__).resolve().parent
CAPAS = AQUI / "aulas"
SAIDA = AQUI / "telas" / "pilha.png"

MAGENTA = (226, 48, 122, 255)
LARGURA, ALTURA = 1500, 1200

# (arquivo, largura da peca, centro x, centro y, giro em graus) — a 1 fica no meio e maior
PECAS = [
    ("capa-3.webp", 250, 250, 330, -8),
    ("capa-5.webp", 250, 540, 230, 4),
    ("capa-7.webp", 240, 840, 300, 10),
    ("capa-2.webp", 250, 1140, 380, -5),
    ("capa-1.webp", 330, 700, 620, -2),
    ("capa-4.webp", 250, 1180, 760, 7),
    ("capa-6.webp", 240, 300, 760, -11),
    ("capa-8.webp", 240, 930, 880, 6),
]
NUMEROS = [3, 5, 7, 2, 1, 4, 6, 8]


def peca(caminho, largura):
    """Uma tela com borda branca, canto arredondado e sombra."""
    img = Image.open(caminho).convert("RGB")
    altura = round(largura * img.height / img.width)
    img = img.resize((largura, altura), Image.LANCZOS)

    moldura = 10
    fundo = Image.new("RGBA", (largura + moldura * 2, altura + moldura * 2), (255, 255, 255, 255))
    fundo.paste(img, (moldura, moldura))

    canto = Image.new("L", fundo.size, 0)
    ImageDraw.Draw(canto).rounded_rectangle([0, 0, fundo.size[0] - 1, fundo.size[1] - 1],
                                            radius=16, fill=255)
    fundo.putalpha(canto)
    return fundo


def com_sombra(img, giro):
    girada = img.rotate(giro, expand=True, resample=Image.BICUBIC)
    folga = 46
    tela = Image.new("RGBA", (girada.width + folga * 2, girada.height + folga * 2), (0, 0, 0, 0))
    sombra = Image.new("RGBA", tela.size, (0, 0, 0, 0))
    sombra.paste(Image.new("RGBA", girada.size, (24, 14, 18, 150)), (folga, folga + 14), girada)
    tela.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(18)))
    tela.alpha_composite(girada, (folga, folga))
    return tela


def fonte(tamanho):
    for nome in ("poppinsb.ttf", "Poppins-SemiBold.ttf", "segoeuib.ttf", "arialbd.ttf"):
        try:
            return ImageFont.truetype(nome, tamanho)
        except OSError:
            continue
    return ImageFont.load_default()


pilha = Image.new("RGBA", (LARGURA, ALTURA), (0, 0, 0, 0))
for (arquivo, largura, cx, cy, giro), numero in zip(PECAS, NUMEROS):
    p = com_sombra(peca(CAPAS / arquivo, largura), giro)
    pilha.alpha_composite(p, (cx - p.width // 2, cy - p.height // 2))

pilha = pilha.crop(pilha.getbbox())
pilha.thumbnail((1400, 1400), Image.LANCZOS)
pilha.save(SAIDA, "PNG", optimize=True)
print("pilha", pilha.size, SAIDA.stat().st_size // 1024, "KB")
