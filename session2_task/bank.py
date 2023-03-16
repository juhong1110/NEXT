class Bank:
    def __init__(self, total_amount, limit_for_loan, limit_for_withdrawl):
        self.total_amount = total_amount
        self.limit_for_loan = limit_for_loan
        self.limit_for_withdrwal = limit_for_withdrawl
    def repeat_withdrawing_money(self, amount, limit_for_withdrwal):
        count=amount//limit_for_withdrwal
        rest=amount%limit_for_withdrwal
        
        for i in range(count):
            print(f'This is your money - {limit_for_withdrwal}')
            if i == (count - 1):
                print(f'This is your money - {rest}')
                
    def show_me_the_money(self, amount):
        if amount <= self.total_amount:
            self.repeat_withdrawing_money(amount, self.limit_for_withdrwal)
        elif amount <= (self.total_amount + self.limit_for_loan):
            print('Wait! Do you want loan??')
        else:
            print('Your money is not enough')
            
hana_bank=Bank(1000,200,100)
hana_bank.show_me_the_money(450)
print()

sinhan_bank=Bank(500,500,50)
sinhan_bank.show_me_the_money(250)