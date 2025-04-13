import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AdminDashboard:
    def __init__(self, root, username):
        self.root = root
        self.root.title(f"Admin - {username}")
        self.username = "Wendy Mathonsi"
        self.center_window(400, 300)

        self.create_widgets()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        # Row 0: Verifications
        verification_button = ttk.Button(self.root, text="Verifications", command=self.show_verifications)
        verification_button.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

        # Row 1: Reports or Suggestions
        reports_button = ttk.Button(self.root, text="Reports / Suggestions", command=self.view_reports)
        reports_button.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

        # Row 2: Data
        data_button = ttk.Button(self.root, text="View Data", command=self.view_data)
        data_button.grid(row=2, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

        # Row 3: Shutdown the app for updates
        shutdown_button = ttk.Button(self.root, text="Shutdown for Updates", command=self.shutdown_app)
        shutdown_button.grid(row=3, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

        # Row 4: Exit
        exit_button = ttk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.grid(row=4, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

        # Configure column weights for resizing
        self.root.grid_columnconfigure(0, weight=1)

    def show_verifications(self):
        messagebox.showinfo("Verifications", "Functionality to handle verifications will be implemented here.")

    def view_reports(self):
        messagebox.showinfo("Reports / Suggestions", "Displaying reports and suggestions...")

    def view_data(self):
        messagebox.showinfo("Data", "Displaying application data...")

    def shutdown_app(self):
        response = messagebox.askyesno("Shutdown", "Are you sure you want to shutdown the application for updates?")
        if response:
            messagebox.showinfo("Shutdown", "Application is shutting down...")
            self.root.quit()

if __name__ == '__main__':
    root = tk.Tk()
    dashboard = AdminDashboard(root, "Wendy Mathonsi") # Replace "admin" with the actual admin username
    root.mainloop()