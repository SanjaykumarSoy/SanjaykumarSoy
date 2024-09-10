import tkinter as tk
from tkinter import ttk

class CookingCompetitionPortal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cooking Competition Portal")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.config(bg="#f0f0f0")
        self.welcome_page()

    def welcome_page(self):
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="Welcome to Cooking Competition Portal", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.subtitle_label = tk.Label(self.root, text="Where culinary skills meet creativity", font=("Arial", 18), bg="#f0f0f0", fg="#000000")
        self.subtitle_label.pack(pady=10)
        self.register_button = tk.Button(self.root, text="Register", command=self.register_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.register_button.pack(pady=10)
        self.login_button = tk.Button(self.root, text="Login", command=self.login_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.login_button.pack(pady=10)

    def register_page(self):
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="Register", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.name_label = tk.Label(self.root, text="Name:", font=("Arial", 14), bg="#f0f0f0", fg="#000000")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root, font=("Arial", 14), width=30)
        self.name_entry.pack()
        self.email_label = tk.Label(self.root, text="Email:", font=("Arial", 14), bg="#f0f0f0", fg="#000000")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root, font=("Arial", 14), width=30)
        self.email_entry.pack()
        self.password_label = tk.Label(self.root, text="Password:", font=("Arial", 14), bg="#f0f0f0", fg="#000000")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, font=("Arial", 14), width=30, show="*")
        self.password_entry.pack()
        self.register_button = tk.Button(self.root, text="Register", command=self.register_user, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.register_button.pack(pady=10)

    def login_page(self):
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="Login", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.email_label = tk.Label(self.root, text="Email:", font=("Arial", 14), bg="#f0f0f0", fg="#000000")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root, font=("Arial", 14), width=30)
        self.email_entry.pack()
        self.password_label = tk.Label(self.root, text="Password:", font=("Arial", 14), bg="#f0f0f0", fg="#000000")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, font=("Arial", 14), width=30, show="*")
        self.password_entry.pack()
        self.login_button = tk.Button(self.root, text="Login", command=self.login_user, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.login_button.pack(pady=10)

    def register_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Add registration logic here
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="Registration successful!", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.login_button = tk.Button(self.root, text="Login", command=self.login_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.login_button.pack(pady=10)

    def login_user(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Add login logic here
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="Login successful!", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.dashboard_button = tk.Button(self.root, text="Dashboard", command=self.dashboard_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.dashboard_button.pack(pady=10)

    def dashboard_page(self):
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="Dashboard", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.recipe_button = tk.Button(self.root, text="Recipe", command=self.recipe_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.recipe_button.pack(pady=10)
        self.judge_button = tk.Button(self.root, text="Judge", command=self.judge_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.judge_button.pack(pady=10)

    def recipe_page(self):
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="Recipe", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.add_recipe_button = tk.Button(self.root, text="Add Recipe", command=self.add_recipe_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.add_recipe_button.pack(pady=10)
        self.view_recipe_button = tk.Button(self.root, text="View Recipe", command=self.view_recipe_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.view_recipe_button.pack(pady=10)

    def add_recipe_page(self):
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="Add Recipe", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.name_label = tk.Label(self.root, text="Name:", font=("Arial", 14), bg="#f0f0f0", fg="#000000")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root, font=("Arial", 14), width=30)
        self.name_entry.pack()
        self.ingredients_label = tk.Label(self.root, text="Ingredients:", font=("Arial", 14), bg="#f0f0f0", fg="#000000")
        self.ingredients_label.pack()
        self.ingredients_entry = tk.Entry(self.root, font=("Arial", 14), width=30)
        self.ingredients_entry.pack()
        self.instructions_label = tk.Label(self.root, text="Instructions:", font=("Arial", 14), bg="#f0f0f0", fg="#000000")
        self.instructions_label.pack()
        self.instructions_entry = tk.Entry(self.root, font=("Arial", 14), width=30)
        self.instructions_entry.pack()
        self.add_recipe_button = tk.Button(self.root, text="Add Recipe", command=self.add_recipe, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.add_recipe_button.pack(pady=10)

    def view_recipe_page(self):
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="View Recipe", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.view_recipe_button = tk.Button(self.root, text="View Recipe", command=self.view_recipe, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.view_recipe_button.pack(pady=10)

    def add_recipe(self):
        name = self.name_entry.get()
        ingredients = self.ingredients_entry.get()
        instructions = self.instructions_entry.get()
        # Add recipe logic here
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="Recipe added successfully!", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.view_recipe_button = tk.Button(self.root, text="View Recipe", command=self.view_recipe_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.view_recipe_button.pack(pady=10)

    def view_recipe(self):
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="Recipe viewed successfully!", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.view_recipe_button = tk.Button(self.root, text="View Recipe", command=self.view_recipe_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.view_recipe_button.pack(pady=10)

    def judge_page(self):
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="Judge", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.view_judges_button = tk.Button(self.root, text="View Judges", command=self.view_judges_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.view_judges_button.pack(pady=10)
        self.add_judge_button = tk.Button(self.root, text="Add Judge", command=self.add_judge_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.add_judge_button.pack(pady=10)

    def view_judges_page(self):
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="View Judges", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.view_judges_button = tk.Button(self.root, text="View Judges", command=self.view_judges_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.view_judges_button.pack(pady=10)

    def add_judge_page(self):
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="Add Judge", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.name_label = tk.Label(self.root, text="Name:", font=("Arial", 14), bg="#f0f0f0", fg="#000000")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root, font=("Arial", 14), width=30)
        self.name_entry.pack()
        self.add_judge_button = tk.Button(self.root, text="Add Judge", command=self.add_judge, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.add_judge_button.pack(pady=10)

    def add_judge(self):
        name = self.name_entry.get()
        # Add judge logic here
        self.clear_frame()
        self.title_label = tk.Label(self.root, text="Judge added successfully!", font=("Arial", 24), bg="#f0f0f0", fg="#000000")
        self.title_label.pack(pady=20)
        self.view_judges_button = tk.Button(self.root, text="View Judges", command=self.view_judges_page, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
        self.view_judges_button.pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CookingCompetitionPortal()
    app.run()
