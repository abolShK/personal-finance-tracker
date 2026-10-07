import tkinter as tk
from gui.transaction_window import open_income_window

def start_app():
    window = tk.Tk()

    window.title("Personal Finance Tracker")
    window.geometry("800x600")

    title = tk.Label(
        window,
        text="Personal Finance Tracker",
        font=("Arial", 24)
    )

    title.pack(pady=30)

    add_income_button = tk.Button(
        window,
        text="Add Income",
        command= lambda: open_income_window(window)
    )

    add_income_button.pack(pady=10)

    add_expense_button = tk.Button(
        window,
        text="Add Expense"
    )

    add_expense_button.pack(pady=10)

    transactions_button = tk.Button(
        window,
        text="Transactions"
    )

    transactions_button.pack(pady=10)

    reports_button = tk.Button(
        window,
        text="Reports"
    )

    reports_button.pack(pady=10)

    window.mainloop()