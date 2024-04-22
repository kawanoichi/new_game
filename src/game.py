import pyxel
import os
import PyxelUniversalFont as puf

from game_option import Option as Op


class Game:
    """ゲームクラス."""
    # 子クラス間で共有する変数
    # count_index = 0

    def __init__(self):
        # ゲームウィンドウの作成
        self.read_common_data()
        # フォントを指定
        self.writer = puf.Writer("misaki_gothic.ttf")

    def read_common_data(self):
        """必要データの読み来み."""
        # テキストボックス
        path = os.path.join(Op.data_dir, Op.text_box_image)
        if not os.path.exists(path):
            raise FileNotFoundError(f"File does not exist: {path}")
        pyxel.images[Op.text_box_image_index].load(0, 0, path)
        # Game.count_index += 1

    def show_text_box(self):
        """テキストボックスの表示.
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
            描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        pyxel.blt(0, pyxel.height-48, Op.text_box_image_index,
                  0, 0, pyxel.width, 48)

    def calu_text_size(self, text: str):
        """テキスト(文字数をカウント)
        全角を1, アルファベットを0.5でカウントする
        """
        count = 0
        for t in text:
            # print(t)
            # 全角の場合
            if (0x3000 <= ord(t) <= 0x9FFF) \
                    or (0xFF00 <= ord(t) <= 0xFFEF):
                count += 1
            # アルファベットの場合
            elif (0x41 <= ord(t) <= 0x5A) \
                    or (0x61 <= ord(t) <= 0x7A):
                count += 0.5
            else:  # アルファベットと合わせてもいい？
                count += 0.5
        return count

    def calu_text_x(self, text, font_size):
        """テキストを画面中心に配置する際のx座標を求める関数."""
        adjustment = 4
        text_size = self.calu_text_size(text)
        return (pyxel.width - (font_size * text_size)) / 2 + adjustment


if __name__ == "__main__":
    pyxel.init(Op.WINDOW_W, Op.WINDOW_H)  # (W, H)
    Game()
