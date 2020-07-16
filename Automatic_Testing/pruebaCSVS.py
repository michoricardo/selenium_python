import os
import csv
import time
wait = True
while(wait==True):
    for fname in os.listdir('C:/Users/ricar/Downloads'):
        if ('orders') in fname:
            print('se encontro un archivo csv <br>')
            time.sleep(1)
            with open('C:/Users/ricar/Downloads/orders.csv') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                folio_nuevo = None
                for row in readCSV:
                    foliocurrent = row[0]
                    if folio_nuevo == foliocurrent:
                        print(row[24],row[25])
                        print('<br>')
                        
                    elif folio_nuevo != foliocurrent:
                        print('*******************************************')
                        print('<br>')
                        print(row[0])
                        print('<br>')
                        print(row[24],row[25])
                    folio_nuevo = foliocurrent
        else:
            wait=False
print('archivos encontrados')
