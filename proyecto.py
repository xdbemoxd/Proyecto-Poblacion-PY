import lector_csv
import grafica

listo = False
while( not listo ):

    try:

        print('1.Poblacion Mundial\n2.Poblacion de un continente especifico')
        opcion = int(input('Ingrese la opcion: '))
        
        if opcion <= 0 or opcion > 2:

            print('\n\ningrese un numero relacionado con las opciones disponibles\n\n')

        else:

            listo = True

    except ValueError as error:
        print('\n\ningrese un entero\n\n')

datos = lector_csv.read_csv('./new_proyect/data.csv') 

def continente():

    lista_continentes =[ 'Africa', 'Asia', 'Europe','North America', 'South America', 'Oceania'] 
    
    listo = False

    while(not listo):

        try:

            print('1.Africa\n2.Asia\n3.Europe\n4.North America\n5.South America\n6.Oceania')
            opcion = int(input('Ingrese la opcion: '))

            if opcion <= 0 or opcion > 6:

                print('\n\ningrese un numero relacionado con las opciones disponibles\n\n')

            else:

                listo = True

        except ValueError as error:

            print('\n\ningrese un entero\n\n')

    return lista_continentes[opcion-1]

if opcion == 2:

    continente_var = continente()

    datos = list( filter(lambda item : item['Continent'] == continente_var, datos ) )

pais = []
poblacion = []

pais_mayor_poblacion_1 =''
poblacion_pais_1 = 0
pais_mayor_poblacion_2 =''
poblacion_pais_2 = 0
pais_mayor_poblacion_3 =''
poblacion_pais_3 = 0
poblacion_aux = 0
pais_aux =''
poblacion_total = 0

for row in datos:

    pais.append( row[ 'Country/Territory' ] )
    poblacion.append( int( row[ '2022 Population' ] ) )
    

    if poblacion_pais_1 < int( row[ '2022 Population' ] ):
        
        pais_aux = pais_mayor_poblacion_1
        poblacion_aux = poblacion_pais_1

        pais_mayor_poblacion_1 = row[ 'Country/Territory' ]
        poblacion_pais_1 = int( row[ '2022 Population' ] )

        poblacion_total += poblacion_pais_3

        pais_mayor_poblacion_3 = pais_mayor_poblacion_2
        poblacion_pais_3 = poblacion_pais_2

        pais_mayor_poblacion_2 = pais_aux
        poblacion_pais_2 = poblacion_aux
    
    elif poblacion_pais_2 < int( row[ '2022 Population' ] ) <= poblacion_pais_1:

        pais_aux = pais_mayor_poblacion_2
        poblacion_aux = poblacion_pais_2

        pais_mayor_poblacion_2 = row[ 'Country/Territory' ]
        poblacion_pais_2 = int( row[ '2022 Population' ] )

        poblacion_total += poblacion_pais_3

        pais_mayor_poblacion_3 = pais_aux
        poblacion_pais_3 = poblacion_aux
    
    elif poblacion_pais_3 < int( row[ '2022 Population' ] ) <= poblacion_pais_2:

        poblacion_total += poblacion_pais_3

        pais_mayor_poblacion_3 = row[ 'Country/Territory' ]
        poblacion_pais_3 = int( row[ '2022 Population' ] )

    else:
        poblacion_total += int( row[ '2022 Population' ] )

lista_pais_mayor = []
lista_poblacion_pais = []

lista_pais_mayor.append(pais_mayor_poblacion_1)
lista_pais_mayor.append(pais_mayor_poblacion_2)
lista_pais_mayor.append(pais_mayor_poblacion_3)
lista_pais_mayor.append('Otros')

lista_poblacion_pais.append(poblacion_pais_1)
lista_poblacion_pais.append(poblacion_pais_2)
lista_poblacion_pais.append(poblacion_pais_3)
lista_poblacion_pais.append(poblacion_total)

grafica.generatePieChart(pais,poblacion)

grafica.generatePieChart(lista_pais_mayor,lista_poblacion_pais)

#print(datos)