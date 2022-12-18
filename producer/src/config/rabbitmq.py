import logging

import pika

from src.exception.rabbitmq import RabbitMQConfigException


class RabbitMQConfig:
    def __init__(self, queue, host, routing_key, username, password, exchange=''):
        self._connection = None
        self._channel = None
        self._queue = queue
        self._host = host
        self._routing_key = routing_key
        self._exchange = exchange
        self._username = username
        self._password = password

    def create_rabbitmq_components(self):
        self._create_channel()
        self._create_exchange()
        self._create_bind()
        logging.info('Rabbitmq components created..')

    def get_channel(self):
        if self._channel:
            return self._channel
        else:
            raise RabbitMQConfigException('Channel not created..')

    def _create_channel(self):
        credentials = pika.PlainCredentials(username=self._username, password=self._password)
        parameters = pika.ConnectionParameters(self._host, credentials=credentials)
        self._connection = pika.BlockingConnection(parameters)
        self._channel = self._connection.channel()

    def _create_exchange(self):
        self._channel.exchange_declare(
            exchange=self._exchange,
            exchange_type='direct',
            passive=False,
            durable=True,
            auto_delete=False
        )
        self._channel.queue_declare(queue=self._queue, durable=False)

    def _create_bind(self):
        self._channel.queue_bind(
            queue=self._queue,
            exchange=self._exchange,
            routing_key=self._routing_key
        )
        self._channel.basic_qos(prefetch_count=1)
