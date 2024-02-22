# Definiendo una clase para representar tareas
class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

# Lista para guardar las tareas
tareas = []

# Funcion para mostrar el menu
def mostrar_menu():
    print("\n*** Sistema de Gestion de Tareas ***")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Listar tareas completadas")
    print("6. Listar tareas no completadas")
    print("7. Salir")

# Funcion para agregar tarea
def agregar_tarea():
    descripcion = input("Ingrese la descripcion de la tarea: ")
    tarea = Tarea(descripcion)
    tareas.append(tarea)
    print("Tarea agregada con exito")

# Funcion para listar tareas
def listar_tareas():
    print("\n--- Lista de Tareas ---")
    for idx, tarea in enumerate(tareas, start=1):
        print(f"{idx}. Descripcion: {tarea.descripcion} - Completada: {tarea.completada}")

# Función para marcar tarea como completada
def marcar_completada():
    listar_tareas()
    try:
        idx_tarea = int(input("Ingrese el número de la tarea que desea marcar como completada: "))
        if 1 <= idx_tarea <= len(tareas):
            tareas[idx_tarea - 1].completada = True
            print(f"Tarea '{tareas[idx_tarea - 1].descripcion}' marcada como completada.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Función para eliminar tarea
def eliminar_tarea():
    listar_tareas()
    try:
        idx_tarea = int(input("Ingrese el número de la tarea que desea eliminar: "))
        if 1 <= idx_tarea <= len(tareas):
            tarea_eliminada = tareas.pop(idx_tarea - 1)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Bucle de menú
while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        listar_tareas()
    elif opcion == "3":
        marcar_completada()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")