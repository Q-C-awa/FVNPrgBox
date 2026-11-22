define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }
style history_vscrollbar:
    xysize(20,720)
    offset(-275,0)
    thumb_align 0.5
    thumb_offset 2
    idle_thumb "config_thumb_idle"
    hover_thumb "config_thumb_hover"
    base_bar "history_bar_idle"
    left_bar "history_bar_hover"
style history_text:
    size 24
    color "#34859B"
style history_name_text:
    size 36
    color "#E57373"
screen history():
    tag menu
    use game_menu("history",main_button=False)
    predict False
    style_prefix "history"
    viewport: 
        pos(0.13,0.17)
        xysize(1800,800)
        scrollbars "vertical"
        mousewheel True
        draggable True
        yinitial 1.0
        vbox:
            for h in _history_list:
                hbox:
                    offset(20,10)
                    ysize 100
                    button:
                        offset(-20,15)
                        xysize(50,50)
                        idle_background "history_replay_idle"
                        hover_background "history_replay_hover"
                        action If("h.voice.filename != None",
                                true=Play("voice", h.voice.filename),
                                false=NullAction())
                    frame:
                        yalign -0.1
                        xysize(98,98)
                        background "history_title"
                    button:
                        xysize(175,200) 
                        if h.who:
                            text h.who:
                                outlines[(7,"#B24F4F",0,0),(4,"#ffffff",0,0)]
                                style "history_name_text"
                                substitute False
                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    button:
                        xysize(1100,100)
                        text what:
                            outlines[(7,"#34859B",0,0),(4,"#ffffff",0,0)]
                            substitute False
                        action Confirm("您确定要返回吗？\n位保存的内容将会消失！",yes=RollbackToIdentifier(h.rollback_identifier),no=NullAction())
        if not _history_list:
                    label _("尚无对话历史记录。")
