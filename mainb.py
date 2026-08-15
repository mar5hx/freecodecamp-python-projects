from budget import Category, create_spend_chart

# 1. Create categories
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

# 2. Deposit funds
food.deposit(1000, "initial deposit")
clothing.deposit(500, "initial deposit")
auto.deposit(300, "initial deposit")

# 3. Make some purchases and transfers
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for the week")
food.transfer(50, clothing)

clothing.withdraw(25.55, "jeans")
auto.withdraw(100, "gas and oil change")

# 4. Print the categories to see the ledger layout
print(food)
print(clothing)
print(auto)

# 5. Print the spend chart
print(create_spend_chart([food, clothing, auto]))