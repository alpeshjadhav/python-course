class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # private variable

    def reset_pass(self):
        print(self.__acc_pass)  # prints the private variable


acc1 = Account("12345", "abcde")

print(acc1.acc_no)  # This will work: public variable
# print(acc1.__acc_pass)  # This will throw an AttributeError

print(acc1.reset_pass())  # This will print the password and then 'None'
