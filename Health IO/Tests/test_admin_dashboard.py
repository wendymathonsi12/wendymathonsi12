import unittest
import tkinter as tk
from unittest.mock import MagicMock
from Admin_Dashboard import AdminDashboard

class TestAdminDashboard(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.admin_dashboard = AdminDashboard(self.root, "test_admin")

    def tearDown(self):
        self.root.destroy()

    def test_admin_dashboard_creation(self):
        self.assertIsNotNone(self.admin_dashboard)
        self.assertEqual(self.admin_dashboard.username, "test_admin")

        self.assertTrue(hasattr(self.admin_dashboard, 'show_verifications'))
        self.assertTrue(hasattr(self.admin_dashboard, 'view_reports'))
        self.assertTrue(hasattr(self.admin_dashboard, 'view_data'))
        self.assertTrue(hasattr(self.admin_dashboard, 'shutdown_app'))

    def test_show_verifications(self):
        with self.assertRaises(tk.TclError):
            self.admin_dashboard.show_verifications()

    def test_view_reports(self):
        with self.assertRaises(tk.TclError):
            self.admin_dashboard.view_reports()

    def test_view_data(self):
        with self.assertRaises(tk.TclError):
            self.admin_dashboard.view_data()

    def test_shutdown_app_yes(self):
        messagebox_mock = MagicMock(return_value=True)
        tk.messagebox = messagebox_mock
        self.admin_dashboard.shutdown_app()
        messagebox_mock.askyesno.assert_called_once()
        messagebox_mock.showinfo.assert_called_once()


    def test_shutdown_app_no(self):
        messagebox_mock = MagicMock(return_value=False)
        tk.messagebox = messagebox_mock
        self.admin_dashboard.shutdown_app()
        messagebox_mock.askyesno.assert_called_once()
        messagebox_mock.showinfo.assert_not_called()

if __name__ == '__main__':
    unittest.main()