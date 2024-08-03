import requests
import os
import shutil

class Updater:
	def __init__(self):
		pass

	def center_text(self, text):
		columns = shutil.get_terminal_size().columns
		left_padding = (columns - len(text)) // 2
		centered_text = ' ' * left_padding + text
		print(centered_text)

	def getVersion(self):
		# Получить текущую версию из интернет-ресурса
		res = requests.get("https://raw.githubusercontent.com/RedPiarOfficial/AminoToolsFix/main/VERSION")
		new_version = res.text.strip()
	
		# Прочитать текущую версию из файла
		try:
			with open("./VERSION", "r") as file:
				current_version = file.read().strip()
		except FileNotFoundError:
		# Если файл не найден, текущую версию считать как "неизвестную"
			current_version = "Unknown"
	
		# Проверить, отличается ли текущая версия от новой
		if new_version != current_version:
			# Вывести отцентрированный текст
			for i in ["Update Warning", f"Your version: {current_version}, new version: {new_version}", "Please update the project to access the latest changes."]:
				self.center_text(i)
			input("(Press Enter to skip): ")
			os.system("cls")

"""res = requests.get("https://github.com/RedPiarOfficial/AminoToolsFix/archive/refs/heads/main.zip")


with open("./autoUpdate/latestVersion.zip", "wb") as file:
	file.write(res.content)"""
