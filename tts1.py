import re

from pygame import mixer
from gtts import gTTS
import os
import sys
import msvcrt
text_en = input("write here whatever you want to make system speak : ")
list_in =  re.split(r"[-;,.\s]\s*",text_en)
language = 'en'
len_in= len(list_in)
for i in range(len_in):
  myobj = gTTS(text=list_in[i], lang=language, slow=False)
  myobj.save("v"+str(i)+".mp3")
  i=i+1

#os.system("start v1.mp3")    #keep this line if you want to hear your speech while running.
