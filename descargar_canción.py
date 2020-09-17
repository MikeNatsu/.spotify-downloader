import os
import time
#import sy


location = "/home/$USERNAME/Música/"

print("\n Spotify - YouTube downloader \n")
option = (input(" 1. Descargar canción. \n 2. Descargar album. \n 3. Descargar playlist. \n 0. Salir. \n Ingrese el número de la opción deseada: "))

if option == "1":
    song = input("\n Ingrese nombre o enlace de canción. (Por defecto busqueda en YouTube): ")
    os.system("cd /home/anthony/Música && spotdl -s " + song)
    time.sleep(2)
    print("\n Descarga terminada.")
elif option == "2":
    album_name = input("\n Ingrese nombre del album: ")
    album_link = input("\n Ingrese el enlace el album: ")
    os.system("mkdir /home/anthony/Música/'" + album_name + "'")
    os.system("cd " + location + "'" + album_name + "' && spotdl -a " + album_link)
    os.system("cd " + location + "'" + album_name + "' && spotdl -l *.txt")
    os.system("cd " + location + "'" + album_name + "' && rm *.txt")
elif option == "3":
    ps_name = input("\n Ingrese nombre del la lista: ")
    ps_link = input("\n Ingrese el enlace de la lista: ")
    os.system("mkdir /home/anthony/Música/'" + ps_name + "'")
    os.system("cd " + location + "'" + ps_name + "' && spotdl -a " + ps_link)
    os.system("cd " + location + "'" + ps_name + "' && spotdl -l *.txt")
    os.system("cd " + location + "'" + ps_name + "' && rm *.txt")
elif option == "0":
    os.system("exit")
else:
    print(" \n Opción invalida")


input("\n Presiona cualquir tecla para continuar")
#os.system("clear")
#os.system("python3 /home/$USERNAME/Escritorio/descargar_canción.py")
















































### Verificación de carpeta, terminar la comprobación
# import os
# if os.path.isdir('/home/dev/Documentos/python/archivos_prueba/'):
#     print('La carpeta existe.');
# else:
#     print('La carpeta no existe.');
# if os.path.isfile('/home/dev/Documentos/python/archivos/archivo.txt'):
#     print('El archivo existe.');
# else:
#     print('El no archivo existe.');