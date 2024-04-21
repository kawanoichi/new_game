class Option:
    # クラス変数
    image_index = -1

    # タイトル画面背景
    title_back_image = "title_background_240_180.png"
    title_back_image_index_1 = None  # 初期値はNoneに設定
    title_back_image_index_2 = None  # 初期値はNoneに設定
    title_back_image_index_3 = None  # 初期値はNoneに設定
    title_back_image_index_4 = None  # 初期値はNoneに設定

    @classmethod
    def count_image_index(cls):
        # クラス変数を変更する際には cls を使用します
        cls.image_index += 1
        return cls.image_index

    # クラス変数の初期化をクラス内で行う
    # クラスがロードされた際にタイトル背景のインデックスを設定
    title_back_image_index_1 = count_image_index()
    # title_back_image_index_2 = count_image_index()
    # title_back_image_index_3 = count_image_index()
    # title_back_image_index_4 = count_image_index()


if __name__ == "__main__":
    Option()
    # print(f"title_back_image_index_1:{Option.title_back_image_index_1}")
    # print(f"title_back_image_index_1:{Option.title_back_image_index_1}")
    # print(f"title_back_image_index_1:{Option.title_back_image_index_1}")
    # print(f"title_back_image_index_1:{Option.title_back_image_index_1}")
