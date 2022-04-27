import numpy as np


def Ejemplo() :
    a = np.array([1, 2, 3])
    print('1D array: ')
    print(a)
    print()
    b = np.array('2D array: ')
    print(b)
    print()


def Unos():
    # Crear una matriz de unos - 3 filas 4 columnas
    uno = np.ones((3, 4))
    print(uno)
    print()


def Ceros():

    # Crear una matriz de ceros - 3 filas 4 columnas
    ceros = np.zeros((3, 4))
    print(ceros)
    print()


def Random():

    # Crear una matriz con valores aleatorios
    aleatorios = np.random.random((2, 2))
    print(aleatorios)
    print()


def Vacia():

    # Crear una matriz vac[ia
    vacia = np.empty((3, 2))
    print(vacia)
    print()


def Full():

    # Crear una matriz con un solo valor
    full = np.full((3, 3), 8)
    print(full)
    print()


def Espaciado():

    # Crear una matriz con valores espaciados uniformemente
    espacio1 = np.arange(0, 30, 5)
    print(espacio1)
    print()
    espacio2 = np.linspace(0, 2, 5)
    print(espacio2)
    print()


def MatrizIdentidad():

    # Crear una matriz identidad
    id1 = np.eye(4, 4)
    print(id1)
    print()

    id2 = np.identity(4)
    print(id2)
    print()


def InspeccionMatrices():

    # Conocer las dimensiones de una matriz
    a = np.array([(1, 2, 3), (4, 5, 6)])
    print(a.ndim)


def TipoDatoMatriz():

    # Conocer el tipo de los datos
    a = np.array([1, 2, 3])
    print(a.dtype)


def TamanoForma():

    # Conocer el tamaño y forma de la matriz
    a = np.array([(1, 2, 3, 4, 5, 6)])
    print(a.size)
    print(a.shape)


def CambioForma():

    # Cambio de forma de una matriz
    a = np.array([(8, 9, 10), (11, 12, 13)])
    print(a)
    a = a.reshape(3, 2)
    print(a)


def SeleccionElemento():
    # Extraer un solo valor de la matriz
    a = np.array([(1, 2, 3, 4), (3, 4, 5, 6)])
    print(a[0, 2])      # Extrae el valor ubicado en la fila 0 columna 2
    print(a[0:, 2])     # Extrae los valores de todas las filas a partir de la primera (fila 0)
                        # en la columna 2


def ValorMin():
    a = np.array([8, 4, 2])
    print(a.min())

def ValorMax():
    a = np.array([8, 4, 2])
    print(a.max())


def ValorSuma():
    a = np.array([8, 4, 2])
    print(a.sum())


def RaizCuadradaMatriz():
    # Calcular la raíz cuadrada y la desviación estándar
    a = np.array([(1, 2, 3), (3, 4, 5)])
    print(np.sqrt(a))
    print(np.std(a))


def SumaMatriz():
    # Calcular la suma de dos matrices
    x = np.array([(1, 2, 3), (3, 4, 5)])
    y = np.array([(1, 2, 3), (3, 4, 5)])
    print(x + y)

def RestaMatriz():
    # Calcular la resta de dos matrices
    x = np.array([(1, 2, 3), (3, 4, 5)])
    y = np.array([(1, 2, 3), (3, 4, 5)])
    print(x - y)


def MultiplicacionMatriz():
    # Calcular la multiplicacion de dos matrices
    x = np.array([(1, 2, 3), (3, 4, 5)])
    y = np.array([(1, 2, 3), (3, 4, 5)])
    print(x * y)


def DivisionMatriz():
    # Calcular la division de dos matrices
    x = np.array([(1, 2, 3), (3, 4, 5)])
    y = np.array([(1, 2, 3), (3, 4, 5)])
    print(x / y)

def MatrizAleatoria():
    # Encontrar numeros aleatorios

    # randint encontrar numeros aleatorios enteros
    x = np.random.randint(10)
    print(x)

    # Size, tamaño de la matriz
    x = np.random.randint(10, size=(5))
    print(x)

    # Matriz de ddiferentes tamaños
    x = np.random.randint(10, size=(5, 3))
    print(x)

    # Numeros aleatorios decimales
    x = np.random.rand(2, 2)
    print(x)

    # Ejercicio:
    # Cree dos matrices de dos dimensiones, con valores aleatorios del 0 al 50 enteros
    # El tamaño de las matrices debe ser 3 por 3
    # Imprimir las matrices y luego imprimir el máximo de la primera matriz y el minimo de la segunda


def Ejercicio1Resuelto():
    x = np.random.randint(50, size=(3, 3))
    y = np.random.randint(50, size=(3, 3))
    print(x)
    print(y)
    print(x.max())
    print(y.min())

def ExtraerValorMatriz():
    # La función choicer permite extraer un número aleatorio que se encuentre dentro de la matriz
    x = np.random.choice([3, 5, 9, 5, 1])
    print(x)

    # Con la función size, se crea una matriz del tamaño x, y que utilice los numeros de la función choice
    x = np.random.choice([3, 5, 9, 5, 1], size=(2, 3))
    print(x)


# Ejercicio Probabilidad

def Ejercicio2():
    # m = np.random.choice([2, 4, 6], p=[0.5, 0.5, 0.0], size=(1))
    # print(m)

    x = np.random.choice([4, 2, 8, 10], p=[0.3, 0.2, 0.2, 0.3], size=[50])
    print(x)

    # Los dados tienen seis caras, si nos preguntamos ¿Cuál es la probabilidad de obtener un número par?
    # el espacio muestral es EspMues = {1, 2, 3, 4, 5, 6}
    # Espacio muestral evento(pares) = {2, 4, 6}
    # La probabilidad es igual al espacio muestral / espacio muestral evento
    # 1/2 para este caso = 0.5

    x = np.random.choice([2, 4, 6], p=[0.3, 0.3, 0.4], size=[6])
    print(x)


def ConcatenacionMatrices():

    # Concatena matrices

    m1 = np.array([[1, 2], [1, 2], [1, 2]])
    m2 = np.array([[8, 9], [8, 9], [8, 9]])
    print(m1)
    print("")
    print(m2)
    print("")
    print(np.concatenate([m1, m2], axis=1))














