import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import pytz

class Clock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        # Common timezones
        self.timezones = {
            'UTC': 'UTC',
            'EST': 'US/Eastern',
            'CST': 'US/Central',
            'MST': 'US/Mountain',
            'PST': 'US/Pacific',
            'GMT': 'Europe/London',
            'CET': 'Europe/Paris',
            'IST': 'Asia/Kolkata',
            'JST': 'Asia/Tokyo',
            'AEST': 'Australia/Sydney',
            'NZDT': 'Pacific/Auckland',
            'SGT': 'Asia/Singapore',
            'HKT': 'Asia/Hong_Kong',
            'BRT': 'America/Sao_Paulo',
            'SAST': 'Africa/Johannesburg',
        }
    
    @app_commands.command(name="clock", description="Display current time in different time zones")
    @app_commands.describe(timezone="Time zone (UTC, EST, PST, JST, etc.)")
    async def digital_clock(self, interaction: discord.Interaction, timezone: str = "UTC"):
        """Display current time in specified timezone"""
        try:
            timezone = timezone.upper()
            
            if timezone not in self.timezones:
                # Show available timezones
                tz_list = ", ".join(sorted(self.timezones.keys()))
                await interaction.response.send_message(
                    f"❌ Invalid timezone. Available: {tz_list}",
                    ephemeral=True
                )
                return
            
            # Get timezone object
            tz = pytz.timezone(self.timezones[timezone])
            current_time = datetime.now(tz)
            
            # Format time
            time_str = current_time.strftime("%H:%M:%S")
            date_str = current_time.strftime("%A, %B %d, %Y")
            offset = current_time.strftime("%z")
            
            # Create embed
            embed = discord.Embed(
                title=f"🕐 Digital Clock - {timezone}",
                color=discord.Color.blue()
            )
            embed.add_field(
                name="Time",
                value=f"```\n{time_str}\n```",
                inline=False
            )
            embed.add_field(
                name="Date",
                value=date_str,
                inline=False
            )
            embed.add_field(
                name="UTC Offset",
                value=f"{offset[:3]}:{offset[3:]}",
                inline=False
            )
            embed.set_footer(text=f"Timezone: {self.timezones[timezone]}")
            
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)}", ephemeral=True)
    
    @app_commands.command(name="worldclock", description="Display current time in multiple time zones")
    async def world_clock(self, interaction: discord.Interaction):
        """Display current time in all major timezones"""
        try:
            embed = discord.Embed(
                title="🌍 World Clock",
                description="Current time in major time zones",
                color=discord.Color.blue()
            )
            
            # Get current time in each timezone
            for tz_abbr in sorted(self.timezones.keys()):
                tz = pytz.timezone(self.timezones[tz_abbr])
                current_time = datetime.now(tz)
                time_str = current_time.strftime("%H:%M:%S")
                offset = current_time.strftime("%z")
                
                embed.add_field(
                    name=f"{tz_abbr} ({offset[:3]}:{offset[3:]})",
                    value=f"```\n{time_str}\n```",
                    inline=True
                )
            
            embed.set_footer(text="All times updated at command execution")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)}", ephemeral=True)
    
    @app_commands.command(name="timezone-list", description="Show all available time zones")
    async def timezone_list(self, interaction: discord.Interaction):
        """List all available timezones"""
        try:
            embed = discord.Embed(
                title="📅 Available Time Zones",
                description="Time zone abbreviations and their full names",
                color=discord.Color.blue()
            )
            
            # Create columns for better readability
            tz_text = ""
            for tz_abbr, tz_full in sorted(self.timezones.items()):
                tz_text += f"**{tz_abbr}** - {tz_full}\n"
            
            embed.add_field(
                name="Supported Zones",
                value=tz_text,
                inline=False
            )
            embed.set_footer(text="Use /clock <timezone> to see time in specific zone")
            
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)}", ephemeral=True)
    
    @app_commands.command(name="time-difference", description="Calculate time difference between two zones")
    @app_commands.describe(
        zone1="First time zone (e.g., EST)",
        zone2="Second time zone (e.g., JST)"
    )
    async def time_difference(self, interaction: discord.Interaction, zone1: str, zone2: str):
        """Calculate time difference between two timezones"""
        try:
            zone1 = zone1.upper()
            zone2 = zone2.upper()
            
            if zone1 not in self.timezones or zone2 not in self.timezones:
                await interaction.response.send_message(
                    f"❌ Invalid timezone. Use /timezone-list to see available zones.",
                    ephemeral=True
                )
                return
            
            # Get timezone objects
            tz1 = pytz.timezone(self.timezones[zone1])
            tz2 = pytz.timezone(self.timezones[zone2])
            
            current_time = datetime.now()
            time_in_tz1 = current_time.astimezone(tz1)
            time_in_tz2 = current_time.astimezone(tz2)
            
            # Calculate difference
            offset1 = time_in_tz1.utcoffset().total_seconds() / 3600
            offset2 = time_in_tz2.utcoffset().total_seconds() / 3600
            diff = abs(offset1 - offset2)
            
            direction = "ahead of" if offset1 > offset2 else "behind"
            
            embed = discord.Embed(
                title="⏱️ Time Difference",
                color=discord.Color.blue()
            )
            embed.add_field(
                name=f"{zone1}",
                value=time_in_tz1.strftime("%H:%M:%S"),
                inline=True
            )
            embed.add_field(
                name=f"{zone2}",
                value=time_in_tz2.strftime("%H:%M:%S"),
                inline=True
            )
            embed.add_field(
                name="Difference",
                value=f"{zone1} is **{diff:.0f} hours** {direction} {zone2}",
                inline=False
            )
            
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Clock(bot))