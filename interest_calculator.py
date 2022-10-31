NAME= (input ("ENTER YOUR NAME ")) 
BP=int (input ("ENTER BASIC PAY "))
DA=25/100 * BP
HRA=15/100 * BP
PF=8.33/100 * BP
NP=BP+DA+HRA
GP=NP-PF
print ("BASIC PAY OF", NAME, "IS", BP)
print ("DEARNESS ALLOWANCE IS", DA)
print ("HRA IS", HRA)
print ("PF IS", PF)
print ("NET PAY IS", NP)
print ("GROSS PAY IS", GP)
