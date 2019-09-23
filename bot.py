from pyrogram import Client, Filters
from pyrogram.api import functions, types
app = Client("my_acc",854941,"bf9632f82af99dc8c3b934ab48d54780")
@app.on_message(Filters.command("get"))
def forawrd(client, message):
 x = client.iter_chat_members(message.chat.id)
 for q in x:
  try:
   app.send(functions.channels.InviteToChannel( channel = app.resolve_peer(int(message.text.split(' ')[1])), users = [app.resolve_peer(q.user.id)]))
  except:
   client.send_message(-1001356076506,str(q.user.id))
   continue 
app.run()
