import pyxel
import os
import PyxelUniversalFont as puf

from game_option import Option as Op


class Story01():
    def __init__(self):

        # ゲーム素材の読み込み
        self.read_data()

        # フォントを指定
        self.writer = puf.Writer("misaki_gothic.ttf")

        # ゲーム続行フラグ
        self.game_running = True

        # ゲーム開始
        self.run()

    def run(self):
        while self.game_running:
            self.update()
            self.draw()
            pyxel.flip()  # フレームを更新

    def read_data(self):
        """必要データの読み来み."""
        pass

    def update(self):
        """ゲームの状態を更新する."""
        pass

    def draw(self):
        # タイトル表示
        self.writer.draw(pyxel.width/3, 50, "ストーリー０１", 20, 1)


if __name__ == "__main__":
    pyxel.init(Op.WINDOW_W, Op.WINDOW_H)  # (W, H)
    Story01()
