import asyncio
import logging
from logging.config import dictConfig
import aio_pika

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s %(levelname)s %(message)s',
#     handlers=[
#         logging.FileHandler(r"app/logger/consumer.log"),
#         logging.StreamHandler()
#     ]
# )


# https://github.com/kieled/fastapi-aiopika-boilerplate/blob/main/src/consumer.py

# dictConfig(LogConfig().dict())
# logger = logging.getLogger("rabbit_service")


async def on_message(message: aio_pika.abc.AbstractIncomingMessage):
    # salvar no banco de dados o que deve ser pago
    async with message.process():
        print(message.body)


async def main() -> None:
    connection = await aio_pika.connect_robust("amqp://vanessa:vanessa123@localhost/")
    queue_name = "property"

    # logger.info("listening consumer")

    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(queue_name, durable=True)
        await queue.consume(callback=on_message)

        try:
            await asyncio.Future()
        finally:
            await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
