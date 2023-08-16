class studenT:
    def name(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)

object=studenT()
object.name("re njik",21)

class myclass:
    num=5
    print(num)
    def sum(self,num2):
        s=self.num+num2
        print(s)
object=myclass()
object.sum(5)

class number:
    num3=20
    def addition(self,num1,num2):
        sum=num1+num2+self.num3
        print(sum)
object=number()
object.addition(11,22)

class name:
    name="renjik"
    print(name)
object=name()

