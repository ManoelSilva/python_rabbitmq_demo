from flask import jsonify


class PublishRequestHandlerService:
    def __init__(self, producer):
        self.producer = producer

    def publish(self, request):
        self.producer.produce(request)
        return jsonify({'message_published': request})
