# Simple-Login-System

# Problem Statement

In many web-based applications, maintaining a secure and persistent user login session is a challenge, especially across multiple browser tabs or page reloads. Traditional session-based authentication systems may fail to preserve user login states efficiently.
The problem is to design and implement a simple, persistent, and cross-tab login system using Streamlit that allows users to register, log in, stay logged in using cookies, and log out securely.

# Approach / Methodology / Data Structures Used
Approach

The project is implemented using Python and Streamlit, focusing on simplicity and session persistence. The system follows these steps:

User credentials are stored in a CSV file (users.csv).

During login, user credentials are verified against the stored data.

Upon successful login:

Encrypted cookies are created to store login status and username.

Streamlit session state is synchronized with cookies.

Cookies allow the user to remain logged in even after page reloads or across browser tabs.

Logout clears both cookies and session state.

# Technologies Used

Python

Streamlit

CSV file handling

EncryptedCookieManager

# Data Structures Used

Dictionary:
Used to store and retrieve user credentials loaded from the CSV file.

CSV File:
Acts as persistent storage for usernames and passwords.

Session State:
Maintains login state during app execution.

Cookies:
Ensures cross-tab and persistent authentication.

# Sample Input / Output
Sample Input

Username: admin

Password: admin123

# Sample Output

Successful login message:
“Welcome, admin 👋”

User remains logged in even after refreshing the page.

On clicking Logout, the user is redirected to the login screen.

# Challenges Faced

Maintaining Persistent Login:
Streamlit does not natively support persistent sessions across tabs.

Cookie Synchronization:
Ensuring cookies and session state remain consistent.

Secure Storage of Credentials:
Handling user data using a CSV file while maintaining simplicity.

Page Reload Handling:
Preventing users from being logged out unintentionally.

Scope for Improvement

Password Hashing:
Implement hashing techniques (e.g., bcrypt) instead of plain-text passwords.

Database Integration:
Replace CSV storage with a database like SQLite or PostgreSQL.

Role-Based Access Control:
Add admin and user roles.

Enhanced UI:
Improve design using Streamlit components and themes.

Multi-Factor Authentication:
Add OTP or email verification for better security.
