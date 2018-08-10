cart=[100,200,300,400,500,600]
for item in cart:
    if item >400:
        print("Can't process item:{}".format(item))
        continue
    if item==0:
        print("DivisionbyZero Error")
        break
    print("Processed Items:",item)
else:# This else will be executed if no break item is encountered in the flow
    print("All items are processed")

for item in cart:
    if item >400:
        print("Can't process item:{}".format(item))
        continue
    print("Processed Items:",item)
else:# This else will be executed if no break item is encountered in the flow
    print("All items are processed")




i=0
for item in cart:
    i+=1
    if 2<i<4:
        print(item)
