import discord
from discord.ext import commands
from discord import app_commands
import aiohttp

class Jokes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.joke_api_url = "https://official-joke-api.appspot.com/random_joke"
    
    @app_commands.command(name="joke", description="Get a random joke")
    async def get_joke(self, interaction: discord.Interaction):
        """Fetch and display a random joke"""
        try:
            await interaction.response.defer()
            
            async with aiohttp.ClientSession() as session:
                async with session.get(self.joke_api_url) as response:
                    if response.status == 200:
                        joke_data = await response.json()
                        
                        # Create embed
                        embed = discord.Embed(
                            title="😂 Random Joke",
                            color=discord.Color.gold()
                        )
                        embed.add_field(
                            name="Setup",
                            value=joke_data['setup'],
                            inline=False
                        )
                        embed.add_field(
                            name="Punchline",
                            value=joke_data['punchline'],
                            inline=False
                        )
                        embed.add_field(
                            name="Type",
                            value=joke_data['type'].capitalize(),
                            inline=True
                        )
                        embed.set_footer(text="Powered by Official Joke API")
                        
                        await interaction.followup.send(embed=embed)
                    else:
                        await interaction.followup.send("❌ Failed to fetch joke. Try again later.", ephemeral=True)
        except Exception as e:
            await interaction.followup.send(f"❌ Error: {str(e)}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Jokes(bot))
