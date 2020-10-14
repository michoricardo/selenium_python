with open('pedidosJaliscoMAYOOCT2020.txt') as file:  
    data = file.readlines() 
    for line in data:
       qty=line[2:4]
       trim=qty.strip(']')
       print(trim)
    for line in data:
       rest=line[4:]
       rest.strip(']')
       print(rest)

    
