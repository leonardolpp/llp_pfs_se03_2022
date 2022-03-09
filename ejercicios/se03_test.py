import math

def CuentAtras(num):
    while num > 0:
        print(num)
        num -= 1
    print('BoooOOOM !!!')

def CuentAtrasR(num):
    # AHORA RECURSIVA
    num -= 1
    if num > 0:
        print(num)
        CuentAtrasR(num)
        return False
    else:
        print('\t BoooOOOM !!!')
    print('\t Fin CuentAtras() recursiva ', num)

def NumeroPrimo(nump):
    if nump <= 3:
        print('Es primo: ', nump)
    elif nump == 0:
        print('es cero: ', nump)
    elif nump % 2 == 0:
        print('No es primo, es par: ', nump)
    else:
        i = 3
        # j = int(nump / 2)
        j = int(math.sqrt(nump))
        while i <= j:
            if nump % i == 0:
                print('*** %d NO es primo, divisible entre: %d (evaluado hasta: %d)' % (nump, i, j))
                return
            else:
                i += 2
        print('es primo %d (%d)' % (nump, i))

def NumeroPrimoR(numq, k=2):
    # Funcion Recursiva --> LLEGA HASTA 992 LLAMADAS
    # Para ampliarlo: sys.setrecursionlimit(n)
    # if k > (numq / 2):
    itera = int(math.sqrt(numq))
    # if itera >= 992:
    #     print('Func.Recursiva No lo puede calcular: %d llamadas' % itera)
    #     return True
    if k > itera:
        print('es primo %d (%d)' % (numq, k))
        return True
    elif numq % k == 0:
        print('%d NO es primo, divisible entre: %d' % (numq, k) )
        return False
    else:
        # print('\t call: ', k + 1 )
        return NumeroPrimoR(numq, k + 1)

if __name__ == '__main__':
    # fruits = ["Apple", "Apricot", "Avocado", "Banana"
    #     , "Bilberry", "Blackberry", "Blackcurrant", "Coconut"
    #     , "Crab apple", "Cranberry", "Currant"]
    # for x in fruits:
    #     print(x)
    #     if x == "Banana":
    #         break
    # CuentAtras(3)
    CuentAtrasR(5)
    X = 792999901
    NumeroPrimo(X)
    NumeroPrimoR(X)
