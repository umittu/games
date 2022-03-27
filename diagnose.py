#モジュールのインポート
import tkinter

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
button = tkinter.Button(text="診断する",font=("Times New Roman",32),bg="lightgreen")

#ボタンを配置
button.place(x=400,y=480)

#テキストの入力欄の部品をつくる
text = tkinter.Text(width=40,height=5,font=("Times New Roman",16))

#テキストの入力欄を配置
text.place(x=320,y=30)

#ウィンドウを表示
root.mainloop()