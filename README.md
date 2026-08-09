# Задание 3 - Автотесты для UI

## Описание проекта
Проект содержит автоматизированные тесты для веб-приложения Stellar Burgers (https://stellarburgers.education-services.ru), спроектированные для Google Chrome и Mozilla Firefox.  
Тесты покрывают основную функциональность: навигацию, работу с ингредиентами и ленту заказов.

## Установка и запуск  
1) Перед работой с репозиторием необходимо установить зависимости:
``` shell
pip3 install -r requirements.txt
```
2) Для запуска всех тестов из директории tests можно использовать:
```shell
pytest tests/ -v --alluredir=allure_results --browser=chrome или pytest tests/ -v --alluredir=allure_results --browser=firefox
```
3) Посмотреть отчет Allure в веб версии по запущенным тестам:
``` shell
allure serve allure_results
```

## Что проверяется

#### Навигация и ингредиенты (`test_main_page.py`)

| Тест | Описание |
|------|----------|
| `test_redirection_to_order_list` | Переход по клику на «Лента заказов» |
| `test_go_to_constructor` | Переход по клику на «Конструктор» |
| `test_popup_of_ingredient` | Клик на ингредиент открывает всплывающее окно с деталями |
| `test_close_ingredient_details_window` | Всплывающее окно закрывается кликом по крестику |
| `test_ingredient_counter` | При добавлении ингредиента счётчик увеличивается |

#### Лента заказов (`test_order_feed.py`)

| Тест | Описание |
|------|----------|
| `test_total_orders_counter_increases` | При создании заказа счётчик «Выполнено за всё время» увеличивается |
| `test_today_orders_counter_increases` | При создании заказа счётчик «Выполнено за сегодня» увеличивается |
| `test_new_order_appears_in_work_list` | После оформления заказа его номер появляется в разделе «В работе» |

## Структура проекта  

tests/ — тесты навигации, работы с ингредиентами и ленты заказов  
locators/ — локаторы главной страницы и ленты заказов  
pages/ — базовый класс для страниц, классы главной страницы и ленты заказов  
helpers.py - вспомогательные функции  
conftest.py — фикстуры   
data.py — тестовые данные   
allure-report/ — cгенерированный Allure-отчёт
