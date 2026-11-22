init -10 python:
    class PreviewSlowText(renpy.Displayable):
        """
        用于预览当前CPS（每秒字符显示速度）和自动前进时间设置的显示组件。
        每次刷新时自动检测字体、样式等变化并更新。

        参数说明：
        -----------
        text : string
            在此预览组件中显示的文本内容。
        style : str
            预览文本使用的Ren'Py样式名称。默认为"say_dialogue"。
        properties : dict
            其他可选的样式关键字参数，会被应用到预览文本上。
        """
        def __init__(self, text, style="say_dialogue", **properties):

            super(PreviewSlowText, self).__init__()

            self.original_text = text
            self._style = style
            self._properties = properties

            # 追踪状态变化
            self._last_def_font = persistent.def_font

            self._rebuild()

            self.start_st = None
            self.current_st = 0

        def _rebuild(self):
            """使用当前设置重建预览文本组件。"""

            # persistent.def_font 在旧存档或首次运行时可能尚未赋值（None），
            # 直接传给 Text 会导致字体加载时崩溃，因此统一回退到默认字体。
            font = persistent.def_font or gui.text_font

            # 只在这里调整行距；颜色、描边等交给 style（perview_dialogue）控制。
            # 否则 Text(...) 的显式参数会覆盖样式里的设置。
            # 注意：SourceHanSansLite 不能使用负行距，否则中文上下行会叠在一起。
            if font == "Noto_Sans_SC_Bold.ttf":
                line_spacing = -8
            else:
                line_spacing = 4

            self.current_child = Text(self.original_text,
                slow_cps=preferences.text_cps,
                style=self._style,
                font=font,
                line_spacing=line_spacing, **self._properties)

            # 更新追踪值
            self._last_def_font = font

        def update_cps(self):
            """当文本速度改变时调用，刷新显示组件。"""
            self._rebuild()
            self.start_st = self.current_st

        def update_afm(self):
            """当自动前进时间改变时调用，刷新显示组件。"""
            self._rebuild()
            self.start_st = self.current_st

        def render(self, width, height, st, at):
            """将文本渲染到屏幕上。每次刷新自动检测状态变化。"""

            if self.start_st is None:
                self.start_st = st
            self.current_st = st

            renpy.redraw(self, 0.03)

            # 检测字体或其他关键状态是否发生变化，自动重建
            if (persistent.def_font or gui.text_font) != self._last_def_font:
                self._rebuild()
                self.start_st = self.current_st

            render = renpy.Render(width, height)
            new_st = st - self.start_st
            render.place(self.current_child, st=new_st, at=at)

            return render
