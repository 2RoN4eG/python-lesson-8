"""Модуль для антиспам‑проверки сообщений """

from datetime import datetime


def count_spam_words(message, spam_words):
    """Возвращает количество спам‑слов в сообщении."""
    count = 0
    for spam_word in spam_words:
        if message.find(spam_word) != -1:
            count += 1
    return count


def has_suspicious_links(message):
    """Проверяет, содержит ли сообщение подозрительные ссылки."""
    LINK_PARTS = ["http://", "https://", "www."]
    for link_part in LINK_PARTS:
        if message.find(link_part) != -1:
            return True
    return False


def check_spam(message, spam_words):
    """Проверяет сообщение на наличие спам‑слов и возвращает предупреждение или None."""
    amount_spam_words = count_spam_words(message, spam_words)
    if amount_spam_words > 4:
        return "В тексте найдено большое количество спам слов"
    elif 0 < amount_spam_words <= 4:
        return "В тексте найдены спам слова"


def check_links(message, spam_count):
    """Проверяет сообщение на наличие ссылок и возвращает предупреждение или None."""
    has_links = has_suspicious_links(message)
    if has_links and spam_count >= 1:
        return "В тексте найдены ссылки и спам слова"
    elif has_links and spam_count == 0:
        return "В тексте есть ссылки"


def moderate_message(message, spam_words):
    """
    Выполняет все проверки и возвращает:
    - список предупреждений
    - флаг публикации (True/False)
    """

    warnings = []

    spam_message = check_spam(message, spam_words)
    if spam_message:
        warnings.append(spam_message)

    amount_spam_words = count_spam_words(message, spam_words)
    links_message = check_links(message, amount_spam_words)
    if links_message:
        warnings.append(links_message)

    result = True
    if has_suspicious_links(message) and amount_spam_words >= 1:
        result = False
    elif not has_suspicious_links(message) and amount_spam_words > 4:
        result = False

    return warnings, result


def add_publish_timestamp(message):
    """Добавляет к сообщению дату и время публикации."""
    now_datetime = datetime.now()
    return f"{now_datetime.year} {now_datetime.month} {now_datetime.day} {now_datetime.hour}:{now_datetime.minute}:{now_datetime.second} {message}"
