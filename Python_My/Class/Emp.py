class emp:
    def __init__(self,eno,ename,eadd):
        self.eno=eno
        self.ename=ename
        self.eadd=eadd
        print('In init')
    def display(self):
        print(self.eno,'\t',self.ename,'\t',self.eadd)
    def test(self):
        print('In test')

