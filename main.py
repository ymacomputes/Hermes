import discord
import smtplib
from email.message import EmailMessage
from email.headerregistry import Address

def writeEmail(emailContents):
    msg = EmailMessage()

    msg['Subject'] = "Discord Messages"
    msg.set_content(emailContents) 
    print(emailContents)
    msg['From'] = Address(addr_spec="amy.collins49@mail.dcu.ie")
    msg['To'] = Address(addr_spec="amy.collins49@mail.dcu.ie")

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print("hello")
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    
    if message.content[:7] == "!email ":
        writeEmail(message.content[7:])
        await message.channel.send(message.content[7:])

client.run("--TOKEN CODE--")
