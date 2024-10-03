# README

## Project Title: Flask Web Application

### Description
This is a web application built with Flask that incorporates various tasks demonstrating different functionalities such as user management, random number generation, and interaction with external APIs (specifically Codeforces). The application also includes user registration, email verification, and session management for authenticated users.

### Features
- **Menu Navigation**: Home page displays links to various tasks.
- **Random Mark Generation**: A route that generates a random number as a mark.
- **Codeforces Profile Information**: Users can retrieve and display information about Codeforces users.
- **Pagination**: Results can be paginated for better UI experience.
- **Santa Toss Game**: A fun feature where users can create and join a game.
- **Sign Up / Sign In**: User registration and login functionality with email verification.
- **Task Management**: Allows users to create, view, and manage tasks.

### Requirements
- Python 3.6+
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- Requests
- Werkzeug
- A working SMTP server for email functionality.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set environment variables for sensitive data (e.g., secret keys, email credentials):
   ```bash
   export secret=<your_secret_key>
   export token=<your_token>
   export site_key=<your_recaptcha_site_key>
   ```

4. Initialize your database:
   Ensure that the database is set up properly according to your application needs.

### Usage
1. Run the application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000/` to access the web application.

### Routes Overview
- `/`: Display menu links to other tasks.
- `/haba/`: A simple greeting page.
- `/task1/random/`: Returns a random mark.
- `/task1/i_will_not/`: Displays a repetitive statement.
- `/task2/cf/profile/<username>/`: Fetches and displays Codeforces user info.
- `/task3/cf/profile/<handle>/`: Fetches and displays Codeforces user problems subsmissions
- `/task4/santa/create`: Create a Santa game.
- `/task5/sign-up`: User registration process.
- `/task5/sign-in`: User sign in process.
