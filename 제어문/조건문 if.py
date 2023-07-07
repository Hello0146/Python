# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않으면 걸어가라.
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")



# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라.
money = 2000
card = True

if money >= 3000 or card:
    print("택시 타고 가라")
else:
    print("걸어가라")



# 만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라.
pocket = ['paper', 'money', 'card']
if 'money' in pocket:
    print("택시 타고 가라")
else:
    print("걸어가라")



# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
# 주머니에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 카드를 꺼내라.
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드 꺼내라")
