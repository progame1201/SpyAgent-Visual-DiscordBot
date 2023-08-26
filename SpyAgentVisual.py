import os


try:
  import asyncio
except:
    os.system("python -m pip install asyncio")
    import asyncio
from tkinter import filedialog
from PIL import Image, ImageTk

try:
  import pytz
except:
    os.system("python -m pip install pytz")
    import asyncio
import winsound


try:
 import discord
except:
    os.system("python -m pip install discord.py")
    import asyncio
import threading
try:
 import customtkinter
except:
    os.system("python -m pip install customtkinter")
    import customtkinter

channelasigned = False
print("SpyAgentVisual 1.3.0, progame1201")
app = customtkinter.CTk()
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
guildmutelist = []
txtguildmutelist = []
tdialog = customtkinter.CTkInputDialog(title="Key", text="Enter your key") # calling dialog
TOKEN = tdialog.get_input() # getting token
tdialog.destroy()

app.geometry("700x500")
app.title("SpyAgentVisual")
notification = False
print("YOUR TOKEN: " + str(TOKEN) + " <------ if here None kill your self")
intents = discord.Intents.all()
client = discord.Client(intents=intents)
guild_assigned = False
mutelist = []
txtmutelist = []
imgnotcreated = False
r = 2
def sendfile():
    global channelasigned
    global channel
    if channelasigned == True:
     file = filedialog.askopenfilename()
     asyncio.run_coroutine_threadsafe(channel.send(file=discord.File(file)), client.loop)
def sendmsg():
    global insertbox
    global channel
    global channelasigned
    if channelasigned == True:
     loop = asyncio.new_event_loop()
     asyncio.set_event_loop(loop)
     text = insertbox.get()
     insertbox.destroy()
     insertbox = customtkinter.CTkEntry(master=app, width=200)
     insertbox.place(relx=0.36, rely=0.9, anchor=customtkinter.CENTER)
     asyncio.run_coroutine_threadsafe(channel.send(text), client.loop)
