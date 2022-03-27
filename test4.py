#tkinterモジュールをインポート
import tkinter

#関数の宣言
def click_btn():
    #ボタンの文字列変更
    button["text"] = "クリックしました"

#ウィンドウの部品（オブジェクト）を作る
root = tkinter.Tk()
#ウィンドウのタイトルを指定
root.title("初めてのウィンドウ")
#ウィンドウサイズを指定
root.geometry("800x600")
#ボタンの部品を作る際、command=でクリック時に動く関数を指定
button = tkinter.Button(root,text="ボタンの文字列",
font=("Times New Roman",24),command=click_btn)
#ウィンドウにボタンを配置
button.place(x=400,y=200)
#ラベル部品を作る
label = tkinter.Label(root,text="ラベルの文字列",
font=("System",24))
#ウィンドウにラベルを配置
label.place(x=200,y=100)
#ウィンドウを表示
root.mainloop()