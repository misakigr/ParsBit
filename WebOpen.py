import webbrowser
import time
import os
webbrowser.open('https://sagecell.sagemath.org/')
time.sleep(5)
print ("Successed")

browserExe = "chrome.exe"
os.system("taskkill /f /im "+browserExe)