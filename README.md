
# CryptoTracker-API

This is the API for the Capstone Project in Platzi Master. It is the backend for the Crypto Tracker App, an ap that allows you to track financial instruments such as cryptocurrency, stock, commodities etc. The project will further develop knowledge in REST API's using Python Rest Framework, as well as to start diving in algorithms for data science.

We built the backend using Django 3.2.3. The reason to choose Django is that this framework works very well with relational databases. As for now, it is using SQLite, the default database that is used when creating a new project with Django. The database that will be used in production will be MySQL. All the requirements can be found in the requirements.txt file.

To run the project, you can either clone the repository or download the .zip file from Github. As Django is a Python Framework, you need to have Python 3 installed. It is recommended to start a virtual environment with the "python -m venv name" command in the Command Line Interface. after that, you can install the requirements needed using the "pip install -r requirements.txt" command, which will install the needed requirements for the project.

Once you have successfully installed all requirements, you can run the project using the "python manage.py runserver" command, which will start a server in the url "127.0.0.1:8000". This project is also available at https://cryptotrackerapi.herokuapp.com/ (although it has not et been completed).
Luis Fernando Laris assigned the Capstone Project and was built by Luis Loaeza, Andrés Ayala and Miguel Valdés in the backend and Leonardo Rincón and Julián Vergara in the frontend.


## Acknowledgements

 - [Luis Fernando Laris](luis.laris@platzi.com)
 
  
## API Reference

https://cryptotrackerapi.herokuapp.com/

#### SIgnUp

``` SignUp
  Post  /api/auth/signup/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api/auth/signup/` | `Json` | **Required**. Endpoint to register new user|

#### Login

```https
  Post /api/auth/login/
```

| Header | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`api/auth/login/`| `Json` | **Required**. Endpoint for login|

#### Add criptos to portfolio

```https
  Post /criptos/
```

| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `Token` | **Required**. Endpoint where you will insert a cryptocurrency in the authenticated user's portfolio


#### Get all portfolio

```http
  GET /portfolio/
```

| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `Token` | **Required**. Endpoint where get all criptos acquired for loged user|

#### Get a single cripto

```http
  GET /my-cripto/<cripto_id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


#### Get all invested

```http
  GET /invested/
```

| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `Token` | **Required**. Endpoint where get all invested in the portfolio|

  
## Authors

Backend

- [@miguelalf](https://github.com/miguelalf)
- [@Loaezo](https://github.com/Loaezo)
- [@cexperto](https://github.com/cexperto)

Fronted

- [@LeoRincon](https://github.com/LeoRincon)
- [@jtomasvc](https://github.com/jtomasvc)

  
## Deployment

To deploy this project:

clone this repo

Install python3+


```bash
run
py -m venv <name venv>
py install -r requirements.txt
py manage.py runserver  

 
## License

[MIT](https://choosealicense.com/licenses/mit/)
  
## Tech Stack

**Client:** JavaScript, React, SCSS, HTML 

**Server:** Python, Django, MySql, AWS
