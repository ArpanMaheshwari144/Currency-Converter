with open('data.txt') as f:
    lines=f.readlines()

currencyDict={}
for line in lines:
    parsed=line.split("\t")
    currencyDict[parsed[0]]=parsed[1]
amount=int(input("Enter Amount: "))
print("Enter The Name Of Currency You Want To Convert This Amount To? Available Options Are: ")
[print(item) for item in currencyDict.keys()]
currency=input("Please Enter One Of These Values: ")
print(f"{amount} INR Is Equal To {amount * float(currencyDict[currency])} {currency}")
