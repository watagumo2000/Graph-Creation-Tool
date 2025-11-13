import tkinter as tk
from app.ui.main_view import MainView

if __name__ == "__main__":
    # 1. メインウィンドウ(root)を作成する
    root = tk.Tk()
    
    # 2. MainViewクラスにrootを渡して、アプリのUIを組み立てる
    app = MainView(root)
    
    # 3. メインループを開始 (ウィンドウを表示し、ユーザー操作を待機する)
    root.mainloop()