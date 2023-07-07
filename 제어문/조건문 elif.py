"""
주머니에 돈이 있으면 택시를 타고 가고, 
주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 
돈도 없고 카드도 없으면 걸어가라.
"""

pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket:
    print("택시 타고 가라")
elif card:
    print("택시 타고 가라")
else:
    print("걸어가라")