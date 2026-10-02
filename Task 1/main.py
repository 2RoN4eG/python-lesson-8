import garage_utils as gu

clients = [
    [1, "Иван Петров", "Toyota", 2015, 250],
    [2, "Анна Смирнова", "BMW", 2018, 480],
    [3, "Сергей Ковалев", "Audi", 2012, 390],
    [4, "Мария Иванова", "Volkswagen", 2010, 210],
    [5, "Дмитрий Орлов", "Mercedes", 2019, 520],
    [6, "Ольга Сидорова", "Toyota", 2016, 300],
    [7, "Алексей Жуков", "Ford", 2013, 180],
    [8, "Елена Кравцова", "Kia", 2020, 260],
    [9, "Павел Лебедев", "Hyundai", 2017, 240],
    [10, "Ирина Фролова", "BMW", 2014, 450],
    [11, "Николай Громов", "Renault", 2011, 170],
    [12, "Татьяна Белова", "Audi", 2019, 510]
]

def show_menu():
    print("""
1 — вывести всех клиентов
2 — вывести клиентов заданной марки
3 — изменить сумму обслуживания
4 — удалить клиента
5 — найти самую дорогую машину
6 — удалить машины старше n лет
7 — сгруппировать клиентов по марке
0 — выход
""")


def main():
    # Ваш код здесь
    while True:
        show_menu()
        selected = input("Сделайте ваш выбор: ")
        match selected:
            case "0":
                break
            case "1":
                gu.show_all(clients)
            case "2":
                brand = input("Введите бренд автомобиля: ")
                brand_clients = gu.filter_by_brand(clients, brand)
                for client in brand_clients:
                    print(client)
            case "3":
                index = int(input("Введите индекс: "))
                if 1 <= index <= len(clients):
                    amount = int(input("Введите сумму: "))
                    gu.add_service_cost(clients, index - 1, amount)
                else:
                    print(f"Индекс должен быть в диапазоне от 1 до {len(clients)}")
            case "4":
                index = int(input("Введите индекс: "))
                gu.delete_by_index(clients, index - 1)
            case "5":
                client = gu.get_most_expensive(clients)
                print(client)
            case "6":
                years = int(input("Введите кол-во лет: "))
                gu.delete_older_than(clients, years)
                pass
            case "7":
                gu.group_by_brand(clients)
                pass
            case _:
                pass


if __name__ == "__main__":
    main()
