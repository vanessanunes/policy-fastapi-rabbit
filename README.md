
# Seguro

## configuração

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
        "recipient":{
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
        "recipient":{
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