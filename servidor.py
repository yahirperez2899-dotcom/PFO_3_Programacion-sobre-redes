import socket
import json
from concurrent.futures import ThreadPoolExecutor

HOST = "0.0.0.0"
PORT = 5000

# Pool de 4 workers
pool_workers = ThreadPoolExecutor(max_workers=4)


# Funcion que procesa las tareas
def procesar_tarea(tarea):

    operacion = tarea.get("operacion")
    datos = tarea.get("datos")

    if operacion == "suma":
        resultado = sum(datos)

    elif operacion == "multiplicacion":
        resultado = 1
        for numero in datos:
            resultado *= numero

    elif operacion == "mayusculas":
        resultado = datos.upper()

    elif operacion == "invertir":
        resultado = datos[::-1]

    else:
        resultado = "Operacion no reconocida"

    return resultado


# Maneja cada cliente conectado
def manejar_cliente(conn, addr):

    print(f"[+] Cliente conectado: {addr}")

    with conn:
        archivo = conn.makefile("r", encoding="utf-8")

        for linea in archivo:
            try:
                tarea = json.loads(linea)

                print(f"[TAREA] Recibida: {tarea}")

                # Se distribuye la tarea a un worker
                futuro = pool_workers.submit(
                    procesar_tarea, tarea
                )

                resultado = futuro.result()

                respuesta = {
                    "estado": "correcto",
                    "resultado": resultado
                }

            except Exception as error:
                respuesta = {
                    "estado": "error",
                    "mensaje": str(error)
                }

            conn.sendall(
                (json.dumps(respuesta) + "\n").encode("utf-8")
            )

    print(f"[-] Cliente desconectado: {addr}")


# Inicio del servidor TCP
def iniciar_servidor():

    servidor = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    servidor.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"Servidor iniciado en {HOST}:{PORT}")
    print("Esperando conexiones...")

    try:
        while True:
            conn, addr = servidor.accept()

            # Cada cliente se lo atiende en un hilo
            import threading

            hilo = threading.Thread(
                target=manejar_cliente,
                args=(conn, addr),
                daemon=True
            )

            hilo.start()

    except KeyboardInterrupt:
        print("\nCerrando servidor...")

    finally:
        servidor.close()
        pool_workers.shutdown(wait=True)


if __name__ == "__main__":
    iniciar_servidor()
