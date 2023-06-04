# Projeto tecnico Desenvolvimento

## Projeto do teste


![Teste Case](./doc/diagrama_teste.png)

### Detalhes do teste

Criar uma API de emissão de apólice, a API vai receber um payload (payload_1 ou  payload_2) e de acordo com o produto deve direcionar para o worker que o processa.  
Criar um Worker de validação para o produto 111 e outro para o produto 222.  

Regras de negocio:  
O produto 111 tem dados que são required como endereco do imovel, dados do inquilino, beneficiario.  
O produto 222 tem dados que são required como placa do carro, chassis, modelo.  
Ao final do processamento precisamos ter salvo no banco de dados as parcelas que o segurado deve pagar.


Payload_1
```JSON
{
    "produto": 111,
    "item":{
        "endereço": {
            "rua": "rua x",
            "numero": 123
        },
        "inquilino":{
            "nome": "jose",
            "CPF": 12345678912
        },
        "beneficiario":{
            "nome": "Imobiliaria X",
            "CNPJ": 12345678912345
        }
    },
    "valores":{
        "precoTotal": 1200.00,
        "parcelas": 6
    }
}
```

Payload_2
```JSON
{
    "produto": 222,
    "item":{
        "placa": "ABC1234",
        "chassis": 123213,
        "modelo": "PORCHE"
    },
    "valores":{
        "precoTotal": 3000.00,
        "parcelas": 12
    }
}
```


# Caracteristicas para Avaliar

## Paralelismo
## AsyncIO
## Teste
### Teste unitario
### Teste integrado
## PUB/SUB
## API
## LOGS
## DOCKER
## K8S
## CI/CD
## Cache
## Observabilidade
## AWS
### SQS, S3, SNS
## RabbitMQ
## Banco de Dados
### DML, ...
