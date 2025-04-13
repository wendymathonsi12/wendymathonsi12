# main_app.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Admin_Dashboard import  AdminDashboard
from Clients_Dashboard import ClientDashboard
 


class SplashScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Loading...")
        self.root.overrideredirect(True)  # Remove window borders

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 300
        height = 550
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="white", highlightthickness=0)
        self.canvas.pack(pady=20)

      
        center_x = width // 2
        center_y = height // 2
        radius = 100
        self.canvas.create_oval(center_x - radius, center_y - radius,
                                center_x + radius, center_y + radius,
                                fill="cyan", outline="cyan")


        self.canvas.create_text(center_x, center_y, text="Health IO",
                                font=("Arial", 24, "bold"), fill="white")

        self.root.after(10000, self.load_login_page)  # Show splash for 2 seconds

    def load_login_page(self):
        self.root.destroy()
        login_root = tk.Tk()
        app = LoginPage(login_root)
        login_root.mainloop()

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.center_window(300, 500)

        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(expand=True, fill="both")

        # Admin Login Section (Left)
        admin_frame = ttk.LabelFrame(main_frame, text="Admin Login", padding="10")
        admin_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(admin_frame, text="Username:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.admin_username_entry = ttk.Entry(admin_frame)
        self.admin_username_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(admin_frame, text="Password:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.admin_password_entry = ttk.Entry(admin_frame, show="0")
        self.admin_password_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        admin_login_button = ttk.Button(admin_frame, text="Admin Login", command=self.login_admin)
        admin_login_button.grid(row=2, column=0, columnspan=2, pady=10)

        admin_frame.columnconfigure(1, weight=1)

        # Client Login Section (Right)
        client_frame = ttk.LabelFrame(main_frame, text="Client Login", padding="10")
        client_frame.grid(row=0, column=1, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(client_frame, text="Username:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.client_username_entry = ttk.Entry(client_frame)
        self.client_username_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(client_frame, text="Password:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.client_password_entry = ttk.Entry(client_frame, show="*")
        self.client_password_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        client_login_button = ttk.Button(client_frame, text="Client Login", command=self.login_client)
        client_login_button.grid(row=2, column=0, columnspan=2, pady=10)

        client_signup_button = ttk.Button(client_frame, text="Client Sign Up", command=self.show_client_signup_page)
        client_signup_button.grid(row=3, column=0, columnspan=2, pady=5)

        client_frame.columnconfigure(1, weight=1)

        # Configure grid weights for the main frame to make sections resize equally
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2) 
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def login_admin(self):
        username = self.admin_username_entry.get()
        password = self.admin_password_entry.get()
        if username == "wendymathonsi" and password == "********":
            messagebox.showinfo("Admin Priviledges", f"ACCESS GRANTED!")
            self.root.destroy()
            admin_root = tk.Tk()
            admin_dashboard = AdminDashboard(admin_root, username)
            admin_root.mainloop()
        else:
            messagebox.showerror("Admin Login Failed", "Invalid admin username or password.")

    def login_client(self):
        username = self.client_username_entry.get()
        password = self.client_password_entry.get()
        if username == "client" and password == "client": # Replace with your actual client auth
            messagebox.showinfo("Client Login Successful", f"Welcome, {username}!")
            self.root.destroy()
            client_root = tk.Tk()
            client_dashboard = ClientDashboard(client_root, username)
            client_root.mainloop()
        else:
            messagebox.showerror("Client Login Failed", "Invalid client username or password.")

    def show_client_signup_page(self):
        signup_window = tk.Toplevel(self.root)
        signup_page = ClientSignupPage(signup_window)

class ClientSignupPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Sign Up")
        self.center_window(300, 200)

        signup_frame = ttk.Frame(self.root, padding="20")
        signup_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(signup_frame, text="New Username:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.new_username_entry = ttk.Entry(signup_frame)
        self.new_username_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(signup_frame, text="New Password:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.new_password_entry = ttk.Entry(signup_frame, show="*")
        self.new_password_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        signup_button = ttk.Button(signup_frame, text="Sign Up", command=self.signup_client)
        signup_button.grid(row=2, column=0, columnspan=2, pady=10)

        signup_frame.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def signup_client(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()
        # In a real application, you would store this in a database
        if new_username and new_password:
            messagebox.showinfo("Sign Up Successful", "Client account created successfully!")
            self.root.destroy() # Close the signup window
        else:
            messagebox.showerror("Sign Up Failed", "Please enter both username and password.")

class AdminApplication:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Admin Dashboard")
        self.center_window(900, 300)

        label = ttk.Label(root, text=f"Welcome, Admin: {username}!", padding=20)
        label.pack()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

class ClientApplication:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Client Dashboard")
        self.center_window(600, 400)
        label = ttk.Label(root, text=f"Welcome, Client: {username}!", padding=20)
        label.pack()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    splash_root = tk.Tk()
    splash = SplashScreen(splash_root)
    splash_root.mainloop()