class Hi:
    def __init__(self,follower,following):
        self.folloers = follower
        self.folllower = following
        self.value = 0
    def value_change(self):
        self.value = 4

c1 = Hi("0","4")
# print(c1.folllower)
# print(c1.folloers)
# print(c1.value)
c1.value_change()
print(c1.value)


