import configparser


config = configparser.RawConfigParser()
config.read("Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getUrl():
        return config.get("common-info","base_url")

    @staticmethod
    def getAppUsername():
        return config.get("common-info","username")

    @staticmethod
    def getAppPassword():
        return config.get("common-info", "password")
