1. Preparation
Install Python: Ensure you have Python installed on your computer.
Save the File: Save the provided code into a file named midterm_solution.py.
Open Terminal: Open your Command Prompt or Terminal and go to the folder where you saved the file.
2. Running the Program
Run the script by typing the following command:
bash
python midterm_solution.py
Use code with caution.
3. How to Use the Program (Step-by-Step)
Step A: Initial Setup
Name: Type your name and press Enter.
Weekly Budget: Enter your total allowance for the week (e.g., 1000). Use numbers only (no "P" or commas).
Step B: Categorize Your Spending
The program provides 5 categories to choose from:
Food & Drinks
Transportation
Mobile / Internet
School Supplies
Entertainment
Step C: Logging Expenses (4 Entries)
The program will loop 4 times to ask for your expenses.
Select Category: Type a number from 1 to 5.
Skip an Entry: If you don't have 4 things to list, type 0 to skip that entry.
Item Description: Type what you bought (e.g., "Jeepney Fare").
Amount: Type the cost of that specific item.
Step D: The "High Expense" Rule
You don't need to do anything here! The program automatically checks if an item costs more than 25% of your budget.
Example: If your budget is P1000 and you spend P300 on one item, the program will automatically tag it with ! High Expense Alert!.
4. Understanding Your Final Report
Once all entries are done, a formatted report will appear showing:
Log Details: A list of every item, its price, and any alerts.
Total Spent: The sum of all your costs.
Remaining Balance: How much money you have left.
Status:
Budget OK! Keep it up. — if you stayed within your budget.
Overspent! Reduce spending. — if you spent more than your allowance.
