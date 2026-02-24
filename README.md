# Python Data Types & String Formatting

## 📌 Goal
To understand basic Python data types and practice string formatting using the `print()` function.

## 🧩 Scenario
This program displays a simple product receipt using hardcoded values and calculates the total cost.

## 🛠 Concepts Covered
- Python Data Types (`int`, `float`, `str`, `bool`)
- Variable declaration
- String formatting using commas in `print()`
- Arithmetic operations

## 📄 Program Description
The script:
- Stores item details such as name, quantity, price, and availability
- Displays a formatted receipt
- Calculates and prints the total cost of the item

## 🧪 Sample Code
```python
item_name = "Laptop"
quantity = 2
price = 499.99
in_stock = True

print("Item:", item_name, ", Qty:", quantity, ", Price:", price, ", Available:", in_stock)

total_cost = quantity * price
print("Total Cost:", total_cost)
