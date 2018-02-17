import os
def go():
 w = input("what would you like to know");
 # windows only
 os.system("start \"\" https://en.wikipedia.org/wiki/{w}")

def no_console_input(whattoknow):
 if whattoknow != "":
  os.system("start \"\" https://en.wikipedia.org/wiki/"+whattoknow)


