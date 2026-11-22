init -99 python:
    def show_code(func):
        import inspect
        print(inspect.getsource(func))
    # config.always_shown_screens.append("debug")
    config.layers.append("debug_layer")
    config.top_layers.append("debug_layer")
default persistent.debug_ap = 0.1
transform debug_mode_t():
    alpha persistent.debug_ap

screen debug:
    layer "debug_layer"
    add "debug/gallery.jpg":
        alpha persistent.debug_ap
    frame:
        background None
        transform:
            blur 1
            alpha 0.85
            fixed:
                text "debug_mode":
                    size 25
                    outlines [(1, "#000000",1,1)]
                    color '#ffffff'
        bar:
            yoffset 80
            bar_vertical True
            xysize(10,500)
            value FieldValue(persistent,"debug_ap",range=1.0,style="slider")
    