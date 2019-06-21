from pyrogram import Client, Filters


app = Client('my_accccount',605563,"7f2c2d12880400b88764b9b304e14e0b")

s = '-1001274887387'

@app.on_message(Filters.private)
def forawrd(client, message):
 if message.from_user.id == 700761174:
  message.reply("Sorry Bhai, Nhi sikha sakta")
 else:
  file = open("userlist.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   t = line.split()
   for m in t:
    if not m == message.from_user.id:
     message.reply("Don't Spam, wait Surendra reply you soon.")
     fil = open("userlist.txt" , "r")
     li = fil.readlines()
     fil.close()
     for lin in li:
      x = lin.split()
      for y in x:
       fil = open("userlist.txt" , "w")
       li = fil.write(y + message.from_user.id)
       fil.close()
       
app.run()
