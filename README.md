## Manager Effectiveness Report

Цей репозиторій містить генерацію тестових даних (Customers/Managers/Orders), аналітику по менеджерах та клієнтах, експорт результатів у CSV, приклад SQL-запитів під цю структуру даних, а також інструкції для побудови звіту в Power BI та виконання частини завдань в Excel (VBA).

## Вимоги

- Python 3.10+ (проєкт запускався з Python 3.13)
- Залежності з `requirements.txt`: `numpy`, `pandas`, `matplotlib`

Встановлення:

```bash
pip install -r requirements.txt
```

## Швидкий старт

1) Згенерувати дані (Customers/Orders):

```bash
python src/generate_data.py
```

2) Виконати аналітику, сформувати агрегати та побудувати графік:

```bash
python src/manager_details.py
```

## Вихідні файли (артефакти)

- **Згенеровані дані (CSV)**:
  - `data/customers.csv`
  - `data/orders.csv`
  - `data/managers.csv` (створюється під час аналітики, бо включає `Experience_diap`)
- **Результати аналітики (CSV)**:
  - `data/grouped_analysis.csv`
- **Графік**:
  - `graph/orders_trend.png`

## Відповідність завдань → файли реалізації

### 1) Генерація pandas DataFrames випадковими значеннями

- **1a. Перелік клієнтів (`df_customers`)**: `src/generate_data.py`
- **1b. Перелік менеджерів (`df_managers`)**: `src/generate_data.py` (DataFrame створюється в пам’яті; CSV з менеджерами формується на кроці 2)
- **1c. Перелік замовлень за останні 6 місяців (`df_orders`)**: `src/generate_data.py`
  - Поля замовлення: `CustomerID`, `ManagerID`, `OrderChannel` (Web/Phone), `OrderDate`, `OrderSum` (1000–5000), `PaymentType` (Online/Cash), `DeliveryType` (Post1/Post2/Post3)

### 2) Аналітика в Python

- **2a. Колонка `Experience_diap` для менеджерів**: `src/manager_details.py`
  - Логіка діапазонів стажу реалізована функцією `get_experience_diap`.
- **2b. Для менеджерів з `Experience_diap = "більше 2 років"`**: `src/manager_details.py`
  - Фільтрація замовлень по `ManagerID`, приєднання віку клієнта (merge з `df_customers`).
  - Групування клієнтів за віком: `до 35 років / 36-42 роки / від 43 років`.
  - Вивід в розрізі `DeliveryType` середньої та медіанної суми `OrderSum`.
  - Експорт результату в `data/grouped_analysis.csv`.
- **2c. Графік кількості замовлень по місяцях**: `src/manager_details.py`
  - Збереження: `graph/orders_trend.png`

### 3) Експорт у CSV + Power BI звіт

- **3. Збереження даних з пп. 1–2 в CSV**:
  - Генерація `customers.csv`, `orders.csv`: `src/generate_data.py`
  - Генерація `managers.csv` (включно з `Experience_diap`), `grouped_analysis.csv`: `src/manager_details.py`
- **3a. Power BI**: інструкції в `powerbi/README.md`
  - Фільтри: діапазон дат, стаж/`Experience_diap`, стать клієнта, тип оплати, тип доставки, канал замовлення.

### 4) SQL-запити під структуру даних

Файл з прикладами запитів: `src/queries.sql`

- **4a. Клієнти без замовлень за останні 3 місяці**
- **4b. Топ-5 менеджерів за сумою замовлень за останній місяць**
- **4c. Середній стаж менеджерів за `Experience_diap`** для менеджерів, у яких були замовлення від жінок віком до 30 років на суму від 3000 грн

> Примітка: `src/queries.sql` написаний у стилі SQL Server (використовує `GETDATE()`/`DATEADD`).

### 5) Excel + VBA

- **5a. VBA імпорт CSV на окремі аркуші + фільтр замовлень**: `excel/Order_system.xlsm`
- **5b. Діаграми та пояснення вибору**: `excel/README.md`