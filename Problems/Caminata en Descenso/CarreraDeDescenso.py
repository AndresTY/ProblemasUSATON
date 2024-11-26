#!/bin/python3

def darAscensoCorredor(pX, pY, geo, verbose=False):
    """
    """
    ruta = [geo[pX][pY]]
    cend =False
    nX1, nY1 = pX, pY
    visited = [(nX1,nY1)]
    while not cend:
        x1N = nX1
        y1N = nY1 - 1 if nY1 - 1 >= 0 else nY1
        x1E = nX1 - 1 if nX1 - 1 >= 0 else nX1
        y1E = nY1
        x1S = nX1
        y1S = nY1 + 1 if nY1 + 1 < len(geo) else nY1
        x1W = nX1 + 1 if nX1 + 1 < len(geo) else nX1
        y1W = nY1
        
        act = False

        if (x1W,y1W) not in visited and geo[x1W][y1W] <= geo[nX1][nY1]:
            nX1, nY1 = x1W, y1W
            act = True

        if (x1S,y1S) not in visited and geo[x1S][y1S] <= geo[nX1][nY1]:
            nX1, nY1 = x1S, y1S
            act = True
        
        if (x1E,y1E) not in visited and geo[x1E][y1E] <= geo[nX1][nY1]:
            nX1, nY1 = x1E, y1E
            act = True

        if (x1N,y1N) not in visited and geo[x1N][y1N] <= geo[nX1][nY1]:
            nX1, nY1 = x1N, y1N
            act = True

        # No encontro un minimo en los 4 adyacentes
        if not act: 
            if (x1W,y1N) not in visited and geo[x1W][y1N] <= geo[nX1][nY1]:
                nX1, nY1 = x1W, y1N
                act = True

            if (x1W,y1S) not in visited and geo[x1W][y1S] <= geo[nX1][nY1]:
                nX1, nY1 = x1W, y1S
                act = True
        
            if (x1E,y1S) not in visited and geo[x1E][y1S] <= geo[nX1][nY1]:
                nX1, nY1 = x1E, y1S
                act = True

            if (x1E,y1N) not in visited and geo[x1E][y1N] <= geo[nX1][nY1]:
                nX1, nY1 = x1E, y1N
                act = True
        
        if verbose : print(nX1, nY1)

        if not act :
            cend = True
        else:
            ruta.append(geo[nX1][nY1])
            visited.append((nX1,nY1))
            if verbose :
                print(ruta)
                
    return ruta


def ascendingCompetence(c1, c2, c3, geography, verbose=False):
    """
    """
    x1, y1 = int(c1[0]), int(c1[1])
    x2, y2 = int(c2[0]), int(c2[1])
    x3, y3 = int(c3[0]), int(c3[1])
    if verbose :
        print("Corredora 1 inicia en (", x1, y1, ")")
        print("Corredora 2 inicia en (", x2, y2, ")")
        print("Corredora 3 inicia en (", x3, y3, ")")

    # rutaC1 = darDescensoCorredor(x1, y1, geography,verbose)
    # rutaC2 = darDescensoCorredor(x2, y2, geography,verbose)
    # rutaC3 = darDescensoCorredor(x3, y3, geography,verbose)
    rutaC1 = darAscensoCorredor(x1, y1, geography)
    rutaC2 = darAscensoCorredor(x2, y2, geography)
    rutaC3 = darAscensoCorredor(x3, y3, geography)
    if verbose:
        print("Ruta C1 >>",rutaC1)
        print("Ruta C2 >>",rutaC2)
        print("Ruta C3 >>",rutaC3)
    
    c1f = (rutaC1[-1] == 0)
    c2f = (rutaC2[-1] == 0)
    c3f = (rutaC3[-1] == 0)

    c1lg = len(rutaC1)
    c2lg = len(rutaC2)
    c3lg = len(rutaC3)

    if c1f and c2f and c3f: # Si los tres terminan, revisar la ruta mas corta
        if c1lg <= c2lg and c1lg <= c3lg:
            return rutaC1
        elif c2lg <= c1lg and c2lg <= c3lg:
            return rutaC2
        else:
            return rutaC3
        
    elif c1f and c2f and not c3f : # Si c1 y c2 terminan, revisar la ruta mas corta
        if c1lg <= c2lg :
            return rutaC1
        else:
            return rutaC2
        
    elif c1f and c3f and not c2f : # Si c1 y c3 terminan, revisar la ruta mas corta
        if c1lg <= c3lg :
            return rutaC1
        else:
            return rutaC3
    
    elif c2f and c3f and not c1f : # Si c2 y c3 terminan, revisar la ruta mas corta
        if c2lg <= c3lg :
            return rutaC2
        else:
            return rutaC3
    elif c1f: # solo termina C1
        return rutaC1
    elif c2f: # solo termina C2
        return rutaC2
    elif c3f: # solo termina C3
        return rutaC3
    
    return list()

    
def main( ):
    # linea 1 numero de casos
    linea = input().strip()
    numcasos = int(linea)
    # print(numcasos)

    for caso in range(numcasos):
        # linea 2 longitud del terreno
        linea = input().strip()
        largo = int(linea)
        # linea 3 posiciones de inicio competidores
        linea = input().strip()
        coords = linea.strip().split(" ")
        # print("\t",coords)
        # las siguientes n lineas contienen el mapa de ascenso
        mapa = list()
        for fi in range(largo):
            linea = input().strip()
            fila = [int(x) for x in linea.strip().split(" ")]
            mapa.append(fila)
            # print("\t",fila)
        
        # ascenso
        result = ascendingCompetence(coords[0:2], coords[2:4], coords[4:], mapa)
        # strResult = str(result)[1:-1]
        # strResult = strResult.replace(',','')
        # print(result, type(result),strResult, type(strResult))
        print((' '.join(map(str, result))).strip())
        # print((' '.join(map(str, result))))


if __name__ == '__main__':
    main()
    