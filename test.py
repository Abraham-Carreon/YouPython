import pytube, os, time

class DescargarVideo:

    def descarga(self, url, nombre):
        try:
            youtube = pytube.YouTube(url)            
            startime = time.time()
            
        except:
            os.system('cls')            
            print("Video no encontrado, prueba con otro")
            return
        
        try:
            #Limpia la consola
            os.system('cls')            
            print('"El tiempo varia dependiendo del tamaño del video"')
            print("Descargando video..... \nEspere un momento...")    
            #Descarga el video
            video = youtube.streams.first()
            video.download('videos', nombre)                        
            #Limpia la consola
            os.system('cls')
            #Toma el tiempo tardado
            tfinal = time.time() - startime
            tfinal = round(tfinal, 2)
            print("Video descargado en la carpeta videos :)\nDisfrutalo")
            print(f"Tiempo tardado: {tfinal}s")

        except:
            os.system('cls')
            print("Ocurrio un error al descargar el video, comprueba tu conexion")

  
descargaVideo = DescargarVideo()        

try:    
    try:
        url = input("Ingrese la url del video a descargar: \n")
        nombre = input("Ingrese el nombre del video a guardar: \n")        
        descargaVideo.descarga(url, nombre)
    
    except:
        print("Fallo la entrada de teclado")
    
except Exception as err:
    print("Ocurrio un error: ", err)

