wight = float(input("enter your wight"))
print("is it in Kg (K) or Lbs (L)")
kgOrLbs = input()
if kgOrLbs == ('K' or 'k'):
    print("your wight in lbs is " + str(wight * 2.205))

elif kgOrLbs == ('l' or 'L'):
    print("your wight in kg is " + str(wight / 2.205))
print("done")
# test