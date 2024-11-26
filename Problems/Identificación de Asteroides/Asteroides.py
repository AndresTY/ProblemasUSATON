# def ordenar(grupos_asteroides):


def identificar_asteroides(cant, asteroides, verbose=False):
    grupos = dict() 
    for ast in asteroides:
        try :
            grupos[ast] += 1 
        except: 
            grupos[ast] = 1
    del(grupos[' '])

    if verbose: print(grupos)
    grupos = list(grupos.items())
    
    # https://docs.python.org/es/3/howto/sorting.html
    inter = sorted(grupos, key=lambda x: x[0])
    grupos_ordenados = sorted(inter, key=lambda x: x[1] , reverse=True)

    #print(grupos_ordenados)

    return grupos_ordenados[:cant] if cant <= len(grupos_ordenados) else grupos_ordenados


def main():
    """
    """
    verbose = False
    # leer el número de casos
    num_casos = int(input().strip())
    if verbose: print(num_casos)

    for caso in range(num_casos):
        # read the number of groups to identify
        grupos = int(input().strip())
        # read the list of elements
        elementos = input()

        if verbose: print(caso+1,"::",grupos,">> ", elementos)
        grupos_asteroides = identificar_asteroides(grupos,elementos,verbose)
        if verbose: print(grupos_asteroides, type(grupos_asteroides), grupos_asteroides[0], type(grupos_asteroides[0]))
        
        print(grupos_asteroides)


if __name__ == "__main__":
    main()