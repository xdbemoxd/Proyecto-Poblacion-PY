import csv

def read_csv(path):
    with open(path, 'r') as csv_file:
       reader = csv.reader(csv_file, delimiter=',') 
       header = next(reader)
       datos  = []
       for row in reader:
        diccionario = {head : data for (head,data) in zip(header,row) }
        datos.append(diccionario)
        
       return datos