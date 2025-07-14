
#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video],
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],}

#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],}

def mostrar_art(dict):
    for key, precio in dict.items():
        print(key, "$",precio) 

while True:
    try:
        print(""" *** MENU PRINCIPAL ***
                1. Stock marca.
                2. Búsqueda por precio.
                3. Actualizar precio.
                4. Salir.
                    """)
        op=int(input("seleccione una opcion (1-4): "))
        match op:
            case 1: 
                print("")
            case 2:
                while True:
                    try:
                        rango_min=int(input("indique el rango minimo del precio a buscar: "))
                        rango_max=int(input("indique el rango maximo del precio a buscar: "))
                        if rango_min>=20000 and rango_max<=30000:
                            print(stock['FS1230HD'])
                        elif rango_min>=20000 and rango_max>=45000:
                            print(stock['UWU131HD'])
                            print(stock['342FHD'])
                            print(stock['JjfFHD'])
                            print(stock['2175HD'])
                            print(stock['8475HD'])
                        elif rango_min>=20000 and rango_max>=80000:
                            print(stock['GF75HD'])
                            print(stock['fgdxFHD'])
                        else:
                            print("no hay notbooks en ese rango de precios! ")
                    except Exception:
                        print("ERROR, solo puede digitar numeros enteros!!")  
            case 3:
                mostrar_art(stock)
                act=input("ingrese el modelo que desea actualizar: ")
                n=int(input("ingrese el nuevo precio: "))
                stock[act]=n 
                print("--Precio actualizado--")
            case 4:
                print("Saliendo...")
                break
            case _:
                print("opcion invalida intente nuevamente")

    except Exception as e:
        print("error", e )