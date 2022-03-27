#モジュールのインポート
import tkinter

#キーコードを入れる変数の宣言
key = 0

#キーを押した時に実行する函数の定義
def key_down(e):
    #keyをグローバルで扱うと宣言
    global key 
    #押されたキーのコードをkeyに代入
    key = e.keycode

#リアルタイム処理を行う函数を定義
def main_proc():
    #ラベルにkey値を表示
    label["text"] = key
    #after()命令で0.1秒後に実行する函数を指定
    root.after(100,main_proc)

#ウィンドウのオブジェクトをつくる
root = tkinter.Tk()

#タイトルを指定
root.title("リアルタイムキー入力")

#bind()命令でキーを押した時に実行する函数を指定
root.bind("<KeyPress>",key_down)

#ラベルの部品をつくる
label = tkinter.Label(font=("Times New Roman",80))

#ラベルの部品を配置
label.pack()

#main_proc()函数を実行
main_proc()

#ウィンドウを表示
root.mainloop()