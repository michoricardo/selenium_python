import sys
try: color = sys.stdout.shell
#except AttributeError: raise RuntimeError("Use IDLE")
except:
  print("No pudimos imprimir al no correr en IDLE")

color.write("Hi, are you called Miharu461? \n","KEYWORD")
color.write("Yes","STRING")
color.write(" or ","KEYWORD")
color.write("No\n","COMMENT")
