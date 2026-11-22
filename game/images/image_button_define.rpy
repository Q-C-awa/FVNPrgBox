## 界面背景定义

image common_bg = "images/screen_bg/common_bg.png"
image confirm_mask = "images/screen_bg/confirm_mask.png"
image main_menu_mask = "images/screen_bg/main_menu_mask.png"
image say_dress = "images/screen_button/say_textbox_dress.png"
image bg = "images/BG/main_bg.png"

## 界面按钮定义
# 主菜单按钮
image main_menu_start_idle = "images/screen_button/main_menu_start_idle.png"
image main_menu_start_hover = "images/screen_button/main_menu_start_hover.png"
image main_menu_load_idle = "images/screen_button/main_menu_load_idle.png"
image main_menu_load_hover = "images/screen_button/main_menu_load_hover.png"
image main_menu_config_idle = "images/screen_button/main_menu_config_idle.png"
image main_menu_config_hover = "images/screen_button/main_menu_config_hover.png"
image main_menu_gallery_idle = "images/screen_button/main_menu_gallery_idle.png"
image main_menu_gallery_hover = "images/screen_button/main_menu_gallery_hover.png"
image main_menu_about_idle = "images/screen_button/main_menu_about_idle.png"
image main_menu_about_hover = "images/screen_button/main_menu_about_hover.png"
image main_menu_quit_idle = "images/screen_button/main_menu_quit_idle.png"
image main_menu_quit_hover = "images/screen_button/main_menu_quit_hover.png"

# 对话界面按钮
image say_hide_idle:
    align(0.5,0.5)
    "images/screen_button/say_hide_idle.png"
image say_hide_hover = "images/screen_button/say_hide_hover.png"
image say_replay_idle:
    align(0.5,0.5)
    "images/screen_button/say_replay_idle.png"
image say_replay_hover = "images/screen_button/say_replay_hover.png"
image say_quit_idle:
    align(0.5,0.5)
    "images/screen_button/say_quit_idle.png"
image say_quit_hover = "images/screen_button/say_quit_hover.png"
image say_load_idle:
    align(0.5,0.5)
    "images/screen_button/say_load_idle.png"
image say_load_hover = "images/screen_button/say_load_hover.png"
image say_save_idle:
    align(0.5,0.5)
    "images/screen_button/say_save_idle.png"
image say_save_hover = "images/screen_button/say_save_hover.png"
image say_qload_idle = "images/screen_button/say_qload_idle.png"
image say_qload_hover = "images/screen_button/say_qload_hover.png"
image say_qsave_idle = "images/screen_button/say_qsave_idle.png"
image say_qsave_hover = "images/screen_button/say_qsave_hover.png"
image say_skip_idle:
    align(0.5,0.5)
    "images/screen_button/say_skip_idle.png"
image say_skip_hover = "images/screen_button/say_skip_hover.png"
image say_history_idle:
    align(0.5,0.5)
    "images/screen_button/say_history_idle.png"
image say_history_hover = "images/screen_button/say_history_hover.png"
image say_config_idle:
    align(0.5,0.5)
    "images/screen_button/say_config_idle.png"
image say_config_hover = "images/screen_button/say_config_hover.png"
image say_auto_idle:
    align(0.5,0.5)
    "images/screen_button/say_auto_idle.png"
image say_auto_hover = "images/screen_button/say_auto_hover.png"
image say_skip_idle:
    align(0.5,0.5)
    "images/screen_button/say_skip_idle.png"
image say_skip_hover = "images/screen_button/say_skip_hover.png"

# 选择界面按钮
image choice_idle = "gui/button/choice_idle_background.png"
image choice_hover = "gui/button/choice_hover_background.png"

# 确认界面按钮
image confirm_frame = "images/screen_button/confirm_frame.png"
image confirm_idle = "images/screen_button/confirm_idle.png"
image confirm_hover = "images/screen_button/confirm_hover.png"

