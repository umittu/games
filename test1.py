import random
print("お互いに1~3までの整数を足していき設定した数値に到達した方が負けになるゲーム")
#任意の数字を入力
n = int(input("好きな数字を入力してください;"))
#先攻後攻を自動で決定
m = random.randint(1,2)

#プレイヤーが先攻
if m == 1:
    print("あなたは先攻です:")
    x = 0
    while x < n:
        y = int(input("1~3の数字を入力:"))
        x = x+y
        if x >= n:
            print("You lose")
        else:
            z = random.randint(1,3)
            x = x+z
            print(x)
            if x >= n:
                print("You win")

    
#コンピュータが先攻
else:
    print("あなたは後攻です:")
    p = 0
    while p < n:
        q = random.randint(1,3)
        p = p+q
        print(p)
        if p >= n:
            print("You win")
        else:
            r = int(input("1~3の整数を入力:"))
            p = p+r
            if p >= n:
                print("You lose")
