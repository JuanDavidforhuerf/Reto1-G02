import sys
import os
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
import App.logic as logic
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    """
        Se crea una instancia del controlador
    """
    dev = logic.new_logic()
    return dev
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    pass

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    name = input("ingrese el numero del porcentaje de datos que desea cargar + .csv ")
    filename = data_dir + "agricultural-"+name
    dev,menor, mayor = logic.load_data(control,filename)
    it = -1
    print("Número total de registros: "+ str(dev['elements']['size']))
    print("Menor año de recolección de registro: " + str(menor))
    print("Mayor año de recolección de registro: " + str(mayor))
    print(" ")
    print("Primeras cinco(5) recopilaciones:")
    for index in range(5):
        print(str(index+1))
        print("año de recolección del registro: " + str(dev['elements']['elements'][index]['year_collection']))
        print('Fecha de carga del registro: '+ dev['elements']['elements'][index]['load_time'])
        print('Departamento de registro: '+ dev['elements']['elements'][index]['state_name'] )
        print('Origen del registro: '+ dev['elements']['elements'][index]['source'] )
        print('Unidad de medida del registro: '+ str(dev['elements']['elements'][index]['unit_measurement']))
        print('Valor de la medicion del registro: '+ str(dev['elements']['elements'][index]['value']))
    print(" ")
    print("Ultimas cinco(5) recopilaciones:")
    while it > -5:
        print(str(it*-1))
        print("año de recolección del registro: " + str(dev['elements']['elements'][it]['year_collection']))
        print('Fecha de carga del registro: '+ dev['elements']['elements'][it]['load_time'])
        print('Departamento de registro: '+ dev['elements']['elements'][it]['state_name'] )
        print('Origen del registro: '+ dev['elements']['elements'][it]['source'] )
        print('Unidad de medida del registro: '+ str(dev['elements']['elements'][it]['unit_measurement']))
        print('Valor de la medicion del registro: '+ str(dev['elements']['elements'][it]['value']))
        it -=1
    
    #TODO: Realizar la carga de datos
    


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
