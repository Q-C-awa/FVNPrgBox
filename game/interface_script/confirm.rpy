define gui.confirm_button_text_size = 48
define gui.confirm_button_text_color = "#34859B"
screen confirm(message, yes_action, no_action):
    style_prefix "confirm"
    modal True
    zorder 520
    if len(message) > 30:
        $ text_get_size = 36
    else:
        $ text_get_size = 42
    add "confirm_mask"
    frame:
        label _(message):
            text_size text_get_size
            xalign 0.5
        hbox:
            button:
                text _("确定")
                action yes_action
            button:
                text _("取消")
                action no_action
    key "game_menu" action no_action
style confirm_button:
    xysize(200, 60)
    idle_background "confirm_idle"
    hover_background "confirm_hover"
style confirm_hbox:
    align(0.5,1.25)
    spacing 150
style confirm_label:
    align(0.5,0.4)
style confirm_label_text is confirm_label:
    properties gui.text_properties("confirm_text")
style confirm_text:
    align(0.5, 0.5)
    size 36
    color "#ffffffff"
style confirm_frame:
    background "confirm_frame"
    xysize (808, 188)
    xalign .5
    yalign .5