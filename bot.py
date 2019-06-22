from pyrogram import Client, Filters

from pyrogram.api import functions, types


app = Client("my22",869912,"a7b049e08df35464047d57e5134327e5")

s = '-1001274887387'

@app.on_message(Filters.command("get"))
def forawrd(client, message):
 x = client.iter_chat_members(message.chat.id)
 for q in x:
  client.send(functions.channels.InviteToChannel(app.resolve_peer(-1001177440186),app.resolve_peer(int(q))))
app.run()
