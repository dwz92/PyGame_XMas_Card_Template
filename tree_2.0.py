#Christmas tree
class xmastree():    
    
    def __init__(self, screen, x, y, cols1, cols2, xstarcol):
        self.screen = screen
        self.x = x
        self.y = y
        self.cols1 = cols1
        self.cols2 = cols2
        self.xstarcol = xstarcol
        
        self.top = [(x-70, y+70), (x-20,y-25), (x+45, y+70)]
        self.mid1 = [(x-140, y+190), (x-20,y+70), (x+115, y+190)]
        self.bot = [(x-200, y+300), (x-20,y+180), (x+175, y+300)]

        self.mid2 = [(x-140, y+180), (x-20,y+70), (x+115, y+180)]
        
        self.xpos1 = [self.top, self.mid1, self.bot]
        self.xpos2 = [self.top, self.mid2, self.bot]
        
        self.top1pos = []
        self.mid1pos = []
        self.bot1pos = []
        
        self.top2pos = []
        self.mid2pos = []
        self.bot2pos = []
        
        #init positions
        for _ in range(75):
            #first layer pos
            if _ <= 14:
                self.top1pos.append(xmastree.xpos(self.xpos1[0][0], self.xpos1[0][1], self.xpos1[0][2]))
            if _ <= 30:
                self.mid1pos.append(xmastree.xpos(self.xpos1[1][0], self.xpos1[1][1], self.xpos1[1][2]))
            if _ <= 44:
                self.bot1pos.append(xmastree.xpos(self.xpos1[2][0], self.xpos1[2][1], self.xpos1[2][2]))
            
            #second layer pos
            if _ <= 14:
                self.top2pos.append(xmastree.xpos(self.xpos2[0][0], self.xpos2[0][1], self.xpos2[0][2]))
            if _ <= 44:
                self.mid2pos.append(xmastree.xpos(self.xpos2[1][0], self.xpos2[1][1], self.xpos2[1][2]))   
            
            self.bot2pos.append(xmastree.xpos(self.xpos2[2][0], self.xpos2[2][1], self.xpos2[2][2]))
            

    def xpos(p1, p2, p3):
        #rand within tri
        r1 = random.random()
        r2 = random.random()
    
        s1 = math.sqrt(r1)
    
        randx = p1[0] * (1.0 - s1) + p2[0] * (1.0 - r2) * s1 + p3[0] * r2 * s1
        randy = p1[1] * (1.0 - s1) + p2[1] * (1.0 - r2) * s1 + p3[1] * r2 * s1
        
        return randx,randy
    
    def setpos(self):
        self.top1pos = []
        self.mid1pos = []
        self.bot1pos = []
        
        self.top2pos = []
        self.mid2pos = []
        self.bot2pos = []        
        for _ in range(75):
            #first layer pos
            if _ <= 13:
                self.top1pos.append(xmastree.xpos(self.xpos1[0][0], self.xpos1[0][1], self.xpos1[0][2]))
            if _ <= 19:
                self.mid1pos.append(xmastree.xpos(self.xpos1[1][0], self.xpos1[1][1], self.xpos1[1][2]))
            if _ <= 44:
                self.bot1pos.append(xmastree.xpos(self.xpos1[2][0], self.xpos1[2][1], self.xpos1[2][2]))
            
            #second layer pos
            if _ <= 14:
                self.top2pos.append(xmastree.xpos(self.xpos2[0][0], self.xpos2[0][1], self.xpos2[0][2]))
            if _ <= 44:
                self.mid2pos.append(xmastree.xpos(self.xpos2[1][0], self.xpos2[1][1], self.xpos2[1][2]))
            
            self.bot2pos.append(xmastree.xpos(self.xpos2[2][0], self.xpos2[2][1], self.xpos2[2][2]))
    
    def drawx(self, pos,col, amount):
        for _ in range(amount):
            #colour x
            pygame.draw.arc(self.screen, random.choice(col), [pos[_][0]-10, pos[_][1], 40, 40], 4*math.pi/3, 11*math.pi/6, 2)
            pygame.draw.arc(self.screen, random.choice(col), [pos[_][0]+10, pos[_][1], 40, 40], 7*math.pi/6, 10*math.pi/6, 2)        
        
    def maintree(self):
        #top1
        self.drawx(self.top1pos, self.cols1,len(self.top1pos))
        
        #mid1
        self.drawx(self.mid1pos, self.cols1,len(self.mid1pos))
        
        #bot1
        self.drawx(self.bot1pos,self.cols1, len(self.bot1pos))
        
        #top1
        self.drawx(self.top2pos,self.cols2, len(self.top2pos))
        
        #mid1
        self.drawx(self.mid2pos,self.cols2, len(self.mid2pos))
        
        #bot1
        self.drawx(self.bot2pos,self.cols2, len(self.bot2pos))
        
        #star
        pygame.draw.polygon(self.screen, self.xstarcol, [(self.x-15,self.y+20),(self.x,self.y-20),(self.x+15,self.y+20),(self.x,self.y+10)])
        pygame.draw.polygon(self.screen, self.xstarcol, [(self.x-20,self.y-5),(self.x,self.y+10),(self.x+20,self.y-5)])
    
    def sparkletree(self):
        self.setpos()
        #top1
        self.drawx(self.top1pos, self.cols1,len(self.top1pos))
        
        #mid1
        self.drawx(self.mid1pos, self.cols1,len(self.mid1pos))
        
        #bot1
        self.drawx(self.bot1pos,self.cols1, len(self.bot1pos))
        
        #top1
        self.drawx(self.top2pos,self.cols2, len(self.top2pos))
        
        #mid1
        self.drawx(self.mid2pos,self.cols2, len(self.mid2pos))
        
        #bot1
        self.drawx(self.bot2pos,self.cols2, len(self.bot2pos))
        
        #star
        pygame.draw.polygon(self.screen, self.xstarcol, [(self.x-15,self.y+20),(self.x,self.y-20),(self.x+15,self.y+20),(self.x,self.y+10)])
        pygame.draw.polygon(self.screen, self.xstarcol, [(self.x-20,self.y-5),(self.x,self.y+10),(self.x+20,self.y-5)])        

