import pyxel
from PIL import Image

# windowの大きさを宣言
WINDOW_H = 120
WINDOW_W = 160

start_button_size_x = 40 
start_button_size_y = 10

class App:
    def __init__(self):
        # ゲームウィンドウの作成
        pyxel.init(WINDOW_W, WINDOW_H)

        self.btn_state = False

        # 背景画像PATH
        image_path = "image/title.jpg"

        # サイズが指定サイズと一致しない場合のみリサイズ
        background_img = Image.open(image_path)
        if background_img.size != (WINDOW_W, WINDOW_H):
            resized_img = background_img.resize((WINDOW_W, WINDOW_H))
            resized_img.save(image_path)
        
        # タイトル画像の読み込み
        pyxel.image(0).load(0, 0, image_path)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # キーボードの Z キーが押されたら、ボタン状態をトグルする
        if pyxel.btnp(pyxel.KEY_Z):
            self.btn_state = not self.btn_state

    def draw(self):
        # 画像の描画(描画位置x, 描画位置y, 画像ID,
        #           描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        pyxel.blt(0, 0, 0, 0, 0, WINDOW_W, WINDOW_H, 1)

        # 
        # (左上座標x, 左上座標y, 横幅, 高さ, 色)
        pyxel.rect((WINDOW_W-start_button_size_x)/2, (WINDOW_H-start_button_size_y)/2,
                    start_button_size_x, start_button_size_y, 12)
        pyxel.text((WINDOW_W-start_button_size_x)/2, (WINDOW_H-start_button_size_y)/2, "Button2", 0)


App()
