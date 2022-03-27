#モジュールのインポート
import tkinter

#診断結果のコメントをリストで定義
result = [
    "前世が猫だった可能性は極めて薄いです",
    "至って普通の人間です",
    "特別おかしなところはありません",
    "やや、猫っぽいところがあります",
    "猫に近い性格のようです",
    "猫にかなり近い性格です",
    "前世は猫だったかもしれません",
    "見た目は人間、中身は猫の可能性があります"
]

"""
ボタンをクリックしたときに動く関数を定義
チェックしたボタンを数える変数
繰り返し命令でチェックされていたら変数の値を１増やす
猫度を計算、少数部分は切り捨て
入力欄の文字列を削除する
入力らに変数の値を挿入
"""
def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            pts = pts + 1
    nekodo = int(100*pts/7)
    text.delete("1.0",tkinter.END)
    text.insert("1.0","<診断結果>\nあなたの猫度は"+str(nekodo)+"%です。\n"+result[pts])

#ウィンドウのオブジェクトをつくる
root = tkinter.Tk()

#タイトルを指定
root.title("猫度診断アプリ")

#サイズを指定
root.resizable(False,False)

#キャンバスの部品を作る
canvas = tkinter.Canvas(root,width=800,height=600)

#キャンバスの配置
canvas.pack()

#画像の読み込み
gazou = tkinter.PhotoImage(file="sumire.png")

#画像の表示
canvas.create_image(400,300,image=gazou)

#ボタンの部品をつくる
button = tkinter.Button(text="診断する",font=("Times New Roman",32),bg="lightgreen",command=click_btn)

#ボタンを配置
button.place(x=400,y=480)

#テキストの入力欄の部品をつくる
text = tkinter.Text(width=40,height=5,font=("Times New Roman",16))

#テキストの入力欄を配置
text.place(x=320,y=30)

"""
BooleanVarのオブジェクト用のリスト
チェックボタン用のリスト
チェックボタンの質問を定義
"""
bvar = [None]*7
cbtn = [None]*7
ITEM =[
    "高いところが好き",
    "ボールを見ると転がしたくなる",
    "びっくりすると髪の毛が逆立つ",
    "ネズミの玩具が気になる",
    "匂いに敏感",
    "魚の骨をしゃぶりたくなる",
    "夜、元気になる"
]

"""
繰り返しでチェックボタンを配置
BooleanVarのオブジェクトを作る
そのオブジェクトにFalseを設定
チェックボタンの部品をつくる
"""
for i in range(7):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i],font=("Times New Roman",12),variable=bvar[i],bg="#dfe")
    cbtn[i].place(x=400,y=160+40*i)


#ウィンドウを表示
root.mainloop()