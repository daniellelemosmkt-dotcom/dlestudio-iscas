from pathlib import Path
from PIL import Image

ORIGEM = Path("G:/Meu Drive/DANIELLE   PROJETOS/REDES SOCIAIS   DANIELLE LEMOS/MATERIAIS VISUAIS/PRINTS REAIS - PARA POSTS/Claude criando e agendando meu post.png")
DESTINO = Path("C:/Users/Micro/dl-work/dlestudio-iscas/claude-do-zero/telas/carrossel-celular.webp")

# no celular a tela inteira fica ilegivel: mostramos o pedaco que prova, que e a frase
# dizendo o que mudou e os nove cards prontos
img = Image.open(ORIGEM).convert("RGB").crop((128, 401, 788, 666))
img.save(DESTINO, "WEBP", quality=90, method=6)
print(img.size, DESTINO.stat().st_size // 1024, "KB")
