from pyrogram import Client, Filters


app = Client('my_accccount',605563,"7f2c2d12880400b88764b9b304e14e0b")

s = '-1001274887387'

@app.on_message(Filters.private)
def forawrd(client, message):
 if message.from_user.id == 700761174:
  message.reply("Sorry Bhai, Nhi sikha sakta")
 else:
  message.reply("Don't Spam, wait Surendra reply you soon.")
 
app.run()
