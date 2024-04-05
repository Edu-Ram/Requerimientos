class Logger:
    def log(self, message):
        print(f"Log: {message}")


class DataAccess:
    def __init__(self, logger):
        self.logger = logger

    def save_data(self, data):
        self.logger.log("Datos guardados correctamente")


logger = Logger()
data_access = DataAccess(logger)
data_access.save_data("Información importante")
