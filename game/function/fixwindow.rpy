# 窗口缩放适配
init python:
    screen_width = config.screen_width
    screen_height = config.screen_height
    last_pw = screen_width
    last_ph = screen_height
    def fixwindow():
        if preferences.fullscreen:
            return
        global last_pw, last_ph
        pw, ph = renpy.get_physical_size()
        dw = abs(pw - last_pw)
        dh = abs(ph - last_ph)
        if dw < 10 and dh < 10:
            return
        if dw >= dh:
            size = round(pw / float(screen_width), 2)
        else:
            size = round(ph / float(screen_height), 2)
        if ph < 255 or pw < 455:
            size = 0.24
        renpy.run(Preference("display", size))
        last_pw, last_ph = pw, ph