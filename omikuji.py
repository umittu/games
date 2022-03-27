#tkinterモジュールをインポート
import tkinter
#ウィンドウのオブジェクトを作る
root = tkinter.Tk()
#タイトルを指定
root.title("おみくじソフト")
#ウィンドウサイズを固定する
root.resizable(False,False)
#キャンバスの部品を作る
canvas = tkinter.Canvas(root,width=800,height=600)
#キャンバスを配置
canvas.pack()
#画像の読み込み
gazou = tkinter.PhotoImage(file="miko.png")
#キャンバスに画像を描写
canvas.create_image(400,300,image=gazou)
#ウィンドウを表示
root.mainloop()