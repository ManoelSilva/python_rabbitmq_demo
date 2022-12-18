import logging

from src.config.rabbitmq import RabbitMQConfig
from src.enums import EnvironmentVariables
from src.service.receiver import ReceiverService


def main():
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO
    )

    test_queue = EnvironmentVariables.RABBITMQ_QUEUE.get_env()
    config = RabbitMQConfig(
        queue=test_queue,
        host=EnvironmentVariables.RABBITMQ_HOST.get_env(),
        routing_key=EnvironmentVariables.RABBITMQ_ROUTING_KEY.get_env(),
        username=EnvironmentVariables.RABBITMQ_USERNAME.get_env(),
        password=EnvironmentVariables.RABBITMQ_PASSWORD.get_env(),
        exchange=EnvironmentVariables.RABBITMQ_EXCHANGE.get_env(),
    )

    config.create_rabbitmq_components()
    ReceiverService(config.get_channel(), test_queue)


main()
