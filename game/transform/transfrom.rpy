transform p1(x=1.5,y=0.1,z=1.2):
    align(x,y)
    zoom z
transform p2(x=0.2,y=0.1,z=1.2):
    align(x,y)
    zoom z
transform p3(x=-0.85,y=0.1,z=1.2):
    align(x,y)
    zoom z
transform p(x,y,z):
    align(x,y)
    zoom z
transform tp(x,y,z,t):
    ease t xalign x yalign y zoom z

init -2 python:
    renpy.register_shader("example.hologram", variables="""
        uniform vec4 u_hologram_color;     // 全息罩色（例如偏蓝、偏绿）
        uniform vec2 u_model_size;         // 立绘的实际像素尺寸
        uniform float u_time;              // Ren'Py 自动时间变量
        uniform float u_scanline_density;  // 扫描线密度
        uniform float u_flicker_speed;     // 闪烁速度
        uniform float u_color_mix;         // 全息色与原图颜色的混合比例 (0.0=纯原图, 1.0=纯全息色)
        
        varying vec2 v_tex_coord;         
        attribute vec4 a_position;
        attribute vec2 a_tex_coord;       
    """, vertex_300="""
        v_tex_coord = a_tex_coord;        
    """, fragment_300="""
        // 1. 获取立绘原本的像素颜色
        vec4 base_color = gl_FragColor;
        

        // 【关键点 1】如果原图这个位置完全透明，直接丢弃，防止透明矩形背景亮起
        if (base_color.a == 0.0) {
            discard;
        }

        // 2. 模拟扫描线 (根据图片像素高度计算)
        float scanline = sin(v_tex_coord.y * u_model_size.y * u_scanline_density);
        scanline = smoothstep(-0.3, 0.3, scanline); 
        float line_intensity = mix(0.6, 1.0, scanline); // 扫描线暗处亮度为 0.6，明处为 1.0

        // 3. 模拟动态闪烁
        float flicker = sin(u_time * u_flicker_speed);
        float flicker_intensity = mix(0.85, 1.0, smoothstep(-0.8, 0.8, flicker));
        // float u_color_mix = 0.5;
        // 【关键点 2】将原图的 RGB 与全息颜色进行混合，显露出立绘原本的颜色
        // u_color_mix 设为 0.5 左右可以让原色和蓝色全息感完美融合
        vec3 mixed_rgb = mix(base_color.rgb, u_hologram_color.rgb, u_color_mix);

        // 4. 组合最终颜色
        // 颜色 = 混合后的RGB * 扫描线 * 闪烁波纹
        // Alpha = 原图自带的透明度 * 全息强度的不透明度
        gl_FragColor = vec4(mixed_rgb * line_intensity * flicker_intensity, base_color.a * u_hologram_color.a);
    """)

transform hologram_effect:
    shader "example.hologram"
    # 颜色混合度：0.0 是纯原图颜色，1.0 是纯蓝色。
    # 推荐 0.4 ~ 0.6，既有科技感，又能清晰看出立绘原本的衣服和五官颜色。
    u_color_mix .3
    
    # 基础全息罩色：淡蓝色（你可以调高 G 通道让它偏向科幻青色）
    u_hologram_color (0.3, 0.6, 1.0, 0.9)


    
    # 扫描线密度：数值越大扫描线越密（根据立绘分辨率调整，若立绘很高，可设为 0.2 ~ 0.5）
    u_scanline_density 0.3

    # 闪烁速度
    u_flicker_speed 4.0

    xalign 0.5

# 立绘位置
# 1.突然出现（适用于立绘）
transform burst_up(y,x):
    subpixel True
    alpha 0.00 
    yalign y
    xalign x
    parallel:
        easein 0.12 alpha 1.0
    parallel:
        easein 0.12 zoom 0.9
        easein 0.12 zoom 1.0

