# py_mine-mod-analyzer
Application for Minecraft`s mods for analyzing them, find errors and duplicates and other mysterious features.
### Needed packages
You need install only Python 3.8.x
### How to install
Unpack archive and move it to your mod library (default: `C:\Users\Current User\AppData\Roaming\.minecraft\mods`)
### Official links
https://trello.com/b/MmLJWvLj/minemodanalyzer - Official page on Trello (only RU)
_____
# Features
- Minecraft mods installer
- Minecraft mods checker (check errors)
- Minecraft mods rename (using mcmod.info file)
- Minecraft game launcher
____
# Commands
:white_check_mark:`help` - Help link to this GitHub Page.

:no_entry_sign:`mine install [forge/codechickenlib]` - install required libraries

:no_entry_sign:`mine launch` - Launch the game

:no_entry_sign:`mine setdirectory game` - Set Minecraft location

:no_entry_sign:`mine setdirectrory mod` - Set mods library on your PC. Default value: application root directory

:no_entry_sign:`mine setdirectrory backup` - Set mods backup directory. Default value: application root directory
 
:no_entry_sign:`mod install [modname]` - Install mod from your mods directory
  
:no_entry_sign:`mod name ` - Set your own modname with `[old] [new]` attribute, or from mcmod.info file with `mcm [old]` attribute 
  
:white_check_mark:`mod remove [modname]` - Remove mod with `[modname]`
  
:white_check_mark:`mod [disable/enable]` - Disable/Enable mod 

:no_entry_sign:`mod info [modname]` - Information about mod
  
:no_entry_sign:`mod backup [modname]` - Backup mod to your folder
  
:no_entry_sign:`mod check [modname]` - Check all mods (without attribute), or only one
  
:white_check_mark:`mod list [disable/enable/(empty)]` - This command allows you to display a list of installed modifications, as well as enabled and disabled

:no_entry_sign:`mod setcategory [category] [modname]` - Set mod category

:no_entry_sign:`settings` - Application settings

