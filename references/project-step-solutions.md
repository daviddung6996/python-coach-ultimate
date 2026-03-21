# Project Step Solutions — COACH INTERNAL REFERENCE

> **RULE:** File này chỉ dành cho coach. KHÔNG gửi link file này cho learner.
> Coach chỉ show solution code của một step SAU KHI learner đã nộp bài cho step đó.
> Flow: learner nộp code → coach chấm → nếu đúng: show solution để so sánh → sang step tiếp.
> Nếu sai: chỉ ra lỗi, gợi ý, yêu cầu sửa. KHÔNG show solution khi learner chưa thử.

---

## Chapter 1 → P1 Step 1: Registration Form

```python
# registration_form.py
name = input("Tên: ")
email = input("Email: ")
password = input("Password: ")

print(f"Tên: {name}, Email: {email}, Password: {password}")
print("Đăng ký thành công!")
```

**Coach check:** Learner phải dùng đúng input() và print(). Bonus nếu dùng f-string.

---

## Chapter 2 → P1 Step 2: Name & Email Validation

```python
# registration_form.py (upgraded)
name = input("Tên: ").strip().title()
email = input("Email: ").strip()
password = input("Password: ")

# Validate name
if len(name) >= 3:
    print("Name hợp lệ:", name)
else:
    print("Name quá ngắn, cần ít nhất 3 ký tự")

# Validate email
if "@" in email and "." in email:
    print("Email hợp lệ:", email)
else:
    print("Email sai format, cần có @ và .")

print(f"Thông tin: {name} - {email}")
```

**Coach check:** Dùng len(), "in" operator, .strip(), .title(). if/else ở đây là preview — chưa cần giải thích sâu.

---

## Chapter 3 → P2 Step 1: Expense Calculator

```python
# expense_calc.py
food = 50000
transport = 20000
coffee = 15000
entertainment = 100000

total = food + transport + coffee + entertainment
count = 4
average = round(total / count)

print(f"Tổng chi: {total:,} VND")
print(f"Số khoản: {count}")
print(f"Trung bình: {average:,} VND")
```

**Coach check:** Phép tính đúng, dùng round(). Bonus nếu dùng f-string format {:,} cho số.

---

## Chapter 4 → P1 Step 3: Password Strength Check

```python
# registration_form.py (upgraded)
password = input("Password: ")

has_length = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
is_valid = has_length and has_upper and has_digit

print(f"Đủ 8 ký tự: {has_length}")
print(f"Có chữ hoa: {has_upper}")
print(f"Có chữ số: {has_digit}")
print(f"Password hợp lệ: {is_valid}")
```

**Coach check:** Dùng any() + generator expression là cách gọn nhất. Nếu learner dùng for loop cũng OK — show any() như cách tốt hơn.

---

## Chapter 4 → P3 Step 1: Balance Check

```python
# balance_check.py
balance = 1000000
withdraw_amount = float(input("Số tiền muốn rút: "))

can_withdraw = balance >= withdraw_amount
is_positive = withdraw_amount > 0
is_valid = can_withdraw and is_positive

print(f"Số dư hiện tại: {balance:,} VND")
print(f"Số tiền rút: {withdraw_amount:,} VND")
print(f"Đủ tiền: {can_withdraw}")
print(f"Số tiền hợp lệ: {is_positive}")
print(f"Có thể rút: {is_valid}")
```

**Coach check:** Dùng comparison + logical operators đúng. Bonus nếu convert input sang float.

---

## Chapter 5 → P2 Step 2: Expense Validator

```python
# expense_validator.py
amount = float(input("Số tiền: "))
category = input("Category (Food/Transport/Entertainment): ")
description = input("Mô tả: ")

if amount <= 0:
    print("Lỗi: Số tiền phải lớn hơn 0")
elif category not in ["Food", "Transport", "Entertainment"]:
    print(f"Lỗi: Category '{category}' không hợp lệ")
else:
    print(f"Expense hợp lệ: {category} - {description} - {amount:,} VND")
```

**Coach check:** if/elif/else đúng thứ tự, dùng "not in" cho list check.

---

## Chapter 5 → P3 Step 2: Transaction Menu

```python
# banking_menu.py
balance = 1000000

action = input("Hành động (deposit/withdraw/check): ").lower()

if action == "deposit":
    amount = float(input("Số tiền nạp: "))
    if amount <= 0:
        print("Số tiền không hợp lệ")
    else:
        balance += amount
        print(f"Đã nạp {amount:,} VND. Số dư: {balance:,} VND")

elif action == "withdraw":
    amount = float(input("Số tiền rút: "))
    if amount <= 0:
        print("Số tiền không hợp lệ")
    elif amount > balance:
        print(f"Không đủ tiền. Số dư chỉ có {balance:,} VND")
    else:
        balance -= amount
        print(f"Đã rút {amount:,} VND. Số dư: {balance:,} VND")

elif action == "check":
    print(f"Số dư hiện tại: {balance:,} VND")

else:
    print("Hành động không hợp lệ")
```

