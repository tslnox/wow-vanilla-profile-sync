WoW Vanilla Profile Sync (profilesync.py)
=========================================

Made with the giant help of ChatGPT, this is a simple python script to copy your character UI to all your other characters.

# Usage:

## MANDATORY! BACKUP your profile folder (WoW\WTF\Account). I have tested the script, but only on my own profile. Neither I nor ChatGPT is responsible for loss of your meticulously handcrafted UI layout!
- Run WoW, login your primary character, set all your addons the way you want.
- If you want to only sync the profile to some characters, temporarily move the other characters folders out of the Account\ACCOUNT_NAME\REALM_NAME\ before running the script.
- If starting fresh, log in every character you want to sync the profile to. You can immediatelly logout.
- Exit the game.

- Download the script and put it in your WoW root directory (where you have WoW.exe)
- Run it:
  - In Linux, navigate into the directory where you put the file and type "python profilesync.py". You should have python installed, if not, refer to your distro's manual.
  - In Windows, you will first have to install python, I can't help with that as I don't use Windows. Then open cmd or powershell and do exactly the same as in Linux.
- It will ask you to confirm the folder - you have to type "yes", to be sure.
- Choose your account, realm and the source character (the one from which you want to copy the profile).
- Optionally enter any addons whose settings you don't want to copy - there are some default exclusions, noted below. You typically won't want to copy any character-specific stuff like roleplay addons. Use comma separated notation:
**addon1.lua,addon2.lua,addon3.lua**

- Press Enter. And the script should do its thing. Inspect the output for any weirdness and if there's any problem, curse at me, restore your backup (you **do** have it, do you?) and if you can spare the time, file a bug there on GitHub. I can't promise I'll fix it, but I can try.

- Builtin exclusions are: "TurtleRP.lua", "engbags.lua", "pfQuest.lua", "ModifiedPowerAuras.lua", "Outfitter.lua"
