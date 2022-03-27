#tkinterモジュールをインポート
import tkinter
#ウィンドウのオブジェクトを作る
root = tkinter.Tk()
#タイトルを指定
root.title("最初からチェックされた状態にする")
#サイズを指定
root.geometry("400x200")
#BoolleanVar()のオブジェくトを用意
cval = tkinter.BooleanVar()
#それをTrueセット
cval.set(True)
#チェックボタンの部品を作成
cbtn = tkinter.Checkbutton(text="チェックボタン",variable=cval)
#チェックボタンの部品を配置
cbtn.pack()
#ウィンドウを表示
root.mainloop()