async def chnnelhistory():
    global textbox
    global r
    global channel
    messages = []

    async for message in channel.history(limit=50, oldest_first=False):
        messages.append(message)

    messages.reverse()
    for message in messages:
        date = message.created_at
        timezone = pytz.timezone('Europe/Moscow')
        rounded_date = date.replace(second=0, microsecond=0)
        rounded_date_string = rounded_date.astimezone(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M')
        textbox.insert(index=f"{r}.0",text=f"\n{message.channel}: {rounded_date_string} {message.author}: {message.content}")
        r += message.content.count('\n') + 1
def nxtchanel(s):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    global chanelsbox
    global channels
    global channel
    global r
    global channelsids
    global textbox
    global guild
    global client
    global channelasigned
    indx = channels.index(s)
    channel = client.get_channel(channelsids[indx])
    textbox.insert(index=f"{r}.0", text=f"\nChannel selected. Channel name: {channel.name}")
    asyncio.run_coroutine_threadsafe(chnnelhistory(), client.loop)
    r += 1
    channelasigned = True
async def serverico():
    global guild
    global imgnotcreated
    global Thisisnotlabel3

    avatar2 = await guild.icon.read()

    avatarurl2 = guild.icon.url


    if ".png" in avatarurl2:

        open("guildico.png", 'wb').write(avatar2)

        img2 = Image.open("guildico.png")

    if ".jpg" in avatarurl2:

        open("guildico.jpg", 'wb').write(avatar2)

        img2 = Image.open("guildico.jpg")

    if ".gif" in avatarurl2:
        open("guildico.gif", 'wb').write(avatar2)

        img2 = Image.open("guildico.gif")

    img2 = img2.resize((64, 64))

    image2 = ImageTk.PhotoImage(img2)

    Thisisnotlabel3 = customtkinter.CTkLabel(master=app, text="", image=image2).place(relx=0.1, rely=0.45,anchor=customtkinter.CENTER)


def nxtguild(s):
    global guild
    global guilds
    global r
    global guildsids
    global channels
    global chanelsbox
    global channelsids
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    indx = guilds.index(s)
    guild = client.guilds[indx]
    asyncio.run_coroutine_threadsafe(serverico(), client.loop)
    channels = []
    channelsids = []
    def channelload():
      global channelas
      global channelsids
      for i, channel in enumerate(guild.text_channels):
        channels.append(channel.name)
        channelsids.append(channel.id)
      chanelsbox.configure(values=channels, command=nxtchanel)
    threading.Thread(target=channelload).start()
    textbox.insert(index=f"{r}.0", text="\n" + f"Guild selected. Guild name: {guild.name}")
    r += 1
async def receive_messages():
    global r
    global notification
    global client
    while True:
        attachment_list = []
        message = await client.wait_for('message')
        if message.channel.id in mutelist:
            continue
        if message.guild.id in guildmutelist:
            continue
        if isinstance(message.channel, discord.DMChannel):
            textbox.insert(index=f"{r}.0", text=f'\nprivate message: {message.channel}: ({message.author.id}) {message.author.name}: {message.content}')
            r += message.content.count('\n') + 1
            if notification == True:
                if str(message.author.name) != str(client.user.name):
                    winsound.Beep(500, 100)
                    winsound.Beep(1000, 100)
            continue

        if message.attachments:
          for attachment in message.attachments:
                  attachment_list.append(attachment.url)
          date = message.created_at
          timezone = pytz.timezone('Europe/Moscow')
          rounded_date = date.replace(second=0, microsecond=0)
          rounded_date_string = rounded_date.astimezone(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M')
          textbox.insert(index=f"{r}.0",text=f'\n{message.guild.name}: {message.channel.name}: {rounded_date_string} {message.author.name}: {message.content}, attachments: {attachment_list}')
          r += message.content.count('\n') + 1
          r += 1
          if notification == True:
              if str(message.author.name) != str(client.user.name):
                  winsound.Beep(500, 100)
                  winsound.Beep(1000, 100)
        else:
          date = message.created_at
          timezone = pytz.timezone('Europe/Moscow')
          rounded_date = date.replace(second=0, microsecond=0)
          rounded_date_string = rounded_date.astimezone(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M')
          textbox.insert(index=f"{r}.0", text=f'\n{message.guild.name}: {message.channel.name}: {rounded_date_string} {message.author.name}: {message.content}')
          r += message.content.count('\n') + 1
          r += 1
          if notification == True:
              if str(message.author.name) != str(client.user.name):
                  winsound.Beep(500, 100)
                  winsound.Beep(1000, 100)
def settings():
     global mutelist
     global sguildids
     global sguilds
     settings = customtkinter.CTk()
     settings.geometry("400x400")
     settings.title("SpyAgentVisual: Settings")
     sguilds = []
     sguildids = []
     for i, guild in enumerate(client.guilds):
         sguilds.append(guild.name)
         sguildids.append(guild.id)
     def setguild(s):
         global schannelsids
         global schannels
         sindx = guilds.index(s)
         sguild = client.guilds[sindx]
         schannels = []
         schannelsids = []
         for i, channel in enumerate(sguild.text_channels):
             schannels.append(channel.name)
             schannelsids.append(channel.id)
         mutebox.configure(values=schannels)
     def mute(s):
         global schannelsids
         global schannels
         global mutelist
         global txtmutelist
         sindx = schannels.index(s)
         mutelist.append(schannelsids[sindx])
         txtmutelist.append(schannels[sindx])
         unmutebox.configure(values=txtmutelist)
     def unmute(s):
         global schannelsids
         global schannels
         global mutelist
         global txtmutelist
         sindx = schannels.index(s)
         mutelist.remove(s)
         txtmutelist.remove(s)
         unmutebox.configure(values=txtmutelist)
     def notification():
         global notification
         global nswitch
         s = nswitch.get()
         if s == 1:
             notification = True
         else:
             notification = False

     def muteguild(s):
         global sguildids
         global sguilds
         global guildmutelist
         global txtguildmutelist
         global unmutesrvbox
         sindx = sguilds.index(s)
         guildmutelist.append(sguildids[sindx])
         txtguildmutelist.append(sguilds[sindx])
         unmutesrvbox.configure(values=txtguildmutelist)
     def unmuteguild(s):
         global unmutesrvbox
         global sguildids
         global sguilds
         global guildmutelist
         global txtguildmutelist
         sindx = sguilds.index(s)
         guildmutelist.remove(sguildids[sindx])
         txtguildmutelist.remove(sguilds[sindx])
         unmutesrvbox.configure(values=txtguildmutelist)
     global nswitch
     global unmutesrvbox
     nswitch = customtkinter.CTkSwitch(master=settings, command=notification, text="notification")
     nswitch.place(relx=0.2, rely=0.1, anchor=customtkinter.CENTER)
     sguildbox = customtkinter.CTkComboBox(master=settings, values=sguilds, command=setguild)
     sguildbox.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
     label3 = customtkinter.CTkLabel(master=settings, text="guilds")
     label3.place(relx=0.5, rely=0.22, anchor=customtkinter.CENTER)

     mutebox = customtkinter.CTkComboBox(master=settings, values=["None"], command=mute)
     mutebox.place(relx=0.2, rely=0.5, anchor=customtkinter.CENTER)
     label = customtkinter.CTkLabel(master=settings, text="mute channel")
     label.place(relx=0.2, rely=0.42, anchor=customtkinter.CENTER)

     unmutebox = customtkinter.CTkComboBox(master=settings, values=["None"], command=unmute)
     unmutebox.place(relx=0.8, rely=0.5, anchor=customtkinter.CENTER)
     label2 = customtkinter.CTkLabel(master=settings, text="unmute channel")
     label2.place(relx=0.8, rely=0.42, anchor=customtkinter.CENTER)

     unmutesrvbox = customtkinter.CTkComboBox(master=settings, values=["None"], command=unmuteguild)
     unmutesrvbox.place(relx=0.8, rely=0.8, anchor=customtkinter.CENTER)
     label4 = customtkinter.CTkLabel(master=settings, text="unmute guild")
     label4.place(relx=0.8, rely=0.72, anchor=customtkinter.CENTER)

     mutesrvbox = customtkinter.CTkComboBox(master=settings, values=sguilds, command=muteguild)
     mutesrvbox.place(relx=0.2, rely=0.8, anchor=customtkinter.CENTER)
     label5 = customtkinter.CTkLabel(master=settings, text="mute guild")
     label5.place(relx=0.2, rely=0.72, anchor=customtkinter.CENTER)

     settings.mainloop()

@client.event
async def on_ready():
         global textbox
         global guild_assigned
         global client
         global intents
         global guilds
         global progress
         global chanelsbox
         global Thisisnotlabel3
         global insertbox
         progress.set(0.5)
         if not guild_assigned:
             guilds = []
             for i, guild in enumerate(client.guilds):
                guilds.append(guild.name)
             avatar = await client.user.avatar.read()
             avatarurl = client.user.avatar.url

             if ".png" in avatarurl:
                 open("guildico.png", 'wb').write(avatar)
                 img = Image.open("guildico.png")
             if ".jpg" in avatarurl:
                 open("guildico.jpg", 'wb').write(avatar)
                 img = Image.open("guildico.jpg")
             if ".gif" in avatarurl:
                 open("guildico.gif", 'wb').write(avatar)
                 img = Image.open("guildico.gif")

             img = img.resize((64,64))
             image = ImageTk.PhotoImage(img)
             Thisisnotlabel = customtkinter.CTkLabel(master=app, text="", image=image).place(relx=0.1, rely=0.8, anchor=customtkinter.CENTER)
             nicknamelabel = customtkinter.CTkLabel(text=f"{client.user.name}", master=app).place(relx=0.1, rely=0.9, anchor=customtkinter.CENTER)
             textbox = customtkinter.CTkTextbox(master=app, width=550, height=300)
             textbox.place(relx=0.6, rely=0.5, anchor=customtkinter.CENTER)
             progress.set(0.6)
             guildsbox = customtkinter.CTkComboBox(master=app, values=guilds, command=nxtguild)
             customtkinter.CTkLabel(master=app, text="guilds").place(relx=0.11, rely=0.04, anchor=customtkinter.CENTER)
             guildsbox.place(relx=0.11, rely=0.1, anchor=customtkinter.CENTER)
             progress.set(0.7)
             customtkinter.CTkLabel(text="SpyAgentVisual 1.3.0", master=app).place(relx=0.5, rely=0.05, anchor=customtkinter.CENTER)
             channels = ["None"]
             customtkinter.CTkLabel(master=app, text="channels").place(relx=0.11, rely=0.25, anchor=customtkinter.CENTER)
             chanelsbox = customtkinter.CTkComboBox(master=app, values=channels)
             chanelsbox.place(relx=0.11, rely=0.3, anchor=customtkinter.CENTER)
             progress.set(0.8)
             insertbox = customtkinter.CTkEntry(master=app, width=200)
             insertbox.place(relx=0.36, rely=0.9, anchor=customtkinter.CENTER)
             progress.set(0.9)
             sendbutton = customtkinter.CTkButton(master=app, text="send", command=sendmsg)
             sendbutton.place(relx=0.63, rely=0.9, anchor=customtkinter.CENTER)
             sendfilebutton = customtkinter.CTkButton(master=app, text="send file", width=50, command=sendfile).place(relx=0.8, rely=0.9, anchor=customtkinter.CENTER)
             settingsbutton = customtkinter.CTkButton(master=app, text="settings", command=settings)
             progress.set(1)
             progress.destroy()
             settingsbutton.place(relx=0.85, rely=0.05, anchor=customtkinter.CENTER)
             guild_assigned = True
             loop = asyncio.new_event_loop()
             asyncio.set_event_loop(loop)
             asyncio.run_coroutine_threadsafe(receive_messages(), client.loop)
def run():
    global client
    client.run(TOKEN)
threading.Thread(target=run).start()
progress = customtkinter.CTkProgressBar(master=app)
progress.place(relx=0.85, rely=0.05, anchor=customtkinter.CENTER)
progress.set(0)
app.mainloop()