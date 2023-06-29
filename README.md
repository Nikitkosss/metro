# Описание задачи

Необходимо выполнить одно задание из трех предложенных.
- Super Hard. Написать парсер для мобильного приложения 4 лапы (https://4lapy.ru/shares/mobilnoe-prilozhenie-chetyre-lapy/) 
- Hard. Написать парсер для сайта Метро (https://online.metro-cc.ru/)
- Normal. Написать парсер для сайта Ашан (https://www.auchan.ru/)
Для каждой торговой площадки требования одни и те же. Спарсить любую категорию, где более 100 товаров, для городов Москва и Санкт-Петербург и выгрузить в любой удобный формат(csv, json, xlsx). Важно, чтобы товары были в наличии.

Необходимые данные: 
- id товара из сайта/приложения, 
- наименование, 
- ссылка на товар, 
- регулярная цена, 
- промо цена, 
- бренд.


## Требования к решению:

Скрипт, файл с результатом парсинга и requirements.txt оформить в публичный гитхаб репозиторий и ссылку вставить в поле ниже в этой форме.

## Инструкция по запуску проекта:
### Создайте виртуальное окружение:
```sh
python -m venv env_name
``` 
### Установите зависимости:
```sh
pip install -r requirements.txt
```
### Запустите проект:
```sh
python main.py
```
