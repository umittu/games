#randomモジュールをインポート
import random

# プレイヤーとコンピュータの位置を管理する変数
pl_pos = 1
com_pos = 1

#関数の宣言
def banmen():

#中黒とPとCで文字列を出力
    print("・"*(pl_pos-1) + "P" + "・"*(30-pl_pos)+"Goal")
    print("・"*(com_pos-1) + "P" + "・"*(30-com_pos)+"Goal")

#盤面を表示
banmen()
print("すごろくスタート！")

while True:
    input("Enterを押すとあなたのコマが進みます")

    #プレイヤーとコンピュータのコマを乱数分進める
    pl_pos = pl_pos + random.randint(1,6)

    #Pの位置が30を超えたら30に戻す。
    if pl_pos > 30:
        pl_pos = 30
    banmen()

    #Pが30に到達したら勝ちを出力
    if pl_pos == 30:
        print("あなたの勝ちです！")

        #繰り返しを抜ける
        break

    input("Enterを押すとコンピュータのコマが進みます")
    com_pos = pl_pos +random.randint(1,6)
    if com_pos > 30:
        com_pos = 30
    banmen()
    if com_pos == 30:
        print("コンピュータの勝ちです！")
        break