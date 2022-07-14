## **Телеграм-бот KittyBot**

Телеграм-бот присылает по запросу котиков, а если не получится, то пришлет собачек.
Котиков он берет [тут](https://thecatapi.com), а собачек [тут](https://thedogapi.com)

Бот использует библиотеку **python-telegram-bot**

### Для запуска бота:
- склонируйте проект
`git clone https://github.com/Andrey-Kugubaev/KittyBot.git`
- установите и активируйте виртуальное окружение
`python -m venv venv (или python3 -m venv venv) / source venv/Scripts/activate (или source venv/bin/activate)`
- установите библиотеку `pip install python-telegram-bot`
- создайте в корне проекта файл `.env` и укажите в нем token вашего бота `TOKEN=xxx`
- запустите файл `kittybot.py`
- наслаждайтесь котиками, или собачками