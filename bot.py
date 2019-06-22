from pyrogram import Client, Filters


app = Client("my_ass",488556,"c722b7aadbf8b72109b2f96f30974c6d")

s = '-1001274887387'

@app.on_message(Filters.command("get"))
def forawrd(client, message):
 x = client.iter_chat_members(message.chat.id)
 for q in x:
  message.reply(int(q))

app.run()
