class media:
    def play(self,msg):
        pass
    def pause(self):
        pass
    def stop(self):
        pass
class MP3(media):
    def play(self,msg):
        print("Playing MP3 ",msg)
    def pause(self):
        print("Paused MP3 ")
    def stop(self):
        print("Stopped MP3")
class VideoPlayer(media):
    def play(self,msg):
        print("Playing videoPlayer ",msg)
    def pause(self):
        print("Paused  videoPlayer")
    def stop(self):
        print("Stopped videoPlayer")
m1=MP3()
v1=VideoPlayer()
m2=MP3()
v2=VideoPlayer()
ls=[m1,v1,m2,v2]
for i in ls:
    i.play("**********")
    i.pause()
    i.stop()