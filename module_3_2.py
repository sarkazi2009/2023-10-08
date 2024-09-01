
def send_email(message, recipient, sender="university.help@gmail.com"):
    dog = '@'
    konec = ".com", ".ru", ".net"
    flags = False
    if dog in recipient:
        for i in konec:
            if i in recipient:
                flags = True
    flags1 = False
    if dog in sender:
        for i in konec:
            if i in sender:
                flags1 = True

    if flags is False or flags1 is False:
        print('Невозможно отправить письмо с адреса', sender, 'На адрес', recipient)
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender =='university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес',  recipient)
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
