"""Модуль для работы со списком клиентов СТО"""


def show_all(clients):
    """Выводит всех клиентов в удобном формате."""

    for client in clients:
        print(client)


def filter_by_brand(clients, brand):
    """Возвращает список клиентов указанной марки автомобиля."""

    return [client for client in clients if client[2].lower() == brand.lower()]


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
    for client in copied_clients:
        if now_year - client[3] >= years:
            clients.remove(client)


def group_by_brand(clients):
    """Группирует клиентов по марке с использованием itertools.groupby."""

    def predicate(client):
        return client[2]

    clients = clients.copy()
    clients.sort(key=predicate)

    from itertools import groupby

    grouped = groupby(clients, key=predicate)
    return [(brand, [brand_client[1] for brand_client in list(brand_clients)])
            for brand, brand_clients in grouped]
