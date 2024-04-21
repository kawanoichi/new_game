import pyxel
from game_title import Title
from story_01 import Story01
from game_option import Option as Op


class Main:
    """ゲームクラス."""

    def __init__(self):
        # ゲームウィンドウの作成
        pyxel.init(Op.WINDOW_W, Op.WINDOW_H)  # (W, H)
        self.run()

    def run(self):
        pyxel.cls(0)  # 画面クリア
        Title()
        pyxel.cls(0)  # 画面クリア

        Story01()
        pyxel.cls(0)  # 画面クリア


if __name__ == "__main__":
    Main()
