import asyncio
import logging

import aio_pika
from fastapi import FastAPI


class RabbitMqConsumer:
    # def __init__(self, loop) -> None:
    #     self.loop = loop

    async def exemplo(self):
        print(f"uhul, exemplo -> {self}")

    async def get_message(self, queue_name: str):
        logging.basicConfig(level=logging.DEBUG)
        connection = await aio_pika.connect_robust(
            "amqp://vanessa:vanessa123@localhost/"
        )

        async with connection:
            channel = await connection.channel()
            await channel.set_qos(prefetch_count=10)
            queue = await channel.get_queue(queue_name)
            print(f" ->>>>>>>>>>>>>>>>>>>>>>>>> {queue}")
            # incoming_message = await queue.get()
            # await incoming_message.ack()
            # await connection.close()
            async with queue.iterator() as queue_iter:
                async for message in queue_iter:
                    async with message.process():
                        print(message.body)
                        if queue.name in message.body.decode():
                            break

    async def connect_to_rabbitmq(self, app: FastAPI, loop) -> None:
        app.state.rabbitmq = self.get_message("property")
        # print(f"chegamos aqui {cls.exemplo}")

    async def close_rabbitmq(self, app: FastAPI):
        await app.state.rabbitmq.close()
