## AI-Powered Healthcare Professional (HCP) Interaction Management System

AI CRM is an AI-powered Customer Relationship Management system designed to help users manage Healthcare Professional (HCP) interactions through natural language conversations.

The system allows users to log meetings, retrieve interaction details, update records, schedule follow-ups, and view complete interaction history using an AI assistant.

This project combines a React frontend, FastAPI backend, PostgreSQL database, and LangGraph-based AI agent architecture to create an intelligent CRM workflow.

---

# Features

## AI CRM Assistant

- Natural language interaction with CRM data
- AI agent automatically selects the required CRM tool
- Converts user requests into database operations
- Provides structured responses from stored information

Example:

```
Show me interaction 5
```

The AI assistant retrieves the requested interaction details from the CRM database.

---

# CRM Capabilities

## 1. Log HCP Interaction

Creates and stores new HCP interaction records.

Supported information:

- HCP Name
- Interaction Type
- Interaction Date
- Attendees
- Discussion Summary
- Materials Shared
- Samples Distributed
- Sentiment
- Outcome
- Follow-up Action
- Follow-up Date

Example:

```
Met Dr. Sarah Williams today for a product discussion.
Discussed Product X effectiveness and clinical benefits.
Shared Product X brochure.
Positive sentiment.
```

---

## 2. Retrieve Interaction Details

Retrieves a specific interaction using the interaction ID.

Example:

```
Show me interaction 23
```

Returns:

- HCP details
- Interaction type
- Discussion summary
- Sentiment
- Follow-up information
- Complete interaction record

---

## 3. Edit Interaction

Updates existing interaction information.

Example:

```
Change interaction 23 sentiment to Negative
```

The AI updates the required field while maintaining the remaining interaction details.

---

## 4. Schedule Follow-up

Creates or updates follow-up dates for existing interactions.

Example:

```
Schedule follow up for interaction 23 on 2026-09-10 14:30
```

The system updates the follow-up schedule associated with the interaction.

---

## 5. HCP Interaction History

Retrieves all previous interactions associated with a Healthcare Professional.

Example:

```
Show me Dr. Sarah Williams interaction history
```

Returns previous meetings, discussions, and interaction records.

---

# System Architecture

```
                    User
                      |
                      v
              React Frontend
                      |
                      v
                FastAPI Backend
                      |
                      v
              LangGraph AI Agent
                      |
          -------------------------
          |                       |
          v                       v
      AI Tools              PostgreSQL
          |                       |
          -------------------------
                      |
                      v
          HCP Interaction Records
```

---

# Technology Stack

## Frontend

- React
- Redux Toolkit
- Axios
- CSS

## Backend

- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL

## Artificial Intelligence

- LangGraph
- LangChain
- Groq LLM

## Development Tools

- Git
- GitHub
- PostgreSQL

---

# Project Structure

```
aivoa-ai-crm/

│
├── backend/
│   │
│   ├── app/
│   │   ├── ai/
│   │   │   ├── graph.py
│   │   │   └── tools.py
│   │   │
│   │   ├── routers/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   └── database.py
│   │
│   ├── requirements.txt
│   └── .env.example
│
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatBox.jsx
│   │   │   └── InteractionForm.jsx
│   │   │
│   │   ├── features/
│   │   └── services/
│   │
│   └── package.json
│
│
├── .gitignore
└── README.md
```

---

# Installation and Setup

## Backend Setup

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create environment file:

```
.env
```

Add your API key:

```
GROQ_API_KEY=your_api_key_here
```

Run backend:

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

# Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run application:

```bash
npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

# Database

PostgreSQL is used for persistent storage.

The system stores:

- Healthcare Professional information
- Interaction details
- Meeting summaries
- Sentiment information
- Materials shared
- Samples distributed
- Follow-up schedules
- Interaction history

---

# AI Agent Workflow

```
User Request

      ↓

LangGraph AI Agent

      ↓

Tool Selection

      ↓

FastAPI Backend

      ↓

Database Operation

      ↓

Tool Response

      ↓

AI Generated Response

      ↓

React UI Update
```

---

# Security

Sensitive information is excluded from GitHub using `.gitignore`.

Ignored files include:

```
.env
venv/
node_modules/
```

API keys and private configuration values are stored locally and are not uploaded.

---

# Future Improvements

- User authentication and authorization
- Voice-based interaction logging
- HCP search and filtering
- CRM analytics dashboard
- Automated reports
- AI-generated interaction summaries
- Role-based access control