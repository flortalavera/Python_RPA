import logging
from datetime import datetime
import inspect

class LogManager:

    LOGGERS = {}

    def __init__(self, log_path):
        self.log_path = log_path
        self.source = f' - Origin: {inspect.stack()[1][1]}'


    def __create_handler(self, name):
        handler = logging.FileHandler(name)
        format = logging.Formatter("%(levelname)s - %(asctime)s - %(message)s")
        handler.setFormatter(format)
        return handler


    def __setup_logger(self, name, lvl):
        handler = self.__create_handler(name)
        logger = logging.getLogger(name)
        logger.setLevel(lvl)
        logger.addHandler(handler)
        LogManager.LOGGERS[name] = logger
        return logger

    
    def __get_logger(self, lvl, log_type=None, global_l=False):
        if global_l:
            name = self.log_path + datetime.now().strftime("%Y%m%d")
        else:
            name = self.log_path + log_type + datetime.now().strftime("%Y%m%d")
        logger = LogManager.LOGGERS.get(name)
        if logger:
            return logger
        logger = self.__setup_logger(name, lvl)
        return logger


    def __get_or_create_loggers(self, lvl, log_type):
        logger = self.__get_logger(lvl, log_type)
        global_logger = self.__get_logger(lvl, global_l=True)
        return logger, global_logger


    def debug(self, message):
        log, global_log = self.__get_or_create_loggers(logging.DEBUG, "debug_")
        log.debug(message + self.source)
        global_log.debug(message + self.source)


    def info(self, message):
        log, global_log = self.__get_or_create_loggers(logging.INFO, "info_")
        log.info(message + self.source)
        global_log.info(message + self.source)


    def warning(self, message):
        log, global_log = self.__get_or_create_loggers(logging.WARNING, "warning_")
        log.warning(message + self.source)
        global_log.warning(message + self.source)


    def error(self, message):
        log, global_log = self.__get_or_create_loggers(logging.ERROR, "error_")
        log.error(message + self.source)
        global_log.error(message + self.source)
    
    
    def critical(self, message):
        log, global_log = self.__get_or_create_loggers(logging.CRITICAL, "critical_")
        log.critical(message + self.source)
        global_log.critical(message + self.source)

logger = LogManager("")
logger.debug("Aplicacion en depuracion")
logger.info("No se pudo leer la linea 128")
logger.warning("Poco espacio en memoria")
logger.error("No se pudo iniciar sesion")
logger.critical("No hay servicio, el programa fue cerrado")
print(10/0)