#light
class light():
    def __init__(self, screen, x, y, lightcolours):
        self.screen = screen
        self.x = x
        self.y = y
        self.lightcolours = lightcolours
        self.cord = [(x-30,y+50), (x+25,y+65), (x-35,y+150), (x+35,y+135), (x+80, y+200), (x-120, y+300),(x+120, y+300), (x,y+190), (x-55, y+250), (x+25,y+265)]
        self.lightcol = []
        self.lightcount = 0
        
        #init light col
        for _ in range(len(self.cord)):
            self.lightcol.append(random.choice(self.lightcolours))
    
    def action(self, rate):
        #rate control
        if self.lightcount % rate == 0:
            self.lightcol = []
            for _ in range(len(self.cord)):
                self.lightcol.append(random.choice(self.lightcolours))
        for i in range(len(self.cord)):
            pygame.draw.circle(self.screen, self.lightcol[i], self.cord[i], 10)
        self.lightcount += 1


#star
class stars():
    def __init__(self, screen, starcolour, staramount):
        self.starcount = 0
        self.starpos = []
        self.starsize = []
        self.screen = screen
        self.starcolour = starcolour
        self.staramount = staramount
        
        #init star size and pos
        for _ in range(self.staramount):
            starx = random.randrange(0, 900)
            stary = random.randrange(0, 400)
            self.starpos.append([starx, stary])
            self.starsize.append(random.randrange(3))
    
    def twinkle(self, rate=1):
        if self.starcount % rate == 0:
            self.starsize = []
            for _ in range(self.staramount):
                self.starsize.append(random.randrange(3))            
    
        for _ in range(len(self.starpos)):
            pygame.draw.circle(self.screen, self.starcolour, self.starpos[_], self.starsize[_])

        self.starcount += 1

#snowman
def snowman(screen, x, y):
    #colours
    WHITE = (245, 245, 250)
    BROWN = (140, 71, 46)
    BLACK = (0, 0, 0)
    CARROT = (232, 95, 16)
    
    #BOTTOM
    pygame.draw.circle(screen, WHITE, (x,y), 40)
    
    #MID
    pygame.draw.circle(screen, WHITE, (x+5,y-50), 35)
    
    #TOP
    pygame.draw.circle(screen, WHITE, (x+10,y-105), 30)
    
    #LEFT ARM
    pygame.draw.line(screen, BROWN, (x-20,y-55),(x-40, y-80), 3)
    pygame.draw.line(screen, BROWN, (x-40, y-80),(x-50, y-86), 2)
    pygame.draw.line(screen, BROWN, (x-40, y-80),(x-35, y-86), 2)
    
    #RIGHT ARM
    pygame.draw.line(screen, BROWN, (x+40,y-50),(x+65, y-58), 3)
    pygame.draw.line(screen, BROWN, (x+65, y-58),(x+75, y-62), 2)
    pygame.draw.line(screen, BROWN, (x+65, y-58),(x+70, y-67), 2)
    
    #FACE
    pygame.draw.circle(screen, BLACK, (x-5,y-115), 4)
    pygame.draw.circle(screen, BLACK, (x+20,y-115), 4)
    pygame.draw.polygon(screen, CARROT, [(x-30,y-105), (x,y-110), (x, y-100)])
    pygame.draw.circle(screen, CARROT, (x,y-105), 5)
    
    #BUTTONS
    pygame.draw.circle(screen, BLACK, (x,y-60), 5)
    pygame.draw.circle(screen, BLACK, (x-3,y-40), 5)
    pygame.draw.circle(screen, BLACK, (x-6,y-10), 5)

