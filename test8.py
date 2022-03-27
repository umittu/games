#tkinterモジュールをインポート
import tkinter
#ウィンドウのオブジェクトを作る
root = tkinter.Tk()
#タイトルを指定
root.title("チェックボタンを扱う")
#サイズを指定
root.geometry("400x200")
#チェックボタンの部品を作成
cbtn = tkinter.Checkbutton(text="チェックボタン")
#チェックボタンの部品を配置
cbtn.pack()
#ウィンドウを表示
root.mainloop()