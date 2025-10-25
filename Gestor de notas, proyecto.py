# Gestor de Notas Académicas
# Sistema para gestionar calificaciones de cursos

# Estructuras de datos principales
cursos = []  # Lista para almacenar cursos como tuplas (nombre, nota)
cola_revision = []  # Cola para solicitudes de revisión
pila_historial = []  # Pila para historial de cambios

def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*50)
    print("      GESTOR DE NOTAS ACADÉMICAS")
    print("="*50)
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (búsqueda lineal)")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (ordenamiento burbuja)")
    print("9. Ordenar cursos por nombre (ordenamiento inserción)")
    print("10. Buscar curso por nombre (búsqueda binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (pila)")
    print("13. Salir")
    print("-"*50)

def validar_nota(nota_str):
    """Valida que la nota sea un número entre 0 y 100"""
    try:
        nota = float(nota_str)
        if 0 <= nota <= 100:
            return True, nota
        else:
            return False, "La nota debe estar entre 0 y 100"
    except ValueError:
        return False, "Por favor ingrese un número válido"

def registrar_curso():
    """Registra un nuevo curso con su nota"""
    print("\n--- REGISTRAR NUEVO CURSO ---")
    
    nombre = input("Ingrese el nombre del curso: ").strip()
    if not nombre:
        print("Error: El nombre del curso no puede estar vacío")
        return
    
    # Verificar si el curso ya existe
    for curso in cursos:
        if curso[0].lower() == nombre.lower():
            print("Error: Este curso ya está registrado")
            return
    
    nota_str = input("Ingrese la nota obtenida: ")
    es_valida, resultado = validar_nota(nota_str)
    
    if es_valida:
        cursos.append((nombre, resultado))
        print(f"Curso '{nombre}' registrado con éxito. Nota: {resultado}")
    else:
        print(f"Error: {resultado}")

def mostrar_cursos():
    """Muestra todos los cursos registrados"""
    print("\n--- CURSOS REGISTRADOS ---")
    
    if not cursos:
        print("No hay cursos registrados")
        return
    
    for i, (nombre, nota) in enumerate(cursos, 1):
        print(f"{i}. {nombre} - Nota: {nota}")

def calcular_promedio():
    """Calcula el promedio general de todas las notas"""
    print("\n--- CALCULAR PROMEDIO GENERAL ---")
    
    if not cursos:
        print("No hay cursos registrados para calcular el promedio")
        return
    
    suma_notas = sum(nota for _, nota in cursos)
    promedio = suma_notas / len(cursos)
    print(f"Promedio general: {promedio:.2f}")

def contar_aprobados_reprobados():
    """Cuenta los cursos aprobados y reprobados"""
    print("\n--- CURSOS APROBADOS Y REPROBADOS ---")
    
    if not cursos:
        print("No hay cursos registrados")
        return
    
    aprobados = 0
    reprobados = 0
    
    for nombre, nota in cursos:
        if nota >= 60:
            aprobados += 1
        else:
            reprobados += 1
    
    print(f"Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}")

def buscar_curso_lineal():
    """Busca un curso por nombre usando búsqueda lineal"""
    print("\n--- BUSCAR CURSO (BÚSQUEDA LINEAL) ---")
    
    if not cursos:
        print("No hay cursos registrados")
        return
    
    nombre_buscar = input("Ingrese el nombre del curso a buscar: ").strip().lower()
    
    encontrados = []
    for nombre, nota in cursos:
        if nombre_buscar in nombre.lower():
            encontrados.append((nombre, nota))
    
    if encontrados:
        print("Cursos encontrados:")
        for nombre, nota in encontrados:
            print(f"- {nombre} - Nota: {nota}")
    else:
        print("No se encontraron cursos con ese nombre")

def actualizar_nota():
    """Actualiza la nota de un curso existente"""
    print("\n--- ACTUALIZAR NOTA DE CURSO ---")
    
    if not cursos:
        print("No hay cursos registrados")
        return
    
    nombre_actualizar = input("Ingrese el nombre del curso: ").strip()
    
    for i, (nombre, nota_anterior) in enumerate(cursos):
        if nombre.lower() == nombre_actualizar.lower():
            nueva_nota_str = input("Ingrese la nueva nota: ")
            es_valida, resultado = validar_nota(nueva_nota_str)
            
            if es_valida:
                # Guardar en historial antes de actualizar
                pila_historial.append(f"Se actualizó: {nombre} - Nota anterior: {nota_anterior} → Nueva nota: {resultado}")
                cursos[i] = (nombre, resultado)
                print("Nota actualizada correctamente")
                return
            else:
                print(f"Error: {resultado}")
                return
    
    print("Curso no encontrado")

def eliminar_curso():
    """Elimina un curso de la lista"""
    print("\n--- ELIMINAR CURSO ---")
    
    if not cursos:
        print("No hay cursos registrados")
        return
    
    nombre_eliminar = input("Ingrese el curso a eliminar: ").strip()
    
    for i, (nombre, nota) in enumerate(cursos):
        if nombre.lower() == nombre_eliminar.lower():
            confirmacion = input("¿Está seguro que desea eliminarlo? (s/n): ").lower()
            if confirmacion == 's':
                # Guardar en historial antes de eliminar
                pila_historial.append(f"Se eliminó: {nombre} - Nota: {nota}")
                curso_eliminado = cursos.pop(i)
                print(f"Curso '{curso_eliminado[0]}' eliminado correctamente")
                return
            else:
                print("Operación cancelada")
                return
    
    print("Curso no encontrado")

