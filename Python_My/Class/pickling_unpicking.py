import pickle
class emp:
    def __init__(self):
        self.eno=1186599
        self.ename='Arunkumar'
        self.eadd='Hyd'
        print('In init')
    def display(self):
        print(self.eno,'\t',self.ename,'\t',self.eadd)

with open('try.txt','wb') as f:
    e=emp()
    e.display()
    #In dump we need to give object and file name 
    pickle.dump(e,f)
    print('pickling of emp object completed...')
with open('try.txt','rb') as f:
    emp1=pickle.load(f)
    print('unpicking of emp object completed...')
    emp1.display()
    
    
