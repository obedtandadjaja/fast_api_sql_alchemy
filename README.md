# fast_api_sql_alchemy
Fast API + SQL Alchemy ORM sample project

This project is made solely to explore the features of Fast API and SQL Alchemy
ORM. In particular, I am trying to find out the following things:

- How easy it is for new developers to use (ease of use)
- Performance (latency + speed)
- Maturity (production ready or not)
- Breadth of features
- Community size (Stackoverflow community + documentation + github
  contributors + online articles)

In trying to find out these things, I will be creating a simple web server with
authentication in mind. This ensures that I do some kind of middleware to verify
users accessing private pages. I will be building a secret message delivery
system much like onetimesecret.com. Of course, I will not put a lot of thought
into the architecture of the system, since I will be focusing on the
functionality of the frameworks and library that I am using.

## Running the project

Create a new Postgres database. Make sure to change the configuration on
`app/db/session.py` to fit to your database information.

Initialize the database using the following command:

```
make seed
```

Start the server using the following command:

```
make start
```

In a new command line tab or TMUX window:

```
curl -v http://localhost:8000/api/health

# This should return a 200 response with {'status': 'OK'} indicating that the
# server is healthy and ready to accept requests
```

## Project Structure

root
  - alembic
  - app
    - api
      - utils (common utility that is shared across multiple versions)
      - v1
        - utils (utilitiy shared only on this v1 api)
        - endpoint.py
        - endpoint2.py
      - v2
    - controllers (mimics the structure of api)
    - db
    - lib (shared utility among controllers and models)
    - models
  - tests (mimics the structure of app)
