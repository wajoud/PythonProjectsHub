import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.categories = set()

    def add_expense(self, date, amount, category):
        self.expenses.setdefault(category, []).append((date, amount))

    def add_category(self, category):
        self.categories.add(category)

    def view_expenses(self):
        expenses_summary = {category: sum(amount for _, amount in items) for category, items in self.expenses.items()}
        return expenses_summary

    def add_expense_dialog(self):
        date = simpledialog.askstring("Input", "Enter date (YYYY-MM-DD):", parent=window)
        amount = simpledialog.askfloat("Input", "Enter amount:", parent=window)
        category = simpledialog.askstring("Input", "Enter category:", parent=window)
        if date and amount and category:
            self.add_expense(date, amount, category)
            messagebox.showinfo("Success", "Expense added successfully.", parent=window)

    def add_category_dialog(self):
        category = simpledialog.askstring("Input", "Enter new category:", parent=window)
        if category:
            self.add_category(category)
            messagebox.showinfo("Success", "Category added successfully.", parent=window)

    def display_pie_chart(self):
        # Calculate total amount per category
        amounts = [sum(amount for _, amount in self.expenses[category]) for category in self.expenses]
        categories = list(self.expenses.keys())

        if not amounts:
            messagebox.showinfo("No Data", "No expenses to display.", parent=window)
            return

        # Plot the pie chart
        fig, ax = plt.subplots()
        ax.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Embed the pie chart in the Tkinter window
        chart = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
        chart.draw()
        chart.get_tk_widget().pack()

# Tkinter window setup
window = tk.Tk()
window.title("Expense Tracker")

tracker = ExpenseTracker()

# Buttons
add_expense_button = tk.Button(window, text="Add Expense", command=tracker.add_expense_dialog)
add_expense_button.pack()

add_category_button = tk.Button(window, text="Add Category", command=tracker.add_category_dialog)
add_category_button.pack()

view_pie_chart_button = tk.Button(window, text="Display Pie Chart", command=tracker.display_pie_chart)
view_pie_chart_button.pack()

exit_button = tk.Button(window, text="Exit", command=window.quit)
exit_button.pack()

# Run the Tkinter loop
window.mainloop()
