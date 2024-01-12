# FastAPI Celery Redis App

This is a small FastAPI application that demonstrates the usage of Celery and Redis for handling asynchronous tasks. The app includes a basic setup for creating tasks, queuing them with Celery, and processing them asynchronously using Redis as the message broker.

## Features

- **FastAPI:** A modern, fast, web framework for building APIs with Python 3.7+.
- **Celery:** Distributed task queue system that executes tasks asynchronously.
- **Redis:** In-memory data structure store used as a message broker for Celery.

## Installation

1. Install docker:

    [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)

2. Build:

    ```bash
    docker-compose build
    ```

3. Run the Docker container:

    ```bash
    docker-compose up
    ```

## Usage

1. Access the application at [http://localhost:8080](http://localhost:8080) in your browser.

2. Use the OpenAPI documentation at [http://localhost:8080/docs](http://localhost:8080/docs) to explore the API and interact with endpoints.

3. Screenshots are available in screenshot folder.