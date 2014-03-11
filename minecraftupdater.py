#minecraftupdater.py
#2014 Nate Sargent
#python 2.7, targetting linux. My system is Ubuntu, your mileage on other systems may vary.
import json
from pprint import pprint
import subprocess

print "Welcome to minecraftupdater.py!"
#Fetch Mojang's newest version file:
print "downloading versions.json"
subprocess.call(["wget", "https://s3.amazonaws.com/Minecraft.Download/versions/versions.json"])

#open and load the JSON file into memory
print "loading versions.json into memory"
json_data = open('versions.json')
print "decoding JSON"
data = json.load(json_data)
#pprint(data)
json_data.close()
#done with versions.json, delete it so it doesn't collide with the next incoming versions.json
print "removing versions.json"
subprocess.call(["rm","versions.json"])

#get the version number of the latest release
print "getting release ID number"
releaseid = data["latest"]["release"]

#now we can use releaseid to build a wget statement
print "building wget statement"
jarurl = "https://s3.amazonaws.com/Minecraft.Download/versions/" + releaseid + "/minecraft_server." + releaseid + ".jar"
#execute the wget. This is the step that actually downloads the new .jar
print "running wget statement"
subprocess.call(["wget",jarurl])

#copy to my minecraft directory. THIS IS USER SPECIFIC. You'll need to supply your own path.
#note that I not only move minecraft_server.version.number.jar, but I rename it.
print "moving and renaming .jar file"
minecraft_server_downloaded_jar = "minecraft_server." + releaseid + ".jar"
subprocess.call(["cp", minecraft_server_downloaded_jar, "/home/hostaccount/minecraft/minecraft_server.jar"])

#remove old .jar from working directory
print "removing old .jar file"
subprocess.call(["rm", minecraft_server_downloaded_jar])

print "Done! Your Minecraft server is updated to the lastest version " + releaseid

