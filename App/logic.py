import csv
csv.field_size_limit(2147483647)
import time
from DataStructures.List import array_list as ar

def new_logic():
    catalog = {'elements': ar.new_list()
               
        }
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    input_file = csv.DictReader(open(filename, encoding = 'uft-8'))
    annio_mayor = 0
    annio_menor = 0
    for index, element in enumerate(input_file ):
        if index == 0:
            annio_mayor = input_file[index]['year_collection']
            annio_menor = input_file[index]['year_collection']
        ar.add_last(catalog['elements'], element)
        if input_file[index]['year_collection']> annio_mayor:
            annio_mayor = input_file[index]['year_collection']
        if input_file[index]['year_collection'] < annio_menor:
            annio_menor = input_file[index]['year_collection']
    return catalog, annio_menor,annio_mayor
    # TODO: Realizar la carga de datos
    pass

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog, year):
    """
    Retorna el resultado del requerimiento 1
    """
    
    for element in catalog:
        if element['year_collection'] == year:
            pass
        
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
