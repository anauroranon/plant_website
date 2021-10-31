import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "key!"
    plant_adjectives = ("adorable", "charming", "beautiful", "pretty", "delightful", "cute", "lovable", "awesome")
    plant_names = ("Maria", "Gesualda", "Razza", "Bifolca", "Allucina")
