import tkinter as tk
from gui import main_gui
from database import initialize_db


def main():
    print("Initializing the Intelligent Tutoring System...")
    initialize_db()
    print("Database initialized successfully.")

    # Launching the main GUI
    main_gui()
    print("Application closed.")


if __name__ == "__main__":
    main()
