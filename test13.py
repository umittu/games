#モジュールをインポート
import tkinter

#キーの値を入れる変数を宣言
key = ""

#キーを押した時に実行する函数の定義
def key_down(e):
    #keyをグローバル変数で扱うと宣言
    global key
    #押されたキーの名称をkeyに代入
    key = e.keysym

#キーを離した時に実行する函数の宣言
def key_up(e):
    #keyをグローバル函数として扱うと宣言
    global key
    #keyにからの文字列を代入
    key = ""

#キャラクターのx座標を管理する変数
cx = 400
#キャラクターのy座標を管理する変数
cy = 300
#リアルタイム処理を行う函数を定義
def main_proc():
    #cx,cyをグローバル函数で扱うと宣言
    global cx,cy
    #方向キーの上が押されたらy座標を20ドット減らす
    if key == "Up":
        cy = cy - 20
    #方向キーの下が押されたらy座標を20ドット増やす
    if key == "Down":
        cy = cy +20
    #方向キーの右が押されたらx座標を20ドット増やす
    if key == "Right":
        cx = cx + 20
    #方向キーの左が押されたらx座標を20ドット減らす
    if key == "Left":
        cx = cx - 20
    #キャラクターの画像を新しい位置に移動させる
    canvas.coords("MYCHR",cx,cy)
    #after()命令で0.1秒後に実行する函数を指定
    root.after(50,main_proc)

#ウィンドウのオブジェクトを作る
root = tkinter.Tk()
#タイトルを指定
root.title("キャラクターの移動")
#bind()命令でキーを押した時に実行する函数を指定
root.bind("<KeyPress>",key_down)
#bind()命令でキーを離した時に実行する函数を指定
root.bind("<KeyRelease>",key_up)
#キャンバスの部品をつくる
canvas = tkinter.Canvas(width=800,height=600,bg="lightgreen")
#キャンバスを配置
canvas.pack()
#キャラクター画像を変数imgに読み込む
img = tkinter.PhotoImage(file="mimi.png")
#キャンバスに画像を表示
canvas.create_image(cx,cy,image=img,tag="MYCHR")
#main_proc()函数を実行
main_proc()
#ウィンドウを表示
root.mainloop()