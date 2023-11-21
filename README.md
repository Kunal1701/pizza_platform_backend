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

3. Create a `.env-vars.sh` file in the project root directory with your database configuration.Then perform the following commands:

    ```bash
    echo 'export DB_ENGINE="django.db.backends.postgresql"' >> .env-vars.sh
    echo 'export DB_NAME="pizza"' >> .env-vars.sh
    echo 'export DB_USER="postgres"' >> .env-vars.sh
    echo 'export DB_PASSWORD="your_password"' >> .env-vars.sh
    echo 'export DB_HOST="localhost"' >> .env-vars.sh
    echo 'export DB_PORT="5432"' >> .env-vars.sh
    ```

    Replace `"your_password"` with your actual database password.

4. Source the `.env-vars.sh` file to set the environment variables.

    ```bash
    source .env-vars.sh
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


## Setup with Docker

1. Install Docker on your machine. You can download Docker from [here](https://www.docker.com/products/docker-desktop).

2. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/Kunal1701/pizza_platform_backend.git
    ```

3. Navigate to the project directory.

    ```bash
    cd pizza_delivery
    ```

4. Create a `.env-vars.sh` file in the project root directory with your database configuration.Then perform the following commands:

    ```bash
    echo 'export DB_ENGINE="django.db.backends.postgresql"' >> .env-vars.sh
    echo 'export DB_NAME="pizza"' >> .env-vars.sh
    echo 'export DB_USER="postgres"' >> .env-vars.sh
    echo 'export DB_PASSWORD="your_password"' >> .env-vars.sh
    echo 'export DB_HOST="localhost"' >> .env-vars.sh
    echo 'export DB_PORT="5432"' >> .env-vars.sh
    ```

    Replace `"your_password"` with your actual database password.

5. Source the `.env-vars.sh` file to set the environment variables.

    ```bash
    source .env-vars.sh
    ```

6. Build the Docker image. Replace the `${DB_ENGINE}`, `${DB_NAME}`, `${DB_USER}`, `${DB_PASSWORD}`, `${DB_HOST}`, and `${DB_PORT}` placeholders with your actual database configuration.

    ```bash
    docker build -t pizza_delivery:latest . -f Dockerfile \
    --build-arg DB_ENGINE=${DB_ENGINE} \
    --build-arg DB_NAME=${DB_NAME} \
    --build-arg DB_USER=${DB_USER} \
    --build-arg DB_PASSWORD=${DB_PASSWORD} \
    --build-arg DB_HOST=${DB_HOST} \
    --build-arg DB_PORT=${DB_PORT}
    ```

7. Run the Docker container.

    ```bash
    docker run -p 8000:8000 pizza_delivery:latest
    ```