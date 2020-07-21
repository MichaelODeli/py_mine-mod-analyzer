import configparser

config=configparser.ConfigParser(comment_prefixes=';', inline_comment_prefixes=';') # set new variable
# Developing now
def setdirback(path):
    config.read(path)
    back_loc=config.get("location", "backup_location")
    print(back_loc)
def setdirmod(path):
    config.read(path)
    mod_loc=config.get('location', 'mod_location')
    print(mod_loc)

# In future
def mineinstall():
    print("Feature in development.")
def minesetcategory():
    print("Feature in development.")
def minelaunch():
    print("Feature in development.")