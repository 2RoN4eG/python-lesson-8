""" Модуль для работы со списком клиентов СТО"""


def show_all(clients):
    """Выводит всех клиентов в удобном формате."""
    for client in clients:
        print(client)


def filter_by_brand(clients, brand):
    """Возвращает список клиентов указанной марки автомобиля."""
    return [client for client in clients if client[2] == brand]


def add_service_cost(clients, index, amount):
    """Добавляет сумму к стоимости обслуживания клиента по номеру в списке."""
    clients[index][4] += amount


def delete_by_index(clients, index):
    """Удаляет клиента по номеру в списке."""
    del clients[index]


def get_most_expensive(clients):
    """Возвращает клиента с максимальной стоимостью обслуживания."""
    clients = clients.copy()
    clients.sort(key=lambda client: client[4])
    return clients[-1]


def delete_older_than(clients, years):
    """Удаляет всех клиентов, чьи машины старше указанного количества лет."""
    copied_clients = clients.copy()

    import datetime

    now_year = datetime.datetime.now().year
    # copied_clients.sort(key=lambda client: client[3])
    for client in copied_clients:
        if now_year - client[3] >= years:
            clients.remove(client)


def group_by_brand(clients):
    """Группирует клиентов по марке с использованием itertools.groupby."""
    from itertools import groupby

    clients = clients.copy()
    clients.sort(key=lambda client: client[2])

    for brand, brand_clients in groupby(clients, key=lambda client: client[2]):
        print(brand, end=" [")
        for client in brand_clients:
            print(client[1], end=", ")
        print(end="]\n")

    # result = [(key, list(group)) for key, group in groupby(clients, key=lambda client: client[2])]
    # for item in result:
    #     print(item)
