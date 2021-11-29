import discord
import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def writeEmail(emailContents):
    sender = 'EMAIL'
    pwd = 'PASSWORD'
    subject = "Discord"

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = 'EMAIL'
    msg.attach(MIMEText(emailContents,'plain'))

    try:
        server = smtplib.SMTP("DOMAIN NAME", PORT)
        server.ehlo()
        server.starttls()
        server.login(sender, pwd)
        server.sendmail(sender, 'EMAIL', msg.as_string())
        server.close()
        print("successfully sent the mail")
    except: print("failed to send mail")

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

client.run("TOKEN")
