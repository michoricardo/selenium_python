
segundos=float(input("introduce los segundos: "))

def durationToMin(duracionSegundos):
    mins=0
    while duracionSegundos >60.0 or duracionSegundos==60:
        print("segundos antes de  dividir: ",duracionSegundos)
        duracionSegundos=duracionSegundos-60
        print("segundos restantes",duracionSegundos)
        mins=mins+1
        if duracionSegundos<60:
            restante=duracionSegundos
            print("El restante es: ",restante)
            break
    minsCalc=mins
    secCalc=restante
    #print("Se calcularon: ", minsCalc, "minutos con ", secCalc, "segundos")
    return "Se calcularon: ", minsCalc, "minutos con ", secCalc, "segundos"

print(durationToMin(segundos))
