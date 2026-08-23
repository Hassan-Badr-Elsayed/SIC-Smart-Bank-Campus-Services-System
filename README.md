# SIC Smart Bank System

## Program Overview

SIC Smart Bank is a console-based banking system built with Python.

The program allows users to:
- Create an account
- Log in
- Deposit money
- Withdraw money
- Transfer money
- View transaction history
- Update personal information

User data is stored in a `users.json` file.

## Main Menu

The main menu contains three options:

- `login` — Log in to an existing account.
- `register` — Create a new account.
- `exit` — Exit the program.

## Registration

When registering, the user enters:

- Name
- Password
- Phone number
- Email
- Gender
- Age
- City
- Account type

The program checks that the phone number and email are not already registered.

A unique ID is generated for every new user.

## Login

Users log in using their ID and password.

The user has 3 password attempts.

The system supports two types of accounts:

- **Admin** — Has access to reports and ATM management.
- **User** — Has access to normal banking operations.

## Banking Operations

### Deposit

Users can deposit money using:

- EGP
- SAR
- USD

SAR and USD are converted to EGP using the exchange rates defined in the program.

### Withdraw

Users can withdraw money from their balance.

The program prevents users from withdrawing more money than they have.

### Transfer

Users can transfer money to another user using their ID.

The program checks that:
- The target user exists.
- The user is not transferring to themselves.
- The amount is valid.
- The sender has enough balance.

### Transaction History

Users can view their previous transactions, including deposits, withdrawals, and transfers.

## Admin Reports

Admins have access to a Reports section.

### Duplicate Detection

Finds duplicate phone numbers and email addresses using sets.

### User Set Analysis

Analyzes users using:

- Union
- Intersection
- Difference
- Symmetric Difference

### Transaction Reports

Shows transaction frequency and repeated transaction types.

### Membership Check

Checks whether a user belongs to groups such as:

- Active users
- VIP users
- Users with failed logins
- Users who made transfers

## ATM Management

The ATM system uses a 2D matrix.

- `1` = Available
- `0` = Out of Service

The admin can:

- Display the ATM matrix
- Count available and unavailable ATMs
- Update an ATM status

## Personal Information

Users can update:

- City
- Phone number
- Password
- Emergency contact
- Optional profile fields

All changes are saved to the JSON file.

## Data Storage

The program uses Python's `json` module.

User data is loaded from:

`users.json`

Whenever user data is changed, the `save_users()` function saves the updated data back to the JSON file.

## Project Files

- `main.py` — Main Python program.
- `users.json` — Stores users, wallet data, and transaction history.
- `README.md` — Project documentation.

## Requirements

- Python 3.x
- `users.json` must be in the same folder as the Python file.

## How to Run

```bash
python main.py