# 设置界面按钮
image config_textbox = "images/screen_button/config_textbox.png"
image config_right_bar = "images/screen_button/config_bar_idle.png"
image config_left_bar= "images/screen_button/config_bar_hover.png"
image config_thumb_idle:
    xysize(36,36)
    "images/screen_button/config_thumb_idle.png"
image config_thumb_hover:
    xysize(36,36)
    "images/screen_button/config_thumb_hover.png"
image config_dress = "images/screen_button/config_title_dress.png"
image config_bar_dress = "images/screen_button/config_bar.png"
image config_button_hover:
    align(0.5,0.5)
    "images/screen_button/config_button_hover.png"

# 游戏菜单界面
image common_config = "images/screen_button/common_config_title.png"
image common_load = "images/screen_button/common_load_title.png"
image common_save = "images/screen_button/common_save_title.png"
image common_gallery = "images/screen_button/common_gallery_title.png"
image common_about = "images/screen_button/common_about_title.png"
image common_history = "images/screen_button/common_history_title.png"
image common_return_idle = "images/screen_button/common_close_idle.png"
image common_return_hover = "images/screen_button/common_close_hover.png"
image common_load_idle = "images/screen_button/common_load_idle.png"
image common_load_hover = "images/screen_button/common_load_hover.png"
image common_save_idle = "images/screen_button/common_save_idle.png"
image common_save_hover = "images/screen_button/common_save_hover.png"
image common_title_idle = "images/screen_button/common_title_idle.png"
image common_title_hover = "images/screen_button/common_title_hover.png"

# 存读档
image slot_button_empty_idle = "images/screen_button/slot_shot_idle.png"
image slot_button_empty_hover = "images/screen_button/slot_shot_hover.png"
image slot_button_idle:
    contains:
        align(0.5,0.125)
        "slot_button_empty_idle"
    contains:
        "gui/button/slot_idle_background.png"
image slot_button_hover:
    contains:
        align(0.5,0.125)
        "slot_button_empty_hover"
    contains:
        "gui/button/slot_hover_background.png"
image slot_page_idle = "images/screen_button/common_page_idle.png"
image slot_page_hover = "images/screen_button/common_page_hover.png"
image slot_page_selected = "images/screen_button/common_page_selected.png"
image slot_left_idle = "images/screen_button/common_left_idle.png"
image slot_left_hover = "images/screen_button/common_left_hover.png"
image slot_right_idle = "images/screen_button/common_right_idle.png"
image slot_right_hover = "images/screen_button/common_right_hover.png"
image new:
    xysize(120,45)
    "images/screen_button/slot_new.png"
image slot_delete_idle = "images/screen_button/slot_delete_idle.png"
image slot_delete_hover = "images/screen_button/slot_delete_hover.png"
# 历史界面
image history_replay_idle:
    align(0.5,0.5)
    "images/screen_button/history_replay_idle.png"
image history_replay_hover:
    align(0.5,0.5)
    "images/screen_button/history_replay_hover.png"
image history_title = "images/screen_button/history_title.png"
image history_textbox_1 = "images/screen_button/history_textbox_bg_1.png"
image history_textbox_2 = "images/screen_button/history_textbox_bg_2.png"
image history_textbox_3 = "images/screen_button/history_textbox_bg_3.png"
image history_bar_idle = "images/screen_button/common_vertical_bar_idle.png"
image history_bar_hover = "images/screen_button/common_vertical_bar_hover.png"

# 画廊界面
image gallery_button_idle = "images/screen_button/gallery_frame_idle.png"
image gallery_button_hover = "images/screen_button/gallery_frame_hover.png"
image gallery_slot = "images/screen_button/gallery_shot.png"

image cg1 = "images/CG/CG (1).png"
image cg2 = "images/CG/CG (2).png"
image cg3 = "images/CG/CG (3).png"
image cg4 = "images/CG/CG (4).png"
image cg5 = "images/CG/CG (5).png"
image cg6 = "images/CG/CG (6).png"