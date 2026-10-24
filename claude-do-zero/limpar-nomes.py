from pathlib import Path
from PIL import Image, ImageFilter

PASTA = Path("C:/Users/Micro/dl-work/dlestudio-iscas/claude-do-zero/telas")
ORIGEM = Path("G:/Meu Drive/DANIELLE   PROJETOS/REDES SOCIAIS   DANIELLE LEMOS/MATERIAIS VISUAIS/PRINTS REAIS - PARA POSTS/Plugins.png")

# a tela de plugins tem o nome de uma cliente na primeira linha: nome de cliente nao entra
# em peca de venda, entao essa faixa vai embacada
img = Image.open(ORIGEM).convert("RGB")
caixa = (222, 158, 900, 206)
img.paste(img.crop(caixa).filter(ImageFilter.GaussianBlur(9)), caixa)
img.save(PASTA / "plugins.webp", "WEBP", quality=88, method=6)
print("plugins", img.size)

(PASTA / "videos.webp").unlink(missing_ok=True)
print("videos.webp apagado: era a pauta de uma cliente de saude, nao o cartao de memoria")
