
# Task Management Web App

## Overview

This is a simple Task Management Web App built with Flask, MySQL, HTML, and Bootstrap. The app allows users to add, edit, and delete tasks. It provides a user-friendly interface to manage tasks efficiently.

## Features

- Add new tasks
- Edit existing tasks
- Delete tasks

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/mysql/)
- [pip](https://pip.pypa.io/en/stable/) (comes with Python)

## Installation Steps

Follow these steps to set up and run the Task Management Web App:

1. **Clone the Repository**:
   Open your terminal (Command Prompt, PowerShell, etc.) and run:
   \`\`\`
   git clone https://github.com/christiangomonit/task-management.git
   \`\`\`

2. **Navigate to the Project Directory**:
   \`\`\`
   cd task-management
   \`\`\`

3. **Create a Virtual Environment**:
   (Optional but recommended)
   \`\`\`
   python -m venv venv
   \`\`\`

4. **Activate the Virtual Environment**:
   - **Windows**:
     \`\`\`
     venv\Scripts\activate
     \`\`\`
   - **macOS/Linux**:
     \`\`\`
     source venv/bin/activate
     \`\`\`

5. **Install Required Packages**:
   Install the necessary Python packages using pip:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`
   If you don’t have a `requirements.txt`, you can create one with:
   \`\`\`
   pip freeze > requirements.txt
   \`\`\`

6. **Set Up the MySQL Database**:
   - Open your MySQL command line and create a new database:
     \`\`\`
     CREATE DATABASE mydb;
     USE mydb;

     CREATE TABLE tasks (
         id INT AUTO_INCREMENT PRIMARY KEY,
         title VARCHAR(255) NOT NULL,
         description TEXT,
         due_date DATE
     );
     \`\`\`
   - Adjust the database connection settings in your application code if necessary.

7. **Run the Application**:
   \`\`\`
   python app.py
   \`\`\`

8. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

- **Add Task**: Click on the "Add Task" button and fill out the form to add a new task.
- **Edit Task**: Click the "Edit" button next to any task to modify it.
- **Delete Task**: Click the "Delete" button next to any task to remove it.