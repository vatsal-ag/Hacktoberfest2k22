CP=450
MP=int(input('Enter Marked Price'))
D=0.1*MP
SP=MP-D
P=SP-CP
PPer=(P/CP)*100
if P<0:
  print('loss= ',P*10)
else: 
  print('Profit= ',P*10)
