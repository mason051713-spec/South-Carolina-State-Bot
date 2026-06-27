import discord
from discord.ext import commands
from discord import app_commands

class Sessions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    session_group = app_commands.Group(name="session", description="Session management commands")
    
    @session_group.command(name="start", description="Post a session startup embed")
    @app_commands.describe(
        host="Session host/host name",
        type="Type of session (e.g., Patrol, Training, etc.)"
    )
    async def start_session(self, interaction: discord.Interaction, host: str, type: str):
        """Post session startup embed with South Carolina theme"""
        try:
            embed = discord.Embed(
                title="🟢 SESSION STARTED",
                description="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nA new session has been initiated in South Carolina State Roleplay.\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                color=discord.Color.green()
            )
            embed.add_field(name="🎯 Session Host", value=f"**{host}**", inline=False)
            embed.add_field(name="📋 Session Type", value=f"**{type}**", inline=False)
            embed.add_field(name="👤 Started by", value=interaction.user.mention, inline=False)
            embed.add_field(name="⏰ Time", value=str(discord.utils.utcnow()), inline=False)
            embed.set_footer(text="South Carolina State Roleplay • Session System")
            
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)}", ephemeral=True)
    
    @session_group.command(name="vote", description="Post an interactive session vote")
    @app_commands.describe(
        question="Vote question",
        option1="First option",
        option2="Second option"
    )
    async def session_vote(self, interaction: discord.Interaction, question: str, option1: str, option2: str):
        """Post an interactive session vote with styled embed"""
        try:
            embed = discord.Embed(
                title="🗳️ SESSION VOTE",
                description="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n" + question + "\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                color=discord.Color.blue()
            )
            embed.add_field(name="👍 Option 1", value=f"**{option1}**", inline=False)
            embed.add_field(name="👎 Option 2", value=f"**{option2}**", inline=False)
            embed.set_footer(text="React to vote • South Carolina State Roleplay")
            
            message = await interaction.response.send_message(embed=embed)
            await message.add_reaction('👍')
            await message.add_reaction('👎')
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)}", ephemeral=True)
    
    @session_group.command(name="end", description="Post a session ended embed")
    @app_commands.describe(
        host="Session host/host name",
        duration="How long the session lasted"
    )
    async def end_session(self, interaction: discord.Interaction, host: str, duration: str):
        """Post session ended embed with South Carolina theme"""
        try:
            embed = discord.Embed(
                title="🔴 SESSION ENDED",
                description="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nThe session in South Carolina State Roleplay has concluded.\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                color=discord.Color.red()
            )
            embed.add_field(name="🎯 Session Host", value=f"**{host}**", inline=False)
            embed.add_field(name="⏱️ Duration", value=f"**{duration}**", inline=False)
            embed.add_field(name="👤 Ended by", value=interaction.user.mention, inline=False)
            embed.add_field(name="⏰ Time", value=str(discord.utils.utcnow()), inline=False)
            embed.set_footer(text="South Carolina State Roleplay • Session System")
            
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Sessions(bot))
