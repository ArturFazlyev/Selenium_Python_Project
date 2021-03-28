import configparser
import os


class Config:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.abspath('../example.ini'))

    def get_url(self):
        return self.config.get("Settings", "url")

    def get_username(self):
        return self.config.get("Settings", "username")

    def get_password(self):
        return self.config.get("Settings", "password")
