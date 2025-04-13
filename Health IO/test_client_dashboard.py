import unittest
import tkinter as tk
from unittest.mock import MagicMock
from Clients_Dashboard import ClientDashboard

class TestClientDashboard(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.client_dashboard = ClientDashboard(self.root, "test_client")

    def tearDown(self):
        self.root.destroy()

    def test_client_dashboard_creation(self):
        self.assertIsNotNone(self.client_dashboard)
        self.assertEqual(self.client_dashboard.username, "test_client")
        # Check for the presence of UI elements (basic UI check)
        self.assertTrue(hasattr(self.client_dashboard, 'disorders_combo'))
        self.assertTrue(hasattr(self.client_dashboard, 'medications_text'))
        self.assertTrue(hasattr(self.client_dashboard, 'add_doctor'))
        self.assertTrue(hasattr(self.client_dashboard, 'report_issue'))
        self.assertTrue(hasattr(self.client_dashboard, 'show_privacy_policy'))
        self.assertTrue(hasattr(self.client_dashboard, 'open_global_map'))
        self.assertTrue(hasattr(self.client_dashboard, 'logout'))

    def test_add_doctor(self):
        with self.assertRaises(tk.TclError):
            self.client_dashboard.add_doctor()

    def test_report_issue(self):
        with self.assertRaises(tk.TclError):
            self.client_dashboard.report_issue()

    def test_show_privacy_policy(self):
        with self.assertRaises(tk.TclError):
            self.client_dashboard.show_privacy_policy()

    def test_open_global_map(self):
        with self.assertRaises(tk.TclError):
            self.client_dashboard.open_global_map()

    def test_logout(self):
        self.assertTrue(callable(self.client_dashboard.logout))


if __name__ == '__main__':
    unittest.main()