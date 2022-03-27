#tkinterモジュールをインポート
import tkinter

#チェックボタンをクリックした時に実行する関数を定義
#チェックされていたら「チェックされています」と出力
#チェックされていなければ「チェックされていません」と出力
def check():
    if cval.get() == True:
        print("チェックされています")
    else:
        print("チェックされていません")

#ウィンドウのオブジェクトを作る
root = tkinter.Tk()
#タイトルを指定
root.title("最初からチェックされた状態にする")
#サイズを指定
root.geometry("400x200")
#BoolleanVar()のオブジェくトを用意
cval = tkinter.BooleanVar()
#それをFalseセット
cval.set(False)
#チェックボタンの部品を作成、command=でクリックした時に実行する関数を指定
cbtn = tkinter.Checkbutton(text="チェックボタン",variable=cval,command=check)
#チェックボタンの部品を配置
cbtn.pack()
#ウィンドウを表示
root.mainloop()