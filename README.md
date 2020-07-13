# py_mine-mod-analyzer
Application for Minecraft`s mods for analyzing them, find errors and duplicates and other mysterious features.
## Needed packages
# Features
- Minecraft mods installer
- Minecraft mods checker
- Minecraft mods rename (using mcmod.info file)
# Commands
:white_check_mark:`help` - Help link to this GitHub Page.

:x:`mine install [forge/codechickenlib]` - install required libraries

:x:`mine launch` - Launch the game

:x:`mine setdirectory game` - Set Minecraft location

:x:`mine setdirectrory mod` - Set mods library on your PC. Default value: application root directory

:x:`mine setdirectrory backup` - Set mods backup directory. Default value: application root directory
 
:x:`mod install [modname]` - Install mod from your mods directory
  
:x:`mod name ` - Set your own modname with `[old] [new]` attribute, or from mcmod.info file with `mcm [old]` attribute 
  
:x:`mod remove [modname]` - Remove mod with `[modname]`
  
:x:`mod [disable/enable] [modname]` - Disable/Enable mod 

:x:`mod info [modname]` - Information about mod
  
:x:`mod backup [modname]` - Backup mod to your folder
  
:x:`mod check [modname]` - Check all mods (without attribute), or only one
  
:white_check_mark:`mod list [disable/enable/(empty)]` - This command allows you to display a list of installed modifications, as well as enabled and disabled

:x:`mod setcategory [category] [modname]` - Set mod category
