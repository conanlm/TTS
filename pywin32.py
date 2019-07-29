# 首先我们得装上pywin32 
import win32com.client
text="I love you baby"
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.rate=2
speaker.Speak(text)
# speak()
# pause()暂停
# resume() 继续