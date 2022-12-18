import logging


class ReceiverService:
    def __init__(self, channel, queue):
        try:
            logging.info(f'Starting consuming queue {queue}..')
            channel.basic_consume(
                queue=queue,
                on_message_callback=self.on_message,
                auto_ack=True
            )
            channel.start_consuming()
        except Exception as e:
            logging.debug(f'Exception: {e}')

    @staticmethod
    def on_message(channel, method, properties, body):
        logging.info(f'Channel: {channel}\nMethod: {method}\nProperties:{properties}\n'
                     f'Received message: {body.decode()}')
