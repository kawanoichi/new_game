"""
ゲーム素材を管理するモジュール.
"""
import pyxel
import os
from game_option import *

class ReadMaterials:
    # 素材格納ディレクトリ
    data_dir = "image"
    # 背景画像
    title_background_image = "title_background_160_120.jpg"
    # テキストボックス画像
    text_image = "text_box_160_23.png"
    
    @staticmethod
    def read_materials():
        """画像などを読み込み関数."""

        # タイトル画面背景
        path = os.path.join(ReadMaterials.data_dir,
                            ReadMaterials.title_background_image)
        pyxel.image(0).load(0, 0, path)

        # テキストボックス
        path = os.path.join(ReadMaterials.data_dir,
                            ReadMaterials.text_image)
        pyxel.image(1).load(0, 0, path)
