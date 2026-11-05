# 🛜 Minecraft Server
<p align="center">
    <img src="https://skillicons.dev/icons?i=linux,ubuntu,stackoverflow,java,idea,github,eclipse" />
</p>

I'm a fan of Minecraft and a tech enthusiast, thats why I created an Minecraft Server <br>
and here is my small documentation about things I needed to learn

# 🖥️ Screen Commands
| Command  | Explanation |
|-------|------------|
| screen -ls   | Shows all open consoles |
| screen -r (name) | Opens a console |
| screen -S (name) | Creates a console|
| screen -S (id).(name) -X quit | Deletes Console |

# 🔧 How to start

Making an start-file is one of the most common things, because it will save you hours.<br>
Especially when it comes to typos. It is much easier to have a file that gets used over and over again.<br><br>


Preview of the Server-Start file
```
#!bin/bash
java -Xms<MinRam>G -Xmx<MaxRam>G -jar <spigot/paper>.jar --nogui
```

How to start the Minecraft-Server from scratch
1. ✅ SSH login
2. 🔧 create screen and join it
3. 🏃 Go into the Server-Folder
4. ℹ️ ./(startFileName).sh
5. 🥳 And now the Server is starting

How to quit the Screen? CTRL + A then D
