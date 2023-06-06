# Seguro

## configuração

Infelizmente não consegui fazer o fastapi conectar ao banco e ao rabbitmq então rode o comando para funcionar os containers:

```shell
docker-compose build && docker-compose up
```


Faça a instalação do pip.

```shell
pip install -r requirements.txt
```

Inicie o banco de dados

```shell
alembic upgrade head
```


e finalmente rode o fastapi:

```shell
uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
```



## banco de dados

Em `data_definition.py` temos as nossas tabelas.
Para rodar basta apenas usar o comando `alembic upgrade head`

Caso seja necessário a mudança de alguma tabela:

```shell
alembic revision --autogenerate -m "comentario"
alembic upgrade head
```

Para desfazer tudo:

`alembic downgrade base`

Para refazer um commit:

`alembic downgrade {revision}`

## apis

Foi pedido o payload em português, mas acabei optando por deixar em inglês e acredito que isso não será um problema.

Temos apenas um endpoint, esse endpoint recebe o payload e consegue destinguir atrás dele de qual produto se trata.

Payload para produto 111 (seguro residêncial):

```JSON
{
    "product": 111,
    "item":{
        "address": {
            "street": "rua x",
            "number": 123
        },
        "renter":{
            "name": "jose",
            "cpf": 12345678912
        },
        "beneficiary":{
            "name": "Imobiliaria X",
            "cnpj": 12345678912345
        }
    },
    "values":{
        "total_value": 1200.00,
        "installments": 6
    }
}
```

Payload para produto 222 (seguro automóvel)

```JSON
{
    "product": 222,
    "item":{
        "plate": "ABC1234",
        "chassis": 123213,
        "model": "PORCHE",
        "beneficiary":{
            "name": "Imobiliaria X",
            "cnpj": 12345678912345
        }
    },
    "values":{
        "total_value": 1200.00,
        "installments": 6
    }
}
```

## mudanças ?

1. Fiz a escolha pelo postgresql mas eu deveria ter escolhido um nosql. Porém acabei também incluindo o sqlalchemy e alembic :D
2. Sou ainda iniciante nos testes, então teria de tirar um tempo para conseguir iniciar nessa parte. De inicio achei bacana começar a desenvolver e depois tirar um tempo para começar a escrever os testes, mas por fim, não tive tempo habil para tal :/
3. Nunca trabalhei com o rabbitmq, inclusive nem sei se fiz da melhor maneira, mas fiz como pude; acho que teria sido mais experta se tivesse escolhido ter feito com o aws (sns e sqs).
