import numpy as np  # Importar la biblioteca numpy para generar números aleatorios
import matplotlib.pyplot as plt  # Importar la biblioteca matplotlib para graficar

# Definir una función para simular una máquina de Galton
def simular_galton(num_canicas, num_niveles):
    # Crear una lista para almacenar la cantidad de canicas en cada contenedor
    contadores = [0] * (num_niveles + 1)
    
    # Iterar sobre cada canica
    for _ in range(num_canicas):
        pos = 0  # Iniciar en el nivel más bajo
        # Iterar sobre cada nivel de la máquina de Galton
        for _ in range(num_niveles):
            # Decidir si la canica cae hacia la izquierda o la derecha
            if np.random.randint(0, 2) == 1:
                pos += 1  # Mover la canica hacia la derecha
        contadores[pos] += 1  # Incrementar el contador del contenedor donde termina la canica
    return contadores  # Devolver la lista de contadores de canicas en cada contenedor

# Definir una función para graficar un histograma de los resultados
def graficar_histograma(resultados):
    # Crear un histograma de barras con los resultados
    plt.bar(range(len(resultados)), resultados, color='skyblue')
    plt.xlabel('Contenedores')  # Etiqueta del eje x
    plt.ylabel('Cantidad de canicas')  # Etiqueta del eje y
    plt.title('Simulación de máquina de Galton')  # Título del gráfico
    plt.show()  # Mostrar el gráfico

# Parámetros de la simulación
num_canicas = 3000  # Número total de canicas
num_niveles = 12  # Número de niveles de la máquina de Galton

# Simular la máquina de Galton
resultados = simular_galton(num_canicas, num_niveles)

# Graficar el histograma de los resultados
graficar_histograma(resultados)
