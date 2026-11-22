# 黑条，电影效果
image movietext:
    contains:
        "#000"
        size(1920,150)
        xpos 0 ypos 0
    contains:
        "#000"
        size(1920,150)
        xpos 0 ypos 930
transform movietext_tra: # 电影效果（屏幕上下2个黑条）的转场，用于黑条进入和退出
    align(0.5,0.5)
    zoom 2.0
    on show:
        easein 0.25*2 zoom 1.0
    on hide:
        easein 0.25*2 zoom 2.0
# 灰屏
image noise:
    truecenter
    "transform/im/noise1.png"
    pause 0.1
    "transform/im/noise2.png"
    pause 0.1
    "transform/im/noise3.png"
    pause 0.1
    "transform/im/noise4.png"
    pause 0.1
    xzoom -1
    "transform/im/noise1.png"
    pause 0.1
    "transform/im/noise2.png"
    pause 0.1
    "transform/im/noise3.png"
    pause 0.1
    "transform/im/noise4.png"
    pause 0.1
    yzoom -1
    "transform/im/noise1.png"
    pause 0.1
    "transform/im/noise2.png"
    pause 0.1
    "transform/im/noise3.png"
    pause 0.1
    "transform/im/noise4.png"
    pause 0.1
    xzoom 1
    "transform/im/noise1.png"
    pause 0.1
    "transform/im/noise2.png"
    pause 0.1
    "transform/im/noise3.png"
    pause 0.1
    "transform/im/noise4.png"
    pause 0.1
    yzoom 1
    repeat
# 雪花效果
image snow_white_small = SnowBlossom("white_small", count=30, border=10, xspeed=(-10, 10), yspeed=(20, 30), start=0, fast=True, horizontal=False)
image snow_white_big = SnowBlossom("white_big", count=20, border=20, xspeed=(-10, 10), yspeed=(20, 30), start=0, fast=True, horizontal=False)
image snow_white:
    contains:
        "snow_white_small"
    contains:
        "snow_white_big"
image snow_white_small_fast1=SnowBlossom("white_small", count=50, border=20, xspeed=(-120, 300), yspeed=(50, 200), start=0, fast=True, horizontal=False)
image snow_white_small_fast2=SnowBlossom("white_big", count=25, border=20, xspeed=(-120, 300), yspeed=(-70, -40), start=0, fast=True, horizontal=False)
image snow_white_big_fast=SnowBlossom("white_big", count=15, border=20, xspeed=(100, 150), yspeed=(60, 100), start=0, fast=True, horizontal=False)
image snow_white_fast:
    contains:
        "snow_white_small_fast1"
    contains:
        "snow_white_small_fast2"
    contains:
        "snow_white_big_fast"
image white_small:
    "transform/im/snow_white_single.png"
    size(4, 4)
    white_alt
image white_big:
    "transform/im/snow_white_single.png"
    size(7, 7)
    white_alt
transform white_alt:
    zoom 1.0
    alpha 0.75
    parallel:
        choice:
            linear 1.0 alpha 0.5
            linear 1.0 alpha 0.75
        choice:
            linear 1.0 alpha 1.0
            linear 1.0 alpha 0.75
        repeat
    parallel:
        choice:
            linear 1.0 zoom 1.25
            linear 1.0 zoom 1.0
        choice:
            linear 1.0 zoom 0.8
            linear 1.0 zoom 1.0
        repeat
image snow_yellow_small = SnowBlossom("yellow_small", count=40, border=10, xspeed=(-2, 50), yspeed=(20, 30), start=0, fast=True, horizontal=False)
image snow_yellow_big = SnowBlossom("yellow_big", count=25, border=20, xspeed=(-2, 50), yspeed=(20, 30), start=0, fast=True, horizontal=False)
image snow_yellow:
    contains:
        "snow_yellow_small"
    contains:
        "snow_yellow_big"
image yellow_small:
    "transform/im/snow_yellow_single.png"
    size(4, 4)
    white_alt
image yellow_big:
    "transform/im/snow_yellow_single.png"
    size(7, 7)
    white_alt

image snow_blood1=SnowBlossom("blood_single", count=50, border=20, xspeed=(-120, 300), yspeed=(50, 200), start=0, fast=True, horizontal=False)
image snow_blood2=SnowBlossom("blood_single", count=25, border=20, xspeed=(-100, 240), yspeed=(-70, -40), start=0, fast=True, horizontal=False)
image snow_blood:
    contains:
        "snow_blood1"
    contains:
        "snow_blood2"
image blood_single:
    "transform/im/snow_blood_single.png"
    blood_alt
transform blood_alt:
    zoom 1.0
    alpha 0.9
    parallel:
        choice:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.9
        choice:
            linear 1.0 alpha 1.0
            linear 1.0 alpha 0.9
        repeat
    parallel:
        choice:
            linear 1.0 zoom 1.2
            linear 1.0 zoom 1.0
        choice:
            linear 1.0 zoom 0.8
            linear 1.0 zoom 1.0
        repeat
    parallel:
        choice:
            linear 1.0 xzoom -1
            linear 1.0 xzoom 1
        choice:
            linear 1.0 yzoom -1
            linear 1.0 yzoom 1
        choice:
            linear 1.0 yzoom 1
            linear 1.0 yzoom 1
        repeat
    parallel:
        rotate 0
        linear 10 rotate 360
        repeat
# 快速线（横向）
image fastwork:
    truecenter
    "transform/im/fastwork_01.png"
    pause 0.06
    "transform/im/fastwork_02.png"
    pause 0.06
    "transform/im/fastwork_03.png"
    pause 0.06
    "transform/im/fastwork_04.png"
    pause 0.06
    repeat
image 回忆 = "transform/im/recall.png"
