import discord
import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def writeEmail(messageAuthor, emailContents):
    sender = 'SENDER EMAIL'
    pwd = 'PASSWORD'
    subject = "Discord"

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = 'SENDEE EMAIL'
    msg.attach(MIMEText(f"{messageAuthor}-> {emailContents}",'plain'))

    # try:
    server = smtplib.SMTP("DOMAIN", PORT)
    server.ehlo()
    server.starttls()
    server.login(sender, pwd)
    server.sendmail(sender, 'SENDEE EMAIL', msg.as_string())
    server.close()
    print("successfully sent the mail")
    # except Exception as e:
    #     print(e)
    #     print("failed to send mail")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    
    if message.content[:7] == "!email ":
        writeEmail(message.author.display_name, message.content[7:])
        await message.channel.send(message.content[7:])

client.run("TOKEN")
