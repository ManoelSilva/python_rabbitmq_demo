# python-rabbitmq demo

## Stack

- Python 3.11.1
- Flask
- Pika
- Docker
- RabbitMQ

## Install and run

### Docker Compose 
You will need Docker installed. Use the following command:
```bash
docker-compose up --build
```


### API
- Health Check Request - Check if app is available.
Example:
```json
GET http://localhost:7000/
Accept: application/json
Content-Type: application/json
```

- Send Message Request - Sends a message to RabbitMQ.
Example:
```json
POST http://localhost:7000/
Accept: application/json
Content-Type: application/json
Body: {
    "message": "test"
}
```

## Project

```cmd
.
├── producer
│   ├── src
│   │   ├── config
│   │   │   ├── __init__.py
│   │   │   └── rabbitmq.py
│   │   └── exception
│   │   │    ├── __init__.py
│   │   │    └── rabbitmq.py
│   │   └── service
│   │   │    ├── __init__.py
│   │   │    └── request_handler.py
│   │   │    └── producer.py
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── enums.py
│   ├── Dockerfile
│   └── requirements.txt
└── receiver
│   ├── src
│   │   ├── config
│   │   │   ├── __init__.py
│   │   │   └── rabbitmq.py
│   │   └── exception
│   │   │    ├── __init__.py
│   │   │    └── rabbitmq.py
│   │   └── service
│   │   │    ├── __init__.py
│   │   │    └── receiver.py
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── enums.py
│   ├── Dockerfile
│   └── requirements.txt
├── .gitignore
├── docker-compose.yml
├── README.md
```

## ENV
- RabbitMQ:
```cmd
RABBITMQ_DEFAULT_USER:
RABBITMQ_DEFAULT_PASS:
```

- Producer:
```cmd
RABBITMQ_USERNAME:
RABBITMQ_PASSWORD:
RABBITMQ_HOST:
RABBITMQ_QUEUE:
RABBITMQ_ROUTING_KEY:
RABBITMQ_EXCHANGE:
SERVER_PORT:
SERVER_HOST:
```

- Receiver:
```cmd
RABBITMQ_USERNAME:
RABBITMQ_PASSWORD:
RABBITMQ_HOST:
RABBITMQ_QUEUE:
RABBITMQ_ROUTING_KEY:
RABBITMQ_EXCHANGE:
```

## Docs
- [Python](https://docs.python.org/3/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Pika](https://pika.readthedocs.io/en/stable/#)
- [Docker](https://docs.docker.com/)
- [RabbitMQ](https://www.rabbitmq.com)
