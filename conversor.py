
def temperatura():
    pass
def distancia():
    pass
def massa():
    pass
def volume():
    pass
def velocidade():
    pass
def tempo():
    pass
def area():
    pass
def dados():
    pass
def moeda():
    pass
def energia():
    pass




while True:
    print("1 - Temperatura")
    print("2 - Distância")
    print("3 - Peso/Massa")
    print("4 - Volume")
    print("5 - Velocidade")
    print("6 - Tempo")
    print("7 - Área")
    print("8 - Dados Digitais")
    print("9 - Moeda")
    print("10 - Energia")
    print("0 - Sair")
    categoria = input("opção: ")

    if categoria == "1":
         temperatura()
    elif categoria == "2":
         distancia()
    elif categoria == "3":
         massa()
    elif categoria == "4":
        volume()
    elif categoria == "5":
        velocidade()
    elif categoria == "6":
        tempo()
    elif categoria == "7":
        area()
    elif categoria == "8":
        dados()
    elif categoria == "9":
        moeda()
    elif categoria == "10":
        energia()
    elif categoria == "0":
        print("ate logo!")
        break
        

    