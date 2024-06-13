# 🌦️ BE-fastAPI

Tiny Simple Basic Cute FastAPI BE (JSON Dispenser).🎉 (with mysql)


## Project Structure

```sh
    BE-fastAPI/
    ├── app/
    │ ├── core/
    │ │ ├── config.py
    │ │ ├── error_handler.py
    │ │ ├── logging.py
    │ │ ├── response_handler.py
    │ ├── services/
    │ │ ├── common/
    │ │ │ ├── controllers.py
    │ │ │ ├── routes.py
    │ │ │ ├── schemas.py
    │ │ ├── users/
    │ │ │ ├── controllers.py
    │ │ │ ├── routes.py
    │ │ │ ├── schemas.py
    │ ├── main.py
    │ ├── logo.py
    ├── .env 
    ├── README.md
    ├── requirements.txt
```

## Features
- non ORM
- Unified Error Handling
- Routers and Controllers
- ASCII Art Logo!!



## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/zhinCode/BE-fastAPI.git
    cd BE-fastAPI
    ```

2. Install dependencies:

    ```sh
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Usage

```sh
$python -m app.main

   ______ _      _        ______  _____
  |___  /| |    (_)       | ___ \|  ___|
     / / | |__   _  _ __  | |_/ /| |__
    / /  | '_ \ | || '_ \ | ___ \|  __|
  ./ /___| | | || || | | || |_/ /| |___
  \_____/|_| |_||_||_| |_|\____/ \____/

App Version: 0.0.1
Author: Zhin
INFO:     Started server process [18488]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
Database pool initialized successfully.
INFO:root:2024-06-13T20:41:27.372899+09:00 - GET /api/users - 200 - 15.49 ms

```

http://localhost:8000

Swagger API Docs
http://localhost:8000/docs/

## Configuration

Create a .env file in the root directory:

``` lua
# Server Configuration
APP_PORT=3000

# Database Configuration
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USER=tester
DATABASE_PASSWORD=1111
DATABASE_NAME=test

# MongoDB Configuration
MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_USER=mongouser
MONGO_PASSWORD=mongopassword
MONGO_DB_NAME=test_mongo

# Application Information
APP_VERSION=0.0.1
APP_AUTHOR=Your Name
```


## License
This project is licensed under the MIT License.

