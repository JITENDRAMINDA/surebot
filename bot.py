from pyrogram import Client, Filters


app = Client("my22",869912,"a7b049e08df35464047d57e5134327e5")

s = '-1001274887387'

@app.on_message(Filters.command("get"))
def forawrd(client, message):
 x = client.iter_chat_members(message.chat.id)
 for q in x:
  client.AddChatUser(-1001250871922,int(q.user.id))

app.run()
