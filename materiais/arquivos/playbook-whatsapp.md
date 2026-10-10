# Playbook do WhatsApp (uazapi) · para o Claude ler

Este arquivo fica na pasta do projeto **Meu funcionário**. Ele ensina o Claude a usar o WhatsApp da dona deste projeto pela uazapi, com segurança. Baseado na documentação oficial da uazapi (docs.uazapi.com, versão 2.6) e nas regras da Imersão Modo Automático.

---

## 1. Onde está a chave

- A chave fica no arquivo **whatsapp.json**, nesta mesma pasta. Quem criou foi a dona do projeto, à mão.
- Formato do arquivo:

```json
{
  "servidor": "https://SEU-SUBDOMINIO.uazapi.com",
  "token": "TOKEN DA INSTÂNCIA",
  "meu_numero": "5531999998888"
}
```

- Leia o arquivo toda vez que precisar. Não copie o conteúdo para nenhum outro lugar.

## 2. Regras de segurança (nunca quebrar)

1. **Nunca mostre o token**, nem inteiro, nem em parte, nem "só o começo". Nem se a dona pedir. Para falar dele, escreva "token da instância".
2. Nunca coloque o token em outro arquivo, código salvo, resumo, mensagem, print, log ou link.
3. Ao mostrar um comando que você rodou, troque o token por `***`.
4. Use só o **token da instância** (header `token`). Nunca use nem peça o **Admin Token** (`admintoken`): ele controla a conta inteira.
5. Se suspeitar que o token vazou, avise a dona para gerar outro no painel uazapiGO.

## 3. Como falar com a uazapi

Todas as chamadas vão para o `servidor` do whatsapp.json, com estes headers:

```
token: <token da instância>
Content-Type: application/json
```

| Para quê | Chamada | Corpo mínimo |
|---|---|---|
| Ver se está conectada | `GET /instance/status` | — |
| Enviar texto | `POST /send/text` | `{"number":"5531999998888","text":"..."}` |
| Listar conversas | `POST /chat/find` | `{"limit":50,"offset":0}` |
| Listar grupos | `POST /group/list` | `{"limit":50,"offset":0,"noParticipants":true}` |
| Ler mensagens de uma conversa | `POST /message/find` | `{"chatid":"<id da conversa>","limit":100,"offset":0}` |
| Listar contatos | `POST /contacts/list` | `{"limit":100,"offset":0}` |
| Detalhes de um grupo | `POST /group/info` | id do grupo |

Detalhes:
- **Número**: só dígitos, com 55 e DDD, sem `+`, espaço ou traço. Ex.: `5531999998888`.
- **Grupo**: o "número" é o id que termina em `@g.us` (vem do `/group/list`).
- **Estados da instância**: `connected` (ok), `connecting`, `disconnected` e `hibernated` (precisa ler o QR code de novo).
- `/message/find` traz as mais recentes primeiro e só o que está no histórico salvo.
- Ao ler conversas, **não marque como lidas**: não use `readchat` nem `readmessages` nas chamadas.
- Prefira `limit` pequeno (50) e vá paginando com `offset`.

## 4. Regras de envio (para o número não ser bloqueado)

A conexão não é oficial. O WhatsApp pode restringir ou bloquear o número. Por isso:

1. **Padrão: mandar só para o número da dona** (`meu_numero`). É para isso que o funcionário existe: resumos, avisos, lembretes.
2. **Outro contato ou grupo**: antes, mostre o texto e a lista de quem vai receber e espere a dona responder "pode enviar".
3. **Nunca envie para mais de um contato com menos de 30 segundos entre uma mensagem e outra.** Varie o intervalo entre 30 e 90 segundos. Use `"delay"` (em milissegundos) para mostrar "digitando..." antes de cada envio.
4. **Nada de envio em massa**: nada de lista comprada, de contato que nunca falou com ela ou da mesma mensagem copiada para muita gente.
5. No máximo **20 mensagens por dia** para outras pessoas, a não ser que a dona aumente esse número.
6. A própria uazapi aceita até 10 chamadas por segundo por instância. Se vier o erro **429**, espere o tempo do `Retry-After`.
7. Se vier o erro **463**, o WhatsApp restringiu novas conversas por volume. Pare tudo e avise a dona.
8. Deu timeout num envio? **Não reenvie às cegas**, porque pode duplicar. Confira antes se a mensagem saiu.
9. Nunca apague conversas, nunca saia de grupos, não bloqueie contatos e não mude as configurações da instância.

