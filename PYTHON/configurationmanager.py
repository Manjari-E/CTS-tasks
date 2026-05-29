import configparser

class Config:
    pass

class DatabaseConfig(Config):
    pass

config = configparser.ConfigParser()
config.read("db.ini")

if "DATABASE" in config:
    print("Database Settings Loaded")
else:
    print("DATABASE section missing")