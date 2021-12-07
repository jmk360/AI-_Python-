# 튜플은 값을 바꿀 수 가 없다.
# t = (10, 20, 30, 40, 50) # 함수, 반복문 에 많이 사용 # 값을 수정하지 못하기 때문문 값을 보존하기 위해서도 사용이 됨.
# print(t)
# print(type(t))
# print(t[1])
# print(t[1:4])
# t[0] = 100 -> 튜플은 수정이 불가능하다.

# packing, unpacking
# a = 10; b = 20; c = 30 # 이 방법은 잘 안쓴다.
a, b, c = 10, 20, 30 # 이 방법을 주로 사용한다. -> 한 줄로 객체 생성
print(a, b, c)
tt = 11, 22, 33 # packing(튜플로 변환)
print(tt)
d, e, f = (1, 2, 3) # [1, 2, 3]
print(d, e, f) # unpacking -> 이거는 튜플 뿐만아니라 리스트도 가능하다.