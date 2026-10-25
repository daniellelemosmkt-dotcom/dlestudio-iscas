"""Desenha as capas das aulas: foto dela sangrando na capa inteira e o titulo por cima.

A Dani mandou tres correcoes ate aqui, nesta ordem:
  1. o titulo nao pode ser nome de aula, tem que ser uma acao que a pessoa imagina fazendo;
  2. a capa nao pode ser so texto;
  3. e a capa NAO e um print da aula numa moldura: a capa inteira e visual, foto dela
     ocupando tudo, com o texto em cima, como nas capas de carrossel que ela mandou.

Por isso aqui: foto dela cortada em 4:5 ocupando a capa toda, titulo em duas partes
(Poppins em cima, Advercase embaixo, que e a manchete padrao dela), a assinatura pequena e
o tempo da aula. Sem veu e sem degrade sobre a foto, que ela veta: o texto vai na area lisa
que cada foto tem, e ganha sombra propria para nao sumir.

Saida: aulas/capa-1.webp ... capa-8.webp
"""
import io
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass

AQUI = Path(__file__).resolve().parent
ASSETS = Path("G:/Meu Drive/DANIELLE   PROJETOS/PRODUTOS DL ESTÚDIO/04 KIT E PLUGINS/_paginas/assets")
DESTINO = AQUI / "aulas"

L, A = 1080, 1350
CREME = (252, 246, 240)
ESCURO = (28, 20, 24)
ACESA = (226, 48, 122)

# numero, linha em Poppins, linha em Advercase, tempo, foto, onde o texto vai, se a area e clara
CAPAS = [
    (1, "conheça a sua", "funcionária de IA", "2 min"),
    (2, "que plano do Claude", "assinar?", "8 min"),
    (3, "crie o seu", "clone no Claude", "12 min"),
    (4, "ligue o Claude no seu", "Gmail e no Drive", "15 min"),
    (5, "peça uma página", "e receba o link", "12 min"),
    (6, "coloque o Claude", "no seu WhatsApp", "4 min"),
    (7, "crie robôs que", "trabalham sozinhos", "5 min"),
    (8, "espie a plataforma", "da minha equipe", "6 min"),
]

# preenchido por montar-capas-fotos.py: numero -> (caminho, "cima"|"baixo", "claro"|"escuro", foco_y)
FOTOS = {}
exec((AQUI / "capas-fotos.py").read_text(encoding="utf-8"))


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


def fundo(caminho, foco_y, foco_x):
    """A foto cortada em 4:5, ocupando a capa inteira, com o rosto no lugar certo.

    O estudio de 2023 e 2024 e cinza-lilas, frio. A regra dela pede luz quente, entao a
    foto leva um aquecimento leve: isso e tratamento de foto, nao veu por cima dela.
    """
    img = ImageOps.exif_transpose(Image.open(caminho)).convert("RGB")
    escala = max(L / img.width, A / img.height)
    img = img.resize((round(img.width * escala), round(img.height * escala)), Image.LANCZOS)
    x = max(0, min(img.width - L, round(img.width * foco_x - L / 2)))
    y = max(0, min(img.height - A, round(img.height * foco_y - A / 2)))
    corte = img.crop((x, y, x + L, y + A))

    r, g, b = corte.split()
    r = r.point(lambda v: min(255, int(v * 1.045 + 4)))
    b = b.point(lambda v: max(0, int(v * 0.965)))
    return Image.merge("RGB", (r, g, b))


def cabe(texto, fonte, largura, desenho):
    return desenho.textlength(texto, font=fonte) <= largura


def maior_que_cabe(texto, criar_fonte, limite, desenho, teto):
    tamanho = teto
    while tamanho > 28 and not cabe(texto, criar_fonte(tamanho), limite, desenho):
        tamanho -= 2
    return criar_fonte(tamanho)


def escrever(d, xy, texto, fonte, cor, ancora, halo):
    """Texto com sombra propria. Nao e veu sobre a foto: so o texto ganha contorno suave."""
    x, y = xy
    for dx, dy in ((0, 3), (0, -2), (3, 0), (-3, 0), (0, 7)):
        d.text((x + dx, y + dy), texto, font=fonte, fill=halo, anchor=ancora)
    d.text((x, y), texto, font=fonte, fill=cor, anchor=ancora)


for numero, linha_sans, linha_serif, tempo in CAPAS:
    caminho, posicao, tom, foco_y, foco_x = FOTOS[numero]
    capa = fundo(caminho, foco_y, foco_x)

    # o halo segue o tom da area: area clara pede texto escuro, area escura pede texto claro
    cor = ESCURO if tom == "claro" else CREME
    halo = (255, 255, 255, 0) if tom == "claro" else (0, 0, 0)
    halo = (250, 248, 246) if tom == "claro" else (18, 12, 15)

    base = Image.new("RGB", (L, A))
    base.paste(capa)
    capa = base
    d = ImageDraw.Draw(capa)

    margem = 76
    limite = L - margem * 2
    f_sans = maior_que_cabe(linha_sans, poppins, limite, d, 92)
    f_serif = maior_que_cabe(linha_serif, advercase, limite, d, 124)

    if posicao == "cima":
        y_assin, y1 = 96, 164
    else:
        y1 = A - 300 - f_serif.size
        y_assin = y1 - 74

    escrever(d, (margem, y_assin), "Dani Lemos  //  Claude do Zero", poppins(26), cor, "la", halo)
    escrever(d, (margem, y1), linha_sans, f_sans, cor, "la", halo)
    escrever(d, (margem, y1 + f_sans.size + 18), linha_serif, f_serif, cor, "la", halo)

    rotulo = "bônus" if numero == 8 else f"aula {numero}"
    escrever(d, (margem, A - 96), f"{rotulo}  ·  {tempo}", poppins(30), ACESA, "ls", halo)

    saida = DESTINO / f"capa-{numero}.webp"
    capa.save(saida, "WEBP", quality=86, method=6)
    print(f"capa-{numero} {saida.stat().st_size // 1024} KB  {linha_sans} {linha_serif}")
