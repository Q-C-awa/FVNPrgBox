
screen say(who, what):
    window:
        style_prefix "say"
        add "say_dress" yoffset -80
        id "window"
        background Transform(style.window.background, alpha=1-persistent.aplha_config)
        if who is not None:
            hbox:
                id "namebox"
                style "namebox"
                text who id "who"
                imagebutton:
                    xysize(50,50)
                    offset(40,10)
                    auto "say_replay_%s"
                    if  _get_voice_info().filename != None:
                        action Play("voice", _get_voice_info().filename)
                    else:
                        action NullAction()
        if renpy.is_seen(ever = True): 
            text what id "what" color "#B24F4F" # 标记颜色
        else:
            text what id "what" color "#34859B" # 未读颜色
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
    use quick_menu

init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Frame("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos 447
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos -40
    ysize gui.namebox_height
    padding gui.namebox_borders.padding

style say_label:
    color "#ffffff"
    xalign gui.name_xalign
    yalign 0.5
    size 52
    outlines [(4, "#E57373",0,0)]

style say_dialogue:
    properties gui.text_properties("dialogue")
    pos(450,50)
    textalign 0.0
    adjust_spacing False
    size 28
    xsize 1380
    color "#34859B"
    outlines [(4, "#ffffff",0,0)]
    line_spacing 15

style quick_menu_hbox:
    pos(1306,1020)
    spacing 13.8
style quick_menu_image_button:
    xysize(40,40)

screen quick_menu():
    zorder 100
    style_prefix "quick_menu"
    hbox:
        imagebutton:
            xysize(90,40)
            auto "say_qload_%s"
            action FileLoad(name=1,page=1)
        imagebutton:
            xysize(90,40)
            auto "say_qsave_%s"
            action FileSave(name=1,page=1)
        imagebutton:
            auto "say_history_%s"
            action ShowMenu("history")
        imagebutton:
            auto "say_auto_%s"
            action Preference("auto-forward", "toggle")
        imagebutton:
            auto "say_skip_%s"
            action Skip() alternate Skip(fast=True, confirm=True)
        imagebutton:
            auto "say_load_%s"
            action ShowMenu("load")
        imagebutton:
            auto "say_save_%s"
            action ShowMenu("save")
        imagebutton:
            auto "say_config_%s"
            action ShowMenu("preferences")
        imagebutton:
            auto "say_quit_%s"
            action Quit()
        

