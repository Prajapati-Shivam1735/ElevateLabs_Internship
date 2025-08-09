🧮 Calculator CLI App

A simple command-line calculator built with Python that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

🚀 Features
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Handles division by zero
Input validation
User-friendly menu
Runs until user chooses to exit

✅ What I Did

- Created a Python script (`calculator.py`) that:
  - Performs basic arithmetic operations (add, subtract, multiply, divide)
  - Accepts user input via the terminal
  - Handles input errors and division by zero
  - Loops until the user chooses to exit
- Structured the code using functions for clarity and reusability.

🛠️ Tools Used
- Python 3
- Text editor - VS Code

🧠 How It Works
- The app displays a menu of operations.
- The user selects an operation and inputs two numbers.
- The result is printed.
- The app repeats until the user chooses to exit.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📝 Console-Based To-Do List Application

A simple, persistent to-do list manager that runs in the terminal.

🛠 What I Did

- Wrote a Python script `todo.py` that runs in the terminal
- Created a menu-driven interface using simple input() prompts
- Used lists to store tasks in memory
- Used file handling (open(), readlines(), write()) to save and load tasks
- Made sure the to-do list is persistent (saved in `tasks.txt`)
- Implemented functions to:
  - Add tasks
  - View tasks
  - Remove tasks
  - Save/load from file

🚀 Features
- Add tasks
- View all tasks
- Remove tasks by number
- Persistent task storage in `tasks.txt`

💻 Tools Used

- Python 
- Text editor - VS Code

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📰 News Headlines Web Scraper

A simple Python script that scrapes top news headlines from a public news website using `requests` and `BeautifulSoup`, and saves them into a `.txt` file.

📌 Objective

Automate data collection from a public news website by scraping top headlines.

✅ What I Did

- Used `requests` to fetch HTML content from a news website (BBC).
- Parsed the HTML using `BeautifulSoup` to extract `<h2>` headline tags.
- Saved the extracted headlines into a `headlines.txt` file.
- Handled basic error checking for HTTP response.
- Documented the process and created setup files (`README.md`, `requirements.txt`).

🛠️ Tools Used
- Python 3.x
- `requests` – for fetching web pages
- `beautifulsoup4` – for parsing HTML

📁 Deliverables
- `news_scraper.py` – Python script for scraping
- `headlines.txt` – Output file with collected headlines

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Build REST API with flask

A simple REST API built with **Python** and **Flask** for managing user data in memory.

Features

- GET /users – Retrieve all users
- GET /users/<id> – Retrieve a single user by ID
- POST /users – Create a new user
- PUT /users/<id> – Update an existing user
- DELETE /users/<id> – Delete a user

What I Did

- Created a Flask application to manage user data.
- Implemented REST API endpoints for:
  - **GET** – Fetch all users or a single user by ID.
  - **POST** – Add new users.
  - **PUT** – Update existing users.
  - **DELETE** – Remove users.
- Stored user data in an **in-memory dictionary** (no database).
- Tested API endpoints using **Postman** and **curl**.
- Wrote clear usage instructions and examples for testing.

Requirements

- Python 
- Flask – Web framework for building REST APIs
- Postman – API testing tool (optional, you can also use curl)
- curl – Command-line tool to test API endpoints