#letter
def letter(screen, x, y,mode):
    WHITE= (255, 255, 255)
    SUPREMERED = (115, 9, 9)
    HIRED = (82, 20, 20)
    HIWHI = (201, 195, 195)
    
    if mode == 1:
        pygame.draw.polygon(screen, SUPREMERED, [(x,y),(x+45,y), (x+45, y+25), (x, y+25)])
        pygame.draw.line(screen, WHITE, (x,y), (x+22.5, y+12.5))
        pygame.draw.line(screen, WHITE, (x+45,y), (x+22.5, y+12.5))
    elif mode == 2:
        pygame.draw.polygon(screen, HIRED, [(x,y),(x+45,y), (x+45, y+25), (x, y+25)])
        pygame.draw.line(screen, HIWHI, (x,y), (x+22.5, y+12.5))
        pygame.draw.line(screen, HIWHI, (x+45,y), (x+22.5, y+12.5))

def generateCol():
    r = random.randint(60,255)
    g = random.randint(60,255)
    b = random.randint(60,255)
    return r, g, b

#firework
class Fireworks():
    def __init__(self, screen):
        self.screen = screen
        self.colour = generateCol()
        self.x = random.uniform(0,900)
        self.y = 300
        self.velocity = random.uniform(3.5, 7)
        self.explodepos = random.uniform(10,150)
        self.exploded = False
    
    def move(self):
        self.y -= self.velocity
        if self.y <= self.explodepos:
            self.velocity = 0
            self.exploded = True
    
    def draw(self):
        #main
        pygame.draw.rect(self.screen, self.colour, [self.x, self.y,8,8])

class particle():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.colour = generateCol()
        angle = random.uniform(-60, 240)
        velocity_mag = random.uniform(2.5, 4.0)
        self.vx = velocity_mag*math.cos(math.radians(angle))
        self.vy = -velocity_mag*math.sin(math.radians(angle))
        self.timer = 0
        self.ended = False        
    
    def get_angle(self):
        return math.atan2(-self.vy, self.vx)
    
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.timer += 1
        if self.timer >= 30:
            self.ended = True        
    
    def draw(self):
        pygame.draw.rect(self.screen, self.colour, [self.x, self.y,4,4])

#snow
class snow():
    def __init__(self, screen):
        self.colour = (255, 255, 255)
        self.screen = screen
        self.snowfall = []
        for _ in range(50):
            x = random.randrange(0, 800)
            y = random.randrange(0, 600)
            self.snowfall.append([x, y])
    
    def drop(self):
        for i in range(len(self.snowfall)):
            pygame.draw.circle(self.screen, self.colour, self.snowfall[i], 2)
    
            self.snowfall[i][1] += 3
            if self.snowfall[i][1] > 500:
                y = random.randrange(-50, -10)
                self.snowfall[i][1] = y

                x = random.randrange(0, 900)
                self.snowfall[i][0] = x
#letter
def newS(screen):
    #transparency
    s = pygame.Surface((900,520))
    s.set_alpha(200)                
    s.fill((186, 182, 181))

    fontHello = pygame.font.SysFont("Times New Roman",30)

    pygame.draw.rect(s,(255,255,255), [450-300, 20, 600, 480])
    screen.blit(s, (0,0))


