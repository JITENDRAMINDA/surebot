from pyrogram import Client, Filters


app = Client('835349563:AAEju8ekgXVB0JvpgyKyXN_YgCCHHyTBNH0',605563,"7f2c2d12880400b88764b9b304e14e0b")



u = 'id'
s = '-1001378725482'


@app.on_message(Filters.chat(int(s)) & Filters.text & ~ Filters.edited)

def forawrd(client, message):

   client.send_message(int(u),message.text)
           




@app.on_message(Filters.chat(int(s)) & Filters.sticker)

def forawrd(client, message):

   client.send_sticker(int(u),message.sticker.file_id)
            



app.run()
