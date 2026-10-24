"""Tira a capa de cada aula do proprio video da aula.

A capa mais honesta de uma aula e um quadro dela. Os videos finais estao em
C:/Users/Micro/Videos/MINICURSO. O quadro sai a 45% da aula, que e onde ela ja esta
mostrando alguma coisa na tela em vez de falar na abertura.
"""
import subprocess
from pathlib import Path
from PIL import Image

VIDEOS = Path("C:/Users/Micro/Videos/MINICURSO")
DESTINO = Path("C:/Users/Micro/dl-work/dlestudio-iscas/claude-do-zero/aulas")

AULAS = [
    "Aula 1 - Boas-vindas",
    "Aula 2 - Planos, limites e modelos",
    "Aula 3 - Projetos e o seu cérebro",
    "Aula 4 - Conectores, plugins e skills",
    "Aula 5 - Claude Code e artefatos",
    "Aula 6 - O seu WhatsApp ligado",
    "Aula 7 - Rotinas, tarefas programadas e agentes",
    "Bonus - O meu hub",
]

for i, nome in enumerate(AULAS, start=1):
    video = VIDEOS / f"{nome} - EDITADO.mp4"
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                "-of", "csv=p=0", str(video)],
                               capture_output=True, text=True).stdout.strip())
    bruto = DESTINO / f"_a{i}.png"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(int(dur * 0.45)),
                    "-i", str(video), "-frames:v", "1", "-vf", "scale=560:-1", str(bruto)],
                   check=True)
    img = Image.open(bruto).convert("RGB")
    img.save(DESTINO / f"a{i}.webp", "WEBP", quality=84, method=6)
    bruto.unlink()
    print(f"a{i} {img.width}x{img.height} {int(dur)}s "
          f"{(DESTINO / f'a{i}.webp').stat().st_size // 1024} KB")
