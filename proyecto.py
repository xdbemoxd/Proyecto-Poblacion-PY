import lector_csv
import grafica

datos = lector_csv.read_csv('./new_proyect/data.csv') 

#datos = list( filter(lambda item : item['Continent'] == 'Europe', datos ) )

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