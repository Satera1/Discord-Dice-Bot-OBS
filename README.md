
# Dice Bot
## Motivation and Idea
With the need to broadcast virtual board games live, this code was designed so that dice could be rolled on screen, fairly and randomly!
So all you have to do is type in a command of how many dice you want to roll and how many sides each die will have. Easy, right?
# Attention
The use of the programme necessarily requires the use of the [OBS Studio](https://obsproject.com/download) and [Discord](https://discord.com/download) platforms in order to work.
The [OBS Studio](https://obsproject.com/download)  programme will be used to broadcast the live stream and scroll the data on the screen, while [Discord](https://discord.com/download) will be needed to activate the commands used to scroll the data on the screen.
In addition, you will need to install [Python](https://www.python.org/downloads/) and an [IDE](https://code.visualstudio.com/download) (I highly recommend using [Visual Studio Code](https://code.visualstudio.com/download)) to run this programme locally.
# Downloads
[Python](https://www.python.org/downloads/)
[Visual Studio Code](https://code.visualstudio.com/download) *or another IDE*
[OBS Studio](https://obsproject.com/download)
[OBS Studio Plugin](https://obsproject.com/forum/resources/obs-websocket-remote-control-obs-studio-using-websockets.466/) *obs-websocket-remote-control*
[Discord](https://discord.com/download)
# How to use
## Creating your Discord bot
Once you've installed everything you need, you'll need to create a Discord bot that will intermediate the commands you type into OBS Studio. To do this, go [HERE](https://discord.com/developers/applications) and click on ***NEW APPLICATION*** to create your Bot, very simple, isn't it? Now all you have to do is go to the **OAuth2 tab** and tick all the boxes and copy and paste the generated URL into your browser to **invite the Bot to your Discord server** (we strongly recommend that you don't share this link and that you only invite it to a private server, i.e. only to people who will be able to use the application's commands).
## Running the application
Download the project and open it in your IDE (in my case, Visual Studio Code), then type ‘**pip install -r requirements.txt**’ into the terminal and, in the ‘**config.json’** file, replace ‘**YOUR_TOKEN**’ with the **TOKEN** you copied (put it inside the quotes).

    {
    "TOKEN": "YOUR_TOKEN"
    }

## Configurações
Go to the file ‘**obs_helper.py**’ and change the settings for scene_name, host, port and password (on the fifth line) according to the settings used in the plugin within OBS Studio:

    scene_name = ‘Screen’, host=‘127.0.0.1’, port=4444, password=‘rolldice’

There you can also change some settings such as: source settings, creation of browser source in OBS scene, etc.

> Read ‘http://dice.bee.ac/’ website to learn more about dice settings.

Once you've done that, just run the '**bot.py**' file and **start using it!**

# Commands
**Type these commands into a Discord channel that your bot has access to:**

    '!r' (example: !r 3d6)

    '!ping' (Show your ping)