**Coach check:** Nested if đúng (withdraw cần check cả amount > 0 VÀ sufficient funds). .lower() cho input là bonus.

---

## Chapter 6 → P1 Step 4: Multi-User Registration Loop

```python
# registration_loop.py
success_count = 0
fail_count = 0

while True:
    action = input("\nĐăng ký (r) hay thoát (q)? ").lower()
    if action == "q":
        break
    if action != "r":
        print("Chọn 'r' hoặc 'q'")
        continue

    name = input("Tên: ").strip().title()
    email = input("Email: ").strip()
    password = input("Password: ")

    # Validate name
    if len(name) < 3:
        print("Tên quá ngắn, cần ít nhất 3 ký tự")
        fail_count += 1
        continue

    # Validate email
    if "@" not in email or "." not in email:
        print("Email sai format")
        fail_count += 1
        continue

    # Validate password
    has_length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    if not (has_length and has_upper and has_digit):
        print("Password yếu: cần >= 8 ký tự, 1 chữ hoa, 1 chữ số")
        fail_count += 1
        continue

    print(f"Đăng ký thành công: {name} ({email})")
    success_count += 1

print(f"\nKết quả: {success_count} thành công, {fail_count} thất bại")
```

**Coach check:** while True + break, continue đúng chỗ, counter variables.

---

## Chapter 6 → P2 Step 3: Expense Aggregator

```python
# expense_aggregator.py
expenses = [50000, 20000, 100000, 15000, 30000]
categories = ["Food", "Transport", "Food", "Coffee", "Food"]

# Tính tổng
total = 0
for amount in expenses:
    total += amount
print(f"Tổng chi: {total:,} VND")

# Đếm và tổng theo Food
food_total = 0
food_count = 0
for i in range(len(expenses)):
    if categories[i] == "Food":
        food_total += expenses[i]
        food_count += 1
print(f"Food: {food_count} khoản, tổng {food_total:,} VND")

# Hiển thị có đánh số
print("\nChi tiết:")
for i, amount in enumerate(expenses, start=1):
    print(f"{i}. {categories[i-1]} - {amount:,} VND")
```

**Coach check:** Accumulator pattern, loop + if filter, enumerate. Nếu learner dùng zip(expenses, categories) thì rất tốt.

---

## Chapter 6 → P3 Step 3: Multi-Transaction Loop

```python
# banking_loop.py
balance = 1000000
transactions = []

while True:
    print(f"\n[Số dư: {balance:,} VND]")
    action = input("deposit/withdraw/check/exit: ").lower()

    if action == "exit":
        break

    if action == "deposit":
        amount = float(input("Số tiền nạp: "))
        if amount <= 0:
            print("Số tiền không hợp lệ")
        else:
            balance += amount
            transactions.append(f"Deposit: {amount:,.0f} VND")
            print(f"Đã nạp. Số dư: {balance:,} VND")

    elif action == "withdraw":
        amount = float(input("Số tiền rút: "))
        if amount <= 0:
            print("Số tiền không hợp lệ")
        elif amount > balance:
            print("Không đủ tiền")
        else:
            balance -= amount
            transactions.append(f"Withdrawal: {amount:,.0f} VND")
            print(f"Đã rút. Số dư: {balance:,} VND")

    elif action == "check":
        print(f"Số dư: {balance:,} VND")

    else:
        print("Không hiểu lệnh")

print(f"\n=== KẾT THÚC ===")
print(f"Số dư cuối: {balance:,} VND")
print(f"Lịch sử ({len(transactions)} giao dịch):")
for t in transactions:
    print(f"  - {t}")
```

**Coach check:** while True + break, list.append() cho transactions, for loop in history.

---

## Chapter 7 → P1 Step 5: Data Storage với List of Dicts

