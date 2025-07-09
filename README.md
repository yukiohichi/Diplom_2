# API Тесты — Stellas Bergers

Автоматизированные тесты для API веб-сайта **Stellas Bergers**, написанные на Python с использованием `pytest`, `requests` и `Allure`.

## Структура проекта

- `allure-report/` — Сгенерированный HTML-отчёт Allure после запуска тестов.
- `allure-results/` — Сырые результаты выполнения тестов для последующей генерации отчета Allure.
- `api/`
  - `methods/` — Реализация функций для API-запросов (`orders.py`, `users.py`).
  - `tests/` — Каталог с автотестами:
    - `orders/` — Тесты заказов (`test_create_orders.py`, `test_order_list_users.py`).
    - `users/` — Тесты пользователей (`test_login_user.py`, `test_register_users.py`, `test_refactor_user.py`).
- `data/` — Вспомогательные данные:
  - `orders.py`, `users.py` — Тестовые данные.
  - `urls.py` — Базовые и конечные точки API.
- `.gitignore` — Исключения для Git.
- `conftest.py` — Фикстуры `pytest`.
- `helpers.py` — Вспомогательные функции по генерации данных
- `run_tests.sh` — Скрипт для запуска тестов.

---

## Технологии

- Python 3.13
- Pytest
- Allure
- requests
- pytest-ordering / pytest-dependency (если используются)

---

## Запуск тестов


1. Запустить тесты и генерация отчета через скрипт:

    ```bash
    ./run_tests.sh
    ```