#canvas
def main():
    #setup
    pygame.init()

    SIZE = (900,520)
    screen = pygame.display.set_mode(SIZE)
    running = True
    myClock = pygame.time.Clock()
    
    gift = pygame.image.load("gift.png")
    smolgift = pygame.transform.scale(gift, (230,150))
    mount = pygame.image.load("mount.png")
    smolmount = pygame.transform.scale(mount, (900,100))
    
    STAR = (169, 252, 252)
    XSTARSHADE= (201, 147, 109)
    GROUND = (23, 22, 22)
    DARKGREEN = (2, 77, 55)
    GREENBLUE = (10, 87, 76)   
    BLUEPURP = (48, 99, 240)
    LIGHTBLU = (48, 166, 240)
    PURP = (87, 29, 46)
    CHEPINK = (250, 142, 175)
    FORSKY = (11, 11, 33)
    SHADOW = (245, 250, 250)
    YELLOW = (255, 216, 138)
    
    #xmastree
    xtree = xmastree(screen, SIZE[0]/2, 100, [DARKGREEN,GREENBLUE], [BLUEPURP, LIGHTBLU], YELLOW)
    xmode = False
    
    #light
    lit = light(screen,SIZE[0]/2, 100, [CHEPINK, PURP])
    
    #star
    sky = stars(screen, STAR, 100)
    
    #fireworks
    fireworks = []
    explosion = []
    
    #magic white powder
    powder = snow(screen)
    
    #letter
    mode = False
    
    while running:
        #mouse pos
        mousex = pygame.mouse.get_pos()[0]
        mousey = pygame.mouse.get_pos()[1]

        #Check for event
        for evnt in pygame.event.get():
            if evnt.type == pygame.QUIT:
                running = False
            elif evnt.type == pygame.MOUSEBUTTONDOWN:
                if SIZE[0]/2 - 20 <= mousex <= SIZE[0]/2 + 20 and 80 <= mousey <= 110:
                    if  xmode:
                        xmode = False
                    else:
                        xmode = True
                if 70 <= mousex <= 290 and 350 <= mousey <= 500:
                    fireworks.append(Fireworks(screen))                   
                if SIZE[0]/2+210 <= mousex <= SIZE[0]/2+255 and 310 <= mousey <= 335 and mode is False:
                    mode = True

                if (0 <= mousex <= 150 or 750 <= mousex <= SIZE[0]) and mode:
                    mode = False

        #clock
        myClock.tick(10)

        #background and init
        screen.fill(FORSKY)

        #stars
        sky.twinkle(2)

        #snowground
        pygame.draw.rect(screen, GROUND, [0,300,1000,300])

        #mount
        mountrect = pygame.Rect(0,200,100, 100)
        screen.blit(smolmount, mountrect)

        #fireworks
        for firework in fireworks:
            firework.draw()
            firework.move()
            if firework.exploded:
                explosion += [particle(screen,firework.x, firework.y) for _ in range(random.randint(30,40))]
                fireworks.remove(firework)

        #explosion
        for explo in explosion:
            explo.draw()
            explo.move()
            if explo.ended:
                explosion.remove(explo)
        
        #tree and shad
        pygame.draw.ellipse(screen, SHADOW,[SIZE[0]/2-100, 400, 360, 100])
        pygame.draw.ellipse(screen, SHADOW,[SIZE[0]/2-200, 380, 360, 80])

        #tree control
        if xmode is False:
            xtree.maintree()
        else:
            xtree.sparkletree()

        #xstarhighlight
        if SIZE[0]/2 - 20 <= mousex <= SIZE[0]/2 + 20 and 80 <= mousey <= 110:
            #star
            pygame.draw.polygon(screen, XSTARSHADE, [(SIZE[0]/2-15,100+20),(SIZE[0]/2,100-20),(SIZE[0]/2+15,100+20),(SIZE[0]/2,100+10)])
            pygame.draw.polygon(screen, XSTARSHADE, [(SIZE[0]/2-20,100-5),(SIZE[0]/2,100+10),(SIZE[0]/2+20,100-5)])

        #light rate control
        lit.action(8)

        #Letter
        if SIZE[0]/2+210 <= mousex <= SIZE[0]/2+255 and 310 <= mousey <= 335:
            letter(screen, SIZE[0]/2+210, 310, 2)
        else:
            letter(screen, SIZE[0]/2+210, 310, 1)

        #snowman
        snowman(screen, SIZE[0]/2+280, 420)

        #gift
        giftrect = pygame.Rect(70,350,100, 100)
        screen.blit(smolgift, giftrect)

        #snow
        powder.drop()

        #letter
        if mode:
            newS(screen)            

        if 70 <= mousex <= 290 and 350 <= mousey <= 500:
            pygame.display.set_caption("Click on the gifts!")        
        else:
            pygame.display.set_caption("MERRY CHRISTMAS")

        #flip
        pygame.display.flip()

if __name__ == '__main__':
    import pygame, random, math
    main()
    pygame.quit() 