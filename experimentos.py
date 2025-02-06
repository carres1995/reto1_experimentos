#inicializar proyecto reto 1

#Lista global para almacenar los diccionarios.
lista_experimentos=[]

#FUNCIONES*************************

#Funcion para agragar experimentos a la lista de diccionarios.
def agregar_exp(nombre, fecha, resultado, temperatura, energia):
    nuevo_exp = {"Nombre": nombre,"Fecha": fecha,"Resultado": resultado,"Temperatura (°C)": temperatura,"Energía Liberada(kJ)": energia}
    lista_experimentos.append(nuevo_exp)
    
    print(f"\n{'Nombre':<40}{'Fecha':<12}{'Resultado':<50}{'Temp (°C)':<15}{'Energía (kJ)':<15}")

    print(f"{nombre:<40}{fecha:<12}{resultado:<50}{temperatura:<15}{energia:<15}")
   
    print(f"\nExperimento {nombre} grabado con exito!!!!!")

#Funcion de eliminar experimento.
def eliminar_experimento(nombre_eliminar):
    global lista_experimentos  
    for exp in lista_experimentos:
        if exp["Nombre"].lower() == nombre_eliminar.lower(): 
            lista_experimentos.remove(exp)
            print(f"\nEl experimento '{nombre_eliminar}' ha sido eliminado con éxito.")
            return
    print(f"\nNo se encontró ningún experimento con el nombre '{nombre_eliminar}'.")