# 2.从左侧进入（适用于立绘）
transform enter_from_left:
    subpixel True
    alpha 0.00 
    xoffset -20
    parallel:
        easein 0.5 alpha 1.0
    parallel:
        easein 1.0 xoffset 500

# 3.从右侧进入（适用于立绘）
transform enter_from_right:
    subpixel True
    alpha 0.00 
    xoffset 20
    parallel:
        easein 0.5 alpha 1.0
    parallel:
        easein 1.0 xoffset 500

# 4.人物淡出（适用于立绘）
transform exit:
    subpixel True
    alpha 1.00 
    easein 0.5 alpha 0.0

# 5.从左侧淡出（适用于立绘）
transform exit_from_left:
    subpixel True
    alpha 1.00 
    xoffset 0
    parallel:
        easein 0.5 alpha 0.0
    parallel:
        easein 0.5 xoffset -20

# 6.从右侧淡出（适用于立绘）
transform exit_from_right:
    subpixel True
    alpha 1.00 
    xoffset 0
    parallel:
        easein 0.5 alpha 0.0
    parallel:
        easein 0.5 xoffset 20

# 7.快速起身(适用于立绘)
transform stand_up:
    subpixel True
    yoffset 800
    linear 0.1 yoffset 0

# 8.点头一次,y为点头幅度(适用于立绘)
transform nod_once(x,y,z,f = 44):
    xalign x
    yalign y
    zoom z 
    subpixel True
    easein 0.24 yoffset f 
    easeout 0.24 yoffset 0 

# 9.点头两次,y为点头幅度(适用于立绘)
transform nod_twice(x,y,z,f = 44):
    subpixel True
    xalign x
    yalign y
    zoom z 
    easein 0.24 yoffset f  
    easeout 0.24 yoffset 0 
    easein 0.24 yoffset f  
    easeout 0.24 yoffset 0

# 10.摇头，t为时间(适用于立绘)
transform shocked(x,y,z,t=0.1):
    subpixel True
    xalign x
    yalign y
    zoom z    
    easein t yoffset 0
    easeout t yoffset -100
    easein t yoffset 0

# 11.吓一跳(适用于立绘)
transform shake_head(t=0.15):
    subpixel True
    easein t yoffset -40
    easeout t yoffset 0

# 12.剧烈抖动(不循环)，t为时间(适用于立绘)
transform dithering(t=0.05):
    subpixel True
    easein t xoffset 20
    easeout t xoffset 0
    easein t xoffset -15
    easeout t xoffset 0
    easein t xoffset 10
    easeout t xoffset 0

# 13.剧烈抖动(循环)，t为时间(适用于立绘)
transform dithering_loop(t=0.05):
    subpixel True
    easein t xoffset 20
    easeout t xoffset 0
    easein t xoffset -15
    easeout t xoffset 0
    easein t xoffset 10
    easeout t xoffset 0
    repeat 3

###########
##
## 以下语句只有在特殊情况下使用
##
## extend语句切换立绘时替代with dissolve语句使用，可在显示对话框的情况下切换立绘，改变表情
##
###########

# 14.展示
transform display(delay):
    alpha 0.0
    easein delay alpha 1.0

# 15.消失
transform disappear:
    alpha 1.0
    easein 0.12 alpha 0.0

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

# 18.逐渐出现

transform bright(delay):
    alpha 0.4
    linear delay alpha 1.0

# 19.左淡入

transform enter_left:
    alpha 0.00 
    yalign 1.0
    xoffset -20
    parallel:
        easein 0.5 alpha 1.0
    parallel:
        easein 0.5 xoffset 0

# 20.右淡入

transform enter_right:
    alpha 0.00 
    yalign 1.0
    xoffset 20
    parallel:
        easein 0.5 alpha 1.0
    parallel:
        easein 0.5 xoffset 0

# 21.相机横扫（左到右）
transform camera_pan_1(t=5.0):
    xalign 0.0 yalign 0.5 zoom 1.3
    linear t xalign 1.0

