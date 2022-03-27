#tkinter,randomモジュールをインポート
import tkinter
import random

#ボタンをクリックしたときの関数を定義
#ラベルの文字をランダムに変更
def click_btn():
    label["text"]=random.choice(["大吉","中吉","小吉","凶"])
    label.iupdate()

#ウィンドウのオブジェクトを作る
root = tkinter.Tk()
#タイトルを指定
root.title("おみくじソフト")
#ウィンドウサイズを固定する
root.resizable(False,False)
#キャンバスの部品を作る
canvas = tkinter.Canvas(root,width=800,height=600)
#キャンバスを配置
canvas.pack()
#画像の読み込み
gazou = tkinter.PhotoImage(file="miko.png")
#キャンバスに画像を描画
canvas.create_image(400,300,image=gazou)
#ラベルの部品を作る
label = tkinter.Label(root,text="??",font=("Times New Roman",120),bg="white")
#ラベルを配置
label.place(x=380,y=60)
#ボタンの部品を作る,commandでクリック時に動く関数を設定
button = tkinter.Button(root,text="おみくじを引く",font=("Times New Roman",36),command=click_btn,fg="skyblue")
#ボタンを配置
button.place(x=360,y=400)
#ウィンドウを表示
root.mainloop()