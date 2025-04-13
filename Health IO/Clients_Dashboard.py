import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ClientDashboard:
    
    def __init__(self, root, username):
        self.root = root
        self.root.title(f"Client Dashboard - {username}")
        self.username = username
        self.center_window(600, 400)

        self.create_widgets()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        # Row 0: Diseases and Disorders (Dropbox)
        disorders_label = ttk.Label(self.root, text="Diseases and Disorders:")
        disorders_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.disorders_list = ["Flu", "Headache", "Allergy", "Diabetes", "Hypertension"] # Sample data
        self.disorders_combo = ttk.Combobox(self.root, values=self.disorders_list)
        self.disorders_combo.grid(row=0, column=1, padx=10, pady=10, sticky=(tk.W, tk.E))
        self.disorders_combo.set("Select a disorder")

        # Row 1: Recommended Medications
        medications_label = ttk.Label(self.root, text="Recommended Medications:")
        medications_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.medications_text = tk.Text(self.root, height=3, width=40)
        self.medications_text.insert(tk.END, "Medication A - Pharmacy X: $10\nMedication B - Pharmacy Y: $15\nMedication A - Pharmacy Z: $12") # Sample data
        self.medications_text.config(state=tk.DISABLED)
        self.medications_text.grid(row=1, column=1, padx=10, pady=10, sticky=(tk.W, tk.E))

        # Row 2: Add Doctor
        add_doctor_button = ttk.Button(self.root, text="Add Doctor", command=self.add_doctor)
        add_doctor_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        # Row 3: Report
        report_button = ttk.Button(self.root, text="Report Issue", command=self.report_issue)
        report_button.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        # Row 4: Privacy Policy
        privacy_button = ttk.Button(self.root, text="Privacy Policy", command=self.show_privacy_policy)
        privacy_button.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

        # Row 5: Global Map for Locations
        map_button = ttk.Button(self.root, text="Global Map", command=self.open_global_map)
        map_button.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

        # Row 6: Exit/Log out
        logout_button = ttk.Button(self.root, text="Log Out", command=self.logout)
        logout_button.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
        exit_button = ttk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.grid(row=6, column=1, padx=10, pady=10, sticky=tk.E)

        # Configure column weights for resizing
        self.root.grid_columnconfigure(1, weight=1)

    def add_doctor(self):
        messagebox.showinfo("Add Doctor", "Functionality to add a doctor will be implemented here.")

    def report_issue(self):
        messagebox.showinfo("Report Issue", "Functionality to report an issue will be implemented here.")

    def show_privacy_policy(self):
        messagebox.showinfo("Privacy Policy", "Displaying the privacy policy here...")

    def open_global_map(self):
        messagebox.showinfo("Global Map", "Functionality to open a global map will be implemented here.")

    def logout(self):
        self.root.destroy()
        # You would typically return to the login screen here
        print("Logged out")

if __name__ == '__main__':
    root = tk.Tk()
    dashboard = ClientDashboard(root, "test_client") # Replace "test_client" with the actual username
    root.mainloop()