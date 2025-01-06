# Polling System API

This project is a simple Polling System implemented using **FastAPI** and **PostgreSQL**. Users can create polls, add options, and vote on them.

## ✅Features

- **Create and manage polls**
- **Add options to polls**
- **Vote on options**
- **User authentication with JWT**
- **Pagination support for fetching polls**
<!-- - **Unit tests for API endpoints** -->

## 🔥Technologies Used

- **FastAPI**: For building the API
- **PostgreSQL**: As the primary database
- **SQLAlchemy**: For ORM and database management
- **Alembic**: For database migrations
- **Docker**: For containerization and easy deployment
<!-- - **Pytest**: For writing unit tests  -->

# ⭐Setup and Installation

## 📌Prerequisites

- Docker and Docker Compose must be installed.

## 📌Steps to Run the Project

1. **Clone the repository**:
    ```
    git clone https://github.com/your-username/polling-system.git
    cd polling-system
    ```
2. **Build and run the containers**:
    ```
    docker-compose up --build
    ```
    This will start the FastAPI application and PostgreSQL database.

---

## 🔎Access the API:

1. The API will be available at http://localhost:80.


---

## 🧾API Endpoints
</br>

⭐**You can interact with the API using Swagger UI at `http://localhost:80/docs`**.

</br>

1. Authentication
  ```
    POST /auth/token: Login and get an access token.
  ```

2. Polls
  ```
    POST /polls/cerate: Create a new poll.

    GET /polls/: Get a list of all polls (supports pagination).

    GET /polls/{poll_id}: Get details of a specific poll.
  ```

3. Options
  ```
    PATCH /options/{option_id}: Update an option.
  ```

4. Votes
  ```
    POST /votes/create: Vote on an option.

    DELETE /votes/{vote_id}: Delete a vote.
  ```

---
<!--
### Running Tests

- To run the unit tests, use the following command:
```
docker-compose exec app pytest
```
-->

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Submit a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


---

### 🔗 Connect with Me
<!-- - GitHub: [Visit Profile](https://github.com/erfansafarzad7) -->
- LinkedIn: [Visit Profile](https://linkedin.com/in/erfansafarzad7)
- Email: [Send Me an Email](mailto:erfansafarzad7@gmail.com)
- Telegram: [Send Me Message](https://t.me/erfansafarzad7)

---

Happy Coding! 🎉








   
