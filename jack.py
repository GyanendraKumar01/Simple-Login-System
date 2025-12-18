import streamlit as st
import csv
import os
from streamlit_cookies_manager import EncryptedCookieManager

CSV_FILE = "users.csv"

# --- Cookie Manager ---
cookies = EncryptedCookieManager(
    prefix="login_system",  # same prefix across apps
    password="your-secret-password"  # use a secure value
)

if not cookies.ready():
    st.stop()

# --- Initialization from cookies ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = cookies.get("logged_in") == "True"

if "username" not in st.session_state:
    st.session_state.username = cookies.get("username")

# --- Utility Functions ---
def load_users():
    users = {}
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                users[row["username"]] = row["password"]
    return users

def authenticate(username, password):
    users = load_users()
    return username in users and users[username] == password

def add_user(username, password):
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["username", "password"])
        writer.writerow([username, password])

def login(username, password):
    if authenticate(username, password):
        # Save login info in cookies
        cookies["logged_in"] = "True"
        cookies["username"] = username
        cookies.save()

        # Sync session_state with cookies
        st.session_state.logged_in = True
        st.session_state.username = username

        st.rerun()
    else:
        st.error("Invalid username or password")

def logout():
    cookies["logged_in"] = "False"
    cookies["username"] = ""
    cookies.save()

    st.session_state.logged_in = False
    st.session_state.username = None

    st.success("Logged out successfully")
    st.rerun()

# --- UI ---
st.title("Login System with Cookies (Cross-Tab)")

if not st.session_state.logged_in:
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        login(username, password)

    st.divider()
    st.subheader("Register (If not done)")

    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")

    if st.button("Register"):
        add_user(new_user, new_pass)
        st.success("User registered successfully!")

else:
    st.success(f"Welcome, {st.session_state.username} 👋")
    if st.button("Logout"):
        logout()
