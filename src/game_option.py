import os
SCRIPT_DIR_PATH = os.path.dirname(
    os.path.abspath(__file__))  # create_object_py/src
PROJECT_DIR_PATH = os.path.dirname(SCRIPT_DIR_PATH)  # create_object_py
DATA_DIR_PATH = os.path.join(PROJECT_DIR_PATH, "data")


class Option:
    # windowの大きさを宣言
    WINDOW_H = 180
    WINDOW_W = 240

    # 以下画面素材
    data_dir = DATA_DIR_PATH
    # タイトル画面背景
    title_back_image = "title_background_240_180.png"
    # タイトル
    game_title = "TITLE"
    title_font_size = 30

    # セレクトボタン
    title_option_0 = "つづきから"
    title_option_1 = "はじめから"
    select_font_size = 15
