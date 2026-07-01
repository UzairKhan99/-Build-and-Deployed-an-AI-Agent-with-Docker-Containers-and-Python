# Dockerized AI Agent API

## Project Overview

This project is a Dockerized FastAPI backend for an AI Agent application.

The current version focuses on setting up a clean backend structure, connecting FastAPI with a MySQL database running inside Docker, saving agent requests into the database, and reading saved messages through API routes.

The AI logic will be added later using LangChain and LangGraph.

## Current Features

1. FastAPI backend
2. Dockerized application setup
3. MySQL database running inside Docker
4. Database persistence using Docker volume
5. SQLModel based table model
6. API route to save agent messages
7. API route to fetch saved messages
8. Health check route for database connection
9. FastAPI Swagger documentation for testing APIs
10. MySQL Workbench support for visual database viewing

## Tech Stack

Python
FastAPI
Docker
Docker Compose
MySQL
SQLModel
SQLAlchemy
PyMySQL
Pydantic

Future AI stack:

LangChain
LangGraph
OpenAI API

## Project Structure

```text
AI AGENT WITH DOCKER/
│
├── backend/
│   └── src/
│       ├── main.py
│       ├── database.py
│       └── chat/
│           ├── models.py
│           └── routing.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .env.example
└── README.md
```

## How The Project Works

The project has two main Docker containers.

1. Backend container

This container runs the FastAPI application.

2. Database container

This container runs MySQL.

FastAPI connects to the MySQL container using:

```text
db:3306
```

MySQL Workbench connects to the same Docker MySQL database using:

```text
127.0.0.1:3307
```

The database data is saved inside a Docker volume called:

```text
mysql_data
```

## Important Port Explanation

FastAPI runs on:

```text
localhost:8000
```

MySQL inside Docker runs on:

```text
db:3306
```

MySQL Workbench connects from the laptop using:

```text
127.0.0.1:3307
```

So the same Docker MySQL database can be accessed in two ways:

FastAPI uses `db:3306`
Workbench uses `127.0.0.1:3307`

## Environment Variables

Create a `.env` file in the root directory.

```env
DATABASE_URL=mysql+pymysql://ai_user:ai_password@db:3306/ai_agent_db
```

Example `.env.example`:

```env
DATABASE_URL=mysql+pymysql://ai_user:ai_password@db:3306/ai_agent_db
```

Do not upload real secret keys to GitHub.

## Docker Compose Services

The project uses Docker Compose to run:

1. FastAPI backend
2. MySQL database

MySQL database details:

```text
Database name: ai_agent_db
Username: ai_user
Password: ai_password
Root password: rootpassword
Host for Workbench: 127.0.0.1
Port for Workbench: 3307
```

## Installation And Setup

### 1. Clone The Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Create Environment File

Create a `.env` file and add:

```env
DATABASE_URL=mysql+pymysql://ai_user:ai_password@db:3306/ai_agent_db
```

### 3. Build And Run The Project

```bash
docker compose up --build
```

This command will:

1. Build the FastAPI backend image
2. Pull the MySQL image if needed
3. Start the backend container
4. Start the MySQL container
5. Create the MySQL database
6. Create the database volume

### 4. Stop The Project

```bash
docker compose down
```

This stops the containers but keeps the database data because the volume is still saved.

To delete database data completely:

```bash
docker compose down -v
```

Use this only when you want to reset the database.

## API Documentation

After running the project, open:

```text
http://localhost:8000/docs
```

FastAPI Docs allows you to test all API routes visually.

## API Routes

### 1. Home Route

```text
GET /
```

Checks if the API is running.

Example response:

```json
{
  "message": "AI Agent API is running"
}
```

### 2. Health Check Route

```text
GET /health
```

Checks if the backend can reach the database.

Example response:

```json
{
  "status": "ok",
  "database": "reachable"
}
```

### 3. Database Test Route

```text
GET /db-test
```

Shows which database the backend is connected to.

Example response:

```json
{
  "connected_database": "ai_agent_db"
}
```

### 4. Save Agent Message

```text
POST /agent/run
```

Saves a user message into the MySQL database.

Example request:

```json
{
  "message": "Hey Agent How are You"
}
```

Example response:

```json
{
  "id": 1,
  "status": "success",
  "message": "Agent request saved successfully. AI logic will be added later.",
  "input": "Hey Agent How are You"
}
```

### 5. Get All Saved Agent Messages

```text
GET /agent/runs
```

Fetches all saved messages from the database, with the newest messages first.

Example response:

```json
[
  {
    "id": 3,
    "message": "Hey Agent How are You",
    "response": "Agent request saved successfully. AI logic will be added later.",
    "status": "success"
  }
]
```

## Viewing Database In MySQL Workbench

Open MySQL Workbench and create a new connection.

Use these values:

```text
Connection Name: AI Agent Docker DB
Hostname: 127.0.0.1
Port: 3307
Username: ai_user
Password: ai_password
Default Schema: ai_agent_db
```

After connecting, run:

```sql
USE ai_agent_db;

SHOW TABLES;

SELECT * FROM agent_runs;
```

You should see the saved API messages inside the `agent_runs` table.

## Database Table

The project currently uses one table:

```text
agent_runs
```

Columns:

```text
id
message
response
status
```

This table stores every message sent to the `/agent/run` API route.

## Development Notes

The backend code is mounted using Docker volume:

```text
./backend/src:/app
```

This means changes in the local `backend/src` folder are reflected inside the backend container.

If you install new Python packages, rebuild the containers:

```bash
docker compose up --build
```

## Future Improvements

1. Add real AI logic using LangChain
2. Add LangGraph workflow
3. Add supervisor agent
4. Add research tool
5. Add email sending tool
6. Add authentication
7. Add frontend dashboard
8. Add chat history UI
9. Add deployment support for Railway or Render
10. Add production database configuration

## Project Status

Current status:

Database connected successfully
FastAPI routes working
Messages saving into MySQL
Messages visible in MySQL Workbench
AI logic pending

## Author

Uzair Khan

## License

This project is for learning and development purposes.
