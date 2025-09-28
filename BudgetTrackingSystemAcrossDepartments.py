from datetime import datetime


class Transaction:
    def __init__(self, transaction_id, amount, t_type, description, timestamp=None):
        self.transaction_id, self.amount, self.type, self.description = transaction_id, amount, t_type, description
        self.timestamp = timestamp if timestamp else datetime.now()

    def __str__(self):
        return f"[{self.timestamp}] ID: {self.transaction_id}, {self.type.title()}, Amount: {self.amount}, {self.description}"


class Department:
    def __init__(self, department_id, name, budget=0):
        self.department_id, self.name, self.budget = department_id, name, budget

    def adjust_budget(self, amount, action='increase'):
        self.budget = self.budget + amount if action == 'increase' else self.budget - amount

    def __str__(self):
        return f"Department: {self.name}, Budget: {self.budget}"


class BudgetTrackingSystem:
    def __init__(self):
        self.transactions, self.departments = [], []

    def create_transaction(self, transaction_id, amount, t_type, description):
        t = Transaction(transaction_id, amount, t_type, description)
        self.transactions.append(t)
        return t

    def add_department(self, department_id, name, budget=0):
        d = Department(department_id, name, budget)
        self.departments.append(d)
        return d

    def manage_department_budgets(self, department_id, amount, action):
        d = next((d for d in self.departments if d.department_id == department_id), None)
        if d: d.adjust_budget(amount, action)

    def report_financial_overview(self):
        total_budget = sum(d.budget for d in self.departments)
        spending = sum(t.amount if t.type == 'debit' else -t.amount for t in self.transactions)
        return {
            "Total Budget": total_budget,
            "Total Spending": spending,
            "Departments": {d.name: d.budget for d in self.departments},
            "Transactions": [str(t) for t in self.transactions]
        }


def main():
    bts = BudgetTrackingSystem()
    while True:
        print("1.Add departments")
        print("2.Add transactions")
        print("3.Modify department budget")
        print("4.Financial overview")
        print("5.exit")
        
        choice=input('enter your choice(1-5):').strip()
        if choice == '1':
        # Input number of departments
            num_departments = int(input("Enter the number of departments: "))
                
                # Add departments
            for _ in range(num_departments):
                dept_id = int(input("\nEnter department ID: "))
                dept_name = input("Enter department name: ")
                dept_budget = float(input("Enter department budget: "))
                dept = bts.add_department(dept_id, dept_name, dept_budget)
                print(f"Added {dept}")
                print('\n')
        elif choice == '2':
                # Input number of transactions
            num_transactions = int(input("\nEnter the number of transactions: "))
                
                # Add transactions
            for _ in range(num_transactions):
                transaction_id = int(input("\nEnter transaction ID: "))
                amount = float(input("Enter transaction amount: "))
                transaction_type = input("Enter transaction type (debit/credit): ").lower()
                description = input("Enter transaction description: ")
                transaction = bts.create_transaction(transaction_id, amount, transaction_type, description)
                print(f"Added {transaction_type} transaction: {transaction_id}, Amount: {amount}, Description: {description}")
                print('\n')
        elif choice =='3':       
                # Modify department budgets
            num_modifications = int(input("\nEnter the number of budget modifications: "))
                
            for _ in range(num_modifications):
                dept_id = int(input("\nEnter department ID for budget modification: "))
                amount = float(input("Enter amount to modify: "))
                action = input("Enter action (increase/decrease): ").lower()
                bts.manage_department_budgets(dept_id, amount, action)
                print(f"Updated budget for department {dept_id}")
                print('\n')
        elif choice =='4':
                # Print financial overview
            financial_report = bts.report_financial_overview()
            print("\nFinancial Overview:")
            for dept, budget in financial_report.items():
                print(f"{dept}: {budget}")
                print('\n')
        elif choice =='5':
            print('exiting the system')
            break
            print('\n')
        else:
            print('Invalid choice please try again')
            print('\n')
    # Run the main function
if __name__ == "__main__":
    main()
    
