## 语音文件辅助函数
## 简化语音文件的引用

init python:
    # 语音文件路径映射
    voice_paths = {
        "example":"audio/voice/example/example_{ep}/{ep}_{num}.mp3",
    }
    
    # 当前章节号（需要在每个章节开始时设置）
    current_episode = 1
    
    def v(character, num): # 获取语音文件路径的函数，character为角色名，num为语音编号
        if character in voice_paths: 
            path_template = voice_paths[character]
            return path_template.format(ep=current_episode, num=num)
        return None
    
    def set_episode(ep):
        global current_episode
        current_episode = ep

# 定义一个更简洁的语音标签
define config.voice_filename_format = "{filename}"
