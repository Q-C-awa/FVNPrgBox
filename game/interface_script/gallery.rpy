image locked = "images/screen_button/gallery_shot.png"
init python:
    # 代码本身就是注释
    class Ga_cg():
        def __init__(self,tag,images,condition=None,transform=Dissolve(0.25)): # tag为图片标签，images为差分图列表，condition为解锁条件，transform为过渡动画
            self.images = images
            self.condition = condition
            self.transform = transform
            self.tag = tag
    CG_list = [
        Ga_cg(tag="p1", images="cg1"),
        Ga_cg(tag="p2", images="cg2"),
        Ga_cg(tag="p3", images="cg3"),
        Ga_cg(tag="p4", images="cg4"),
        Ga_cg(tag="p5", images="cg5"),
        Ga_cg(tag="p6", images="cg6"),
        Ga_cg(tag="p7", images="cg1"),
        Ga_cg(tag="p8", images="cg2"),
        Ga_cg(tag="p9", images="cg3"),
        Ga_cg(tag="p10", images="cg4"),
        Ga_cg(tag="p11", images="cg5"),
        Ga_cg(tag="p12", images="cg6"),
        Ga_cg(tag="p13", images="cg1"),
        Ga_cg(tag="p14", images="cg2"),
        Ga_cg(tag="p15", images="cg3"),
        Ga_cg(tag="p16", images="cg4"),
        Ga_cg(tag="p17", images="cg5"),
        Ga_cg(tag="p18", images="cg6"),
        Ga_cg(tag="p19", images="cg6"),
        Ga_cg(tag="p20", images="cg6"),
        Ga_cg(tag="p21", images="cg6"),
        Ga_cg(tag="p22", images="cg6"),
        Ga_cg(tag="p23", images="cg6"),
        Ga_cg(tag="p24", images="cg6"),
        Ga_cg(tag="p25", images="cg6"),
        Ga_cg(tag="p26", images="cg6"),
        Ga_cg(tag="p27", images="cg6"),
        Ga_cg(tag="p28", images="cg6"),
        Ga_cg(tag="p29", images="cg6"),
        Ga_cg(tag="p30", images="cg6"),
        Ga_cg(tag="p31", images="cg6"),
        Ga_cg(tag="p32", images="cg6"),
        Ga_cg(tag="p33", images="cg6"),
        Ga_cg(tag="p34", images="cg6"),
        Ga_cg(tag="p35", images="cg6"),
        Ga_cg(tag="p36", images="cg6"),
        Ga_cg(tag="p37", images="cg6"),
        Ga_cg(tag="p38", images="cg6"),
        Ga_cg(tag="p39", images="cg6"),
        Ga_cg(tag="p40", images="cg6"),
        Ga_cg(tag="p41", images="cg6"),
        Ga_cg(tag="p42", images="cg6"),
        Ga_cg(tag="p43", images="cg6"),
        Ga_cg(tag="p44", images="cg6"),
        Ga_cg(tag="p45", images="cg6"),
        Ga_cg(tag="p46", images="cg6"),
        Ga_cg(tag="p47", images="cg6"),
        Ga_cg(tag="p48", images="cg6"),
        Ga_cg(tag="p49", images="cg6"),
        Ga_cg(tag="p50", images="cg6"),
        Ga_cg(tag="p51", images="cg6"),
        Ga_cg(tag="p52", images="cg6"),
        Ga_cg(tag="p53", images="cg6"),
        Ga_cg(tag="p54", images="cg6"),
        # 在这里填入图片 tag为图片标签，image为差分
        ]
    gall = Gallery()
    for CG_num in CG_list:
        gall.button(CG_num.tag)
        if CG_num.condition is not None:
            gall.condition(f"{str(CG_num.condition)}")
        for image_num in CG_num.images:
            gall.unlock(image_num)
        for image_num in CG_num.images:
            gall.image(image_num)
        if CG_num.transform is not None:
            gall.transition = CG_num.transform
    gall.locked_button =  "locked"
    def page_next():
        global gallery_page_index, start_page, end_page
        (gallery_page_index := gallery_page_index + 1) if (gallery_page_index + 1) * per_button < len(CG_list) else (gallery_page_index := 0)
    def page_last():
        global gallery_page_index
        (gallery_page_index := gallery_page_index - 1) if gallery_page_index > 0 else (gallery_page_index := (len(CG_list) - 1) // per_button)
init python:
    gallery_page_index = 0 # 当前页码索引
    CG_list_index = 0 # 当前CG索引
    Gallery_gird_width = 3 # 画廊网格宽度
    Gallery_gird_hight = 2 # 画廊网格高度
    per_button = Gallery_gird_hight*Gallery_gird_width # 每页按钮数量
screen gallery():
    tag menu
    use game_menu("gallery")
    use gallery_page()
    $ start_page = gallery_page_index * per_button # 当前页起始CG索引
    $ end_page = min(start_page+per_button,len(CG_list)) # 当前页结束CG索引
    grid Gallery_gird_width Gallery_gird_hight: # 画廊网格布局
        align(0.5, 0.5)
        spacing 40
        for CG_list_index in range(start_page,end_page):
            button:
                background "gallery_button_idle"
                hover_background "gallery_button_hover"
                add gall.make_button(name=CG_list[CG_list_index].tag,unlocked=CG_list[CG_list_index].images[0]) # 添加画廊按钮
screen gallery_page():
    hbox:
        style_prefix "slot_page"
        imagebutton:
            xoffset -20
            xysize(61,60)
            auto "slot_left_%s"
            action Function(page_last)
        for page in range(1,10):
            button:
                xysize(61,60)
                text "[page]"
                idle_background "slot_page_idle"
                hover_background "slot_page_hover"
                selected_background "slot_page_selected"
                action SetVariable("gallery_page_index",page-1)
        imagebutton:
            xoffset 20
            xysize(61,60)
            auto "slot_right_%s"
            action Function(page_next)     