# py_mine-mod-analyzer
Application for Minecraft`s mods for analyzing them, find errors and duplicates and other mysterious features.
## Needed packages
# Features
- Minecraft mods installer
- Minecraft mods checker
- Minecraft mods rename (using mcmod.info file)
# Commands
:white_check_mark: `help` - Help link to this GitHub Page.

`mine install [forge/codechickenlib]` - install required libraries

`mine launch` - Launch the game

`mine setdirectory game` - Set Minecraft location

`mine setdirectrory mod` - Set mods library on your PC. Default value: application root directory

`mine setdirectrory backup` - Set mods backup directory. Default value: application root directory
 
`mod install [modname]` - Install mod from your mods directory
  
`mod name ` - Set your own modname with `[old] [new]` attribute, or from mcmod.info file with `mcm [old]` attribute 
  
`mod remove [modname]` - Remove mod with `[modname]`
  
`mod [disable/enable] [modname]` - Disable/Enable mod 

`mod info [modname]` - Information about mod
  
`mod backup [modname]` - Backup mod to your folder
  
`mod check [modname]` - Check all mods (without attribute), or only one
  
:white_check_mark: `mod list [disable/enable/(empty)]` - This command allows you to display a list of installed modifications, as well as enabled and disabled

`mod setcategory [category] [modname]` - Set mod category
