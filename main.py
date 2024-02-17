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
    print("3. Salir")

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

# Bucle de menu
while True:
    mostrar_menu()

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        listar_tareas()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida, intente de nuevo.")