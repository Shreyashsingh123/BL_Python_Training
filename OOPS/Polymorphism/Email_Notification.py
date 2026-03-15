class Notification:
    def send(self,msg):
        pass
class Email(Notification):
    def send(self,msg):
       print("sending email notification",msg)
class SMS(Notification):
    def send(self,msg):
        print("Sending SMS notication",msg)
class PushNotification(Notification):
    def send(self,msg):
        print("Sending Push Notification",msg)

e1=Email()
s1=SMS()
p1=PushNotification()
ls=[e1,s1,p1]

for i in ls:
    i.send("server down")# same method doffrent behaviour depending on object type calling method