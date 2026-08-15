class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount * -1 , 'description': description})
            return True
        return False
        

    def get_balance(self):
        total = 0
        for i in self.ledger:
            total += i['amount']
        return total

    def transfer(self, amount, instance):
        if self.withdraw(amount, f'Transfer to {instance.name}'):
            instance.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True

    def __str__(self):
        title_line = f'{self.name:*^30}'
        receipt = title_line + '\n'
        for i in self.ledger:
            des = i['description'][:23]
            amt = i['amount']
            receipt += f'{des:<23}{amt:>7.2f}\n'
        receipt += f'Total: {self.get_balance():.2f}'
        return receipt

#this is so cool

def create_spend_chart(categories):
    title = 'Percentage spent by category'
    spending_totals = []
    for cat in categories:
        cat_spent = 0
        for i in cat.ledger:
            amount = i['amount'] 
            if amount < 0:
                cat_spent += abs(amount)
        spending_totals.append(cat_spent)
    grand_total = sum(spending_totals)
    percentages = []
    for e in spending_totals:
        per = ((e / grand_total) * 100) // 10 * 10
        percentages.append(per)
    y_axis = range(100, -1, -10)
    chart = title + '\n'
    for y in y_axis:
        chart += f"{y:>3}|"
        for p in percentages:
            if p >= y:
                chart += ' o '
            else:
                chart += '   '
        chart += ' \n'
    chart+= '    ' + ('-' * (len(categories) * 3 + 1)) + '\n'
    max_len = max([len(cat.name) for cat in categories])
    for i in range(max_len):
        chart += '    ' 
        for r in categories:
            if i < len(r.name):
                chart += f' {r.name[i]} '
            else: 
                chart += '   '
        chart += ' \n'
    return chart.rstrip('\n')