import random

def sprawdzRuch(ruch):
    option = ['p', 'k', 'n']
    ruchPC = random.choice(option)
    print(ruchPC)
    if ruch == ruchPC:
        return 0
    elif (ruch == 'p' and ruchPC == 'k' or
         ruch == 'k' and ruchPC == 'n' or
         ruch == 'n' and ruchPC == 'p'):
         return 1
    else:
        return -1;


liczbaRund = -1
while liczbaRund <= 0:
    try:
        liczbaRund = int(input("Podaj liczbe rund: "))
        if liczbaRund <=0:
            print("Wartosc musi byc wieksza od 0")
    except:
        print("Podana wartosc nie jest typu integer")

wygranePC = 0
wygraneGracz = 0
remis = 0
okRuch = True
option = ['p', 'k', 'n']

for i in range(0,liczbaRund):
    while okRuch:
        ruch =  input("Twoj ruch: ")
        if (ruch == 'p' or ruch == 'k' or ruch =='n'):
            wynikRundy = sprawdzRuch(ruch)
            okRuch = False
        else:
            print("Podales zla wartosc ruchu")
    okRuch = True
    if wynikRundy == -1:
        wygranePC +=1
    elif wynikRundy == 1:
        wygraneGracz +=1
    else:
        remis  += 1

print("Wygrane Gracza: ", wygraneGracz)
print("Wygrane PC: ", wygranePC)
print("Remisy: ", remis)