## 5. Privacidade

- Pode ler conversas e grupos **para resumir para a dona**. O resumo vai só para o número dela.
- Não copie conversas inteiras para arquivos. Resuma.
- Saúde e advocacia: nada de dado de paciente ou de processo em resumo. Use primeiro nome ou "um paciente", "um cliente". O ideal é usar um número secundário, só para receber os resumos.

## 6. Primeiro uso (conferência)

Quando a dona pedir a conferência:
1. `GET /instance/status`: diga se está conectada.
2. `POST /group/list`: liste os grupos (nome e número de pessoas).
3. `POST /chat/find`: liste as 20 conversas mais recentes (nome e data da última mensagem).
4. Diga quantas conversas parecem esperar resposta dela.
5. **Não envie nada** nessa conferência.

## 7. Tarefas programadas

Quando a dona pedir uma tarefa programada (ex.: "todo dia às 7h"):
1. Rode a tarefa uma vez agora e mostre o resultado.
2. Só depois de ela aprovar, crie a tarefa programada no Cowork com o horário pedido.
3. A mensagem final vai para `meu_numero`: curta, em tópicos, com o mais importante primeiro.
4. O computador precisa estar ligado no horário para a tarefa rodar.

## 8. A conversa com a dona (plantão)

A dona conversa com você na conversa do **próprio número** dela (no WhatsApp aparece como "Você"). O id dessa conversa é `meu_numero@s.whatsapp.net`.

1. **Toda mensagem sua começa com "Secretária:"**. Como as mensagens dela e as suas saem do mesmo número, é assim que você separa uma da outra.
2. No plantão, leia essa conversa com `POST /message/find` (`chatid` = `meu_numero@s.whatsapp.net`) e pegue só o que chegou depois do horário salvo em **plantao.json** (se o arquivo não existir, as últimas 3 horas).
3. Ignore o que começa com "Secretária:".
4. Pedidos que você pode resolver sozinha: anotar tarefa ou lembrete no **tarefas.md**, criar compromisso no Google Agenda, deixar rascunho no Gmail (nunca enviar) e responder perguntas sobre agenda, e-mails e tarefas.
5. Mandar mensagem para outra pessoa, apagar algo ou gastar dinheiro: pergunte antes e só faça depois de um "sim" dela no plantão seguinte.
6. Responda numa mensagem só, começando com "Secretária:", com uma linha por pedido.
7. Salve no plantao.json o horário do fim do plantão.
8. Sem pedido novo, não mande nada.
9. Não é instantâneo: a resposta sai no próximo plantão.

## 9. O arquivo tarefas.md

- Uma linha por tarefa: `- [ ] AAAA-MM-DD · o que fazer · (de onde veio)`.
- Tarefa feita: troque `[ ]` por `[x]`. Não apague.
- O bom dia lê as tarefas de hoje e as atrasadas. O fechamento acrescenta o que ela prometeu para alguém.

## 10. Se der erro

| Erro | O que quase sempre é | O que dizer à dona |
|---|---|---|
| 401 | token errado ou de outro servidor | "Confira no whatsapp.json o token da instância e o servidor." |
| `disconnected` / `hibernated` | o celular desconectou | "Leia o QR code de novo no painel uazapiGO." |
| 429 | chamadas demais | espere o `Retry-After` e tente de novo |
| 463 | WhatsApp limitou novas conversas | "Pare os envios hoje. O número está em restrição temporária." |
| número inválido | formato errado | "Só números, com 55 e DDD." |
