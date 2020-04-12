from gtts import gTTS
import re
for i in range(1,250):

	f = open(str(i)+".txt","r")	
	Text = str(f.read())
	print(Text)
	for k in Text.split("\n"):
		final = re.sub(r"[^a-zA-Z0-9]+", ' ', k)
		print("please wait...processing"+str(final))
		TTS = gTTS(text=final, lang='en-in', slow = False)
		TTS.save(str(i)+".mp3")
		break


