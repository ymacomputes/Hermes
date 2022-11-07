import discord
import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from os import getenv
load_dotenv()

def writeEmail(messageAuthor, emailContents):
    sender = getenv('sender_email')
    pwd = getenv('sender_pwd')
    subject = "Discord"

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = getenv('sendee_email')
    msg.attach(MIMEText(f"{messageAuthor}-> {emailContents}",'plain'))

    # try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(sender, pwd)
    server.sendmail(sender, getenv('sendee_email'), msg.as_string())
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
    print(message.content)
    print(message.author)
    print("hello")
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    
    if message.content[:7] == "!email ":
        writeEmail(message.author.display_name, message.content[7:])
        await message.channel.send(message.content[7:])

client.run(getenv('discord_token'))
