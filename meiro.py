#モジュールのインポート
import tkinter
import tkinter.messagebox

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

#塗った床を数える函数
yuka = 0

#リアルタイム処理を行う函数を定義
def main_proc():
    #cx,cyをグローバル函数で扱うと宣言
    global mx,my,yuka
    #左Shiftキーを押し、かつ2マス以上塗っていたら
    if key == "Shift_L" and yuka > 1:
        #塗った床を消す
        canvas.delete("PAINT")
        #mxに1を代入する
        mx = 1
        #myに1を代入する
        my = 1
        #yukaに0を代入する
        yuka = 0
        #二重ループの繰り返し
        for y in range(7):
            #内側のfor
            for x in range(10):
                #塗った床があれば
                if maze[y][x] == 2:
                    #値を0に
                    maze[y][x] = 0
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
    #キャラクターのいる場所が通路なら
    if maze[my][mx] == 0:
        #リストの値を2にする
        maze[my][mx] = 2
        #塗った回数を1増やす
        yuka = yuka + 1
        #そこをピンク色に塗る
        canvas.create_rectangle(mx*80,my*80,mx*80+79,my*80+79,fill="pink",width=0,tag="PAINT")
    #一旦キャラクターを消す
    canvas.delete("MYCHR")

    #再びキャラクターの画像を表示する
    canvas.create_image(mx*80+40,my*80+40,image=img,tag="MYCHR")
    #30ヶ所の床を塗ったら
    if yuka == 30:
        #キャンバスを更新
        canvas.update()
        #メッセージを表示
        tkinter.messagebox.showinfo("おめでとう！","全ての床を塗りました！")
        #そうでなければ
    else:
        #0.3秒後にふたたびこの函数を実行
        root.after(50,main_proc)

    #キャラクターの画像を新しい位置に移動させる
    canvas.coords("MYCHR",mx*80+40,my*80+40)

    #after()命令で0.05秒後に実行する函数を指定
    root.after(50,main_proc)

#ウィンドウにオブジェクトをつくる
root = tkinter.Tk()

#タイトルを指定
root.title("迷路を塗るにゃん")

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
    [1,0,1,1,0,0,1,0,0,1],
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
