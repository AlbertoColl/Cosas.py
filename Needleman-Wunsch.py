### Alineamiento de secuencias mediante programación dinámica (Needleman-Wunsch) ###

seq1 = input("Introduzca la primera secuencia para alinear:\n")
seq2 = input("Introduzca la segunda secuencia para alinear:\n")

# En primer lugar creamos una estructura de datos bidimensional a partir de las secuencias problema. Seq1 estará asociada a las columnas, y seq2 a las filas
columnas = len(seq1) + 1
filas = len(seq2) + 1
matriz = [[0 for x in range(0, filas)] for y in range(0, columnas)]

# En los siguientes bucles for se constuyen la primera fila y columna de la matriz, de manera que cada posición valga la anterior más la penalización por gap
gap = -1
for i in range(1,len(matriz)):
    matriz[i][0] = matriz[i-1][0] + gap
for j in range(1, len(matriz[0])):
    matriz[0][j] = matriz[0][j-1] + gap
    

# A continuación comenzamos la construcción de la matriz mediante un bucle anidado, y establecemos el criterio siguiente:
            ### matriz[i][j] = max( (matriz[i-1][j-1] + match), (matriz[i][j-1] + gap), (matriz[i-1][j] + gap)) ###
            # match vale 1 si las dos letras de la cadena en ese punto de la tabla coincide, y -1 si no lo hacen
            # gap es el valor de la penalización otorgada a la introducción de espacios
            
for i in range(1,len(matriz)):
    for j in range(1,len(matriz[i])):
        match = -1
        if seq1[i-1] == seq2[j-1]:
            match = 1
        matriz[i][j] = max((matriz[i-1][j-1] + match), (matriz[i-1][j] + gap), (matriz[i][j-1] + gap))            

print(matriz)

# Cuando se termine la construcción de la matriz, rastreo la solución óptima.

#Esto lo voy a hacer con otro bucle, que vaya cambiando sus coordenadas en la matriz a medida que rastree. A cada paso que de el bucle, guardará las letras
# de cada secuencia en dos strings distintos. Al final, habrá que invertir los strings, ya que empezamos desde el final y reconstruimos el proceso.

#En cada paso, el bucle deberá tener en cuenta matriz[i][j], matriz[i-1][j-1], matriz[i-1][j] y matriz[i][j-1]; además del valor de match.
# Cuando de los tres valores anteriores, el mayor sea el horizontal o vertical, se añadirá un gap a la secuencia correspondiente.
# Cuando los tres sean iguales y haya match, habrá una coincidencia y se añadirá la misma letra
# Cuando los tres valores sean iguales y no haya match, habrá una no coincidencia, y se añadirán letras distintas a cada cadena. No es necesario hacer un caso
# aparte, ya que en estos string no vamos a especificar si hay coincidencia o no.

alineamiento1 = ""
alineamiento2 = ""
i = len(matriz) - 1
j = len(matriz[0]) - 1
while i != 0 and j != 0:
    match = -1
    if seq1[i-1] == seq2[j-1]:
        match = 1
    if max((matriz[i-1][j-1] + match), (matriz[i-1][j] + gap), (matriz[i][j-1] + gap)) == (matriz[i-1][j-1] + match):
        alineamiento1 += seq1[i-1]
        alineamiento2 += seq2[j-1]
        i -= 1
        j -= 1       
            
    elif max((matriz[i-1][j-1] + match), (matriz[i-1][j] + gap), (matriz[i][j-1]) + gap) == (matriz[i][j-1] + gap):
        alineamiento1 += "-"
        alineamiento2 += seq2[j-1]
        j -= 1

    elif max((matriz[i-1][j-1] + match), (matriz[i-1][j] + gap), (matriz[i][j-1]) + gap) == (matriz[i-1][j] + gap):
        alineamiento1 += seq1[i-1]
        alineamiento2 += "-"
        i -= 1

print(alineamiento1[::-1])
print(alineamiento2[::-1])

#Próximo paso: obtener todos los alineamientos posibles para dos secuencias, ya que actualmente solo devuelve uno, por defecto el que más se ajusta a la diagonal

