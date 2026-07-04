# Contact Book

A command-line contact management application built with Python and SQLite.

## Features
- Add contacts with name, email and phone validation
- Search contacts by partial name match
- View all contacts
- Update specific contact fields without affecting others
- Delete contacts by ID
- Data persists between sessions using SQLite database

## Concepts used
- Object Oriented Programming (2 classes: ContactBook, Contact)
- SQLite database with sqlite3 (no external dependencies)
- CRUD operations (Create, Read, Update, Delete)
- **kwargs for flexible contact updates
- SQL LIKE operator for partial name search
- Type hints on Contact class

## Requirements
Python 3.x (no external libraries needed)

## How to run
python contact_book.py

## Menu options
| Option | Description |
|--------|-------------|
| 1 | Add a new contact |
| 2 | Delete a contact by ID |
| 3 | Show all contacts |
| 4 | Find a contact by name |
| 5 | Update a contact |
| 6 | Quit |

## Database schema
```sql
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT
)
```
