#tkinterモジュールをインポート
import tkinter
#ウィンドウオブジェクトを作る
root = tkinter.Tk()
#ウィンドウのタイトルを指定
root.title("初めてのキャンバス")
#キャンバス部品を作る
canvas = tkinter.Canvas(root,width=400,height=600,
bg="skyblue")
#ウィンドウにキャンバスを配置
canvas.pack()
#ウィンドウを表示
root.mainloop()