import pygame
pygame.init()

#Ekraani seaded
screen=pygame.display.set_mode([640,480]) #annab resulutsiooni loodud aknale
pygame.display.set_caption("Ülessanne 2") #nimetab akna
screen.fill([204, 255, 204]) #taustavärv

#Piltide kasutamine failidest
bg_shop = pygame.image.load("img/bg_shop.jpg")
seller = pygame.image.load("img/seller.png")
chat = pygame.image.load("img/chat.png")
vikklogo = pygame.image.load("img/vikklogo.png")
mõõk = pygame.image.load("img/mõõk.png")
tort = pygame.image.load("img/tort.png")
#Piltide suurused
bg_shop = pygame.transform.scale(bg_shop, [640, 480])
seller = pygame.transform.scale(seller, [200, 240]) #müüja suurus
chat = pygame.transform.scale(chat, [200, 150]) #chat suurus
vikklogo = pygame.transform.scale(vikklogo, [300, 50])
mõõk = pygame.transform.scale(mõõk, [100, 100])
tort = pygame.transform.scale(tort, [100, 100])
#Piltide kordinaadid
screen.blit(bg_shop,[0,0])
screen.blit(seller,[175,170])
screen.blit(chat,[340,120])
screen.blit(vikklogo,[0,0])
screen.blit(mõõk,[480,180])
screen.blit(tort,[350,190])
pygame.display.flip() #Värskendab akent
font = pygame.font.Font(None, 30) #Annab tekstile fondi ning selle suuruse
text = font.render("Tere Toomas!", True, [255,255,255]) #Teksti sisu ja värv
screen.blit(text, [375,175]) #Vaatab mis koodrinaatidele on see tekst kirjutatud
pygame.draw.rect(screen, [255, 255, 255], [0, 0, 300, 50], 2) #Joonistab vikk logo ümber ristküliku
pygame.draw.arc(screen,[255,255,255], [240,0,80,50], -3.14/3, 1) #Joonistab kaare vikklogo juurde joonistatud ristküliku kõrvale
pygame.display.flip() #Värskendab akent
#Alustab tsükliga
run = True
while run: #teeb tsükli     
    for event in pygame.event.get(): #Käivitab mooduli mis sulgeb akna
        if event.type == pygame.QUIT: #kui programm pannakse kinni läheb ka pygame kinni
            run = False
pygame.quit
