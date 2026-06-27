# South Carolina State Bot

A comprehensive Discord bot for ERLC (Emergency Response: Liberty County) staff management, including infractions, applications, training, duty tracking, and more.

## Features

### 📋 Staff Management
- `/infraction warn` - Warn a staff member
- `/infraction terminate` - Terminate a staff member
- `/infraction demote` - Demote a staff member
- `/infraction view` - View infraction history
- `/infraction void` - Void an infraction by case ID
- `/promotion` - Promote a staff member with rank and reason

### 📝 Applications
- `/application accept` - Accept an application with reason
- `/application deny` - Deny an application with reason

### 🎓 Training
- `/training request` - Submit a training request
- `/training result` - Log training results (Pass/Fail)

### 📅 Session Management
- `/session start` - Post session startup embed
- `/session vote` - Create interactive session vote
- `/session end` - Post session ended embed

### 👮 Duty System
- `/onduty` - Go on duty
- `/offduty` - Go off duty
- `/shiftlist` - See who is on duty
- `/shifttime` - View your total shift time

### 🚨 Moderation
- `/warn add` - Add a warning to a member
- `/warn view` - View member's warnings
- `/warn remove` - Remove a warning from a member
- `/warn clear` - Clear all warnings from a member
- `/roleadd user` - Add role to a specific user
- `/roleadd everyone` - Add role to all server members
- `/rules all` - Post all server rules
- `/rules add` - Add a new rule
- `/rules remove` - Remove a rule

### 📞 Call Signs
- `/callsign generate` - Find available call sign (SCSO, RCPD, SCHP, SCFD, EMS, DOT)
- `/callsign claim` - Claim a specific call sign
- `/callsign release` - Release your current call sign

### 🛠️ Utilities
- `/ticket-panel` - Post support ticket panel
- `/erlc-preset` - View ERLC in-game command list
- `/embedbuilder` - Interactive embed builder

### 😂 Fun Commands
- `/joke` - Get a random joke from an external API

### 🕐 Clock & Timezone
- `/clock [timezone]` - Display current time in a specific timezone (UTC, EST, CST, MST, PST, GMT, CET, IST, JST, AEST, NZDT, SGT, HKT, BRT, SAST)
- `/worldclock` - Display current time in all 15 major timezones
- `/timezone-list` - Show all available timezone abbreviations
- `/time-difference <zone1> <zone2>` - Calculate time difference between two zones

## Installation

### Requirements
- Python 3.8+
- discord.py 2.4.0+
- aiohttp 3.9.1+
- pytz 2024.1+

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/mason051713-spec/South-Carolina-State-Bot.git
cd South-Carolina-State-Bot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Create a `.env` file**
```bash
cp .env.example .env
```

4. **Add your bot token to `.env`**
```
DISCORD_TOKEN=your_bot_token_here
```

5. **Run the bot**
```bash
python main.py
```

## Data Storage

All data is stored as JSON files in the `data/` folder (auto-created on first run):

- `data/shifts.json` - Active and completed shifts
- `data/infractions.json` - Staff infraction records with auto-incrementing case IDs
- `data/callsigns.json` - Claimed call signs
- `data/config.json` - Per-guild configuration
- `data/warnings.json` - Member warnings
- `data/tickets.json` - Active ticket channels
- `data/rules.json` - Server rules
- `data/applications.json` - Application records
- `data/training.json` - Training requests and results
- `data/nuke.json` - Anti-raid/nuke settings

## Bot Setup in Discord

1. Create a new Discord application at [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a bot under the application
3. Copy the bot token and add it to your `.env` file
4. Go to OAuth2 → URL Generator
5. Select scopes: `bot`
6. Select permissions:
   - `Send Messages`
   - `Embed Links`
   - `Manage Roles`
   - `Manage Channels`
   - `Read Message History`
   - `Add Reactions`
7. Use the generated URL to invite the bot to your server

## Commands Overview

All commands use Discord's slash command system. Simply type `/` and the bot will show available commands.

### Key Features

- **4+ Sentence Embeds** - All staff action notifications include detailed embeds
- **DM Notifications** - Staff members are notified via DM when actions affect them
- **Auto-incrementing Case IDs** - Infractions automatically get unique case IDs
- **JSON Data Persistence** - All data is stored locally in JSON format
- **Department Support** - Call sign system supports SCSO, RCPD, SCHP, SCFD, EMS, DOT
- **External APIs** - Integrates with joke and timezone APIs
- **Interactive Features** - Session votes, ticket panels, and role management

## Command Cogs

The bot is organized into separate command modules (cogs):

- `cogs/infractions.py` - Staff infractions and warnings
- `cogs/promotions.py` - Staff promotions
- `cogs/applications.py` - Application management
- `cogs/training.py` - Training requests and results
- `cogs/sessions.py` - Session management
- `cogs/duty.py` - Duty and shift tracking
- `cogs/moderation.py` - Moderation and rules
- `cogs/callsigns.py` - Call sign system
- `cogs/utilities.py` - Utility commands
- `cogs/jokes.py` - Joke generator
- `cogs/clock.py` - Clock and timezone commands

## Support

For issues or feature requests, please create an issue on GitHub.

## License

This project is licensed under the MIT License.
