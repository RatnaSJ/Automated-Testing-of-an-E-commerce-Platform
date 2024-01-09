from configparser import ConfigParser


def read_configuration(category,key):
    config = ConfigParser()
    config.read("C:\\Users\\Admin\\PycharmProjects\\pythonSeleniumPersonalProject2\\configuration\\config.ini")
    return config.get(category,key)


