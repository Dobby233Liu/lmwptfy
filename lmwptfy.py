import os
def go():
 w = input("what would you like to know");
 # windows only
 if w != "":
  os.system("start \"\" https://en.wikipedia.org/wiki/{w}")
 else:
  printf("sorry not today")

def no_console_input(whattoknow):
 if whattoknow != "":
  os.system("start \"\" https://en.wikipedia.org/wiki/"+whattoknow)


