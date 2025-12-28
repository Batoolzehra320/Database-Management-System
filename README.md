# Terminal-Based Database Management System

This is a **command-line Database Management System (DBMS)** written in **Python**. It allows users to create, manage, and manipulate databases directly from the terminal using CSV files. No graphical interface is required.

## Features

- Create a new database with custom fields.
- Open and work with existing databases.
- Add new records to the database.
- Delete or clear specific field values from records.
- Search for records based on field values.
- Display all records in a database.
- Fully terminal-based, lightweight, and easy to use.

## How It Works

- Databases are stored as **CSV files**.
- Python's **`csv`** and **`os`** modules are used for file handling and management.
- Implements modular functions for each operation (create, open, add, delete, search, display).
- Uses loops and input validation to guide users through operations.

## Requirements

- Python 3.x installed on your system.
- No external libraries required.

## How to Run

1. Clone or download the repository.
2. Open a terminal and navigate to the project folder.
3. Run the script:

```bash
python dbms.py
