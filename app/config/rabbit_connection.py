from dataclasses import dataclass
import json
from typing import Any, Dict, Union
import aio_pika
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel

# https://github.com/kieled/fastapi-aiopika-boilerplate/blob/main/src/config/rabbit_connection.py


@dataclass
class RabbitConnection:
    connection: Union[AbstractRobustConnection, None] = None
    channel: Union[AbstractRobustChannel, None] = None

    async def connect(self) -> None:
        self.connection = await aio_pika.connect_robust(
            "amqp://vanessa:vanessa123@localhost/"
        )
        self.channel = await self.connection.channel()

    async def disconnect(self) -> None:
        if not self.channel.is_closed:
            await self.channel.close()
        if not self.connection.is_closed:
            await self.connection.close()

    async def send_message(self, body: Dict[Any, Any], routing_key: str):
        exchange = await self.channel.declare_exchange(
            name="products_topic", type=aio_pika.ExchangeType.TOPIC, durable=True
        )
        message = aio_pika.Message(body=json.dumps(body).encode())
        await exchange.publish(message, routing_key=routing_key)


rabbit_conn = RabbitConnection()
