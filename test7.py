#tkinterモジュールをインポート
import tkinter
#関数の定義、入力欄の文字列を変数txtに代入、ボタンの文字列をtxtの値にする
def click_btn():
    txt = entry.get()
    button["text"] = txt

#ウィンドウにオブジェクトを作る
root = tkinter.Tk()
#ウィンドウのタイトルを指定
root.title("初めてのテキスト入力欄")
#ウィンドウのサイズを指定
root.geometry("400x200")
#半角20文字部分の入力欄の部品を作る
entry =tkinter.Entry(width=20)
#入力欄の表示
entry.place(x=20,y=20)
#ボタンの部品を作りクリック時に実行する関数を指定
button = tkinter.Button(text="文字列の取得",command=click_btn)
#ボタンを配置
button.place(x=20,y=100)
#ウィンドウを表示
root.mainloop()