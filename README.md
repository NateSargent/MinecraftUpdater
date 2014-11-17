MinecraftUpdater
================

MinecraftUpdater is a python 2.7 script that automates updates to servers running Mojang's Minecraft.

Run the script with "python minecraftupdater.py". I would advise that you shut down your server before attempting to run this script.

My system is Ubuntu linux, your mileage on other distributions may vary. Minecraft is commonly run on Windows servers. This script uses command line utilities not available on Windows, but the general approach should remain valid on any system.

EXPLANATION OF SCRIPT FUNCTION:

Generally, the most recent version of the minecraft .jar file will be located at:

https://s3.amazonaws.com/Minecraft.Download/versions/NUMBER/minecraft_server.NUMBER.jar

where NUMBER is the version number. For instance, currently the latest version is 1.7.5, so the appropriate file is found at:

https://s3.amazonaws.com/Minecraft.Download/versions/1.7.5/minecraft_server.1.7.5.jar

Wouldn't it be great if we knew what the latest version number was so we could format the URL ourselves and then just use "wget" to download the .jar file? Mojang has our back. They keep a .json file at:

https://s3.amazonaws.com/Minecraft.Download/versions/versions.json

that lists versions of the software. This file contains a "latest" field with two members: "snapshot" and "release". "release" contains the version number of the latest release version. I choose to run release versions rather than snapshot versions, so I use Python's "json" library to access the value of this field (which happens to be "1.7.5" today) and then I use it to build a URL to the .jar download.

Note that once you have the .jar in hand, its name will contain its version number, such as "minecraft_server.1.7.5.jar"
It is my understanding that you should rename the file to: "minecraft_server.jar" for it to be usable.

The above steps are likely to be the same for every user. What follows next depends on the specifics of your server and your filesystem. Should you open up my code, you'll see a hardcoded filepath:

/home/accountnamegoeshere/minecraft/minecraft_server.jar

If you want to use my code, replace this bit with a filepath that actually exists on your machine.

This concludes the explanation of script function. A few minor details have been omitted, such as the removal of old files. The script itself is relatively readable and, in my opinion, is one of my better-commented pieces. Feel free to refer to the script itself for more information.

This code is offered as-is with no guarantee whatsoever of anything, let alone functionality or safety.
