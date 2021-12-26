# 這是一個終極密碼的遊戲

import random

MIN = 0
MAX = 100
ans = random.randint(1, 99) # 隨機產生一個終極數字
print('終極密碼：', ans)

key = input('0 ~ 100 請猜密碼：')
key = int(key)

while True: # 判斷數字區間
	if key == ans:
		print('恭喜答對！')
		break
	elif key > ans:
		MAX = key
	elif key < ans:
		MIN = key
	print(MIN, '~', MAX, end = '')
	key = input(' 請猜密碼：')
	key = int(key)

