#tkinterモジュールをインポート
import tkinter
#ウィンドウにオブジェクトを作る
root = tkinter.Tk()
#ウィンドウのタイトルを指定
root.title("初めてのテキスト入力欄")
#ウィンドウのサイズを指定
root.geometry("400x200")
#半角20文字部分の入力欄の部品を作る
entry =tkinter.Entry(width=20)
#入力欄の表示
entry.place(x=10,y=10)
#ウィンドウを表示
root.mainloop()