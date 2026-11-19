import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado com sucesso como {bot.user}!')

@bot.command()
async def recicla(ctx):
    texto = (
        "♻️ **Recicla Tech: A Importância da Reciclagem Eletrônica**\n"
        "Descartar eletrônicos corretamente protege o planeta e transforma resíduos em novos recursos.\n\n"
        "🔌 **Por que reciclar peças eletrônicas?**\n"
        "Aparelhos como celulares, computadores e cabos contêm metais valiosos (ouro, prata, cobre e lítio). "
        "A reciclagem permite reaproveitar esses materiais (mineração urbana) e recondicionar peças para inclusão digital.\n\n"
        "🌍 **Impacto no Meio Ambiente**\n"
        "• **Evita contaminação:** Impede que metais tóxicos (como chumbo, mercúrio e cádmio) vazem para o solo e lençóis freáticos.\n"
        "• **Menos poluição:** Reduz a necessidade de extrair novos minérios da natureza, economizando água e energia.\n"
        "• **Menos lixo acumulado:** Evita que componentes que levam séculos para se decompor lotem os aterros sanitários.\n\n"
        "_Faça sua parte: descarte seu lixo eletrônico em pontos de coleta!_"
    )
    
    await ctx.send(texto)

bot.run('')