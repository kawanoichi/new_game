import pyxel
import os
from game_option import Option


class ShowWindow:
    def __init__(self):
        # ゲームウィンドウの作成
        pyxel.init(Option.WINDOW_W, Option.WINDOW_H) # (W, H)

        # ゲーム素材の読み込み
        self.read_data()

        # ゲーム開始
        pyxel.run(self.update, self.draw)

    def read_data(self):
        """ゲーム画面の読み込み"""
        # タイトル画面背景
        path = os.path.join(Option.image_dir, Option.title_back_image)
        pyxel.image(0).load(0, 0, path)

    def update(self):
        """ゲームの状態を更新する."""
        pass

    def draw(self):
        """
        画像の描画
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
                  描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        pyxel.blt(0, 0, 0, 0, 0, Option.WINDOW_W, Option.WINDOW_H) # 背景
        pyxel.text(50, 50, "Hello World!", 2)


if __name__=="__main__":
    ShowWindow()
