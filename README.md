<h1 align = "center"> Test-Task </h1>
<h1 align = "center" ><img src = "https://svgsilh.com/svg/2773336.svg" height = 256></h1>

<h2>Описание</h2>
<a> Российские Космические Системы. Мультимедийность. Работа с API <a>

<h2>Задача</h2>
    <div>
      Написать web-приложение используя Django и Django Rest Framework для запросов к API.:
      <ol>
        <li>Приложение должно содержать 3 модели</li>
          <ul>
            <li>Artist</li>
            <li>Album</li>
            <li>Track</li>
          </ul>
        <li>Приложение должно поддерживать CRUD-операции</li>
        <li>Приложение должно поддерживать сортировку выданных данных по заданному значению</li>
        <li>Вложенные поля должны разделяться @</li>
      </ol>
    </div>
<h2>Установка</h2>
<p>Устанавливаем Python <a href = "https://www.python.org/downloads/">Install Python</a></p>
<a>Клонируем этот репозиторий</a>
    
``` 
git clone https://github.com/morozooff/test-task.git
```
 
<a>Создаем виртуальную среду в питоне</a>
    
```
python -m venv env_name
```

<a>Ставим требуемые пакеты</a>

```
pip install django
pip install djangorestframework 
```

<a>Джанго-проекты работают с SECRET_KEY, я сознательно скрыл его в local_settings, придется сгенерировать новый</a>

```
python manage.py shell
from django.core.management import utils
utils.get_random_secret_key()
```

<a>Затем создаем суперпользователя джанго, для работы с БД и Django-admin</a>

```
python manage.py createsuperuser
```

<a>Создаем миграции с джанго моделей</a>

```
python manage.py makemigrations
```

<a>Мигрируем их</a>

```
python manage.py migrate
```

<a>Теперь запускаем локалхост</a>

```
python manage.py runserver
```

<a>Теперь можем пользоваться приложением (URL: http://127.0.0.1:8000/)</a>

<h2> Описание работы </h2>
<h3>CRUD-операции</h3>
CRUD-операции можно осуществлять посредством работы с Django-admin (URL: http://127.0.0.1:8000/admin), который предостовляет удобный интерфейс, а также посредстом отправки запросов на работающий сервер приложения.

<h3>Create</h3>
Для создания объектов будем отправлять POST-запрос по URL: http://127.0.0.1:8000/model_name/, где model_name - имя модели, объект которой мы хотим создать в базе данных. Попробуем создать новый альбом.

Перед этим нам нужно создать артиста, так как модель Album зависить от модели Artist.
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/1.png">

Для этого отправим по URL: http://127.0.0.1:8000/artists/ post-запрос. Артист создан. 
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2015.37.40.png">

Теперь перейдем с созданию альбома. Скриншот до создания нового альбома:
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2015.42.48.png">

Для создания альбома теперь отправим POST-запрос по URL: http://127.0.0.1:8000/albums/. Скриншот нового списка альбомов:
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2015.43.00.png">

Теперь заполним треками этот альбом, отправив новые POST-запросы по URL: http://127.0.0.1:8000/tracks/, где и привяжем их к текущему альбому:
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2015.46.47.png">

Cоздание объектов работает корректно, перейдем к другим операциям.

<h3>Read</h3>
Для чтения объектов будем отправлять Get-запрос по URL: http://127.0.0.1:8000/model_name/, где model_name - имя модели, объекты которой мы хотим получить из базы данных. Причем для получения конкретного объекта будем дополнять этот url параметром id - целочисленным уникальным идентификатором каждого объекта в системе. 

Попробуем получить список всех альбомов. Отправим GET-запрос по URL: http://127.0.0.1:8000/albums/
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2015.56.28.png">

Теперь попробуем получить конкретный альбом, который мы недавно создали. Отправим GET-запрос по URL: http://127.0.0.1:8000/albums/5/
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2016.01.09.png">

Как видно из скриншотов, данные выводятся корректно в заданном в ТЗ формате, вложенные поля разделяются знаком @. Также корректно работает возможность сортировки, давайте проверим ее. Для этого достаточно обратиться аналогичным с GET-запросом по аналогичному URL, добавим к нему параметр ?ordering=field_name, где field_name - это имя поля, по которому нужно сортировать.
<div> Попробуем отсортировать список треков по текстовому представлению поля name. Отправим GET-запрос по URL: http://127.0.0.1:8000/tracks/?ordering=name:</div>
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2016.15.32.png">

<div> Для обратной сортировки нужно перед field_name указать знак минуса. Отправим GET-запрос по URL: http://127.0.0.1:8000/tracks/?ordering=-name:</div>
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2016.18.48.png">

<div> В приложении доступна сортировка по текстовому представлению всех полей всех моделей, а также доступна сортировка по числовому значению года выпуска альбома. Отправим GET-запрос по URL: http://127.0.0.1:8000/al/?ordering=year:</div>
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2016.21.07.png">

Таким образом сортировка и операция чтения работают корретно, перейдем к следующим.

<h3>Update</h3>
Для обновления объектов будем отправлять PUT-запрос по URL: http://127.0.0.1:8000/model_name/id, где model_name - имя модели, объект которой мы хотим обновить в базе данных, а id - целочисленным уникальным идентификатором каждого объекта в системе.

Попробуем обновить год выпуска недавно созданного альбома. Отправим PUT-запрос по URL: http://127.0.0.1:8000/albums/5/ следующего содержания:
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2016.05.11.png">

Обратимся к списку альбомов и посмотрим на интересующий нас:
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2016.05.43.png">

Обновление года выпуска отработало корректно, также работают обновления и других полей других моделей.

<h3>Delete</h3>
Для удаления объектов будем отправлять DELETE-запрос по URL: http://127.0.0.1:8000/model_name/id, где model_name - имя модели, объект которой мы хотим удалить из базы данных, а id - целочисленным уникальным идентификатором каждого объекта в системе.

Попробуем удалить один из треков из недавно созданного альбома. Отправим DELETE-запрос по URL: http://127.0.0.1:8000/tracks/15/:
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2016.10.03.png">

Обратимся к списку альбому и посмотрим на его список треков:
<img src="https://github.com/morozooff/test-task/blob/master/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2016.11.21.png">

Удаление трека альбома отработало корректно, также работают удаления и других объектов других моделей.

<h2>Методики тестирования</h2>
В ходе тестирования работоспособности приложения были использованы следующие инструменты: 
<ol></ol>
<li>Django rest framework web interface, который позволял отправлять простейшие запросы прямо по адресной строке браузера и получать данные ответа в удобном представлении. </li>
<li>Также был использован инструемент Postman, который позволяет отправлять самые разные запросы на сервер приложения, при этом работая непосредственно с телом запроса и его заголовками, что дает возможность испытывать и тестировать самые разные запросы. </li>
Про модульное тестирование или написание тестов к приложению в ТЗ не говорилось, поэтому тесты не были написаны, были использованы только вышеперечисленные инструменты.


