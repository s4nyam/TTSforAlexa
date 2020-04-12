from gtts import gTTS
import time
for i in range(1,250):
	f = open(str(i)+".txt","r")	
	Text = f

	print("please wait...processing")
	TTS = gTTS(text=Text, lang='en-uk')
	ts=time.time()
	# Save to mp3 in current dir.
	TTS.save(str(i)+".mp3")


