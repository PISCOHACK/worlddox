from colorama import Fore, init
import requests
init()

azul = Fore.BLUE
verde = Fore.GREEN
rojo = Fore.RED
amarillo = Fore.YELLOW
cyan = Fore.CYAN
blanco = Fore.WHITE

print(f"""{azul} __     __     ______     ______     __         _____     _____     ______     __  __    
/\ \  _ \ \   /\  __ \   /\  == \   /\ \       /\  __-.  /\  __-.  /\  __ \   /\_\_\_\   
\ \ \/ ".\ \  \ \ \/\ \  \ \  __<   \ \ \____  \ \ \/\ \ \ \ \/\ \ \ \ \/\ \  \/_/\_\/_  
 \ \__/".~\_\  \ \_____\  \ \_\ \_\  \ \_____\  \ \____-  \ \____-  \ \_____\   /\_\/\_\ 
  \/_/   \/_/   \/_____/   \/_/ /_/   \/_____/   \/____/   \/____/   \/_____/   \/_/\/_/ 
                                                                                         {azul}
                            {verde} CREADO POR PISCO {verde}
                            {rojo} EL CREADOR NO SE HACE RESPONSABLE DEL MAL USO {rojo} 
                            {blanco} [  1  ] INVESTIGAR INFORMACION DE UN DNI ARGENTINO {blanco} 
                            {cyan} VERSION = V1 {cyan}""")


dni = input("Ingresa el DNI: ")

url = f"https://dni-finder.herokuapp.com/api/dni/{dni}"

peticion = requests.get(url)

data = peticion.json()

nombre = data['person']

cuit = data['cuit']

sexo = data['sex']

print(f"[ + ] Cuit : {cuit}")
print(f"[ + ] Nombre completo : {nombre}")
print(f"[ + ] Sexo : {sexo}")
