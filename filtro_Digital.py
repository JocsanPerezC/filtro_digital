#   Nombre: Kenda Corrales Porras 
#   Carnet: 2023800000
#   Filtro digital de imagenes

#   --- Manual de Usuario ---

#   - Al momento de iniciar este codigo se nos van a dar 3 opciones, ver una imagen, filtrar una imagen o salir.
    
#   - Para ver una imagen, ingresamos el numero 1, luego se nos va a pedir la ruta donde contenemos la imagen
#   un ejemplo de una ruta puede ser: C:\Users\Admin\OneDrive - Estudiantes ITCR\Escritorio\trabajo\nombre_de_la_imagen.jpg
#   De esta manera podemos apreciar la imagen deseada.

#   - Para filtrar una imagen, ingresamos el numero 2, luego se nos va a pedir la ruta donde contenemos la imagen
#   un ejemplo de una ruta puede ser: C:\Users\Admin\OneDrive - Estudiantes ITCR\Escritorio\trabajo\nombre_de_la_imagen.jpg

#   Luego nos piden dos valores, ingresar el tamaño de la dimensión de la ventana, ya sea un 3 para 3x3
#   Luego nos piden ingresar el tipo de ordenamiento deseado, 1.Bubblesort 2.Insertion Sort 3.Selection Sort 4.Merge Sort
#   Entonces ingresamos el numero y luego de esto se hace el proceso

#   Una vez finalizado, se nos muestra el tiempo y la imagen, para posteriormente nos piden ingresar la ruta y el nombre de la imagen
#   donde queremos guardarla, un ejemplo seria: C:\Users\Admin\OneDrive - Estudiantes ITCR\Escritorio\trabajo\nombre_de_la_imagen.jpg
#   Luego de esto la imagen queda guardada en esa carpeta.


# -- Ejemplos rapidos de las rutas que podemos usar para las imágenes
# C:\Users\Admin\OneDrive - Estudiantes ITCR\Escritorio\trabajo\nombre_de_la_imagen.jpg
# C:\Users\Admin\OneDrive - Estudiantes ITCR\Escritorio\trabajo\perry.jpg
# C:\Users\Admin\OneDrive - Estudiantes ITCR\Escritorio\trabajo\charlie_snoopy.jpg

# -- Ejemplos rapidos de la ruta para guardar una imagen
# C:\Users\Admin\OneDrive - Estudiantes ITCR\Escritorio\trabajo\nombre_de_la_imagen.jpg
# C:\Users\Admin\OneDrive - Estudiantes ITCR\Escritorio\trabajo\perry_3x3_merge.jpg

import imageio
import matplotlib.pyplot as plt
import time


# == Algoritmos de Ordenamiento ==
"""
    Detalles de Funcionamiento:
    - Recorre la lista varias veces.
    - En cada iteración, compara elementos adyacentes y los intercambia si están en el orden incorrecto.
    - Después de cada iteración, el elemento más grande "burbujea" hasta la posición correcta.
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

"""
    Detalles de Funcionamiento:
    - Divide la lista en una parte ordenada y una parte desordenada.
    - Toma cada elemento de la parte desordenada e inserta en su posición correcta dentro de la parte ordenada.
    - Itera hacia atrás para encontrar la posición correcta de inserción.
"""
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

"""
    Detalles de Funcionamiento:
    - Divide la lista en una parte ordenada y una parte desordenada.
    - Encuentra el elemento mínimo en la parte desordenada y lo coloca al principio de la parte ordenada.
    - Repite este proceso hasta que toda la lista esté ordenada.
"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


"""
    Detalles de Funcionamiento:
    - Divide la lista en mitades hasta que cada sublista tenga un solo elemento.
    - Fusiona las sublistas en orden combinando las partes ordenadas.
    - Utiliza una estrategia de "divide y conquista" para ordenar eficientemente la lista.
"""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


