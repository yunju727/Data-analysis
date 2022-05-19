n=int(input())
numerator=[]
denominator=[]
print("쪼갠 사건의 확률") 
for i in range(n):
    numerator.append(float(input()))
print("쪼갠 사건의 조건부 확률")
for i in range(n):
    denominator.append(float(input()))
denom=[]
for i in range(n):
    denom.append(numerator[i]*denominator[i])
want=int(input("원하는 확률 인덱스"))

print("섬",sum(denom))
print("특정 사건이 일어날 확률",sum(denom))
print("답:",denom[want]/sum(denom))

