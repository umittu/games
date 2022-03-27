#tkinterモジュールをインポート
import tkinter
#ウィンドウオブジェクトを作る
root = tkinter.Tk()
#ウィンドウのタイトルを指定
root.title("初めての画像表示")
#キャンバス部品を作る
canvas = tkinter.Canvas(root,width=800,height=800,
bg="skyblue")
#ウィンドウにキャンバスを配置
canvas.pack()
#gazouに画像ファイルを読み込む
gazou = tkinter.PhotoImage(file="otter.png")
#キャンバスに画像を描画
canvas.create_image(400,400,image=gazou)
#ウィンドウを表示
root.mainloop()