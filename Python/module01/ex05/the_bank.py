
class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """

    def fix_account(self, account):
        for acc in self.account:
            if acc.id == account or acc.name == account:
                break
        clean = 0
        while clean == 0:
            lst = []
            for attribute in acc.__dict__:
                lst.append(attribute)
                if str(attribute)[0] == 'b':
                    break
                if len(lst) == len(acc.__dict__):
                    clean = 1
            if str(attribute)[0] == 'b':
                delattr(acc, attribute)
                lst.remove(attribute)
        if not all(i in lst for i in ["id", "name", "value"]):
            print("Corrupted for name/id/value")
            return 1
        elif not any(any(sub in x for x in lst) for sub in ["zip", "addr"]):
            print("Corrupted for zip/addr")
            return 1
        elif (len(lst) % 2) == 0:
            print("Corrupted by even number of attributes")
            return 1
        return 0

        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """

    def check_corrupted(self, account):
        for acc in self.account:
            if acc.id == account or acc.name == account:
                break
        lst = []
        for attribute in acc.__dict__:
            lst.append(attribute)
            if str(attribute)[0] == 'b':
                print("Corrupted because of b")
                return 1
        if not all(i in lst for i in ["id", "name", "value"]):
            print("Corrupted for name/id/value")
            return 1
        elif not any(any(sub in x for x in lst) for sub in ["zip", "addr"]):
            print("Corrupted for zip/addr")
            return 1
        elif (len(lst) % 2) == 0:
            print("Corrupted by even number of attributes")
            return 1
        return 0


A = Account("Arthur", value=10, address=92, blue=2, br=87)
B = Account("Bob")
C = Account("Charles", value=10, zip=21, rdm = 78)

LCL = Bank()
LCL.add(A)
LCL.add(B)
LCL.add(C)
print(A.__dict__)
LCL.fix_account(1)
print(A.__dict__)

#Reste a faire: Finir la fonction de correction des comptes corrompus, mettre en place les virements