#Funcion para validacion de datos.
def validar_num(lim_min, lim_max, mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= lim_min and numero <= lim_max:
                return numero
            else:
                print(f"\nEl numero debe estar entre {lim_min} y {lim_max}. Intenta de nuevo!\n")
        except ValueError:
            print(" \nDebe ingresar un numero.\n ")

#Funcion para visualizar registros de los experimentos
def visualizar_exp():
    if not lista_experimentos:
        print("\nNo hay experimentnos agregados!!!")
        return
    print("\nTabla de Experimentos\n") 
    
    print(f"{'Nombre':<25}{'Fecha':<12}{'Resultado':<50}{'Temp (°C)':<15}{'Energía (kJ)':<15}")

    
    for exp in lista_experimentos:
        print(f"{exp['Nombre']:<25}{exp['Fecha']:<12}{exp['Resultado']:<50}{exp['Temperatura (°C)']:<15}{exp['Energía Liberada(kJ)']:<15}")
    
        

#Funcion para modificacion de datos.
def modificar_experimento(lista, nombre_modificar, clave, nuevo_valor):
    global lista_experimentos
    # Buscar el experimento por nombre
    for exp in lista:
        if exp["Nombre"].lower() == nombre_modificar.lower(): 
            if clave.lower() in exp:
                
                exp[clave] = nuevo_valor  # Modificar el valor
                print(f'\nModificado con éxito: {clave} ahora es "{nuevo_valor}" en el experimento "{nombre_modificar}".\n')
                return  # Salir de la función una vez modificado
            else:
                print(f'\nLa clave "{clave}" no existe en el experimento "{nombre_modificar}".\n')
                return

    # Si no se encontró el experimento
    print(f'\nNo se encontró el experimento con el nombre "{nombre_modificar}".\n')

#Funcion para obtener promedios.
def promedio(list_diccionario, clave):
    valores = []
    for exp in list_diccionario:
        if clave in exp:
            try:
                valores.append(float(exp[clave]))
            except ValueError:
                pass
    return sum(valores)/ len(valores) if valores else None


def comparar_experimentos(lista, nombre1, nombre2):
    """Compara temperatura y energía liberada entre dos experimentos."""
    exp1 = next((exp for exp in lista if exp["Nombre"].lower() == nombre1.lower()), None)
    exp2 = next((exp for exp in lista if exp["Nombre"].lower() == nombre2.lower()), None)

    if exp1 is None or exp2 is None:
        print("\n❌ Uno o ambos experimentos no existen en la lista.")
        return

    print(f"\n📊 Comparación entre '{nombre1}' y '{nombre2}':")

    # Comparación de temperatura
    temp1 = float(exp1["Temperatura (°C)"])
    temp2 = float(exp2["Temperatura (°C)"])
    
    if temp1 > temp2:
        print(f"{nombre1} tiene mayor temperatura ({temp1}°C) que {nombre2} ({temp2}°C).")
    elif temp1 < temp2:
        print(f"{nombre1} tiene menor temperatura ({temp1}°C) que {nombre2} ({temp2}°C).")
    else:
        print(f" Ambos experimentos tienen la misma temperatura ({temp1}°C).")

    # Comparación de energía liberada
    energia1 = float(exp1["Energía Liberada(kJ)"])
    energia2 = float(exp2["Energía Liberada(kJ)"])
    
    if energia1 > energia2:
        print(f" {nombre1} liberó más energía ({energia1} kJ) que {nombre2} ({energia2} kJ).")
    elif energia1 < energia2:
        print(f" {nombre1} liberó menos energía ({energia1} kJ) que {nombre2} ({energia2} kJ).")
    else:
        print(f" Ambos experimentos liberaron la misma cantidad de energía ({energia1} kJ).")

    print("\n Comparación finalizada.")


#MENU******


while True:
    print("\nMenu principal: ")
    print("\n1. Agregar experimento")
    print("2. Eliminar experimento")
    print("3. Visualizar experimentos")
    print("4. Modificar experimento")
    print("5. Operaciones experimentos")
    print("6. Salir")
        
    ingreso= input("Ingresa un numero de opcion: ")
    
    if ingreso == "6":
        print("\nGracias Adios!! ")
        break
    
#SUBMENU DE OPERACIONES*********
    if ingreso == "5":
        while True:
            print("\nMenu operaciones: ")
            print("\n1. Promedio")
            print("2. Minimos")
            print("3. Maximos")
            print("4. Comparar")
            print("5. Volver menu principal")
        
            ingreso1= input("Ingrese operacion: ")
            if ingreso1 == '1':#Ingreso para obtener los promedios
                print('\nOpciones disponibles para calcular el promedio: ')
                print('1. Temperatura (°C)')
                print('2. Energía Liberada(kJ)')
                clave_op = input('\nIngresa la opcion de clave a promediar: ')
                if clave_op == '1':
                    clave1="Temperatura (°C)"
                elif clave_op == '2':
                    clave1 = "Energía Liberada(kJ)"
                else:
                    print('\nOpcion invalida.')
                    continue
                result = promedio(lista_experimentos,clave1)
                if result is not None:
                    print(f'\nEl resultado de {clave1} es: {result:.2f}')
                else:
                    print(f'\nNo hay datos numericos para {clave1}.')
                    
                ingreso1 = input("Ingrese operación: ")

            elif ingreso1 == '4':  # Comparar experimentos
                nombre1 = input("\nIngrese el nombre del primer experimento: ")
                nombre2 = input("Ingrese el nombre del segundo experimento: ")
                comparar_experimentos(lista_experimentos, nombre1, nombre2)

            elif ingreso1 == '5':  # Salir del menú de operaciones
                break    
                    

#SUBMENU DE MINIMOS*********
            if ingreso1 == '2':
                while True:
                    print("\nMenu minimos: ")
                    print("\n1. Temperatura")
                    print("2. Energia Liberada")
                    print("4. Menu anterior")
        
                    ingreso2= input("\nIngrese la opcion al cual desea conocer el minimo: \n ")

                    if ingreso2 == '4':
                        break

#SUBMENU DE MAXIMOS*********
            if ingreso1 == "3":
                while True:
                    print("\nMenu maximos: ")
                    print("\n1. Temperatura")
                    print("2. Energia Liberada")
                    print("4. Menu anterior")
        
                    ingreso3= input("\nIngrese la opcion al cual desea conocer el maximo:\n ")

                    if ingreso3 == "4":
                        break

            if ingreso1 == "4":
                break

    if ingreso =="1":
        nombre= input("\nIngrese nombre experimento: ")
        dia = validar_num(1,31,'Digita dia del experimento: ')
        mes = validar_num(1,12, 'Digita el mes que se realizo el experimento: ')
        año = validar_num(1000,2025, 'Ingresa el año que se realiza el experimento:  ')
        fecha= f'{dia}/{mes}/{año}'
        resultado= input("Ingrese resultado del experimento: ")
        temperatura = validar_num(0,100000, 'Digita la temperatura de ignicion (°C): ')
        energia= validar_num(0,100000, 'Digita la energia liberada (kj): ')
        agregar_exp(nombre, fecha, resultado, temperatura, energia)
    
    if ingreso == "2":
        nombre_eliminar = input("\nIngrese el nombre del experimento a eliminar: ")
        eliminar_experimento(nombre_eliminar)      
    
    if ingreso == '3':
        visualizar_exp()     
              
    if ingreso == '4':
        nomb_modificar = input('Ingresa nombre del experimento a modificar: ')
        clave = input('Ingresa el parametro al cual le quieres cambiar el resultado: ')
        nuevo_valor = input('Ingresa el nuevo valor: ')
        modificar_experimento(lista_experimentos,nomb_modificar,clave,nuevo_valor)
        