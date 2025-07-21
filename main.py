import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
bot = commands.Bot(command_prefix='!', intents=intents)
token = os.environ['Tokendiscord']

created = os.name == "nt"


@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")


@bot.command()
async def reglement(ctx):
    regles = (
        "📜・**RÈGLES DU SERVEUR**\n"
        "\n"
        "🧠 **Respect & bienveillance**\n"
        "Tout le monde mérite le respect. Pas d’insultes, de harcèlement, de propos haineux, ou de discrimination. C’est tolérance zéro.\n"
        "\n"
        "🧼 **Pas de spam ni de flood**\n"
        "Évite les messages en chaîne, emojis en excès, pubs non autorisées ou spam vocal. Reste lisible.\n"
        "\n"
        "🛑 **Contenu interdit**\n"
        "Pas de NSFW, gore, contenu illégal. Les mineurs sont protégés.\n"
        "\n"
        "📌 **Respecte les salons**\n"
        "Chaque canal a sa fonction : utilise le bon au bon endroit. Un modérateur peut supprimer ou déplacer ton message.\n"
        "\n"
        "🔊 **Vocal = calme & respect**\n"
        "Pas de cris, de bruit de fond abusif, ou d’ambiances toxiques en vocal. On est là pour chill, pas se ruiner les tympans.\n"
        "\n"
        "🔧 **Obéis aux modos**\n"
        "Les modérateurs sont là pour veiller à la bonne ambiance. Leurs décisions doivent être respectées. Tu peux les contacter en cas de souci.\n"
        "\n"
        "⚠️ **Sanctions en cas d’abus**\n"
        "Warn, mute, kick ou ban : les sanctions sont progressives mais fermes si tu dépasses les limites.\n"
        "\n"
        "🤝 **Zéro rivalité entre serveurs**\n"
        "On est tous là pour progresser, créer, partager. Ce serveur n’accepte aucune rivalité ni compétition toxique entre membres ou entre communautés. "
        "Pas de drama, pas de guerre d’ego : l’entraide avant tout.")

    await ctx.send(regles)

keep_alive()
bot.run(token)
