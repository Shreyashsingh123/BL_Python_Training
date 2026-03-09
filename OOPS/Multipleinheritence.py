class Father:
    def skills1(self):
        print("Driving")
class Child():
    def skills2(self):
         print("Playing")
class GrandChild(Father,Child):
    def skills(self):
        print("none")
c=GrandChild()
c.skills()
c.skills1()
c.skills2()

# multiple inheritence means one child inherit from multiple parents