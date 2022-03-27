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
root.geometry("800x800")
#半角20文字部分の入力欄の部品を作る
entry =tkinter.Entry(width=20)
#入力欄の表示
entry.place(x=20,y=20)
#ボタンの部品を作りクリック時に実行する関数を指定
button = tkinter.Button(text="文字列の取得",command=click_btn)
#ボタンを配置
button.place(x=20,y=100)
#ボタンをクリックした時に動く関数を定義、テキスト入力の最後尾に文字列を追加
def click_btn():
    text.insert(tkinter.END,"モンスターが現れた！")
#ボタンの部品を作り、comman=でクリック時に実行する関数を指定
button = tkinter.Button(text="メッセージ",command=click_btn)
#ボタンの部品を配置
button.pack()
#複数行のテキスト入力欄を作成
text = tkinter.Text()
#入力欄の部品を配置
text.pack()
#ウィンドウを表示
root.mainloop()