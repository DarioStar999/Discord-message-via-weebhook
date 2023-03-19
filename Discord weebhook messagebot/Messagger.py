from discord_webhook import DiscordWebhook 
weebhook= input("your weebhook link: ")
mention= input("do you want mentions?yes or no: ")
if mention== "yes":
  allowed_mentions = {
    "parse": ["everyone", "users"],
    "roles": ["role-id"]
  }
  content= input("ciao?: ")
  webhook = DiscordWebhook(url=weebhook, content=content, allowed_mention=allowed_mentions)
  response = webhook.execute()
if mention== "no":
  content= input("your message: ")
  webhook = DiscordWebhook(url=weebhook, content=content)
  response = webhook.execute()
finish= input("finish?yes or no: ")
if finish== "yes":
 exit()
embedss= input("want to use embeds? yes or no: ")
if embedss== "yes":
  titt= input("title of the embed:")
  descipt= input("description of the embed: ")
  embeds=  {
  "embeds":   [{
    "title": titt,
    "description": descipt, 
     }]
   }
  webhook = DiscordWebhook(url=weebhook, embeds=embeds)
  response = webhook.execute()
finsih2= input("finish?yes or no: ")
if finsih2== "yes":
  exit()
if finsih2== "no":
  print("i don't support anymore sry")
  finish3= input("Made whit code by DarioStar999: ")
if finish3== "yes":
  exit()
if finish3== "no":
  exit()
else:
  exit()