import pygame,random,time
pygame.init()
d=pygame.display.set_mode((600,600))
d.fill((0,0,0))
pygame.display.update()
clock=pygame.time.Clock()
class rain:
    x=10
    y=10
    v=0
    size=10
    def __init__(self):
        self.x=random.randint(0,600)
        self.y=random.randint(0,600)
        self.v=random.randint(7,10)
        self.size=random.randint(5,10)
        pygame.draw.line(d,(51, 153, 255),(self.x,self.y),(self.x,self.y+self.size),2)
    def fall(self):
        self.y=self.y+self.v
        if self.y>600:
            self.y=0
        pygame.draw.line(d, (51, 153, 255), (self.x, self.y), (self.x, self.y + self.size), 2)

drops=[]
for i in range(300):
    object=rain()
    drops.append(object)
pygame.display.update()
while(1):
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            quit()
    d.fill((0,0,0))
    for ob in drops:
        ob.fall()
    pygame.display.update()
    clock.tick(70)