def ordenar_por_nota_burbuja():
    """Ordena los cursos por nota usando el algoritmo burbuja"""
    print("\n--- ORDENAR CURSOS POR NOTA (BURBUJA) ---")
    
    if not cursos:
        print("No hay cursos registrados")
        return
    
    # Crear copia para no modificar la lista original permanentemente
    cursos_ordenados = cursos.copy()
    n = len(cursos_ordenados)
    
    # Algoritmo burbuja
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if cursos_ordenados[j][1] < cursos_ordenados[j + 1][1]:
                # Intercambiar elementos
                cursos_ordenados[j], cursos_ordenados[j + 1] = cursos_ordenados[j + 1], cursos_ordenados[j]
    
    print("Cursos ordenados por nota (descendente):")
    for i, (nombre, nota) in enumerate(cursos_ordenados, 1):
        print(f"{i}. {nombre} - Nota: {nota}")

def ordenar_por_nombre_insercion():
    """Ordena los cursos por nombre usando ordenamiento por inserción"""
    print("\n--- ORDENAR CURSOS POR NOMBRE (INSERCIÓN) ---")
    
    if not cursos:
        print("No hay cursos registrados")
        return
    
    # Crear copia para no modificar la lista original permanentemente
    cursos_ordenados = cursos.copy()
    
    # Algoritmo de ordenamiento por inserción
    for i in range(1, len(cursos_ordenados)):
        clave = cursos_ordenados[i]
        j = i - 1
        
        while j >= 0 and cursos_ordenados[j][0].lower() > clave[0].lower():
            cursos_ordenados[j + 1] = cursos_ordenados[j]
            j -= 1
        
        cursos_ordenados[j + 1] = clave
    
    print("Cursos ordenados por nombre (alfabéticamente):")
    for i, (nombre, nota) in enumerate(cursos_ordenados, 1):
        print(f"{i}. {nombre} - Nota: {nota}")

def buscar_curso_binaria():
    """Busca un curso por nombre usando búsqueda binaria"""
    print("\n--- BUSCAR CURSO (BÚSQUEDA BINARIA) ---")
    
    if not cursos:
        print("No hay cursos registrados")
        return
    
    # Verificar si los cursos están ordenados por nombre
    esta_ordenado = all(cursos[i][0].lower() <= cursos[i + 1][0].lower() 
                       for i in range(len(cursos) - 1))
    
    if not esta_ordenado:
        print("Advertencia: Los cursos no están ordenados por nombre.")
        print("Por favor, use la opción 9 primero para ordenarlos.")
        return
    
    nombre_buscar = input("Ingrese el nombre del curso a buscar: ").strip().lower()
    
    # Búsqueda binaria
    izquierda = 0
    derecha = len(cursos) - 1
    encontrado = False
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        nombre_medio = cursos[medio][0].lower()
        
        if nombre_medio == nombre_buscar:
            nombre, nota = cursos[medio]
            print(f"Curso encontrado: {nombre} - Nota: {nota}")
            encontrado = True
            break
        elif nombre_medio < nombre_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    if not encontrado:
        print("Curso no encontrado")

def simular_cola_revision():
    """Simula una cola de solicitudes de revisión"""
    print("\n--- COLA DE SOLICITUDES DE REVISIÓN ---")
    print("Ingrese curso para revisión (escriba 'fin' para terminar):")
    
    cola_revision.clear()  # Limpiar cola anterior
    
    while True:
        curso = input("> ").strip()
        if curso.lower() == 'fin':
            break
        if curso:
            cola_revision.append(curso)
    
    print("\nProcesando solicitudes:")
    if not cola_revision:
        print("No hay solicitudes para procesar")
        return
    
    for curso in cola_revision:
        print(f"Revisando: {curso}")

def mostrar_historial_cambios():
    """Muestra el historial de cambios recientes"""
    print("\n--- HISTORIAL DE CAMBIOS RECIENTES ---")
    
    if not pila_historial:
        print("No hay cambios recientes")
        return
    
    # Mostrar en orden inverso (el más reciente primero)
    for i, cambio in enumerate(reversed(pila_historial), 1):
        print(f"{i}. {cambio}")

def main():
    """Función principal del programa"""
    print("Bienvenido al Gestor de Notas Académicas")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            registrar_curso()
        elif opcion == '2':
            mostrar_cursos()
        elif opcion == '3':
            calcular_promedio()
        elif opcion == '4':
            contar_aprobados_reprobados()
        elif opcion == '5':
            buscar_curso_lineal()
        elif opcion == '6':
            actualizar_nota()
        elif opcion == '7':
            eliminar_curso()
        elif opcion == '8':
            ordenar_por_nota_burbuja()
        elif opcion == '9':
            ordenar_por_nombre_insercion()
        elif opcion == '10':
            buscar_curso_binaria()
        elif opcion == '11':
            simular_cola_revision()
        elif opcion == '12':
            mostrar_historial_cambios()
        elif opcion == '13':
            print("\nGracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 13.")
        
        input("\nPresione Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()