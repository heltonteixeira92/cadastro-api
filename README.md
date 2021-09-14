# cadastro-api

[![Updates](https://pyup.io/repos/github/heltonteixeira92/cadastro-api/shield.svg)](https://pyup.io/repos/github/heltonteixeira92/cadastro-api/)
[![Python 3](https://pyup.io/repos/github/heltonteixeira92/cadastro-api/python-3-shield.svg)](https://pyup.io/repos/github/heltonteixeira92/cadastro-api/)


# To run this application

##Console:

```python -m venv .venv```

```.venv\acripts\activate```

``pip install -r requirements.txt``

``cp contrib/env-sample .env``

`` python manage.py makemigrations``

```python manage.py migrate```

``python manage.py runserver``

## Endpoints

- localhost:8000/clientes

- localhost:8000/clientes/create

- localhost:8000/clientes/update/<id>

- localhost:8000/clientes/detail/<id>

- localhost:8000/clientes/delete/<id>
