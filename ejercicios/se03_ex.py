def Exe06:

def Exe09:
    R = float(input('Inidique el Radio:'))
    CIR = math.pow(R, 2) * zpi
    print('área de un círculo %.3f ' % CIR)

def Exe10:
    R = int(input('Inidique un número:'))
    N = (R % 2)
    if N == 0:
        print('%d es par' % R)
    else:
        print('Impar, a %d, el resto es %d' % (R, N))

def Exe12:
    R = 0
    while R <= 10:
        R += 1
        print(R)
    vec = list(range(R))
    del vec[0]
    print(vec)
