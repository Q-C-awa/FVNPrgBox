screen main_menu():
    tag menu
    add "bg"
    add "main_menu_mask"
    add Text("LOGO",size=100, color="#000000", outlines=[(2, "#ffffff")]):
        pos(165,100)
    vbox:
        pos(170,263)
        spacing 10
        imagebutton:
            auto "main_menu_start_%s"
            action Start()
        imagebutton:
            auto "main_menu_load_%s"
            action ShowMenu("load")
        imagebutton:
            auto "main_menu_config_%s"
            action ShowMenu("preferences")
        imagebutton:
            auto "main_menu_gallery_%s"
            action ShowMenu("gallery")
        imagebutton:
            auto "main_menu_about_%s"
            action ShowMenu("about",mode=True)
        imagebutton:
            auto "main_menu_quit_%s"
            action Quit()