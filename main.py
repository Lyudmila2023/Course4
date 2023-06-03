from classes import HeadHunter, Superjob, Connector


def main():
	vacancies_json = []
	# keyword = input("Введите ключевое слово: ")
	keyword = "Python"

	hh = HeadHunter(keyword)
	sj = Superjob(keyword)
	for api in (hh, sj):
		api.get_vacancies(pages_count=1)
		vacancies_json.extend(api.get_formatted_vacancies())


	connector = Connector(keyword=keyword, vacancies_json=vacancies_json)

	while True:
		command = input(
			"1 - Вывести список вакансий; \n"
			"exit - для выхода.\n"
		)
		if command.lower() == "exit":
			break
		elif command == "1":
			vacancies = connector.select()
		else:
			print("Некорректный ввод!\n"
				  "Повторите попытку \n")
			continue
		for vacancy in vacancies:
			print(vacancy, end='\n\n')

if __name__ == "__main__":
	main()