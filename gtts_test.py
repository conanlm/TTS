from gtts import gTTS
# 使用gTTS需要翻墙
tts = gTTS('''提供给我们的客房，是在剥离城二楼通路排开的房间的中央位置。''', lang='zh-cn')
tts.save('hello.mp3')