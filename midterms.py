name = input("Enter your name: ")

while True:
    try:
        budget = float(input("Enter your weekly budget: "))
        break
    except ValueError:
        print("Invalid input! Please enter a number for your budget.")

print("\n--- Expense Categories ---")
print("1. Food & Drinks")
print("2. Transportation")
print("3. Mobile / Internet")
print("4. School Supplies")
print("5. Entertainment")

total_spent = 0
log_details = ""

for i in range(1, 5): 
    print("\nExpense Entry", i)
    
    try:
        cat_num = int(input("Enter category (1-5, or 0 to skip): "))
        if cat_num == 0:
            continue
            
        item = input("Description: ")
        cost = float(input("Amount: "))
        
        alert = ""
        if cost > (budget * 0.25):
            alert = " ! High Expense Alert!"
            
        total_spent = total_spent + cost
        log_details = log_details + str(i) + ". " + item + " (P" + str(cost) + ")" + alert + "\n"
    except ValueError:
        print("Invalid input. Skipping this entry...")
        continue

balance = budget - total_spent

if balance >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

print("\n==========================")
print("WEEKLY REPORT FOR", name)
print("Budget: P", budget)
print("--------------------------")
print(log_details)
print("--------------------------")
print("Total Spent: P", total_spent)
print("Remaining: P", balance)
print("Status:", status)
print("==========================")
