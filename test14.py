#モジュールのインポート
from pickle import FALSE
import tkinter
#マウスポインタのx座標
mouse_x=0
#マウスポインタのy座標
mouse_y=0
#マウスポンタをクリックした時の変数(フラグ)
mouse_c=0
#マウスを動かした時に実行する函数
def mouse_move(e):
    #これらをグローバル函数で扱うと宣言
    global mouse_x,mouse_y
    #mouse_xにマウスポインタのx座標を代入
    mouse_x=e.x
    #mouse_yにマウスポンタのy座標を代入
    mouse_y=e.y
#マウスボタンをクリックした時に実行する函数
def mouse_press(e):
    #この変数をグローバルで扱うと宣言
    global mouse_c
    #mouse_cに1を代入
    mouse_c=1
#マウスボタンを離した時に実行する函数
def mouse_release(e):
    #この変数をグローバル函数で扱うと宣言
    global mouse_c
    #mouse_cに0を代入
    mouse_c=0
#リアルタイム処理を行う函数
def game_main():
    #フォントを指定する変数
    fnt=("Times New Roman",30)
    #表示する文字列
    txt="mouse({},{}){}".format(mouse_x,mouse_y,mouse_c)
    #一旦文字列を削除する
    cvs.delete("TEST")
    #キャンバスに文字列を表示
    cvs.create_text(456,384,text=txt,fill="black",font=fnt,tag="TEST")
    #0.1秒後に再びこの函数を実行する
    root.after(100,game_main)
#ウィンドウオブジェクトをつくる
root=tkinter.Tk()
#タイトルの設定
root.title("マウス入力")
#ウィンドウサイズを変更できないようにする
root.resizable(False,False)
#マウスが動いた時に実行する函数を指定
root.bind("<Motion>",mouse_move)
#マウスボタンをクリックした時に実行する函数を指定
root.bind("<ButtonPress>",mouse_press)
#マウスボタンを離した時に実行する函数を指定
root.bind("<ButtonRelease>",mouse_release)
#キャンバスの部品をつくる
cvs=tkinter.Canvas(root,width=912,height=768)
#キャンバスを配置する
cvs.pack()
#メインの処理を行う函数を呼び出す
game_main()
#ウィンドウを表示
root.mainloop()