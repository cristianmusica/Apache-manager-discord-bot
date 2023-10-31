import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot is ready.')

    # Change current directory to root
    os.chdir('/')

    # Change current directory to "/var/www/html/"
    os.chdir('/var/www/html/')

@bot.command()
async def modify_index(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.send("Presiona el botón 'Modificar' para continuar.")
    
    def check_button(m):
        return m.author == ctx.author and m.content.lower() == "modificar" and m.channel == ctx.channel

    try:
        await bot.wait_for('message', check=check_button, timeout=60)
        await ctx.send("Adelante, dime el nombre del archivo a modificar.")

        try:
            filename = await bot.wait_for('message', check=check, timeout=60)
            filename = filename.content.strip()

            if os.path.isfile(filename):
                await ctx.send("Genial! El archivo está disponible. Envía el código para modificarlo.")

                try:
                    code = await bot.wait_for('message', check=check, timeout=60)
                    code = code.content.strip()

                    with open(filename, 'w') as file:
                        file.write(code)

                    await ctx.send(f"El archivo '{filename}' ha sido modificado exitosamente.")
                except asyncio.TimeoutError:
                    await ctx.send("No se ha proporcionado el código a tiempo.")
            else:
                await ctx.send("Oh no, al parecer ese archivo no está disponible en la carpeta actual.")
        except asyncio.TimeoutError:
            await ctx.send("No se ha proporcionado el nombre del archivo a tiempo.")
    except asyncio.TimeoutError:
        await ctx.send("No se ha presionado el botón 'Modificar' a tiempo.")

@bot.command()
async def create_file(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.send("Presiona el botón 'Crear' para continuar.")
    
    def check_button(m):
        return m.author == ctx.author and m.content.lower() == "crear" and m.channel == ctx.channel

    try:
        await bot.wait_for('message', check=check_button, timeout=60)
        await ctx.send("¿Dónde deseas crear el archivo?")

        try:
            location = await bot.wait_for('message', check=check, timeout=60)
            location = location.content.strip()

            if location.lower() == "aca":
                await ctx.send("Adelante, dime el nombre del archivo.")

                try:
                    filename = await bot.wait_for('message', check=check, timeout=60)
                    filename = filename.content.strip()

                    with open(filename, 'w') as file:
                        file.write("")

                    await ctx.send(f"El archivo '{filename}' ha sido creado exitosamente en la ubicación actual.")
                except asyncio.TimeoutError:
                    await ctx.send("No se ha proporcionado el nombre del archivo a tiempo.")
            else:
                await ctx.send("Ubicación no reconocida.")
        except asyncio.TimeoutError:
            await ctx.send("No se ha proporcionado la ubicación a tiempo.")
    except asyncio.TimeoutError:
        await ctx.send("No se ha presionado el botón 'Crear' a tiempo.")

bot.run('YOUR_DISCORD_TOKEN')
