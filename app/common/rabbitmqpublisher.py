import json
from typing import Any, Dict
from pydantic import BaseSettings
import aio_pika


class RabbitMqSettings(BaseSettings):
    rabbitmq_login: str
    rabbitmq_pawrd: str
    rabbitmq_host: str
    rabbitmq_port: int

    class Config:
        env_file = "./.env"


class RabbitMqPublisher:
    def __init__(self, topic_name: str) -> None:
        self._topic_name = topic_name
    
    async def __create_channel(self):
        connection = await aio_pika.connect("amqp://vanessa:vanessa123@localhost/")
        #         connection = await aio_pika.connect_robust(
        #     f"amqp://{self.__settings.rabbitmq_login}:{self.__settings.rabbitmq_pawrd}@{self.__settings.rabbitmq_host}/",
        # )
        return connection

    async def send_message(self, routing_key: str, body: Dict[Any, Any]):
        connection = await self.__create_channel()
        channel = await connection.channel()
        exchange = await channel.declare_exchange(
            name=self._topic_name,
            type=aio_pika.ExchangeType.TOPIC,
            durable=True
        )
        await exchange.publish(
                message=aio_pika.Message(body=json.dumps(body).encode()),
                routing_key=routing_key,
            )
        
        await channel.close()

