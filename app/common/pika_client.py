import json
import aio_pika


class PikaClient:
    def __init__(self) -> None:
        self.channel = None
    
    async def consume(self, loop):
        queue_name = "fila_teste"

        connection = await aio_pika.connect("amqp://vanessa:vanessa123@localhost/")
        self.channel = await connection.channel()
        queue = await self.channel.get_queue(queue_name)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print(message.body)

                    if queue.name in message.body.decode():
                        break
        return connection

    async def process_incoming_message(self, message):
        """Processing incoming message from RabbitMQ"""
        message.ack()
        body = message.body
        if body:
            self.process_callable(json.loads(body))
        
    def send_message(self, message: dict):
        """Method to publish message to RabbitMQ"""
        self.channel.basic_publish(
            exchange='',
            routing_key=self.publish_queue_name,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=str(uuid.uuid4())
            ),
            body=json.dumps(message)
        )