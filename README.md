
# Seguro

## configuração

## banco de dados

Em `data_definition.py` temos as nossas tabelas.
Para rodar basta apenas usar o comando ```alembic upgrade head```

Caso seja necessário a mudança de alguma tabela:
```shell
alembic revision --autogenerate -m "comentario"
alembic upgrade head
```

Para desfazer tudo:

```alembic downgrade base```

Para refazer um commit:

```alembic downgrade {revision}```

## apis

Foi pedido o payload em português, mas acabei optando por deixar em inglês e acredito que isso não será um problema.

Temos apenas um endpoint, esse endpoint recebe o payload e consegue destinguir atrás dele de qual produto se trata.

Payload para produto 111 (seguro residêncial):

``` JSON
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
``` JSON
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