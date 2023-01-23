import pygame
pygame.init()

#ekraani seaded
screen=pygame.display.set_mode([640,480]) #Ekraani laius
pygame.display.set_caption("Ülesanne 2") #Ekraani nimi
screen.fill([204, 255, 204]) #Ekraani täitmine

#Lisame pildid
shop = pygame.image.load("image/bg_shop.jpg") #poe taustapilt
chat = pygame.image.load("image/chat.png") #chat pilt
seller = pygame.image.load("image/seller.png") #müüja pilt
seller = pygame.transform.scale(seller, [200, 240]) #müüja suurus
chat = pygame.transform.scale(chat, [200, 150]) #chat suurus
screen.blit(shop,[0,0]) #pildi kordinaadid
screen.blit(seller,[175,170]) #pildi kordinaadid
screen.blit(chat,[340,120]) #pildi kordinaadid
#Text
font = pygame.font.Font(None, 30) #Fonti sätted
text = font.render("Tere Toomas!", True, [255,255,255]) #Teksti sisu ja värv
screen.blit(text, [375,175])


pygame.display.flip() #värskendab aknaid
running = True #Hoiab programmi töös

#Sulgeb akna punasest ristist
while running: #Loop
    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get(): # Alustab programm mis paneb akna kinni
        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False