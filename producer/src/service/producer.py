import json
import logging

import pika


class RabbitMQProducerService:
    def __init__(self, channel, exchange, queue):
        self._channel = channel
        self._exchange = exchange
        self._queue = queue

    def produce(self, message):
        self._publish(self._exchange, self._queue, message)

    def _publish(self, exchange, queue, message):
        self._channel.basic_publish(
            exchange=exchange,
            routing_key=queue,
            body=json.dumps(message),
            properties=pika.BasicProperties(content_type='application/json')
        )
        logging.info('Published Message: {}'.format(message))
