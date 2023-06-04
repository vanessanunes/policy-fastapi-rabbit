import asyncio
import logging
import os
import aio_pika


from dotenv import load_dotenv
from logging.config import dictConfig


load_dotenv()
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
    async with message.process():
        print(message.body)


async def main() -> None:
    rabbitmq_url = os.getenv("RABBITMQ_URL")
    connection = await aio_pika.connect_robust(rabbitmq_url)
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
