import os
SCRIPT_DIR_PATH = os.path.dirname(
    os.path.abspath(__file__))  # create_object_py/src
PROJECT_DIR_PATH = os.path.dirname(SCRIPT_DIR_PATH)  # create_object_py
DATA_DIR_PATH = os.path.join(PROJECT_DIR_PATH, "data")


class Option:
    """
    ゲーム全体
    """
    # windowの大きさを宣言
    WINDOW_H = 180
    WINDOW_W = 240
    # テキストボックス
    text_box_image = "text_box_240_48.png"
    text_box_image_index = 0
    # 画像データディレクトリ
    data_dir = DATA_DIR_PATH

    """
    タイトル画面
    """
    # タイトル画面背景
    bkg_title = "title_background_240_180.png"
    bkg_title_index = 1
    # タイトル
    game_title = "TITLE"
    title_font_size = 30
    # セレクトボタン
    title_option_0 = "つづきから"
    title_option_1 = "はじめから"
    select_font_size = 15

    """
    ストーリー１
    """
    # タイトル画面背景
    bkg_story01 = "story_240_180.png"
    bkg_story01_index = 1
