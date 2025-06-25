# Auto QA HW6 — Тест для saucedemo.com

Автоматизированный тест с использованием **Page Object Model (POM)** на Python + Selenium + Pytest.

## 🔍 Что делает скрипт

1. Открывает сайт https://www.saucedemo.com/
2. Авторизуется как `standard_user`
3. Добавляет 3 товара в корзину:
   - Sauce Labs Backpack
   - Sauce Labs Bolt T-Shirt
   - Sauce Labs Onesie
4. Переходит к оформлению заказа
5. Заполняет форму: имя, фамилия, индекс
6. Проверяет, что сумма заказа — **$58.29**

---

## ⚙️ Установка

```bash
pip install selenium
```

❗ Убедись, что у тебя установлен [geckodriver](https://github.com/mozilla/geckodriver/releases) и он лежит в корне проекта.

---

## 🚀 Запуск теста

```bash
pytest tests/test_saucedemo_order.py
```

Браузер откроется, выполнит все шаги и закроется автоматически после проверки суммы.

---

## 📁 Структура проекта

```
autoqa_hw6/
├── pages/                # Page Object классы
├── tests/                # Тесты
├── conftest.py           # WebDriver setup
├── geckodriver.exe       # Драйвер Firefox
└── README.md             # Этот файл
```

---

## 👨‍💻 Автор

[Vitalijs Filipovs](https://github.com/VitalijsFilipovs)
