## Power BI: побудова звіту

Ціль: завантажити CSV з папки `data/` та побудувати звіт по **середній сумі замовлення** з можливістю одночасно застосовувати фільтри:

- діапазон дат замовлення
- стаж роботи менеджера / `Experience_diap`
- стать клієнта
- тип оплати
- тип доставки
- канал замовлення

### 1) Завантаження даних

1. Відкрийте Power BI Desktop → **Get data** → **Text/CSV**.
2. Послідовно завантажте:
   - `data/customers.csv`
   - `data/managers.csv`
   - `data/orders.csv`

### 2) Зв’язки між таблицями

У **Model view** перевірте/створіть зв’язки:

- `Orders[CustomerID]` → `Customers[CustomerID]` (Many-to-one)
- `Orders[ManagerID]` → `Managers[ManagerID]` (Many-to-one)

### 3) Міра для середньої суми замовлення

Створіть міру (Modeling → New measure):

```DAX
Average Order Sum = AVERAGE(Orders[OrderSum])
```

### 4) Візуали та фільтри

- Додайте Card/Line chart/Bar chart з мірою **Average Order Sum**.
- Додайте Slicer-и:
  - `Orders[OrderDate]` (Between)
  - `Managers[Experience_diap]`
  - `Customers[Gender]`
  - `Orders[PaymentType]`
  - `Orders[DeliveryType]`
  - `Orders[OrderChannel]`

### 5) Перевірка

Перевірте, що при зміні будь-якого слайсера значення міри **Average Order Sum** змінюється, і що слайсери можна застосовувати одночасно.

