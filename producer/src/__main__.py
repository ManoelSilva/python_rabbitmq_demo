import logging

from flask import Flask, request
from waitress import serve

from src.config.rabbitmq import RabbitMQConfig
from src.enums import EnvironmentVariables
from src.service.request_handler import PublishRequestHandlerService
from src.service.producer import RabbitMQProducerService

logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO
)

exchange = EnvironmentVariables.RABBITMQ_EXCHANGE.get_env()
queue = EnvironmentVariables.RABBITMQ_QUEUE.get_env()
rabbitmq_config = RabbitMQConfig(
    queue=queue,
    host=EnvironmentVariables.RABBITMQ_HOST.get_env(),
    routing_key=EnvironmentVariables.RABBITMQ_ROUTING_KEY.get_env(),
    username=EnvironmentVariables.RABBITMQ_USERNAME.get_env(),
    password=EnvironmentVariables.RABBITMQ_PASSWORD.get_env(),
    exchange=exchange
)
rabbitmq_config.create_rabbitmq_components()
handler = PublishRequestHandlerService(RabbitMQProducerService(rabbitmq_config.get_channel(), exchange, queue))
app = Flask(__name__)


@app.route('/', methods=['GET'])
def health_status():
    return 'UP'


@app.route('/', methods=['POST'])
def publish():
    return handler.publish(request.json)


server_host = EnvironmentVariables.SERVER_HOST.get_env()
server_port = EnvironmentVariables.SERVER_PORT.get_env()
if EnvironmentVariables.ENV.get_env() == 'prod':
    serve(app, host=server_host, port=server_port)
else:
    app.run(host=server_host, port=server_port)
