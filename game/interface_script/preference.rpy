define gui.preference_text_size = 48
define gui.preference_text_color = "#5CC1E5"
define gui.preference_text_hover_color = "#E57373"
define gui.preference_text_selected_color = "#E57373"
define gui.preference_text_outlines = [(3, "#ffffff",0,0)]
define gui.preference_button_text_color = gui.preference_text_color
default persistent.aplha_config = 0.75
default slow_text_preview = PreviewSlowText(
    "这段文字将用于测试文本显示速\n度和对话框透明度......",
    style="perview_dialogue")

# 初始化默认字体。旧存档/首次运行时 persistent.def_font 可能不存在（值为 None），
# 直接把它传给 Text 的 font 会在渲染时崩溃。必须在样式定义之前初始化。
init -1 python:
    if persistent.def_font is None:
        persistent.def_font = gui.text_font

# preference
style preference_frame:
    background "config_dress" 
    xysize(400,70)
style preference_button:
    xalign 0.5 
    xysize(258,79)
    hover_background "config_button_hover" 
    selected_background "config_button_hover" 
style preference_text is default:
    xalign 0.5
    properties gui.text_properties("preference")
style button_text is preference_text:
    color "#34859B"
    size 60
# text_test_style:
style perview_dialogue: # 文字预览框所用文字样式
    color "#34859B"
    size 24
    line_spacing 4
    adjust_spacing False
    offset(20,25)
    outlines [(3, "#ffffff",0,0)]
    font persistent.def_font
# slider_box
style slider_box_vbox:
    xoffset 10
    spacing -25
    align(0.722,0.495)
style slider_box_hbox:
    spacing 15
    xoffset -10
style slider_box_slider:
    xsize 416
    thumb_align 0.5
    thumb_offset 1
    idle_thumb "config_thumb_idle"
    hover_thumb "config_thumb_hover"
    base_bar "config_right_bar"
    left_bar "config_left_bar"
style slider_box_text is preference_text:
    xalign 0.0
    size 36
style slider_box_frame is preference_frame
style slider_box_button is preference_button

# system_box
style system_box_text is preference_text
style system_box_frame is preference_frame
style system_box_vbox:
    spacing 25
    align(0.235,0.342)
style system_box_button is preference_button:
    hover_background "config_button_hover" 
    selected_background "config_button_hover" 
    
screen preferences():
    use game_menu("config")
    tag menu
    add "config_bar_dress" xalign 0.435 yalign 0.5
    use system
    use slider_box

screen system():
    style_prefix "system_box"
    vbox:
        vbox:
            frame:
                textbutton "显示模式"
            vbox:
                xalign 0.5
                spacing 10
                yoffset 10
                button:
                    text "窗口模式"
                    action Preference("display", "window")
                button:
                    text "全屏模式"
                    action Preference("display", "fullscreen")
        vbox:
            frame:
                textbutton "快进模式"
            vbox:
                xalign 0.5
                spacing 10
                yoffset 10
                button:
                    text "所有文本"
                    action Preference("skip", "all")
                button:
                    text "已读文本"
                    action Preference("skip","seen")
        frame:
            background None
            add "config_textbox":
                alpha (1-persistent.aplha_config)
            add slow_text_preview

screen slider_box():
    style_prefix "slider_box"
    vbox:
        spacing -25
        vbox:
            spacing 45
            frame:
                textbutton "音量调节"
            hbox:
                vbox:
                    ysize 247
                    text "总音量"
                    text "音乐"
                    text "音效"
                    text "语音"
                vbox:
                    ysize 247
                    bar:
                        value Preference("main volume")
                    bar:
                        value Preference("music volume")
                    bar:
                        value Preference("sound volume")
                    bar:
                        value Preference("voice volume")
                vbox:
                    ysize 247
                    text "100"
                    text "100"
                    text "100"
                    text "100"
        vbox:
            spacing 45
            frame:
                textbutton "文本速度"
            hbox:
                vbox:
                    ysize 247/2
                    xsize 114
                    text "正常"
                    text "自动"
                vbox:
                    ysize 247/2
                    bar:
                        value Preference("text speed")
                        released Function(slow_text_preview.update_cps)
                    bar:
                        value Preference("auto-forward time")
                        released Function(slow_text_preview.update_afm)
                vbox:
                    ysize 247/2
                    text "100"
                    text "100"
        vbox:
            spacing 45
            frame:
                textbutton "对话框"
            hbox:
                vbox:
                    text "透明度"
                vbox:
                    bar:
                        value FieldValue(persistent,"aplha_config",range=1.0,style="slider")
                vbox:
                    text "100"



