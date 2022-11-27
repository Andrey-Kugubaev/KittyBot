## **Телеграм-бот для помощи введения канала TheWorldofCats**
![python](https://img.shields.io/badge/Python-3.9-green)
![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-20.0a6-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14.6-green)
<br>
![telegram](https://img.shields.io/badge/telegram-channel-blue)
![telegram](https://img.shields.io/badge/DigitalOcean-grey)
![docker](https://img.shields.io/badge/Docker-grey)
<br>
----
### Описание:
Телеграм-бот для помощи введения канала _https://t.me/theworldofcats_
- Бот умеет принимать от подписчиков фотографии;
- Бот по запросу присылает рандомную фотографию кота, при возникновании ошибки запроса картинки с котом по api, пришлет картинку с собакой
Фотографии котов запрашиваеются [тут](https://thecatapi.com), а собак [тут](https://thedogapi.com);
----
### Планы по развитию:
- Добавление функции обратной связи;
- Добавление нового интерактива;
- Добавление функции загрузки видео.

### Для запуска бота:
<details>

- склонируйте проект
`git clone https://github.com/Andrey-Kugubaev/KittyBot.git`
- установите и активируйте виртуальное окружение
`python -m venv venv (или python3 -m venv venv) / source venv/Scripts/activate (или source venv/bin/activate)`
- установите библиотеку `pip install python-telegram-bot`
- создайте в корне проекта файл `.env` и укажите в нем token вашего бота `TOKEN=xxx`
- запустите файл `kittybot.py`
- наслаждайтесь котиками, или собачками

</details>