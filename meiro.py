#モジュールのインポート
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
mx = 1

#キャラクターのy座標を管理する変数
my = 1

#リアルタイム処理を行う函数を定義
def main_proc():
    #cx,cyをグローバル函数で扱うと宣言
    global mx,my
    #方向キーの上が押されたらy座標を20ドット減らす
    if key == "Up" and maze[my-1][mx] == 0:
        my = my - 1
    #方向キーの下が押されたらy座標を20ドット増やす
    if key == "Down" and maze[my+1][mx] == 0:
        my = my + 1
    #方向キーの右が押されたらx座標を20ドット増やす
    if key == "Right" and maze[my][mx+1] == 0:
        mx = mx + 1
    #方向キーの左が押されたらx座標を20ドット減らす
    if key == "Left" and maze[my][mx-1] == 0:
        mx = mx - 1

    #キャラクターの画像を新しい位置に移動させる
    canvas.coords("MYCHR",mx*80+40,my*80+40)

    #after()命令で0.05秒後に実行する函数を指定
    root.after(50,main_proc)

#ウィンドウにオブジェクトをつくる
root = tkinter.Tk()

#タイトルを指定
root.title("迷路内を移動する")

#bind()命令でキーを押した時に実行する函数を指定
root.bind("<KeyPress>",key_down)

#bind()命令でキーを離した時に実行する函数を指定
root.bind("<KeyRelease>",key_up)

#キャンバスの部品をつくる
canvas = tkinter.Canvas(width=800,height=560,bg="white")

#キャンバスを配置
canvas.pack()

#リストで迷路を定義
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,1,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ]

#繰り返し　yは012345
for y in range(7):
    #繰り返しxは0123456789
    for x in range(10):
        #maze[y][x]が1つまり壁ならば
        if maze[y][x] == 1:
            # 灰色の四角を描写する
            canvas.create_rectangle(x*80,y*80,x*80+79,y*80+79,fill="gray")

#キャラクター画像を変数imgに読み込む
img = tkinter.PhotoImage(file="mimi_s.png")

#キャンバスに画像を表示
canvas.create_image(mx*80+40,my*80+40,image=img,tag="MYCHR")

#main_proc()函数を実行
main_proc()

#ウィンドウを表示
root.mainloop()
