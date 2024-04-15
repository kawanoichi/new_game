import pyxel
from PIL import Image

from game_option import *
from read_image_material import ReadMaterials

start_button_size_x = 40 
start_button_size_y = 10

class ShowWindow:
    def __init__(self):
        # ゲームウィンドウの作成
        pyxel.init(WINDOW_W, WINDOW_H)

        self.btn_state = False
        self.show_text_box = True
        
        # ゲームで使用する素材の読み込み
        ReadMaterials.read_materials()

        image_path = "image/text_box_160_23.png"
        pyxel.image(1).load(0, 0, image_path)


        # ゲーム開始
        pyxel.run(self.update, self.draw)

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
        pyxel.blt(0, 0, 0, 0, 0, WINDOW_W, WINDOW_H, 1)
        if self.show_text_box: self.text_box()
        
        """
        pyxel.rect(左上座標x, 左上座標y, 横幅, 高さ, 色)
        """ 
        # pyxel.rect((WINDOW_W-start_button_size_x)/2, (WINDOW_H-start_button_size_y)/2,
        #             start_button_size_x, start_button_size_y, 12)
        # pyxel.text((WINDOW_W-start_button_size_x)/2, (WINDOW_H-start_button_size_y)/2, "Button2", 0)

    def text_box(self):
        """テキストボックスを管理する関数."""
        if self.show_text_box:
            pyxel.blt(0, WINDOW_H-23, 1, 0, 0, 160, 23, 1)



if __name__=="__main__":
    ShowWindow()
