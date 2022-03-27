#モジュールをインポート
import tkinter
import tkinter.messagebox

#函数を定義メッセージボックスの表示
def click_btn():
    tkinter.messagebox.showinfo("情報","ボタンを押しました")

#ウィンドウのオブジェクトを作る
root = tkinter.Tk()

#タイトルを指定
root.title("初めてのメッセージボックス")

#サイズを指定
root.geometry("400x200")

#ボタンを作りクリック時の関数を指定
btn = tkinter.Button(text="てすと",command=click_btn)

#ボタンを配置
btn.pack()

#ウィンドウを表示
root.mainloop()
