#Assert function
x=int(input('enter x:'))
assert(x==0),'Input value is {}'
if x>0:
    pass
else:
    assert(x>0),'Input value is {}'.format(x)
    
