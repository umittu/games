#tkinterモジュールをインポート
import tkinter

#ウィンドウの部品（オブジェクト）を作る
root = tkinter.Tk()
#ウィンドウのタイトルを指定
root.title("初めてのウィンドウ")
#ウィンドウサイズを指定
root.geometry("800x600")
#ボタンの部品を作る
button = tkinter.Button(root,text="ボタンの文字列",
font=("Times New Roman",24))
#ウィンドウにボタンを配置
button.place(x=400,y=200)
#ラベル部品を作る
label = tkinter.Label(root,text="ラベルの文字列",
font=("System",24))
#ウィンドウにラベルを配置
label.place(x=200,y=100)
#ウィンドウを表示
root.mainloop()