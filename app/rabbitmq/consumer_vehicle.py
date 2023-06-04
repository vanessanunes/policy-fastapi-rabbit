import asyncio
import os
import aio_pika


from dotenv import load_dotenv


load_dotenv()


async def on_message(message: aio_pika.abc.AbstractIncomingMessage):
    async with message.process():
        print(message.body)


async def vehicle() -> None:
    rabbitmq_url = os.getenv("RABBITMQ_URL")
    print(rabbitmq_url)
    connection = await aio_pika.connect_robust(rabbitmq_url)
    queue_name = "vehicle"

    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(queue_name, durable=True)
        await queue.consume(callback=on_message)

        try:
            await asyncio.Future()
        finally:
            await connection.close()


if __name__ == "__main__":
    asyncio.run(vehicle())
