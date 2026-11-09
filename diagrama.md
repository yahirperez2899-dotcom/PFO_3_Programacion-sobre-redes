# Diagrama de Arquitectura - PFO 3

## Sistema Distribuido Cliente-Servidor

El siguiente diagrama representa la arquitectura propuesta para el sistema distribuido.

```mermaid
flowchart TD
    A[Cliente Web] --> LB[Balanceador Nginx / HAProxy]
    B[Cliente Movil] --> LB
    C[Cliente Python] --> LB

    LB --> S1[Servidor Worker 1]
    LB --> S2[Servidor Worker 2]

    S1 --> W1[Pool de hilos]
    S2 --> W2[Pool de hilos]

    W1 --> MQ[RabbitMQ]
    W2 --> MQ

    MQ --> DB[(PostgreSQL)]
    MQ --> S3[Amazon S3]
```

## Componentes

- **Clientes:** envían solicitudes al sistema.
- **Balanceador de carga:** distribuye las solicitudes entre servidores.
- **Servidores workers:** reciben y procesan tareas.
- **Pool de hilos:** permite procesar múltiples tareas concurrentemente.
- **RabbitMQ:** gestiona la comunicación mediante colas de mensajes.
- **PostgreSQL:** almacena datos y resultados.
- **Amazon S3:** almacena archivos.

## Flujo de funcionamiento

1. El cliente envía una solicitud.
2. El balanceador selecciona un servidor.
3. El servidor recibe la tarea mediante un socket TCP.
4. Un worker procesa la solicitud.
5. RabbitMQ permite la comunicación entre servidores.
6. Los resultados pueden almacenarse en PostgreSQL.
7. Los archivos pueden almacenarse en Amazon S3.
8. El servidor devuelve el resultado al cliente.
