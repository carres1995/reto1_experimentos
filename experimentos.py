#inicializar proyecto reto 1

#Lista global para almacenar los diccionarios.
lista_experimentos=[{'Nombre': 'Reaccion del sodio al agua', 
               'Fecha': '14/05/2023', 
               'Resultado': 'Explosion con liberacion de hidrogeno y calor',
               'Temperatura (°C)': 90,
               'Energía Liberada(kJ)': 250           
               },
               {'Nombre': 'Combustion del magnesio', 
               'Fecha': '22/07/2023', 
               'Resultado': 'Emision de luz blanca intensa y formacion de oxido de magnesio',
               'Temperatura (°C)': 500,
               'Energía Liberada(kJ)': 500
            
               }]

#FUNCIONES********************************************************

#Funcion para agragar experimentos a la lista de diccionarios.
def agregar_exp(nombre, fecha, resultado, temperatura, energia):
    nuevo_exp = {"Nombre": nombre,"Fecha": fecha,"Resultado": resultado,"Temperatura (°C)": temperatura,"Energía Liberada(kJ)": energia}
    lista_experimentos.append(nuevo_exp) #Se crea nuevo diccionario conn los datos del experimento y se almacena en la lista global
    
    print(f"\n{'Nombre':<35}{'Fecha':<12}{'Resultado':<80}{'Temp (°C)':<15}{'Energía (kJ)':<15}") #Se imprime en formato tabla con la informacion del experimento agregado

    print(f"{nombre:<35}{fecha:<12}{resultado:<80}{temperatura:<15}{energia:<15}")
   
    print(f"\nExperimento {nombre} grabado con exito!!!!!")



#Funcion de eliminar experimento.
def eliminar_experimento(nombre_eliminar):
    global lista_experimentos  #Referencia a la lista global
    for exp in lista_experimentos:
        if exp["Nombre"].lower() == nombre_eliminar.lower(): #Busca por nombre sin distinguir mayusculas
            lista_experimentos.remove(exp) #Elimina el experimento encontrado
            print(f"\nEl experimento '{nombre_eliminar}' ha sido eliminado con éxito.")
            return
    print(f"\nNo se encontró ningún experimento con el nombre '{nombre_eliminar}'.")



