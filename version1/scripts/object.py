from scripts.pyscreen import *
from scripts.colors import colors
class item:
    def __init__(self,x,y,type,color):
        self.x = x
        self.y = y
        self.amount = 1
        self.type = type
        self.color = color
        self.id = screen.objectAmount
        screen.objectAmount += 1
        self.ob = "item"
        screen.objects.append(self)
        self.alive = True
    def update(self):
        pygame.draw.rect(screen.screen, self.color, pygame.Rect((self.x+screen.CAMPOS[0])* screen.scale, (self.y+screen.CAMPOS[1])*screen.scale, 35*screen.scale, 35*screen.scale))
        r = 0
        inItem = 0
        for i in screen.objects:
            recter = pygame.Rect(i.x, i.y, 35, 35)
            self.rect = pygame.Rect(self.x, self.y, 25, 25)
            k = pygame.Rect.colliderect(self.rect,recter)
            if(k):
                if(i.ob=="conwayor"):    
                    match i.towardsTo:
                        case 1: self.x += 265.5 * screen.deltaTime
                        case 2: self.y += 265.5 * screen.deltaTime
                        case 3: self.x -= 265.5 * screen.deltaTime
                        case 4: self.y -= 265.5 * screen.deltaTime
                    break
                elif(i.ob=="seller"):
                    screen.money += 10
                    screen.researchPoint += 1
                    self.alive = False
                elif(i.ob=="item"):
                    inItem += 1
        if(inItem>4): self.alive = False
        r += 1
class seller:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.towardsTo = screen.TOWARD
        self.color = "purple"
        self.ob = "seller"
        self.alive = True
        screen.objects.append(self)
    def update(self):
        pygame.draw.rect(screen.screen, self.color, pygame.Rect((self.x+screen.CAMPOS[0])* screen.scale, (self.y+screen.CAMPOS[1])*screen.scale, 50*screen.scale, 50*screen.scale))
class object:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.towardsTo = screen.TOWARD
        self.color = color
        self.alive = True
        self.ob = "conwayor"
        screen.objects.append(self)
    def update(self):
        pygame.draw.rect(screen.screen, self.color, pygame.Rect((self.x+screen.CAMPOS[0])* screen.scale, (self.y+screen.CAMPOS[1])*screen.scale, 25*screen.scale, 25*screen.scale))
class miner:
    def __init__(self,x,y,type):
        self.type = type
        self.x = x
        self.y = y
        self.color = colors.REALYDARKGRAY
        self.towardsTo = screen.TOWARD
        self.id = screen.objectAmount
        screen.objects.append(self)
        self.spawn = 0
        self.ob = "mier"
        k = self.testOnBlock()
        self.alive = True
        if(k):
            self.color = "red"
    def testOnBlock(self):
        for i in screen.map:
            irect = pygame.Rect(i.x,i.y,25,25)
            k = pygame.Rect.colliderect(self.myrect,irect)
            if(k):
                return True
        return False
    def update(self):
        self.myrect = pygame.Rect(self.x,self.y,50,50)
        pygame.draw.rect(screen.screen, self.color, pygame.Rect((self.x+screen.CAMPOS[0])* screen.scale,(self.y+screen.CAMPOS[1])* screen.scale,50* screen.scale,50* screen.scale))
        if(self.color!="red"):
            if(self.spawn<60):
                self.spawn += 200 * screen.deltaTime
            else:
                self.spawn = 0
                match self.towardsTo:
                    case 1: item(self.x+50,self.y,"rock",self.type)
                    case 2: item(self.x,self.y+50,"rock",self.type)
                    case 3: item(self.x-50,self.y,"rock",self.type)
                    case 4: item(self.x,self.x-50,"rock",self.type)
