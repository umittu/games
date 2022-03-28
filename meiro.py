#モジュールのインポート
import tkinter

#ウィンドウにオブジェクトをつくる
root = tkinter.Tk()

#タイトルを指定
root.title("迷路の表示")

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
            canvas.create_rectangle(x*80,y*80,x*80+80,y*80+80,fill="gray")
#ウィンドウを表示
root.mainloop()
