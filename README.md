# MADRS Web Commerce Backend

[![Build Status](https://img.shields.io/travis/com/your-username/madrs-web-commerce-backend.svg?style=for-the-badge)](https://travis-ci.com/your-username/madrs-web-commerce-backend)
[![Coverage Status](https://img.shields.io/coveralls/github/your-username/madrs-web-commerce-backend.svg?style=for-the-badge)](https://coveralls.io/github/your-username/madrs-web-commerce-backend?branch=main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Docker Pulls](https://img.shields.io/docker/pulls/your-dockerhub-username/madrs-web-commerce-backend.svg?style=for-the-badge)](https://hub.docker.com/r/your-dockerhub-username/madrs-web-commerce-backend)

A production-ready, modular web retail system built with Django, Docker, Celery, and Stripe. This project is designed with a distributed architecture, leveraging asynchronous task processing and containerized deployment for scalability and maintainability.

---

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Deployment](#deployment)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Introduction

MADRS is a robust and scalable backend solution for modern e-commerce platforms. It provides all the essential features for an online retail business, from product management and user authentication to order processing and payments. The use of Docker ensures easy setup and consistent environments, while Celery handles long-running tasks asynchronously, ensuring the application remains responsive.

## Key Features

-   **Modular Design:** Built with Django apps for easy extension and maintenance.
-   **Containerized with Docker:** Includes `Dockerfile` and `docker-compose.yml` for easy setup and deployment.
-   **Asynchronous Task Queues:** Utilizes Celery with Redis/RabbitMQ for background tasks like sending emails and processing payments.
-   **Stripe Integration:** Secure and reliable payment processing out-of-the-box.
-   **JWT Authentication:** Stateless authentication using JSON Web Tokens.
-   **Comprehensive API:** A well-documented API for managing products, users, orders, and more.
-   **Scalable Architecture:** Designed to handle high traffic and large volumes of data.

## System Architecture

The system is designed as a set of interacting services, containerized using Docker.

1.  **Web Server (Nginx):** Acts as a reverse proxy, serving static files and forwarding requests to the Django application.
2.  **Application Server (Gunicorn & Django):** The core of the application, handling business logic and API requests.
3.  **Database (PostgreSQL):** The primary data store for the application.
4.  **Cache (Redis):** Used for caching frequently accessed data to improve performance.
5.  **Task Queue (Celery & RabbitMQ/Redis):** Manages asynchronous background tasks, decoupling long-running processes from the main application flow.
6.  **External Services:** Integrates with third-party services like Stripe for payments.

## Technology Stack

### Backend
-   **Framework:** Django & Django REST Framework
-   **Database:** PostgreSQL
-   **Asynchronous Tasks:** Celery
-   **Message Broker:** RabbitMQ / Redis
-   **Caching:** Redis
-   **Web Server:** Gunicorn, Nginx

### DevOps & Deployment
-   **Containerization:** Docker, Docker Compose
-   **CI/CD:** GitHub Actions
--   **Hosting:** Microsoft Azure

### Others
-   **Payments:** Stripe API
-   **Authentication:** Simple JWT

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:
-   [Docker](https://www.docker.com/get-started)
-   [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to get a local development environment up and running.

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/mr-mukherjee03/madrs-web-commerce-backend.git](https://github.com/mr-mukherjee03/madrs-web-commerce-backend.git)
    cd madrs-web-commerce-backend
    ```

2.  **Create an Environment File**
    Create a `.env` file in the project root by copying the example file.
    ```bash
    cp .env.example .env
    ```
    Update the `.env` file with your configuration details (database credentials, Stripe keys, etc.).

3.  **Build and Run with Docker Compose**
    ```bash
    docker-compose up --build -d
    ```
    This command will build the Docker images and start all the services in detached mode.

4.  **Run Database Migrations**
    ```bash
    docker-compose exec web python manage.py migrate
    ```

5.  **Create a Superuser**
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```
    Follow the prompts to create an administrator account.

6.  **Collect Static Files**
    ```bash
    docker-compose exec web python manage.py collectstatic --no-input
    ```

The application should now be running at `http://localhost:8000`. You can access the Django admin panel at `http://localhost:8000/admin/`.

## Configuration

All configuration is managed through environment variables in the `.env` file. Key variables include:

-   `SECRET_KEY`: Django secret key.
-   `DEBUG`: Set to `True` for development, `False` for production.
-   `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`: Database credentials.
-   `CELERY_BROKER_URL`: URL for the message broker (e.g., Redis or RabbitMQ).
-   `STRIPE_SECRET_KEY`, `STRIPE_PUBLISHABLE_KEY`: Your Stripe API keys.

## Running Tests

To run the test suite, execute the following command:
```bash
docker-compose exec web python manage.py test