```python
# registration_system.py
registered_users = []
failed_registrations = []

while True:
    action = input("\nĐăng ký (r) hay thoát (q)? ").lower()
    if action == "q":
        break
    if action != "r":
        continue

    name = input("Tên: ").strip().title()
    email = input("Email: ").strip()
    password = input("Password: ")

    # Check duplicate email
    duplicate = False
    for user in registered_users:
        if user["email"] == email:
            duplicate = True
            break

    if duplicate:
        failed_registrations.append({"email": email, "error": "Email đã tồn tại"})
        print("Email đã được đăng ký")
        continue

    # Validate name
    if len(name) < 3:
        failed_registrations.append({"email": email, "error": "Tên quá ngắn"})
        print("Tên quá ngắn")
        continue

    # Validate email
    if "@" not in email or "." not in email:
        failed_registrations.append({"email": email, "error": "Email sai format"})
        print("Email sai format")
        continue

    # Validate password
    if not (len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password)):
        failed_registrations.append({"email": email, "error": "Password yếu"})
        print("Password yếu")
        continue

    # Success
    user = {"name": name, "email": email, "password": password, "status": "active"}
    registered_users.append(user)
    print(f"Đăng ký thành công: {name}")

# Summary
print("\n=== REGISTERED USERS ===")
for u in registered_users:
    print(f"  {u['name']} | {u['email']} | {u['status']}")

print("\n=== FAILED REGISTRATIONS ===")
for f in failed_registrations:
    print(f"  {f['email']}: {f['error']}")
```

**Coach check:** Dict creation đúng, list.append(dict), for loop search duplicate, access dict["key"].

---

## Chapter 7 → P2 Step 4: Structured Expenses

```python
# expense_system.py
expenses = []

# Thêm expenses
expenses.append({"amount": 50000, "category": "Food", "description": "Groceries"})
expenses.append({"amount": 20000, "category": "Transport", "description": "Taxi"})
expenses.append({"amount": 100000, "category": "Food", "description": "Restaurant"})
expenses.append({"amount": 15000, "category": "Coffee", "description": "Morning coffee"})
expenses.append({"amount": 30000, "category": "Food", "description": "Lunch"})

# Tổng tất cả
total = 0
for expense in expenses:
    total += expense["amount"]
print(f"Tổng chi: {total:,} VND")

# Tổng theo category
target = "Food"
cat_total = 0
for expense in expenses:
    if expense["category"].lower() == target.lower():
        cat_total += expense["amount"]
print(f"Tổng {target}: {cat_total:,} VND")

# Hiển thị
print("\nChi tiết:")
for i, exp in enumerate(expenses, start=1):
    print(f"{i}. {exp['category']} - {exp['description']}: {exp['amount']:,} VND")
```

**Coach check:** List of dicts, dict access, loop + filter bằng .lower(), enumerate.

---

## Chapter 7 → P3 Step 4: Account với Nested Data

```python
# banking_system.py
accounts = []

# Tạo account
account = {"name": "Baraa", "balance": 1000000, "transactions": []}
accounts.append(account)

# Tìm account
def find_in_accounts(name):
    for acc in accounts:
        if acc["name"].lower() == name.lower():
            return acc
    return None

# Deposit
target = find_in_accounts("Baraa")
if target:
    amount = 200000
    target["balance"] += amount
    target["transactions"].append({"type": "Deposit", "amount": amount})
    print(f"Đã nạp {amount:,}. Số dư: {target['balance']:,}")

# Withdraw
if target:
    amount = 150000
    if amount <= target["balance"]:
        target["balance"] -= amount
        target["transactions"].append({"type": "Withdrawal", "amount": amount})
        print(f"Đã rút {amount:,}. Số dư: {target['balance']:,}")
    else:
        print("Không đủ tiền")

# Show account
if target:
    print(f"\n=== Account: {target['name']} ===")
    print(f"Số dư: {target['balance']:,} VND")
    print("Giao dịch:")
    for t in target["transactions"]:
        print(f"  - {t['type']}: {t['amount']:,} VND")
```

**Coach check:** Nested data — dict chứa list of dicts. Mutation đúng (target["balance"] += amount). transactions.append(dict).
Note: find_in_accounts dùng function vì learner đã preview từ code trước, nhưng chính thức học functions ở Ch.8.

---

## Chapter 8 → P1 FINAL: Complete User Registration System

