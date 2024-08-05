import configparser
import json

import logging
import coloredlogs
from colorama import init

init()

class confg:
	def __init__(self):
		self.config = configparser.ConfigParser()
		self.config.read('./settings.ini')

	def convert_value(self, value):
		if value == 'True':
			return True
		elif value == 'False':
			return False
		elif value == 'None':
			return None
		return value
	
	def GetSettings(self):
		sections = self.config.sections()
		data = {}
		for section in sections:
			# Преобразование значений из строк в соответствующие типы
			data[section] = {key: self.convert_value(val) for key, val in self.config.items(section)}
		data = json.dumps(data)
		return json.loads(data)

class Logger:
	def __init__(self):
		self.logger = logging.getLogger('RedLog')
		self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
		coloredlogs.install(level='DEBUG', logger=self.logger, fmt='%(asctime)s - %(levelname)s - %(message)s')

		# Optionally add file handler
		if confg().GetSettings()["logging"]["log_to_file"]:
			self.add_file_handler()

	def add_file_handler(self):
		file_handler = logging.FileHandler('Script.log', mode='a+', encoding="utf-8")
		file_handler.setLevel(logging.DEBUG)
		file_handler.setFormatter(self.formatter)
		self.logger.addHandler(file_handler)

	def get_logger(self):
		# Вложенные функции для разных уровней логирования
		if not confg().GetSettings()["logging"]["status"]:
			return None
		def debug(text):
			self.logger.debug(text)
		
		def info(text):
			self.logger.info(text)
		
		def warning(text):
			self.logger.warning(text)
		
		def error(text):
			self.logger.error(text)
		
		def critical(text):
			self.logger.critical(text)
		
		# Возвращаем объект, который имитирует поведение логгера
		class LoggerWrapper:
			def __init__(self, logger):
				self.logger = logger
				self.debug = debug
				self.info = info
				self.warning = warning
				self.error = error
				self.critical = critical
		return LoggerWrapper(self.logger)