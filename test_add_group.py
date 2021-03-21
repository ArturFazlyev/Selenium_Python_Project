# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
from application import Application
import unittest


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_app_dynamics_job(self):
        self.app.open_home_page()
        self.app.login("admin", "secret")
        self.app.open_group_page()
        self.app.create_group(Group("test", "test", "test"))
        self.app.returns_to_groups_page()
        self.app.logout()

    def is_element_present(self, how, what):
        try:
            self.app.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.app.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.app.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
