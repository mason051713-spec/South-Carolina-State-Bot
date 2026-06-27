import discord
from discord.ext import commands
from discord import app_commands

class Promotions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="promotion", description="Promote a staff member")
    @app_commands.describe(
        member="Staff member to promote",
        new_rank="New rank for the staff member",
        reason="Reason for promotion"
    )
    async def promote_staff(self, interaction: discord.Interaction, member: discord.Member, new_rank: str, reason: str):
        """Promote a staff member"""
        try:
            # Create embed
            embed = discord.Embed(
                title="🎉 Staff Promotion",
                description=f"Congratulations! You have been promoted.",
                color=discord.Color.green()
            )
            embed.add_field(name="New Rank", value=new_rank, inline=False)
            embed.add_field(name="Promoted by", value=interaction.user.mention, inline=False)
            embed.add_field(name="Reason", value=reason, inline=False)
            embed.add_field(name="Guild", value=interaction.guild.name, inline=False)
            embed.add_field(name="Congratulations", value="We look forward to your continued service in this new role.", inline=False)
            
            # DM user
            await member.send(embed=embed)
            
            # Post in channel
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Promotions(bot))
