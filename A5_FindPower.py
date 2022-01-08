class FindPower():
    def pow(self,x,n):
        return x**n
x = int(input("enter X value : "))
n = int(input("enter N value : "))

power = FindPower()
print(power.pow(x,n))
