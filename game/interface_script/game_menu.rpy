screen game_menu(title,mode="None",main_button=True):
    add "common_bg"
    add "common_[title]" xalign 0.5 yalign 0.04
    if main_button:
        imagebutton:
            align(0.889,0.933)
            auto "common_title_%s"
            action MainMenu()
    if mode == "save":
        imagebutton:
            align(0.775,0.933)
            auto "common_load_%s"
            action ShowMenu("load")
    elif mode == "load":
        imagebutton:
            align(0.775,0.933)
            auto "common_save_%s"
            action ShowMenu("save")
    elif mode == "None":
        pass
    imagebutton:
        align(0.935,0.933)
        auto "common_return_%s"
        action Return()