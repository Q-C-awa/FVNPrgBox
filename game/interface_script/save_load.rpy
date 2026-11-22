define config.thumbnail_width = 480
define config.thumbnail_height = 270
define gui.slot_page_text_size = 36
define gui.slot_page_text_color = "#ffffff"
define gui.slot_page_text_hover_color = "#ffffff"
define gui.slot_page_text_selected_color = "#5CC1E5"
define config.has_autosave = False

screen save():
    tag menu
    use file_slots(title="save")
screen load():
    tag menu
    use file_slots(title="load")
style slot_page_hbox:
    align(0.125,0.932)
    spacing 15
style slot_page_text:
    align(0.5, 0.5)
    properties gui.text_properties("slot_page")
style slot_button_text:
    size 34
    color "#34859B"
    hover_color "#E57373"
    selected_color "#E57373"
    outlines [(3,"#ffffff",0,0)]
screen file_slots(title):
    tag menu
    use game_menu(title=title,mode=title)
    use slot_page()
    grid 3 2:
        style_prefix "slot_button"
        xalign 0.5
        yalign 0.5
        xspacing 60
        yspacing 50
        for i in range(6):
            $ slot = i + 1
            button:
                xysize(492,323)
                background "slot_button_idle"
                hover_background "slot_button_hover"
                action FileAction(slot)
                vbox:
                    add FileScreenshot(slot) xalign 0.5
                    hbox:
                        xalign 0.5
                        yoffset 10
                        if slot != 1:
                            text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位"))
                        else:
                            text FileTime(slot, format=_("快速存档-{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位"))
                        text FileSaveName(slot)
                if FileNewest(slot):
                    add "new" offset(-35,-20)
                imagebutton:
                    offset(460,-395)
                    auto "slot_delete_%s"
                    action FileDelete(slot)
                    # key "save_delete" action FileDelete(slot)

screen slot_page():
    hbox:
        style_prefix "slot_page"
        imagebutton:
            xoffset -20
            xysize(61,60)
            auto "slot_left_%s"
            action FilePagePrevious(max=1,wrap=True)
        for page in range(1,10):
            button:
                xysize(61,60)
                text "[page]"
                idle_background "slot_page_idle"
                hover_background "slot_page_hover"
                selected_background "slot_page_selected"
                action FilePage(page)
        imagebutton:
            xoffset 20
            xysize(61,60)
            auto "slot_right_%s"
            action FilePageNext(max=9)
        