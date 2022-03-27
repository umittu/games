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
    #シェルウィンドウにkeyの値を出力
    print("KEY:"+str(key))

#ウィンドウのオブジェクトをつくる
root = tkinter.Tk()

#タイトルを指定
root.title("キーコードを取得")

#bind()命令でキーを押した時に実行する函数を指定
root.bind("<KeyPress>",key_down)

#ウィンドウを表示
root.mainloop()