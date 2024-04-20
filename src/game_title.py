import pyxel
import os
import PyxelUniversalFont as puf

from game_option import Option as Op

class Title:
    def __init__(self):
        # super().__init__() # 継承

        # ゲーム素材の読み込み
        self.read_data()

        # フォントを指定
        self.writer = puf.Writer("misaki_gothic.ttf")

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
        path = os.path.join(Op.data_dir, Op.title_back_image)
        if os.path.exists(path):
            pyxel.image(0).load(0, 0, path)
        else:
            print(f"No exists file {path}")
            exit()

    def update(self):
        """ゲームの状態を更新する."""
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_DOWN):
            self.button_flag *= -1

        if pyxel.btnp(pyxel.KEY_SPACE): #pyxel.KEY_ENTERは使えない
            self.game_running = False
    
    def draw(self):
        """描画を行う関数.
        画像の描画
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
                  描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        pyxel.blt(0, 0, 0, 0, 0, pyxel.width, pyxel.height) # 背景

        # タイトルが中心に来るように計算
        x = Title.calu_text_x(Op.game_title, 30)
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
        x = Title.calu_text_x(select_0, 20)
        self.writer.draw(int(x), 100, select_0, Op.select_font_size, 1)
        x = Title.calu_text_x(select_1, 20)
        self.writer.draw(int(x), 130, select_1, Op.select_font_size, 1)

    @staticmethod
    def calu_text_size(text:str):
        """テキスト(文字数をカウント)
        全角を1, アルファベットを0.5でカウントする
        """
        count = 0
        for t in text:
            # print(t)
            # 全角の場合
            if (0x3000 <= ord(t) <= 0x9FFF) \
                or (0xFF00 <= ord(t) <= 0xFFEF):
                count+=1
            # アルファベットの場合
            elif (0x41 <= ord(t) <= 0x5A) \
                or (0x61 <= ord(t) <= 0x7A):
                count+=0.5
            else:
                count+=0.5
        return count

    @staticmethod
    def calu_text_x(text, font_size):
        """テキストを画面中心に配置する際のx座標を求める関数."""
        adjustment = 4
        text_size = Title.calu_text_size(text)
        return (pyxel.width - (font_size * text_size)) / 2 + adjustment


if __name__=="__main__":
    pyxel.init(Op.WINDOW_W, Op.WINDOW_H) # (W, H)
    Title()
