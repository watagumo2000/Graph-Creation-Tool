import tkinter as tk

class MainView:
    """
    メインウィンドウのUI（見た目）を担当するクラス
    """
    def __init__(self, root):
        self.root = root
        self.root.title("CSVグラフアプリ")
        self.root.geometry("800x600") # ウィンドウサイズ (幅x高さ)

        # ここにボタンやグラフ領域などのUI部品を
        # 追加していく
        
        # 例: 仮のラベルを配置
        label = tk.Label(root, text="ここにグラフが表示されます", font=("Arial", 16))
        label.pack(pady=20, padx=20)