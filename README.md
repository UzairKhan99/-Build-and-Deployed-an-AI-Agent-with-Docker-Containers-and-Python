# Dockerized AI Agent Web Application

## Project Overview

This project is a Dockerized AI Agent Web Application built using Python, FastAPI, Docker, LangChain/LangGraph, and PostgreSQL.

The application allows users to send a request to an AI agent through an API endpoint. The AI agent can understand the request, use different tools, perform research, store information in a database, and send results through email.

The main goal of this project is to build an AI-powered backend system that can run locally using Docker and can also be deployed online using platforms such as Railway or DigitalOcean.

## Features

* AI agent built with LangChain and LangGraph
* FastAPI backend for handling API requests
* Dockerized development and deployment environment
* Docker Compose support for managing multiple services
* PostgreSQL database integration
* Research tool for gathering information
* Email tool for sending results
* Supervisor agent to manage multiple tools
* Easy deployment using Docker containers

## Tech Stack

* Python
* FastAPI
* Docker
* Docker Compose
* LangChain
* LangGraph
* PostgreSQL
* OpenAI or open-source LLMs
* Railway / DigitalOcean for deployment

## Project Architecture

```text
User Request
     ↓
FastAPI Backend
     ↓
AI Supervisor Agent
     ↓
Agent Tools
 ├── Research Tool
 ├── Email Tool
 └── Database Tool
     ↓
Final Response / Email / Stored Data
```

## Project Structure

```text
project-folder/
│
├── backend/
│   ├── src/
│   │   ├── main.py
│   │   ├── agents/
│   │   ├── tools/
│   │   ├── database/
│   │   └── config.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## How It Works

1. The user sends a request to the FastAPI endpoint.
2. The backend passes the request to the AI supervisor agent.
3. The supervisor agent decides which tool should be used.
4. The research tool can collect information.
5. The database tool can store user requests and results.
6. The email tool can send the final result to the user.
7. The final response is returned through the API.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Create Environment File

Create a `.env` file in the root directory.

```bash
cp .env.example .env
```

Add your environment variables:

```env
OPENAI_API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:password@db:5432/ai_agent_db
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USER=your_email@example.com
EMAIL_PASSWORD=your_email_password
```

### 3. Build and Run with Docker

```bash
docker compose up --build
```

The FastAPI application will run at:

```text
http://localhost:8000
```

## API Documentation

After running the project, open:

```text
http://localhost:8000/docs
```

This will show the automatic FastAPI Swagger documentation.

## Example API Request

```bash
curl -X POST "http://localhost:8000/agent/run" \
-H "Content-Type: application/json" \
-d '{"message": "Research why going outside is good and email me the result."}'
```

## Example Response

```json
{
  "status": "success",
  "message": "Research completed and email sent successfully."
}
```

## Main Components

### FastAPI Backend

FastAPI is used to create API endpoints and handle requests from users.

### Docker

Docker is used to package the application with all dependencies so it can run on any system.

### Docker Compose

Docker Compose is used to manage multiple services such as the backend application and PostgreSQL database.

### LangChain / LangGraph

LangChain and LangGraph are used to create the AI agent workflow and manage tool calling.

### Supervisor Agent

The supervisor agent controls the workflow and decides which tool should be used for each task.

### PostgreSQL Database

PostgreSQL is used to store user requests, responses, and agent activity.

## Roadmap

* Set up Docker and Docker Compose
* Create FastAPI backend
* Add PostgreSQL database
* Build research tool
* Build email-sending tool
* Add LangChain/LangGraph agent
* Create supervisor agent
* Test API endpoints
* Deploy application online

## Future Improvements

* Add frontend interface
* Add user authentication
* Add chat history
* Add file upload support
* Add more AI tools
* Improve error handling
* Add logging and monitoring
* Deploy with CI/CD pipeline

## Deployment

This application can be deployed using Docker-supported platforms such as:

* Railway
* DigitalOcean
* Render
* AWS
* Google Cloud
* Azure

Basic deployment flow:

```text
Build Docker Image
     ↓
Push Image / Connect Repository
     ↓
Set Environment Variables
     ↓
Deploy Container
     ↓
Access AI Agent Online
```

## Author

Uzair Khan

## License

This project is for learning and development purposes. You can update the license according to your requirement.
