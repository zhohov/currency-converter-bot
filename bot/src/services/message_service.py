def handle_message_service(text: str) -> str:
    greetings = [
        "привет",
    ]
    farewells = [
        "пока",
    ]

    words = text.split()

    for word in words:
        if word in greetings:
            return "Привет!"
        elif word in farewells:
            return "Пока!"
        else:
            return "Сообщение не распознано"
