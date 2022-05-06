### Kenzie Auction House - KAH

## PARTNERS ##
POST /partners
    
    **** Formato da requisição ****
    {
        "name": "Nome",
        "email": "email@mail.com",
        "cnpj": "XXXXXXXXXXXXXX", 
        "phone_number": "XXXXXXXXXXX",
        "about": "",
        "password": "xxxxxx",
        "address": {
            "country": "Brasil",
            "state": "SP",
            "city": "São Paulo",
            "street": "Avenida Faria Lima",
            "number": "666",
            "complement": "Não tem",
            "postal_code": "00000-00"
        }
    }

    **** Retorno da requisição ****
    {
        "about": "",
        "cnpj": "XXXXXXXXXXXXXX",
        "email": "email@mail.com",
        "id": "<id-hash>",
        "name": "Nome",
        "phone_number": "XXXXXXXXXXX"
    }

GET /partners
    **** Retorno da requisição ****
    [
        {
            "id": "<id-hash>",
            "name": "Nome",
            "email": "mail@mail.com",
            "phone": "XXXXXXXXXXX",
        },
        {
            "id": "<id-hash>",
            "name": "Nome 2",
            "email": "mail2@mail.com",
            "phone": "XXXXXXXXXXX",
        }
    ]

GET /partners/<partner_id>
    **** Retorno da requisição ****
    {
        "about": "",
        "cnpj": "1234489422311",
        "email": "paulo3@gmail.com",
        "id": "ba203770-818a-48b9-bf86-d928fa7f58eb",
        "name": "Paulo Tres",
        "phone_number": "952658423"
    }

POST /partners/login
    **** Formato da requisição ****
    {
        "email": "<email>",
        "password": "<password>"
    }

## Categories

POST /categories
 **** Formato da requisição ****
    {
        "name":"Nome",
        "description":"Descrição",
    }

GET /categories
    {

    }