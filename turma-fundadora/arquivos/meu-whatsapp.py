# -*- coding: utf-8 -*-
"""
MEU WHATSAPP NO PAINEL

Este é o ajudante que faz o seu painel mostrar as suas conversas de verdade,
na tela "Meu WhatsApp", e responder por ali mesmo.

Como usar: peça ao seu funcionário "liga o meu WhatsApp na tela".
Se você quiser fazer à mão, abra a pasta no terminal e rode:

    python meu-whatsapp.py

Depois abra no navegador o endereço que aparecer.

A SUA CHAVE: ela fica no whatsapp.json, lida só aqui dentro.
Ela nunca vai para o navegador, nunca aparece na tela e nunca entra em conversa.
Este ajudante só atende o seu próprio computador.
"""

import json
import os
import sys
import time
import urllib.parse
import urllib.request
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PASTA = os.path.dirname(os.path.abspath(__file__))
PORTA = 4545

# quanto tempo esperar entre duas mensagens enviadas, em segundos.
# é a regra da casa: nunca disparar mensagem em rajada.
ESPERA_ENTRE_ENVIOS = 30
ultimo_envio = 0.0


def ler_chave():
    caminho = os.path.join(PASTA, "whatsapp.json")
    if not os.path.exists(caminho):
        return None, (
            "Não achei o arquivo whatsapp.json nesta pasta. "
            "Ele é criado no passo 5 da Parte 4 da sua biblioteca."
        )
    try:
        with open(caminho, encoding="utf-8-sig") as f:
            c = json.load(f)
    except Exception:
        return None, (
            "O whatsapp.json existe, mas está escrito errado. "
            "Confira se ele tem as três linhas do modelo e se não virou whatsapp.json.txt."
        )
    falta = [k for k in ("servidor", "token") if not str(c.get(k, "")).strip()]
    if falta:
        return None, "Falta preencher no whatsapp.json: " + ", ".join(falta) + "."
    c["servidor"] = c["servidor"].strip().rstrip("/")
    return c, None


def uazapi(caminho, corpo=None, metodo=None):
    """Fala com a uazapi. A chave fica só aqui."""
    chave, erro = ler_chave()
    if erro:
        return {"erro": erro}
    dados = json.dumps(corpo, ensure_ascii=False).encode("utf-8") if corpo is not None else None
    req = urllib.request.Request(
        chave["servidor"] + caminho,
        data=dados,
        method=metodo or ("POST" if dados else "GET"),
    )
    req.add_header("token", chave["token"])
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        corpo_erro = e.read().decode("utf-8", "replace")[:300]
        if e.code in (401, 403):
            return {"erro": "O seu token não foi aceito. Confira o whatsapp.json: ele usa o token da instância, não o Admin Token."}
        return {"erro": "A uazapi respondeu com erro " + str(e.code) + ". " + corpo_erro}
    except Exception:
        return {"erro": "Não consegui falar com a uazapi. Confira a sua internet e o endereço do servidor no whatsapp.json."}


def so_etiquetas(c):
    """As etiquetas desta conversa, só o número de cada uma."""
    fora = []
    for marca in (c.get("wa_label") or []):
        marca = str(marca)
        fora.append(marca.split(":")[-1])
    return fora


def so_o_que_a_tela_precisa(c):
    """Devolve só os campos que a tela mostra. Nada de token, nada de dado solto."""
    texto = c.get("wa_lastMessageTextVote") or ""
    return {
        "etiquetas": so_etiquetas(c),
        "id": c.get("wa_chatid") or "",
        "nome": c.get("name") or c.get("wa_name") or c.get("wa_contactName") or "sem nome",
        "grupo": bool(c.get("wa_isGroup")),
        "naoLidas": int(c.get("wa_unreadCount") or 0),
        "ultimaMensagem": texto[:160],
        "quando": int(c.get("wa_lastMsgTimestamp") or 0),
        "foto": c.get("imagePreview") or "",
        "arquivada": bool(c.get("wa_archived")),
    }