```python
"""
User Registration System — Final Version
"""

registered_users = []
failed_registrations = []


def validate_name(name):
    """Validate tên >= 3 ký tự."""
    return len(name) >= 3


def validate_email(email):
    """Validate email chứa @ và ."""
    return "@" in email and "." in email


def validate_password(password):
    """Validate password: >= 8 ký tự, có chữ hoa, có số."""
    if len(password) < 8:
        return False
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_uppercase and has_digit


def validate_user_data(name, email, password):
    """Gọi 3 hàm validate. Raise ValueError nếu fail."""
    if not validate_name(name):
        raise ValueError("Name must contain at least 3 characters.")
    if not validate_email(email):
        raise ValueError("Email must contain '@' and '.'.")
    if not validate_password(password):
        raise ValueError(
            "Password must be at least 8 characters long and "
            "contain one uppercase letter and one digit."
        )
    return True


def create_user_account(name, email, password):
    """Tạo account. Return dict nếu thành công, None nếu fail."""
    try:
        validate_user_data(name, email, password)

        if any(user["email"] == email for user in registered_users):
            raise ValueError("An account with this email already exists.")

        user_record = {
            "name": name,
            "email": email,
            "password": password,
            "status": "active",
        }
        registered_users.append(user_record)
        return user_record

    except ValueError as error:
        failed_registrations.append({"email": email, "error": str(error)})
        return None


def run_tests():
    test_cases = [
        ("Baraa", "baraa@email.com", "Password1"),       # Valid
        ("AnotherUser", "baraa@email.com", "Password1"),  # Duplicate email
        ("Al", "al@email.com", "Password1"),              # Invalid name
        ("Sarah", "sarah@email.com", "weakpass"),          # Weak password
    ]

    for index, (name, email, password) in enumerate(test_cases, start=1):
        print(f"\nTest {index}")
        result = create_user_account(name, email, password)
        if result:
            print("Registration successful:", result)
        else:
            print("Registration failed.")

    print("\nFinal Registered Users:")
    print(registered_users)
    print("\nFailed Registrations:")
    print(failed_registrations)


run_tests()
```

**Coach check:** Functions clean, raise/try-except đúng chỗ, any() cho duplicate check, docstrings.

---

## Chapter 8 → P2 FINAL: Complete Expense Tracking System

```python
"""
Expense Tracker System — Final Version
"""

expenses = []


def add_expense(amount, category, description):
    """Thêm expense. Raise ValueError nếu amount <= 0."""
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    expense = {"amount": amount, "category": category, "description": description}
    expenses.append(expense)
    return expense


def calculate_total_expenses():
    """Tính tổng tất cả expenses."""
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_total_by_category(category):
    """Tính tổng theo category."""
    total = 0
    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]
    return total


def show_expenses():
    """Hiển thị tất cả expenses."""
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nAll Expenses:")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['category']} - "
            f"{expense['description']} : ${expense['amount']}"
        )


def run_tests():
    try:
        add_expense(50, "Food", "Groceries")
        add_expense(20, "Transport", "Taxi")
        add_expense(100, "Food", "Restaurant")
        add_expense(0, "Entertainment", "Cinema")  # Invalid
    except ValueError as error:
        print("Error:", error)

    print("\nTotal Expenses:", calculate_total_expenses())
    print("Total Food Expenses:", calculate_total_by_category("Food"))
    show_expenses()


if __name__ == "__main__":
    run_tests()
```

**Coach check:** Mỗi function một việc, validation + raise đúng, .lower() cho category, enumerate.

---

## Chapter 8 → P3 FINAL: Complete Mini Banking System

```python
"""
Mini Banking System — Final Version
"""

accounts = []


def find_account(name):
    """Tìm account theo tên. Return dict hoặc None."""
    for account in accounts:
        if account["name"].lower() == name.lower():
            return account
    return None


def create_account(name, initial_balance):
    """Tạo account mới. Raise ValueError nếu invalid."""
    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative.")
    if find_account(name):
        raise ValueError("Account with this name already exists.")
    account = {"name": name, "balance": initial_balance, "transactions": []}
    accounts.append(account)
    return account


def deposit(name, amount):
    """Nạp tiền. Raise ValueError nếu invalid."""
    if amount <= 0:
        raise ValueError("Deposit amount must be greater than 0.")
    account = find_account(name)
    if not account:
        raise ValueError("Account not found.")
    account["balance"] += amount
    account["transactions"].append({"type": "Deposit", "amount": amount})
    return account["balance"]


def withdraw(name, amount):
    """Rút tiền. Raise ValueError nếu invalid hoặc không đủ tiền."""
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than 0.")
    account = find_account(name)
    if not account:
        raise ValueError("Account not found.")
    if amount > account["balance"]:
        raise ValueError("Insufficient funds.")
    account["balance"] -= amount
    account["transactions"].append({"type": "Withdrawal", "amount": amount})
    return account["balance"]


def show_account(name):
    """Hiển thị summary + transactions."""
    account = find_account(name)
    if not account:
        print("Account not found.")
        return
    print(f"\nAccount Summary for {account['name']}")
    print(f"Current Balance: ${account['balance']}")
    print("Transactions:")
    if not account["transactions"]:
        print("No transactions yet.")
    else:
        for transaction in account["transactions"]:
            print(f"- {transaction['type']} : ${transaction['amount']}")


def run_tests():
    try:
        create_account("Baraa", 1000)
        deposit("Baraa", 200)
        withdraw("Baraa", 150)
        withdraw("Baraa", 2000)  # Overdraft test
    except ValueError as error:
        print("Error:", error)
    show_account("Baraa")


run_tests()
```

**Coach check:** Helper function find_account() reused everywhere, nested data mutation, docstrings, raise/try-except.
