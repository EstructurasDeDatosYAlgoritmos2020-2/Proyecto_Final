"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import mapentry as me

from DISClib.DataStructures import listiterator as it
from DISClib.DataStructures import edge as e


from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Sorting import mergesort as mg

from DISClib.Utils import error as error 
assert config   

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

def newAnalyzer():
    """ Inicializa el analizador.
    """
    try:
        analyzer = {
                    'Companies_Map': None,
                    '': None,
                    'Num_Of_Total_Trips': None,
                    }

        analyzer['Companies_Map'] = m.newMap(numelements=100,
                                            maptype='CHAINING',
                                            loadfactor=0.5,
                                            comparefunction=CompareCompanies)

        analyzer['Num_Total_Cabs'] = 0

        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')


# ==============================
# Funciones para agregar informacion al grafo
# ==============================

def AddCabTrip(catalog,trip):
    """
    """
    addCompany(catalog,trip)

def addCompany(catalog,trip):
    """
    """

    company = trip['company']
    entry = m.get(catalog['Companies_Map'],company)

    if entry is None:
        company_entry = NewCompanyEntry()
        m.put(catalog['Companies_Map'],company,company_entry)
    else:
        company_entry = me.getValue(entry)
    
    company_entry['NumServices'] += 1

    taxi_entry = m.get(company_entry['Taxis'],trip['taxi_id'])
    if taxi_entry is None:
        m.put(company_entry['Taxis'],trip['taxi_id'],None)

        company_entry['NumCabs'] += 1
        catalog['Num_Total_Cabs'] += 1
        

def addNumTripsToTotal(catalog,numFileTrips):
    """
    Calcula el total de viajes en Taxi realizados.
    """
    citibike['Num_Of_Total_Trips'] = citibike['Num_Of_Total_Trips'] + numFileTrips



def NewCompanyEntry():
    """
    """
    entry = {'NumCabs':0,'NumServices':0, 'Taxis':None}
    entry['Taxis'] = m.newMap(numelements=100,
                            maptype='CHAINING',
                            comparefunction=compareTaxisIDS)
    return entry

# ==============================
# Funciones de consulta requisitos
# ==============================

def CompaniesInfo(analyzer,criteria1,criteria2):
    """
    Proyecto Final | Req 1
    Retorna:
        Número total de taxis reportados.
        Número total de compañías.
        TOP X compañías con más taxis afiliados.
        TOP Y compañías con más servicios prestados.
    """

    companies_lt = m.keySet(analyzer['Companies_Map'])
    num_companies = lt.size(companies_lt)

    moreCabs = lt.newList(datastructure='ARRAY_LIST',cmpfunction=None)
    moreServices = lt.newList(datastructure='ARRAY_LIST',cmpfunction=None)

    iterator = it.newIterator(companies_lt)
    while it.hasNext(iterator):
        company_name  = it.next(iterator)
        company = m.get(citibike['Companies_Map'],company_name)

        lt.addLast(moreCabs,company)
        lt.addLast(moreServices,company)

    mg.mergesort(arrival_lt_sorted,greaterNumCabs)
    mg.mergesort(departure_lt_sorted,greaterNumServices)

    TOPNumCabs = lt.subList(moreCabs,1,criteria1)
    TOPNumServices = lt.subList(moreServices(criteria2))

    return catalog['Num_Total_Cabs'] , num_companies , TOPNumCabs , TOPNumServices




# ==============================
# Funciones de consulta generales
# ==============================



# ==============================
# Funciones Helper
# ==============================

def greaterNumCabs(elem1,elem2):
    """
    Proyecto Final | Req 1
    Función de comparación para el método MergeSort.   
    """
    return int(elem1['value']['NumCabs']) > int(elem2['value']['NumCabs'])

def greaterNumServices(elem1,elem2):
    """
    Proyecto Final | Req 1
    Función de comparación para el método MergeSort.   
    """
    return int(elem1['value']['NumServices']) > int(elem2['value']['NumServices'])

# ==============================
# Funciones de Comparacion
# ==============================


def compareTaxisIDS(Id1,Id2):
    """
    Función de comparación utilizada en:
        Mapa de Compañias.
    """
    
    if (Id1 == Id2):
        return 0
    elif (Id1 > Id2):
        return 1
    else:
        return -1

def CompareCompanies(comp1,comp2):
    """
    Función de comparación utilizada en:
        Mapa de Compañias.
    """
    value1 = comp1['key']
    value2 = comp2['key']
    
    if (value1 == value2):
        return 0
    elif (value1 > value2):
        return 1
    else:
        return -1