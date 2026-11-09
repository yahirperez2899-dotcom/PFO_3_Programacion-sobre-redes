# PFO 3 - Sistema Distribuido Cliente-Servidor

## Descripción
Este proyecto consiste en el diseño e implementación de un sistema distribuido utilizando Python y sockets TCP.

El sistema permite que distintos clientes envíen tareas a un servidor, que las distribuye entre múltiples workers mediante un pool de hilos.

## Tecnologías utilizadas
- Python 3
- Sockets TCP
- Threading
- ThreadPoolExecutor
- JSON

## Arquitectura
El sistema utiliza una arquitectura cliente-servidor.

Los clientes envían solicitudes al servidor mediante sockets TCP. El servidor recibe las tareas y las distribuye entre los workers disponibles para procesarlas y devolver una respuesta.

## Funcionalidades
El sistema permite realizar las siguientes operaciones:

- Sumar números.
- Multiplicar números.
- Convertir texto a mayúsculas.
- Invertir texto.

## Estructura del proyecto

- servidor.py: contiene el servidor TCP y el pool de workers.
- cliente.py: permite enviar tareas y recibir resultados.
- README.md: documentación del proyecto.

## Instalación y ejecución

No requiere instalar librerías externas.

1. Ejecutar el servidor:

   python servidor.py

2. Ejecutar el cliente en otra terminal:

   python cliente.py

3. Seleccionar una operación desde el menú del cliente.
