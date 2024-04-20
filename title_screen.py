import pyxel
import os
from game_option import Option
# from read_image_material import ReadMaterials

# 日本語表示
# https://qiita.com/n_koba/items/cb03aeeb2a413d1cbbb0
# import PyxelUniversalFont as puf

class ShowWindow:
    def __init__(self):
        self.btn_state = False
        self.show_text_box = False
        
        # ゲームウィンドウの作成
        pyxel.init(Option.WINDOW_W, Option.WINDOW_H) # (W, H)
        print(f"window size: height, width = ({pyxel.height}, {pyxel.width})")

        # 素材の読み込み
        # self.read_data()
        path = os.path.join(Option.image_dir, Option.title_back_image)
        pyxel.image(0).load(0, 0, path)


        # フォントを指定
        # self.writer = puf.Writer("IPA_Mincho.ttf")
        
        # ゲームで使用する素材の読み込み
        # ReadMaterials.read_materials()

        # ゲーム開始
        pyxel.run(self.update, self.draw)

    def read_data(self):
        """ゲーム画面の読み込み"""
        # タイトル画面背景
        path = os.path.join(Option.image_dir, Option.title_back_image)
        pyxel.image(0).load(0, 0, path)


    def update(self)->None:
        """ゲームの状態を更新する."""
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # キーボードの Z キーが押されたら、ボタン状態をトグルする
        if pyxel.btnp(pyxel.KEY_Z):
            self.btn_state = not self.btn_state

    def draw(self):
        """
        画像の描画
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
                  描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        pyxel.blt(0, 0, 0, 0, 0, Option.WINDOW_H, Option.WINDOW_W, 1) # 背景
        # if self.show_text_box: self.text_box()
        
        """
        pyxel.rect(左上座標x, 左上座標y, 横幅, 高さ, 色)
        """ 
        # pyxel.rect((WINDOW_W-start_button_size_x)/2, (WINDOW_H-start_button_size_y)/2,
        #             start_button_size_x, start_button_size_y, 12)
        # pyxel.text((WINDOW_W-start_button_size_x)/2,(WINDOW_H-start_button_size_y)/2, "Button2", 0)

    # def text_box(self):
    #     """テキストボックスを管理する関数."""
    #     if not self.show_text_box: return
    #     pyxel.blt(TEXT_BOX_COORDI_X, TEXT_BOX_COORDI_Y,
    #               1, 0, 0, 160, 23, 1)
        # draw(x座標, y座標, テキスト, フォントサイズ, 文字の色(16:モザイク))
        # 背景色はデフォルト値(-1:透明)
        # self.writer.draw(TEXT_COORDI_X, TEXT_COORDI_Y, "ああああ", FONT_SIZE, 1)


if __name__=="__main__":
    """
    from PIL import Image
    image_path = "image/title_background_400_300.png"
    with Image.open(image_path) as img:
        width, height = img.size

        print("Width:", width)
        print("Height:", height)
    # """

    ShowWindow()
