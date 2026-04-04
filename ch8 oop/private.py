class account:
    def __init__(self, account_number, account_pw):
            self.account_number = account_number
            self.__account_pw = account_pw
        
acc1 = account("123-456-789", "1234")
print(acc1.account_number) # 123-456-789
print(acc1.__account_pw) # AttributeError: 'account' object has no attribute '__account_pw'