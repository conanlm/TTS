from aip import AipSpeech
""" 你的 APPID AK SK """
APP_ID = 'APP_ID'
API_KEY = 'API_KEY'
SECRET_KEY = 'SECRET_KEY'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
#这些是参数可以去http://ai.baidu.com/docs#/TTS-Online-Python-SDK/top有详细解释
with open('1.txt','r',encoding='utf-8') as f:
    line = f.read()#文件不大，一次性读取
# lan="欢迎使用这个东东，呃盒，你，是不是，傻"
result  = client.synthesis(line, 'zh', 1, {  
    'vol': 5,'per':4,'spd':5
})

#识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)