class Ajudante(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=PASTA, **k)

    def log_message(self, *a):
        pass  # sem poluir a tela do terminal

    def responder_json(self, dados, codigo=200):
        corpo = json.dumps(dados, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(corpo)

    def so_daqui(self):
        """Só atende o próprio computador."""
        return self.client_address[0] in ("127.0.0.1", "::1")

    # ---------- leitura ----------
    def do_GET(self):
        caminho = urllib.parse.urlparse(self.path)
        if not caminho.path.startswith("/api/"):
            return super().do_GET()
        if not self.so_daqui():
            return self.responder_json({"erro": "Este ajudante só atende este computador."}, 403)

        campos = urllib.parse.parse_qs(caminho.query)

        if caminho.path == "/api/estado":
            chave, erro = ler_chave()
            if erro:
                return self.responder_json({"ligado": False, "erro": erro})
            r = uazapi("/instance/status")
            if "erro" in r:
                return self.responder_json({"ligado": False, "erro": r["erro"]})
            numero = str(chave.get("meu_numero", ""))
            info = r.get("instance") or r
            return self.responder_json({
                "ligado": str(info.get("status", "")).lower() in ("connected", "open", "conectado"),
                "situacao": info.get("status", ""),
                "finalDoNumero": numero[-4:] if numero else "",
            })

        if caminho.path == "/api/etiquetas":
            r = uazapi("/labels")
            if isinstance(r, dict) and "erro" in r:
                return self.responder_json(r, 502)
            colunas = []
            for et in (r or []):
                nome = (et.get("name") or "").strip()
                # as que começam com o caractere invisível são as do próprio WhatsApp
                # (Grupos, Favoritos, Não lidas) e não viram coluna do quadro.
                if not nome or nome[0] == "\u200e":
                    continue
                colunas.append({
                    "id": str(et.get("labelid") or ""),
                    "nome": nome,
                    "cor": et.get("colorHex") or "",
                })
            return self.responder_json({"etiquetas": colunas})

        if caminho.path == "/api/conversas":
            r = uazapi("/chat/find", {"sort": "-wa_lastMsgTimestamp", "limit": 200})
            if "erro" in r:
                return self.responder_json(r, 502)
            conversas = [so_o_que_a_tela_precisa(c) for c in (r.get("chats") or [])]
            if campos.get("tipo", ["pessoas"])[0] == "pessoas":
                conversas = [c for c in conversas if not c["grupo"]]
            conversas = [c for c in conversas if not c["arquivada"]]
            # quem tem etiqueta entra sempre, porque é uma coluna do quadro.
            # sem etiqueta, só as mais recentes, para a coluna de novas não virar lista infinita.
            com_etiqueta = [c for c in conversas if c["etiquetas"]]
            sem_etiqueta = [c for c in conversas if not c["etiquetas"]][:40]
            return self.responder_json({"conversas": com_etiqueta + sem_etiqueta})

        if caminho.path == "/api/mensagens":
            chatid = campos.get("chatid", [""])[0]
            if not chatid:
                return self.responder_json({"erro": "Faltou dizer qual conversa."}, 400)
            # o filtro certo aqui é o chatid. com "number" a uazapi devolve as
            # últimas mensagens da instância inteira, e a tela mostraria a conversa errada.
            r = uazapi("/message/find", {"chatid": chatid, "limit": 25})
            if isinstance(r, dict) and "erro" in r:
                return self.responder_json(r, 502)
            brutas = r.get("messages") if isinstance(r, dict) else r
            mensagens = []
            for m in (brutas or []):
                mensagens.append({
                    "id": m.get("messageid") or "",
                    "minha": bool(m.get("fromMe")),
                    "texto": (m.get("text") or "")[:1500],
                    "tipo": m.get("messageType") or "",
                    "quando": int(m.get("messageTimestamp") or 0),
                })
            mensagens.reverse()  # a mais antiga em cima, como no WhatsApp
            return self.responder_json({"mensagens": mensagens})

        return self.responder_json({"erro": "Não conheço este pedido."}, 404)

    # ---------- envio ----------
    def do_POST(self):
        global ultimo_envio
        if not self.so_daqui():
            return self.responder_json({"erro": "Este ajudante só atende este computador."}, 403)
        rota = urllib.parse.urlparse(self.path).path
        if rota not in ("/api/responder", "/api/mover"):
            return self.responder_json({"erro": "Não conheço este pedido."}, 404)

        tamanho = int(self.headers.get("Content-Length") or 0)
        try:
            pedido = json.loads(self.rfile.read(tamanho).decode("utf-8"))
        except Exception:
            return self.responder_json({"erro": "Não entendi o que você mandou."}, 400)

        if rota == "/api/mover":
            chatid = str(pedido.get("chatid") or "").strip()
            if not chatid:
                return self.responder_json({"erro": "Faltou dizer qual conversa."}, 400)
            tirar = str(pedido.get("tirar") or "").strip()
            por = str(pedido.get("por") or "").strip()
            # primeiro tira a etiqueta antiga, depois põe a nova.
            # a coluna "Novas conversas" é a conversa sem etiqueta nenhuma.
            for acao, qual in (("remove_labelid", tirar), ("add_labelid", por)):
                if not qual:
                    continue
                r = uazapi("/chat/labels", {"number": chatid, acao: qual})
                if isinstance(r, dict) and "erro" in r:
                    return self.responder_json(r, 502)
            return self.responder_json({"movido": True})

        chatid = str(pedido.get("chatid") or "").strip()
        texto = str(pedido.get("texto") or "").strip()
        if not chatid or not texto:
            return self.responder_json({"erro": "Faltou a conversa ou o texto da resposta."}, 400)

        espera = ESPERA_ENTRE_ENVIOS - (time.time() - ultimo_envio)
        if espera > 0:
            return self.responder_json({
                "erro": "Espere " + str(int(espera) + 1) + " segundos para mandar a próxima. "
                        "Mensagem em rajada é o caminho mais curto para o seu número ser bloqueado."
            }, 429)

        r = uazapi("/send/text", {"number": chatid, "text": texto})
        if "erro" in r:
            return self.responder_json(r, 502)
        ultimo_envio = time.time()
        return self.responder_json({"enviado": True})


def main():
    chave, erro = ler_chave()
    print("")
    print("  MEU WHATSAPP NO PAINEL")
    print("  " + "-" * 40)
    if erro:
        print("  " + erro)
        print("  O ajudante vai abrir assim mesmo, e a tela explica o que falta.")
    else:
        numero = str(chave.get("meu_numero", ""))
        print("  Chave lida do whatsapp.json. Número final: " + (numero[-4:] if numero else "não preenchido"))
    endereco = "http://localhost:" + str(PORTA) + "/index.html"
    print("  Abra o seu painel no navegador: " + endereco)
    print("  As conversas aparecem na tela Meu WhatsApp.")
    print("  Para desligar, feche esta janela preta ou aperte Ctrl + C.")
    print("")
    try:
        webbrowser.open(endereco)
    except Exception:
        pass
    servidor = ThreadingHTTPServer(("127.0.0.1", PORTA), Ajudante)
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("  Desligado. Até a próxima.")


if __name__ == "__main__":
    if sys.version_info < (3, 7):
        print("Este ajudante precisa do Python 3.7 ou mais novo.")
    else:
        main()
