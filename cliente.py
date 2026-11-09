import socket
import json

HOST = "127.0.0.1"
PORT = 5000


def enviar_tarea(operacion, datos):

    cliente = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:
        cliente.connect((HOST, PORT))

        tarea = {
            "operacion": operacion,
            "datos": datos
        }

        mensaje = json.dumps(tarea) + "\n"

        cliente.sendall(mensaje.encode("utf-8"))

        archivo = cliente.makefile("r", encoding="utf-8")

        respuesta = archivo.readline()

        if respuesta:
            resultado = json.loads(respuesta)
            print("\nRespuesta del servidor:")
            print(resultado)

    except ConnectionRefusedError:
        print("No se pudo conectar con el servidor.")

    except Exception as error:
        print(f"Error: {error}")

    finally:
        cliente.close()


# Menu principal
def iniciar_cliente():

    print("=== SISTEMA CLIENTE-SERVIDOR ===")

    while True:

        print("\n1. Sumar numeros")
        print("2. Multiplicar numeros")
        print("3. Convertir texto a mayusculas")
        print("4. Invertir texto")
        print("5. Salir")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            datos = [
                int(x) for x in
                input("Ingrese numeros separados por coma: ").split(",")
            ]
            enviar_tarea("suma", datos)

        elif opcion == "2":
            datos = [
                int(x) for x in
                input("Ingrese numeros separados por coma: ").split(",")
            ]
            enviar_tarea("multiplicacion", datos)

        elif opcion == "3":
            datos = input("Ingrese un texto: ")
            enviar_tarea("mayusculas", datos)

        elif opcion == "4":
            datos = input("Ingrese un texto: ")
            enviar_tarea("invertir", datos)

        elif opcion == "5":
            print("Cliente finalizado.")
            break

        else:
            print("Opcion incorrecta.")


if __name__ == "__main__":
    iniciar_cliente()