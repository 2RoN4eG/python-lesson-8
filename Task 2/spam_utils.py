"""Модуль для антиспам‑проверки сообщений """

from datetime import datetime


def count_spam_words(message, spam_words):
    """Возвращает количество спам‑слов в сообщении."""
    pass


def has_suspicious_links(message):
    """Проверяет, содержит ли сообщение подозрительные ссылки."""
    pass


def check_spam(message, spam_words):
    """Проверяет сообщение на наличие спам‑слов и возвращает предупреждение или None."""
    pass


def check_links(message, spam_count):
    """Проверяет сообщение на наличие ссылок и возвращает предупреждение или None."""
    pass


def moderate_message(message, spam_words):
    """
    Выполняет все проверки и возвращает:
    - список предупреждений
    - флаг публикации (True/False)
    """
    pass


def add_publish_timestamp(message):
    """Добавляет к сообщению дату и время публикации."""
    pass
