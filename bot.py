from pyrogram import Client, Filters


app = Client('765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc',605563,"7f2c2d12880400b88764b9b304e14e0b")

s = '-1001274887387'

@app.on_message(Filters.chat(int(s)) & Filters.text & ~ Filters.edited)
def forawrd(client, message):
 fil = open("sue.txt" , "r")
 c = fil.readlines()
 fil.close()
 for e in c:
  mes = client.send_message(int(e), "**" + message.text + "**")
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   files = open("sure.txt" , "w")
   files.write( line + " " + str(message.message_id) +  " " + str(mes.message_id))
   files.close()       

@app.on_message(Filters.chat(int(s)) & Filters.text & Filters.edited)
def forawrd(client, message):
 fil = open("sue.txt" , "r")
 c = fil.readlines()
 fil.close()
 for e in c:
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  x = line.split()
  id = str(message.message_id)
  if id in x:
   client.edit_message_text(int(u),int(x[x.index(id)+1]), "**" + message.text + "**" )
@app.on_message(Filters.command("set"))
def forawrd(client, message):
 if message.from_user.id == 491634139 :
  file = open("sue.txt" , "w")
  file.write(message.text.split(' ')[1])
  file.close()
  message.reply('done')
 elif message.from_user.id == 837065534 :
  file = open("sue.txt" , "w")
  file.write(message.text.split(' ')[1])
  file.close()
  message.reply('done')

app.run()
