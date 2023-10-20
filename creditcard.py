def valid(cardnumsplit):
    sum1 = sum(cardnumsplit[0:14])
    div1 = cardnumsplit[14]
    div2 = cardnumsplit[15]
    divend = div1 * 10 + div2
    return sum1 == divend

cardnumIn = input("Enter credit card number:")

cardnumsplit = []
for i in cardnumIn:
    cardnumsplit.append(int(i))

if len(cardnumsplit) == 16:
    if valid(cardnumsplit):
        print("Valid Credit Card Number")
    else:
        print("Invalid Credit Card Number")
else:
    print("Invalid Credit Card Number")
