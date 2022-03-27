#モジュールのインポート
import tkinter

#時間をカウントする変数tmrの宣言
tmr = 0

#リアルタイム処理を行う函数の定義
def count_up():
    #tmrをグローバル函数として扱うと宣言
    global tmr
    #tmrの値を1増やす
    tmr = tmr + 1
    #ラベルにtmrの値を表示
    label["text"] = tmr
    #1秒後に再びこの函数を実行する
    root.after(1000,count_up)

#ウィンドウのオブジェクトをつくる
root = tkinter.Tk()

#ラベルの部品をつくる
label = tkinter.Label(font=("Times New Roman",80))

#ラベルの部品を配置
label.pack()

#1秒後に指定した函数を呼び出す
root.after(1000,count_up)

#ウィンドウを表示
root.mainloop()
