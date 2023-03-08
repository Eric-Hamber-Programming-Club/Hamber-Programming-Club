## How to make a simple discord bot
### *Requirements: have a discord account, have pip and python >= 3.8*

- make a copy of the file `disbot.py` from this folder
- install the python discord library by entering `pip install py-cord` in a terminal
  - Note for experienced programmers: you may want to set up an environment (env/pipenv etc.) before this step

Before we can start editing the code, we need to set up the bot on Discord's end
- visit the [discord developer portal](https://discord.com/developers/applications)
- click "New Application" and select a name (you can change this later)
- optionally configure details: icon (profile picture), description etc.
- go to "Bot" tab on the left and click "Add bot"

The bot now exists!
- Scroll down and toggle the "Message Content Intent" and save

- Go to the OAuth2 tab in the left panel, go to "URL Generator"
  - Under scopes, select "bot" and "applications.commands"
  - Under "Bot Permissions", select "Send Messages", "Read Messages/View Channels", and "Add Reactions"
  - The "Generated URL" is what you will use to invite the bot: copy this and save it somewhere!

- Go back to the "Bot" tab and click the "Copy" button in the Token section
  - This token is like your bot's password - KEEP IT A SECRET!

We are almost there! Now, switch to an editor and open your `disbot.py` file
- Paste your bot's token inside the quotes on the third line (where it says `_TOKEN = `)

Edit the functions in the file or copy/paste to add more commands! When you are done, add your bot to any servers by giving the invite link to a server admin. Run the python file to turn on the bot.