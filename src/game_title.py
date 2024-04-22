import pyxel
import os

from game_option import Option as Op
from game import Game


class Title(Game):
    def __init__(self):
        super().__init__()
        # ゲーム素材の読み込み
        self.read_data()

        # セレクトボタンフラグ
        self.button_flag = 1

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
        # タイトル画面背景
        path = os.path.join(Op.data_dir, Op.bkg_title)
        if os.path.exists(path):
            pyxel.image(Op.bkg_title_index).load(0, 0, path)
        else:
            print(f"No exists file {path}")
            exit()

    def update(self):
        """ゲームの状態を更新する."""
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_DOWN):
            self.button_flag *= -1

        if pyxel.btnp(pyxel.KEY_SPACE):  # pyxel.KEY_ENTERは使えない
            self.game_running = False

    def draw(self):
        """描画を行う関数.
        画像の描画
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
                  描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        pyxel.cls(0)  # 画面クリア
        pyxel.blt(0, 0, Op.bkg_title_index,
                  0, 0, pyxel.width, pyxel.height)  # 背景

        # タイトルが中心に来るように計算
        x = self.calu_text_x(Op.game_title, 30)
        # タイトル表示
        self.writer.draw(int(x), 50, Op.game_title, Op.title_font_size, 1)

        # タイトルオプション
        if self.button_flag == 1:
            select_0 = "→ " + Op.title_option_0
            select_1 = Op.title_option_1
        else:
            select_0 = Op.title_option_0
            select_1 = "→ " + Op.title_option_1

        # セレクトボタンの表示
        x = self.calu_text_x(select_0, 20)
        self.writer.draw(int(x), 100, select_0, Op.select_font_size, 1)
        x = self.calu_text_x(select_1, 20)
        self.writer.draw(int(x), 130, select_1, Op.select_font_size, 1)


if __name__ == "__main__":
    pyxel.init(Op.WINDOW_W, Op.WINDOW_H)  # (W, H)
    Title()
