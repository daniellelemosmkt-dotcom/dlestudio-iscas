"""Monta as tres telas do leque do topo, a partir dos prints feitos na hora.

Sao pedidos genericos, nada da Dani e nada de cliente: uma legenda para uma loja de roupas,
a semana de conteudo de uma cafeteria e um card de post criado pelo Claude. O objetivo do
leque e dar desejo em dois segundos, mostrando o Claude escrevendo e entregando trabalho
pronto.
"""
from pathlib import Path
from PIL import Image

BLOBS = Path("C:/Users/Micro/.claude/projects/G--Meu-Drive-DANIELLE---PROJETOS-REDES-SOCIAIS---DANIELLE-LEMOS/2d521f0d-aa7d-472c-a4e3-26eedfd0f682/tool-results")
DESTINO = Path("C:/Users/Micro/dl-work/dlestudio-iscas/claude-do-zero/telas")

CARDS = [
    ("leque-1", "mcp-claude-in-chrome-blob-1792876401183-ibypab.jpg", (30, 262, 940, 682)),
    ("leque-2", "mcp-claude-in-chrome-blob-1792876382711-y2kir1.jpg", (30, 338, 945, 1056)),
    ("leque-3", "mcp-claude-in-chrome-blob-1792876565271-cluoob.png", (10, 6, 702, 888)),
]

for nome, arquivo, caixa in CARDS:
    img = Image.open(BLOBS / arquivo).convert("RGB").crop(caixa)
    img.save(DESTINO / f"{nome}.webp", "WEBP", quality=88, method=6)
    print(f"{nome} {img.width}x{img.height} {(DESTINO / f'{nome}.webp').stat().st_size // 1024} KB")
