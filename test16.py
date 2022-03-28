#モジュールインポート
import tkinter
#マス目を管理する二次元リスト
neko=[
    [1,0,0,0,0,0,7,7],
    [0,2,0,0,0,0,7,7],
    [0,0,3,0,0,0,0,0],
    [0,0,0,4,0,0,0,0],
    [0,0,0,0,5,0,0,0],
    [0,0,0,0,0,6,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,1,2,3,4,5,6]
    ]
#猫を表示する関数
def draw_neko():
    #繰り返しyは0から9まで1ずつふえる
    for y in range(10):
        #繰り返しxは0から7まで1ずつふえる
        for x in range(8):
            #リストの要素の値が0より大きいなら
            if neko[y][x]>0:
                #猫の画像を表示
                cvs.create_image(x*72+60,y*72+60,image=img_neko[neko[y][x]])
#ウィンドウのオブジェクトをつくる
root=tkinter.Tk()
#タイトル
root.title("二次元リストでますを管理する")
#ウィンドウサイズを変更できないように
root.resizable(False,False)
#キャンバスの部品をつくる
cvs=tkinter.Canvas(root,width=912,height=768)
#キャンバスの配置
cvs.pack()
#背景画像の読み込み
bg=tkinter.PhotoImage(file="neko_bg.png")
#リストで背景の猫の画像を処理
img_neko=[
    None,
    tkinter.PhotoImage(file="neko1.png"),
    tkinter.PhotoImage(file="neko2.png"),
    tkinter.PhotoImage(file="neko3.png"),
    tkinter.PhotoImage(file="neko4.png"),
    tkinter.PhotoImage(file="neko5.png"),
    tkinter.PhotoImage(file="neko6.png"),
    tkinter.PhotoImage(file="neko_niku.png")
]
#キャンバス上に背景を描く
cvs.create_image(456,384,image=bg)
#猫を表示する函数を呼び出す
draw_neko()
#ウィンドウを表示
root.mainloop()