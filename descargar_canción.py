import os
import time




music_location = "/home/$USERNAME/Música/"

print("\n Spotify - YouTube downloader \n")
option = (input(" 1. Descargar canción. \n 2. Descargar álbum. \n 3. Descargar playlist. \n 0. Salir. \n Ingrese el número de la opción deseada: "))

if option == "1":
    song = input("\n Ingrese nombre o enlace de canción. (Por defecto busqueda en YouTube): ")
    os.system("cd /home/$USERNAME/Música && spotdl -s " + song)
    time.sleep(2)
    print("\n Descarga terminada.")
elif option == "2":
    álbum_name = input("\n Ingrese nombre del álbum: ")
    álbum_link = input("\n Ingrese el enlace el álbum: ")
    os.system("mkdir /home/$USERNAME/Música/'" + álbum_name + "'")
    os.system("cd " + music_location + "'" + álbum_name + "' && spotdl -a " + álbum_link)
    os.system("cd " + music_location + "'" + álbum_name + "' && spotdl -l *.txt")
    os.system("cd " + music_location + "'" + álbum_name + "' && rm *.txt")
elif option == "3":
    ps_name = input("\n Ingrese nombre del la lista: ")
    ps_link = input("\n Ingrese el enlace de la lista: ")
    os.system("mkdir /home/$USERMANE/Música/'" + ps_name + "'")
    os.system("cd " + music_location + "'" + ps_name + "' && spotdl -a " + ps_link)
    os.system("cd " + music_location + "'" + ps_name + "' && spotdl -l *.txt")
    os.system("cd " + music_location + "'" + ps_name + "' && rm *.txt")
elif option == "0":
    os.system("exit")
else:
    print(" \n Opción invalida")


input("\n Presiona cualquier tecla para continuar")

