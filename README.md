# AI Job Agent

An AI-powered automation system that scrapes job listings, semantically matches them against a resume, generates ATS-optimized tailored resumes, and exports personalized resume documents using local LLMs.

---

# Features

## Job Scraping & Automation

- LinkedIn job scraping using Playwright
- Multi-page job detail extraction
- Structured job data collection
- Duplicate job detection
- Automated browser workflows

---

## Database & Persistence

- PostgreSQL integration
- SQLAlchemy ORM architecture
- Persistent job storage
- Database ingestion pipeline
- JSON data persistence

---

## AI-Powered Resume Intelligence

- Resume parsing from PDF and DOCX
- Semantic job matching using embeddings
- Local AI inference using Ollama
- ATS keyword extraction
- AI-powered resume bullet rewriting
- Tailored resume generation
- DOCX resume export

---

# Tech Stack

## Backend

- Python

## Browser Automation

- Playwright
- Chromium

## Database

- PostgreSQL
- SQLAlchemy
- psycopg2
- pgAdmin4

## AI / Machine Learning

- Ollama
- Llama3
- nomic-embed-text
- NumPy

## Document Processing

- PyMuPDF
- python-docx

## Storage & Version Control

- JSON
- Git
- GitHub

---

# Project Architecture

```text
LinkedIn Scraper
        ↓
Job Extraction Pipeline
        ↓
JSON / PostgreSQL Persistence
        ↓
Resume Parsing
        ↓
Semantic Embedding Matching
        ↓
ATS Keyword Extraction
        ↓
AI Resume Tailoring
        ↓
DOCX Resume Generation
```

---

# Current Capabilities

The system can:

1. Scrape job listings from LinkedIn
2. Extract detailed job descriptions
3. Parse uploaded resumes
4. Match resumes against jobs semantically
5. Identify ATS keywords from job descriptions
6. Rewrite resume bullets using local LLMs
7. Generate tailored resumes for target jobs
8. Export AI-tailored resumes as DOCX files

---

# Local AI Setup

## Install Ollama

https://ollama.com/download

---

## Pull Required Models

```bash
ollama pull nomic-embed-text
ollama pull llama3
```

---

# Installation

## Clone Repository

```bash
git clone <your-repo-url>
cd ai-job-agent
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running The Project

## Run Main Pipeline

```bash
python main.py
```

---

## Run AI Matching

```bash
python -m app.ai.test_matcher
```

---

## Run Resume Tailoring

```bash
python -m app.ai.test_rewriter
```

---

## Run Resume Export

```bash
python -m app.ai.test_export_resume
```

---

# Project Status

## Completed

- Playwright browser automation
- LinkedIn scraping pipeline
- PostgreSQL integration
- SQLAlchemy ORM setup
- JSON persistence
- Duplicate detection
- Resume parsing
- Semantic AI job matching
- Ollama local AI integration
- ATS keyword extraction
- AI resume rewriting
- Tailored resume generation
- DOCX export pipeline

---

# Future Improvements

- Multi-platform job support
- Full-stack UI dashboard
- Human approval workflows
- Resume analytics
- Explainable AI feedback
- Advanced ATS scoring
- Automated application workflows

---

# Important Note

This project is intended for educational, research, and portfolio purposes.

Users are responsible for complying with:

- platform Terms of Service
- applicable laws
- ethical automation practices

The project is designed around human-assisted AI workflows rather than uncontrolled mass automation.

---

# Learning Outcomes

This project covers concepts from:

- Backend Engineering
- Browser Automation
- AI Engineering
- Applied LLM Engineering
- Semantic Search
- Database Systems
- Workflow Automation
- Document Processing
- Prompt Engineering
- System Design

---

# License

MIT License
