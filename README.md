Financial Market Data API

A Python-based REST API built with FastAPI that provides endpoints for stock lookup, stock comparison, and external market news retrieval. The project demonstrates backend API development, external API integration, and automated CI validation using GitHub Actions.

Features

• Retrieve stock information by symbol
• Compare multiple stocks and calculate price changes
• Fetch external market-related data using an API
• Automatic API documentation via FastAPI Swagger UI
• Continuous Integration pipeline using GitHub Actions

Technologies Used

Python
FastAPI
Requests
Pandas
Uvicorn
Git
GitHub Actions (CI pipeline)

Project Structure
financial-market-api
├── .github/workflows/ci.yml
├── venv
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/financial-market-api.git
cd financial-market-api

Create a virtual environment:

python -m venv venv

Activate it:

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
Running the API

Start the server with:

uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000
API Documentation

FastAPI automatically generates interactive API documentation.

Open:

http://127.0.0.1:8000/docs
Example Endpoints
Get stock information
GET /stock/AAPL

Example response:

{
  "symbol": "AAPL",
  "price": 212.45,
  "previous_close": 210.10,
  "currency": "USD"
}
Compare stocks
GET /compare?symbols=AAPL,MSFT,GOOG
Fetch market news
GET /market-news
Continuous Integration

The project includes a GitHub Actions CI pipeline that runs automatically on every push. The workflow:

Checks out the repository

Installs project dependencies

Validates that the FastAPI application loads successfully

Workflow file:

.github/workflows/ci.yml
Purpose

This project demonstrates:

• REST API development with Python
• Integration with external APIs
• Data processing using Pandas
• Dependency management
• Automated CI validation using GitHub Actions