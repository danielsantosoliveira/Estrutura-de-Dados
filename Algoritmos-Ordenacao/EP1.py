from random import shuffle
from time import time

amostra = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000, 22000]

#>> início seleção;
def selecao(l):
    r = []
    while l:
        m = min(l)
        r.append(m)
        l.remove(m)
    return r
# fim seleção>>;

#>> início mergesort;
def mergesort(l):
    if len(l) <= 1: return l
    else:
        m = len(l) // 2
        e = mergesort(l[:m])
        d = mergesort(l[m:])
        return merge(e, d)

def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r
# fim mergesort>>;

#>> início quicksort;
def quicksort(l):
    if len(l) <= 1: return l    
    pivô = l[0]
    iguais  = [x for x in l if x == pivô]
    menores = [x for x in l if x <  pivô]
    maiores = [x for x in l if x >  pivô]
    return quicksort(menores) + iguais + quicksort(maiores)
# fim quicksort>>;

#>> início native;
def native(l):
    return sorted(l)
# fim native>>;

def returnLista(n):
    v = list(range(n))
    shuffle(v)
    return v

def returnTime(algoritmo, lista):
    t1 = time()
    algoritmo(lista)
    t2 = time()
    return round(t2-t1, 2)

print(f"\n\t\tComparação | Algoritmos de Ordenação")
print(f"\tSeleção\t|  Mergesort\t|  Quicksort    |  Native")
print ('-'*65)
for amo in amostra:
    print(f'{amo} |\t{returnTime(selecao, returnLista(amo))}\t|\t{returnTime(mergesort, returnLista(amo))}\t|\t{returnTime(quicksort, returnLista(amo))}\t|\t{returnTime(native, returnLista(amo))}')
    print ('-'*65)
    


