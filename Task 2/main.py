# main.py
# Основная программа для проверки сообщений на спам

import spam_utils as su

SPAM_WORDS = ["скидка", "бесплатно", "выигрыш", "кликни", "подпишись"]


def main():
    message = "Ваш выигрыш составил 1_000_000 рублей и скидка скидка к следующему шансу выигрыш, кликни по ссылке http://path.org и подпишись, что бы его получить бесплатно."
    # message = "кликни по ссылке http://path.org, что бы увидить как сделано."
    # message = "Надоел этот спам, хорошо, что у нас есть Питон для работы с текстом, что бы найти все спам сообщения! http://python.org"
    # message = "Надоел этот спам, хорошо, что у нас есть Питон для работы с текстом, что бы найти все спам сообщения!"

    warnings, can_be_published = su.moderate_message(message, SPAM_WORDS)

    for warning in warnings:
        print(warning)

    if can_be_published:
        message = su.add_publish_timestamp(message)
        print(message)


if __name__ == "__main__":
    main()
