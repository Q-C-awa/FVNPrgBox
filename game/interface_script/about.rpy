style about_vscrollbar:
    xysize(20,720)
    offset(-800,0)
    thumb_align 0.5
    thumb_offset 2
    idle_thumb "config_thumb_idle"
    hover_thumb "config_thumb_hover"
    base_bar "history_bar_idle"
    left_bar "history_bar_hover"
style about_text:
    xalign 0.5
    size 36
    color "#5CC1E5"
    line_spacing 5
style about_vbox:
    xalign 0.5
screen about(mode=False):
    tag menu
    use game_menu(title="about",main_button=mode)
    style_prefix "about"
    viewport: 
        xpos 625
        ypos 200
        xysize(1800,800)
        scrollbars "vertical"
        mousewheel True
        draggable True
        vbox:
            spacing 30
            vbox:
                spacing 10
                text "<制作人员>" size 60 
                vbox:
                    text "文本设计-烈林凤"
                    text "UI设计-烈林凤"
                    text "立绘设计-MAZ马"
                    text "程序设计-浅唱QCQC"
            vbox:
                spacing 10
                text "<游戏版本>" size 60 
                vbox:
                    text "游戏版本-[config.version]"
                    text "发行日期-2026.01.17"
            vbox:
                spacing 10
                text "<想说的话>" size 60 
                vbox:
                    text "非常感谢使用本视觉小说UI模板！" size 30
                    text "若需标注UI设计/平面设计作者，请著名“烈林凤”" size 30
                    text "切勿将本模板中的任何素材用于非本模板用途！" size 30
                    text "切勿修改使用本模板中的任何素材！" size 30
                    text "本模板为免费模板！切勿进行售卖与购买！" size 30
                    text "在进行使用与分享时务必保留模板水印！" size 30
                    text "BUILD BY QC'S PROJECT TEMPLATE" size 12

            
        
        