import asyncio
import aio_pika


async def on_message(message: aio_pika.abc.AbstractIncomingMessage):
    async with message.process():
        print(message.body)


async def main() -> None:
    connection = await aio_pika.connect_robust("amqp://vanessa:vanessa123@localhost/")
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
    asyncio.run(main())
