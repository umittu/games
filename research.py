#random、datetimeモジュールをインポート
import random
import datetime

#リストでアルファベットを定義
alp = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#抜けている文字をランダムに決める
r = random.choice(alp)

#変数ALPの宣言
ALP = ""

for i in alp:
    if i != r:
        ALP = ALP + i

print(ALP)

#日時を変数stに入れる
st = datetime.datetime.now()

#inputで答えを入力
ans = input("抜けているアルファベットは？")

#入力された答えを判定
if ans == r:
    print("正解です")
    #正解した日時を変数etに入れる
    et = datetime.datetime.now()
    #etとstの差からかかった時間を調べる
    print(str((et-st).seconds)+"秒かかりました。")
else:
    print("違います")

