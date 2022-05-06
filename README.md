# Kenzie Auction House - KAH

[HEROKU APPLICATION SERVER](https://cap-gustavo-g12-server.herokuapp.com/)

## PARTNERS

#### POST /partners

_Formato da requisição_

```json
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
```

_Formato de resposta_

```json
{
  "about": "",
  "cnpj": "XXXXXXXXXXXXXX",
  "email": "email@mail.com",
  "id": "<id-hash>",
  "name": "Nome",
  "phone_number": "XXXXXXXXXXX"
}
```

#### GET /partners

_Formato de resposta_

```json
[
  {
    "id": "<id-hash>",
    "name": "Nome",
    "email": "mail@mail.com",
    "phone": "XXXXXXXXXXX"
  },
  {
    "id": "<id-hash>",
    "name": "Nome 2",
    "email": "mail2@mail.com",
    "phone": "XXXXXXXXXXX"
  }
]
```

#### GET /partners/<partner_id>

_Formato de resposta_

```json
{
  "about": "",
  "cnpj": "1234489422311",
  "email": "paulo3@gmail.com",
  "id": "ba203770-818a-48b9-bf86-d928fa7f58eb",
  "name": "Paulo Tres",
  "phone_number": "952658423"
}
```

#### POST /partners/login

_Formato da requisição_

```json
{
  "email": "<email>",
  "password": "<password>"
}
```

## Categories

#### POST /categories

_Formato da requisição_

```json
{
  "name": "Nome",
  "description": "Descrição"
}
```

#### GET /categories

_Formato de resposta_

```json
[
  {
    "description": "Descrição",
    "id": "<id-hash>",
    "name": "Nome"
  },
  {
    "description": "Descrição",
    "id": "<id-hash>",
    "name": "Nome 2"
  }
]
```

#### GET /categories/<category_id>

_Formato de resposta_

```json
{
  "description": "Descrição",
  "id": "<id-hash>",
  "name": "Nome"
}
```

#### PATCH /categories/<category_id>

_Formato da requisição_

```json
{
  "description": "Nova descrição"
}
```

#### DELETE /categories/<category_id>

_Formato de resposta_

```json
{
  "sucesso": "A categoria foi removida com sucesso"
}
```

## Users

#### POST /users

_Formato da requisição_

```json
{
  "name": "Nome",
  "email": "mail@email.com",
  "cpf": "XXXXXXXXXXX",
  "phone_number": "XXXXXXXXX",
  "birth_date": "DD/MM/YYYY",
  "password": "xxxxxx",
  "address": {
    "country": "Brazil",
    "state": "PR",
    "city": "Curitiba",
    "street": "Rua Tal",
    "number": "XXX",
    "complement": "",
    "postal_code": "XXXXXXXX"
  }
}
```

#### GET /users/<user_id>

_Formato da resposta_

```json
{
  "api_key": "<auth-token>",
  "birth_date": "Thu, 01 Jan 1001 00:00:00 GMT",
  "cpf": "XXXXXXXXXXX",
  "email": "mail@email.com",
  "id": "<hash-id>",
  "name": "Nome",
  "phone_number": "XXXXXXXXXXX",
  "role": "user"
}
```

#### GET /users

_Formato da resposta_

```json
[
  {
    "api_key": "<auth-token>",
    "birth_date": "Thu, 01 Jan 1001 00:00:00 GMT",
    "cpf": "XXXXXXXXXXX",
    "email": "mail@email.com",
    "id": "<hash-id>",
    "name": "Nome",
    "phone_number": "XXXXXXXXXXX",
    "role": "user"
  },
  {
    "api_key": "<auth-token>",
    "birth_date": "Thu, 01 Jan 1001 00:00:00 GMT",
    "cpf": "XXXXXXXXXXX",
    "email": "mail@email.com",
    "id": "<hash-id>",
    "name": "Nome",
    "phone_number": "XXXXXXXXXXX",
    "role": "user"
  },
  {
    "api_key": "<auth-token>",
    "birth_date": "Thu, 01 Jan 1001 00:00:00 GMT",
    "cpf": "XXXXXXXXXXX",
    "email": "mail@email.com",
    "id": "<hash-id>",
    "name": "Nome",
    "phone_number": "XXXXXXXXXXX",
    "role": "user"
  }
]
```

#### DELETE /users/<user_id>

_Formato de resposta_

```json
    {
        ""
    }
```

#### PATCH /users/<user_id>

_Formato da requisição_

```json
{
  "<field>": "<value>"
}
```

_Formato da resposta_

```json
{
  "<field>": "<value>"
}
```

## BIDS

#### POST /bids

_Formato de requisição_

```json
{
  "id_product": "42a629b4-fb57-4af2-b1cd-103fe0646604",
  "price": "50",
  "id_user": "2fa7e80c-4584-4343-ad5b-3f194472b620"
}
```

_Formato de resposta_

```json
{
  "id": "447fa3f4-ccda-4d73-ad25-47f5ff542d69",
  "price": "50"
}
```
