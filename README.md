Задание 1
Продолжаем работать с проектом. Установите брокер для кеширования Redis. Внесите необходимые настройки и проверьте работоспособность проекта с новыми настройками.

Задание 2
Настройте кеширование всего контроллера отображения данных относительно одного продукта.

Помните, что кеширование можно подключать не только в файле views.py, но и в файле маршрутизации urls.py. Важно делать всё в одном месте, чтобы достичь единообразия в коде проекта и не запутаться впоследствии.

Задание 3
Создайте сервисную функцию, которая будет отвечать за выборку категорий и которую можно переиспользовать в любом месте системы. Добавьте низкоуровневое кеширование для списка категорий.

Задание 4
Вынесите необходимые настройки в переменные окружения и настройте проект для работы с ними.

* Дополнительное задание

Добавьте кеширование всего сайта целиком, при этом отключите от кеширования определенные контроллеры, которые отвечают за работу по заполнению продуктов и блога.














22-1
Задание 1
Создайте новое приложение для работы с пользователем. Определите собственную форму для пользователя, при этом задайте электронную почту как поле для авторизации.

Также добавьте поля:

«Аватар»,
«Номер телефона»,
«Страна».
Задание 2
В сервисе реализуйте функционал аутентификации, а именно:

регистрацию пользователя по почте и паролю;
верификацию почты пользователя через отправленное письмо;
авторизацию пользователя;
восстановление пользователя на автоматически сгенерированный пароль.
Задание 3
Закройте для анонимных пользователей все контроллеры, которые отвечают за работу с продуктами. При этом создаваемые продукты должны автоматически привязываться к авторизованному пользователю.

Не забудьте добавить поле для продуктов, через которое пользователь будет привязываться. Текущий авторизованный пользователь доступен в любом контроллере через 
self.request.user
.

* Дополнительное задание
Добавьте интерфейс редактирования профиля пользователя.

Дополнительное задание, помеченное звездочкой, желательно, но не обязательно выполнять.







Задание 1
Продолжаем работать с проектом из предыдущего домашнего задания. Для модели продуктов реализуйте механизм CRUD, задействовав модуль 
django.forms
.

Условия для пользователей:

могут создавать новые продукты;
не могут загружать запрещенные продукты на платформу.
Для исключения загрузки запрещенных продуктов реализуйте валидацию названия и описания продукта таким образом, чтобы нельзя было в них добавлять слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.

Задание 2
Добавьте новую модель «Версия», которая должна содержать следующие поля:

продукт,
номер версии,
название версии,
признак текущей версии.
При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.

Задание 3
Для работы с версиями продукта добавьте реализацию работы с формами. При этом версия может быть внесена только в существующий продукт.

Все созданные формы нужно стилизовать так, чтобы они были в единой стилистике оформления всей платформы. Для этого можно воспользоваться методом 
__init__
 либо самостоятельно изучить пакет crispy-forms: https://pypi.org/project/django-crispy-forms/.


# HW21.1
Задание 1
Продолжаем работать с проектом из предыдущего домашнего задания. Переведите имеющиеся контроллеры с FBV на CBV.

Задание 2
Создайте новую модель блоговой записи со следующими полями:
заголовок,
slug (реализовать через CharField),
содержимое,
превью (изображение),
дата создания,
признак публикации,
количество просмотров.
Для работы с блогом реализуйте CRUD для новой модели.

Задание 3
Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:

при открытии отдельной статьи увеличивать счетчик просмотров;
выводить в список статей только те, которые имеют положительный признак публикации;
при создании динамически формировать slug name для заголовка;
после успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.