# 21.相机横扫（左到右）
transform camera_pan_2(t=5.0):
    xalign 1.0 yalign 0.5 zoom 1.3
    linear t xalign 0.0
# camera复位
transform re_cm(t=0.0):
    easein t xalign 0.5 yalign 0.5 zoom 1.0
# 1.突然出现（适用于立绘）
transform burst_up(y,x):
    subpixel True
    alpha 0.00 
    yalign y
    xalign x
    parallel:
        easein 0.12 alpha 1.0
    parallel:
        easein 0.12 zoom 0.9
        easein 0.12 zoom 1.0

# 2.从左侧进入（适用于立绘）
transform enter_from_left:
    subpixel True
    alpha 0.00 
    xoffset -20
    parallel:
        easein 0.5 alpha 1.0
    parallel:
        easein 1.0 xoffset 500

# 3.从右侧进入（适用于立绘）
transform enter_from_right:
    subpixel True
    alpha 0.00 
    xoffset 20
    parallel:
        easein 0.5 alpha 1.0
    parallel:
        easein 1.0 xoffset 500

# 4.人物淡出（适用于立绘）
transform exit:
    subpixel True
    alpha 1.00 
    easein 0.5 alpha 0.0

# 5.从左侧淡出（适用于立绘）
transform exit_from_left:
    subpixel True
    alpha 1.00 
    xoffset 0
    parallel:
        easein 0.5 alpha 0.0
    parallel:
        easein 0.5 xoffset -20

# 6.从右侧淡出（适用于立绘）
transform exit_from_right:
    subpixel True
    alpha 1.00 
    xoffset 0
    parallel:
        easein 0.5 alpha 0.0
    parallel:
        easein 0.5 xoffset 20

# 7.快速起身(适用于立绘)
transform stand_up:
    subpixel True
    yoffset 800
    linear 0.1 yoffset 0

# 8.点头一次,y为点头幅度(适用于立绘)
transform nod_once(x,y,z,f = 44):
    xalign x
    yalign y
    zoom z 
    subpixel True
    easein 0.24 yoffset f 
    easeout 0.24 yoffset 0 

# 9.点头两次,y为点头幅度(适用于立绘)
transform nod_twice(x,y,z,f = 44):
    subpixel True
    xalign x
    yalign y
    zoom z 
    easein 0.24 yoffset f  
    easeout 0.24 yoffset 0 
    easein 0.24 yoffset f  
    easeout 0.24 yoffset 0

# 10.摇头，t为时间(适用于立绘)
transform shocked(x,y,z,t=0.1):
    subpixel True
    xalign x
    yalign y
    zoom z    
    easein t yoffset 0
    easeout t yoffset -100
    easein t yoffset 0

# 11.吓一跳(适用于立绘)
transform shake_head(x,y,z,t=0.15):
    xalign x
    yalign y
    zoom z 
    subpixel True
    easein t xoffset 20
    easeout t xoffset 0
    easein t xoffset -15
    easeout t xoffset 0
    easein t xoffset 10
    easeout t xoffset 0

# 12.剧烈抖动(不循环)，t为时间(适用于立绘)
transform dithering(t=0.05):
    subpixel True
    easein t xoffset 20
    easeout t xoffset 0
    easein t xoffset -15
    easeout t xoffset 0
    easein t xoffset 10
    easeout t xoffset 0

# 13.剧烈抖动(循环)，t为时间(适用于立绘)
transform dithering_loop(t=0.05):
    subpixel True
    easein t xoffset 20
    easeout t xoffset 0
    easein t xoffset -15
    easeout t xoffset 0
    easein t xoffset 10
    easeout t xoffset 0
    repeat 3


# 定义震动特效 Shake
init:

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,time,child,add_sizes=True,**properties)

        Shake = renpy.curry(_Shake)
    #

#