"""
    La siguiente funcion aplica un filtro de mediana a una imagen en escala de grises.
    Este tipo de filtro se utiliza comúnmente en procesamiento de imágenes para reducir el ruido impulsivo o aleatorio, 
    como el ruido sal y pimienta.

    imagen: Es la imagen de entrada sobre la cual se aplicará el filtro de mediana. 
    Debe estar representada como una lista de listas donde cada elemento representa el valor de intensidad de un píxel en escala de grises.
    tamano_ventana: Especifica el tamaño de la ventana que se utilizará para calcular la mediana alrededor de cada píxel. 
    Por ejemplo, un tamaño de ventana de 3 indica una ventana de 3x3 píxeles alrededor de cada píxel.
    tipo_ordenamiento: el algoritmo de ordenamiento que se va a usar

    Detalles de Funcionamiento:
    - La función recorre cada píxel de la imagen.
    - Define una ventana alrededor de cada píxel según el tamaño especificado.
    - Extrae los valores de intensidad de los píxeles dentro de la ventana.
    - Utiliza el tipo de ordenamiento seleccionado para ordenar estos valores.
    - Asigna el valor mediano de los píxeles ordenados a la imagen filtrada.
"""
# == Funcion para aplicar el filtro de mediana a la imagen ==
def filtro_mediana(imagen, tamano_ventana, tipo_ordenamiento):

    # Dimensiones de la imagen
    alto = len(imagen)
    ancho = len(imagen[0])
    
    # Tamaño de la ventana
    mitad_ventana = tamano_ventana // 2
    
    # Crear una lista vacía para contener la imagen filtrada
    imagen_filtrada = []
    # Es una matriz bidimensional (imagen_filtrada) donde cada elemento inicialmente es 0, y tiene alto filas y ancho columnas, 
    # lo que representa una imagen filtrada inicial con el mismo tamaño que la imagen original pero inicializada con valores de píxeles en negro (0 en escala de grises). 
    # Esta matriz se utilizará para almacenar los valores de píxeles filtrados después de aplicar el filtro de mediana.

    # Iterar a lo largo de las filas (alto)
    for y in range(alto):
        # Crear una lista vacía para la fila actual de la imagen filtrada
        fila_filtrada = []
        
        # Iterar a lo largo de las columnas (ancho)
        for x in range(ancho):
            # Agregar un valor inicial de 0 para cada píxel en la fila actual
            fila_filtrada.append(0)
        
        # Agregar la fila completa a la imagen filtrada
        imagen_filtrada.append(fila_filtrada)

    
    # Para cada píxel (y, x) en la imagen, se define una ventana alrededor de este píxel utilizando dos bucles for adicionales (j y i) 
    # que recorren los índices necesarios para formar una ventana del tamaño tamano_ventana alrededor del píxel actual.
    # Dentro de estos bucles, se calculan las coordenadas (yy, xx) del píxel en la ventana asegurándose de no salirse de los límites de la imagen.
    # Se agrega el valor del píxel imagen[yy][xx] a la lista valores, que contendrá todos los valores de intensidad de los píxeles dentro de la ventana.
    for y in range(alto):
        for x in range(ancho):
            # Definir la ventana alrededor del píxel actual
            valores = []
            for j in range(-mitad_ventana, mitad_ventana + 1):
                for i in range(-mitad_ventana, mitad_ventana + 1):
                    # Coordenadas del píxel en la ventana
                    yy = max(0, min(y + j, alto - 1))
                    xx = max(0, min(x + i, ancho - 1))
                    
                    # Agregar el valor del píxel al listado
                    valores.append(imagen[yy][xx])
            
            # Ordenar los valores utilizando el tipo de ordenamiento seleccionado
            if tipo_ordenamiento == 'bubblesort':
                bubble_sort(valores)
            elif tipo_ordenamiento == 'insertion_sort':
                insertion_sort(valores)
            elif tipo_ordenamiento == 'selection_sort':
                selection_sort(valores)
            elif tipo_ordenamiento == 'merge_sort':
                merge_sort(valores)
            
            # Una vez que los valores están ordenados, se selecciona el valor mediano de la lista de valores. 
            # El valor mediano se encuentra en la posición len(valores) // 2 después de ordenar la lista.
            valor_mediano = valores[len(valores) // 2]
            
            # Asignar el valor mediano a la imagen filtrada
            # El valor mediano seleccionado se asigna al píxel correspondiente en la imagen filtrada 
            imagen_filtrada[y][x] = valor_mediano
    
    return imagen_filtrada

# == Funcion para mostrar la imagen ==
def mostrar_imagen(imagen, titulo):
    # Mostrar la imagen en escala de grises
    plt.imshow(imagen, cmap='gray')
    plt.title(titulo)
    plt.axis('off')
    plt.show()

# == Funcion para ver el menu constantemente hasta que el usuario indique lo contrario ==
def menu():
    while True:
        print("\n-- Filtro Digital --")
        print("1. Ver Imagen")
        print("2. Aplicar Filtro")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        # Opción: Ver imagen
        if opcion == '1':
            
            ruta_imagen = input("Ingrese la ruta y el nombre de la imagen a visualizar: ")
            try:
                imagen = imageio.imread(ruta_imagen, pilmode='L')
                mostrar_imagen(imagen, "Imagen Encontrada")
            except FileNotFoundError:
                print("Error: Archivo no encontrado. Verifique la ruta e inténtelo de nuevo.")
        
        # Opción: Aplicar filtro
        elif opcion == '2': 
            ruta_imagen = input("Ingrese la ruta y el nombre de la imagen a filtrar: ")
            try:
                imagen = imageio.imread(ruta_imagen, pilmode='L')
                mostrar_imagen(imagen, "Imagen Original")
                
                # Pedir al usuario el tamaño de la ventana para el filtro de mediana
                print("\nTamaños para la ventana:")
                print("3. para 3x3")
                print("5. para 5x5")
                print("7. para 7x7")
                tamano_ventana = int(input("Ingrese el numero del tamaño que desea: "))
                
                # Pedir al usuario el tipo de ordenamiento a utilizar
                print("\nSeleccione el tipo de ordenamiento:")
                print("1. Bubblesort")
                print("2. Insertion Sort")
                print("3. Selection Sort")
                print("4. Merge Sort")
                tipo_ordenamiento = input("Ingrese el número correspondiente al tipo de ordenamiento: ")
                
                if tipo_ordenamiento == '1':
                    tipo_ordenamiento = 'bubblesort'
                elif tipo_ordenamiento == '2':
                    tipo_ordenamiento = 'insertion_sort'
                elif tipo_ordenamiento == '3':
                    tipo_ordenamiento = 'selection_sort'
                elif tipo_ordenamiento == '4':
                    tipo_ordenamiento = 'merge_sort'
                else:
                    print("Tipo de ordenamiento inválido. Se utilizará bubblesort por defecto.")
                    tipo_ordenamiento = 'bubblesort'
                
                # Medir tiempo de ejecución del filtrado
                tiempo_inicio = time.time()
                imagen_filtrada = filtro_mediana(imagen.tolist(), tamano_ventana, tipo_ordenamiento)
                tiempo_fin = time.time()
                
                # Calcular tiempo de ejecución en milisegundos
                tiempo_ejecucion = (tiempo_fin - tiempo_inicio) * 1000
                print(f"Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")
                
                # Mostrar la imagen filtrada
                mostrar_imagen(imagen_filtrada, "Imagen Filtrada")
                
                # Guardar la imagen filtrada
                ruta_salida = input("Ingrese la ruta junto con el nombre de la imagen y la extension donde desea guardar la imagen filtrada: ")
                imageio.imwrite(ruta_salida, imagen_filtrada)
                print(f"Imagen filtrada guardada en: {ruta_salida}")
            
            except FileNotFoundError:
                print("Error: Archivo no encontrado. Verifique la ruta e inténtelo de nuevo.")
        
        elif opcion == '3':
            # Opción: Salir del programa
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")

menu()

"""
Algunos resultados obtenidos:

    Usando Bubble:
    • charlie_snoopy_3x3_bubble -> 744.44 ms ≈ 0.74444 segundos
    • charlie_snoopy_5x5_bubble -> 2960.82 ms ≈ 2.96082 segundos
    • charlie_snoopy_7x7_bubble -> 18382.71 ms ≈ 18.38271 segundos

    Usando Insertion:
    • perry_3x3_insertion -> 1801.27 ms ≈ 1.80127 segundos
    • perry_5x5_insertion -> 6283.11 ms ≈ 6.28311 segundos
    • perry_7x7_insertion -> 16232.02 ms ≈ 16.23202 segundos

    Usando Selection:
    • charlie_snoopy_3x3_selection -> 574.74 ms ≈ 0.57474 segundos
    • charlie_snoopy_5x5_selection -> 2094.01 ms ≈ 2.09401 segundos
    • charlie_snoopy_7x7_selection -> 5526.36 ms ≈ 5.52636 segundos

    Usando Merge:
    • perry_3x3_merge -> 3117.50 ms ≈ 3.11750 segundos
    • perry_5x5_merge -> 8774.94 ms ≈ 8.77494 segundos
    • perry_7x7_merge -> 18104.72 ms ≈ 18.10472 segundos
    
"""