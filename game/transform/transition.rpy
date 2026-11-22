# 顺时针转场
define clockwise = ImageDissolve("transform/im/clockwise.png", 1.0, 32)
# 逆时针转场
define anticlockwise = ImageDissolve("transform/im/anticlockwise.png", 1.0, 32)
# 右擦入
define right_in = ImageDissolve("transform/im/right.png", 0.2, 32)
# 左擦入
define left_in = ImageDissolve("transform/im/left.png", 0.2, 32)
# 右擦入_2
define right_in_2 = ImageDissolve("transform/im/right_2.png", 0.2, 32)
# 左擦入_2
define left_in_2 = ImageDissolve("transform/im/left_2.png", 0.2, 32)
# 上擦入
define top_in = ImageDissolve("transform/im/top.png", 0.2, 32)
# 下擦入
define buttom_in = ImageDissolve("transform/im/buttom.png", 0.2, 32)
# 上擦入_2
define top_in_2 = ImageDissolve("transform/im/top_2.png", 0.2, 32)
# 下擦入_2
define buttom_in_2 = ImageDissolve("transform/im/buttom_2.png", 0.2, 32)
# 水波
define tran_water = ImageDissolve("transform/im/watertran.png", 0.5, 64)
# 炫光
define tran_light = ImageDissolve("transform/im/snaketran.png", 0.5, 64)
# 混沌
define tran_fog = ImageDissolve("transform/im/fogtran.png", 0.5, 64)
# 快速
define tran_fast = ImageDissolve("transform/im/fasttran.png", 0.5, 64)
# 下坠
define tran_updown = ImageDissolve("transform/im/updowntran.png", 0.5, 64)
# 睁眼闭眼
init python:
    def eyewarp(x):
        return x**1.33
    eye_open = ImageDissolve("transform/im/eye2.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("transform/im/eye2.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)
    def eye_open_time(t):
        return ImageDissolve("transform/im/eye2.png", t, ramplen=128, reverse=False, time_warp=eyewarp)
    def eye_shut_time(t):
        return ImageDissolve("transform/im/eye2.png", t, ramplen=128, reverse=True, time_warp=eyewarp)