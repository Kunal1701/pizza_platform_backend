# Pizza Platform

## Description

Designed and implemented a microservices-based backend system for a pizza ordering and delivery platform with the following microservices:

User Service:
Allow users to checkout all the restaurants which are online in their city
Allow users to place pizza orders.
Maintain order history for each user.

Delivery Service:
Enable restaurant owners to update the status of pizza deliveries.

Admin Service:
Allow admin users to add or remove restaurants from the platform.

Restaurant Service:
Enable restaurant owners to manage their menu by adding, updating, or removing items.
They can also manage if restaurant is online or offline


## Setup

1. **Clone the repository**

    ```
    git clone https://github.com/Kunal1701/pizza_platform_backend.git
    cd pizza_platform_backend
    ```

2. **Set up a virtual environment**

    ```
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install dependencies**

    ```
    python3 -m pip install -r requirements.txt
    ```

4. **Set up the database**

This project uses PostgreSQL as its database. Here's how you can set it up:

1. Install PostgreSQL if you haven't already. You can download it from [here](https://www.postgresql.org/download/).

2. Create a new PostgreSQL database. You can do this through the PostgreSQL interactive terminal:

```bash
psql -U postgres
```
Then, in the PostgreSQL interactive terminal, run:
```
CREATE DATABASE pizza;
```

3. Update the DATABASES setting in settings.py with your PostgreSQL database details:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pizza',
        'USER': 'postgres',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
    }
}
```


5. **Apply migrations**

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

## Running the Project

1. **Start the server**

    ```
    python3 manage.py runserver
    ```

    The server will start on `http://localhost:8000`.

## Testing

1. **Run tests**

    ```
    python3 manage.py test
    ```

## API Endpoints

All the API endpoints and their descriptions exported via postman is attached as a json file.