#Funcion para validacion de datos.
def validar_num(lim_min, lim_max, mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= lim_min and numero <= lim_max: #Verifica que este en rango permitido
                return numero #Retorna el numero solo si es valido
            else:
                print(f"\nEl numero debe estar entre {lim_min} y {lim_max}. Intenta de nuevo!\n")
        except ValueError:
            print(" \nDebe ingresar un numero.\n ")



#Funcion para visualizar registros de los experimentos
def visualizar_exp():
    if not lista_experimentos: #Verifica que si existan los experimentos en la lista
        print("\nNo hay experimentnos agregados!!!")
        return
    print("\nTabla de Experimentos\n") 
    
    print(f"{'Nombre':<35}{'Fecha':<12}{'Resultado':<80}{'Temp (°C)':<15}{'Energía (kJ)':<15}")

    
    for exp in lista_experimentos: #recorre la lista de experimentos e imprime los datos en formato tabla 
        print(f"{exp['Nombre']:<35}{exp['Fecha']:<12}{exp['Resultado']:<80}{exp['Temperatura (°C)']:<15}{exp['Energía Liberada(kJ)']:<15}")
    
        

#Funcion para modificacion de datos.
def modificar_experimento(lista, nombre_modificar, clave, nuevo_valor):
    global lista_experimentos
    # Buscar el experimento por nombre
    for exp in lista:
        if exp["Nombre"].lower() == nombre_modificar.lower(): #Busca experimento por nombre sin distinguir mayusculas
            if clave in exp:
                
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
    valores = [] #Lista global para extraer los valoresy obtener los promedios
    for exp in list_diccionario:
        if clave in exp:
            try:
                valores.append(float(exp[clave]))#Agrega los valores a la lista global VALORES 
            except ValueError:
                pass
    return sum(valores)/ len(valores) if valores else None #Retorna el promedio si se cumple la condicion, de no ser asi retorna none



#Funcion de comparar 
def comparar_experimentos(lista, nombre1, nombre2):
    """Compara temperatura y energía liberada entre dos experimentos."""
    exp1 = next((exp for exp in lista if exp["Nombre"].lower() == nombre1.lower()), None) #Busca los experimentos por nombre, si no se encuentran genera none
    exp2 = next((exp for exp in lista if exp["Nombre"].lower() == nombre2.lower()), None)

    if exp1 is None or exp2 is None:
        print("\nUno o ambos experimentos no existen en la lista.")
        return

    print(f"\nComparación entre '{nombre1}' y '{nombre2}':")

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



    # Función para obtener valores mínimos y máximos
def obtener_min_max(lista, clave):
    if not lista:
        print("\nNo hay experimentos registrados para calcular mínimos y máximos.")
        return None, None
#Encontrar el minimo y el maximo basandose en la clave numerica
    minimo = min(lista, key=lambda x: x[clave])
    maximo = max(lista, key=lambda x: x[clave])
    
    return minimo, maximo


#MENU**************************************************************


while True:
    print("\nMenu principal: ")
    print("\n1. Agregar experimento")
    print("2. Eliminar experimento")
    print("3. Visualizar experimentos")
    print("4. Modificar experimento")
    print("5. Operaciones experimentos")
    print("6. Salir")
        
    ingreso= input("\nIngresa un numero de opcion: ")

    #Ingreso para registro de experimentos
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

    #Ingreso para eliminar experimentos
    if ingreso == "2":
        nombre_eliminar = input("\nIngrese el nombre del experimento a eliminar: ")
        eliminar_experimento(nombre_eliminar) 

    #Ingreso a visualizar experimentos registrados
    if ingreso == '3':
        visualizar_exp()     

    #Ingreso a modificar experimentos          
    if ingreso == '4':
        nomb_modificar = input('\nIngresa nombre del experimento a modificar: ')
        clave = input('Ingresa el parametro al cual le quieres cambiar el resultado: ')
        nuevo_valor = input('Ingresa el nuevo valor: ')
        modificar_experimento(lista_experimentos,nomb_modificar,clave,nuevo_valor)
        


#SUBMENU DE OPERACIONES***********************************************
    if ingreso == "5":
        while True:
            print("\nMenu operaciones: ")
            print("\n1. Promedio")
            print("2. Maximos y Minimos")
            print("3. Comparar")
            print("4. Volver menu principal")
        
            ingreso1= input("\nIngrese operacion: ")

# Salir del menú de operaciones
            if ingreso1 == '4':  
                 break  

#Ingreso para obtener los promedios
            if ingreso1 == '1':
                print('\nOpciones disponibles para calcular el promedio: ')
                print('1. Temperatura (°C)')
                print('2. Energía Liberada(kJ)')
                clave_opcion = input('\nIngresa la opcion de clave a promediar: ')
                if clave_opcion == '1':
                    clave1="Temperatura (°C)"
                elif clave_opcion == '2':
                    clave1 = "Energía Liberada(kJ)"
                else:
                    print('\nOpcion invalida.')
                    continue
                result = promedio(lista_experimentos,clave1)
                if result is not None:
                    print(f'\nEl resultado de {clave1} es: {result:.2f}')
                else:
                    print(f'\nNo hay datos numericos para {clave1}.')
                        


  # Opción de Mínimos y Máximos           
            if ingreso1 == '2': 
                print('\nOpciones disponibles para calcular mínimos y máximos: ')
                print('1. Temperatura (°C)')
                print('2. Energía Liberada(kJ)')
    
                clave_op = input('\nIngresa la opción de clave a analizar: ')
                if clave_op == '1':
                    clave2 = "Temperatura (°C)"
                elif clave_op == '2':
                    clave2 = "Energía Liberada(kJ)"
                else:
                    print('\nOpción inválida.')
                    continue

                min_exp, max_exp = obtener_min_max(lista_experimentos, clave2)

                if min_exp and max_exp:
                    print(f'\nEl experimento con menor {clave2} es: {min_exp["Nombre"]} ({min_exp[clave2]}).')
                    print(f'El experimento con mayor {clave2} es: {max_exp["Nombre"]} ({max_exp[clave2]}).')


# Comparar experimentos
            if ingreso1 == '3':  
                nombre1 = input("\nIngrese el nombre del primer experimento: ")
                nombre2 = input("Ingrese el nombre del segundo experimento: ")
                comparar_experimentos(lista_experimentos, nombre1, nombre2)



# Abandonar programa                        
    if ingreso == "6":
        print("\nHasta pronto, Adios!! ")
        break   


             
    
