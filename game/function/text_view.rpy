init -99 python:
    preview_text = "这段文本将用于测试文本显示速\n度与对话框透明度....."
    def looping_text_display(st, at):
        speed = preferences.text_cps  #每秒字符数#
        total_len = len(preview_text)
        effective_speed = max(speed, 0.001) # 防止 speed 为0或负数
        duration = total_len / effective_speed + 0.6
        #计算显示字符#
        cycle_time = st % duration
        chars = int(cycle_time * speed)
        if chars > total_len:
            chars = total_len
        #返回动态文字#
        return Text(preview_text[:chars], size=26), 0.03
# 用法 add DynamicDisplayable(looping_text_display)
define textbox_preview_repeat_time = 1.5 
default countdown_time = 1.0 
screen text_view(repeat_text="这段文本将用于测试文本显示速\n度与对话框透明度....."):
    fixed:
        add "config_textbox":
            alpha (1-persistent.aplha_config)
        text repeat_text:
            color "#34859B" outlines [(4, "#ffffff",absolute(0), absolute(0))] 
            slow_cps preferences.text_cps 
            size 24
        timer textbox_preview_repeat_time:
            action [SetScreenVariable("display_preview",False)]
        timer textbox_preview_repeat_time+1.5 repeat True action [
                                                                    Hide('text_view'),
                                                                    Show("text_view"),
                                                                    SetVariable("countdown_time",textbox_preview_repeat_time+2.0)
                                                                ] 