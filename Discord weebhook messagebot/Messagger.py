from discord_webhook import DiscordWebhook

weebhook= input("your weebhook link: ")

content= input("your message: ")

mention= input("do you want mentions?yes or no: ")

if mention== "yes":
  allowed_mentions = input("name for mention: ")

  webhook = DiscordWebhook(url=weebhook, content=content, allowed_mention=allowed_mentions)
  response = webhook.execute()
  input("Ciao")



if mention== "no":
 webhook = DiscordWebhook(url=weebhook, content=content)
 response = webhook.execute()


