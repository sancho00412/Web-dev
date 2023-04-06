import pygame
pygame.init()


w,h = 1000,550
screen=pygame.display.set_mode((w,h))


#playlist
music='sound/mus1.mp3'
music2='sound/mus2.mp3'
music3='sound/mus3.mp3'
playlist=[music,music2,music3]
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

# #screen_photo
# photo='images/mus2.jpg'
# image = pygame.image.load(photo)
# image_rect = image.get_rect()


paused=False
volume=0.5
key={
    pygame.K_SPACE:"pause",
    pygame.K_DOWN:"v_down",
    pygame.K_UP:"v_up",
    pygame.K_RIGHT:"next",
    pygame.K_LEFT:"previous"
}
current_song=0
def play_next():
   global current_song
   
   pygame.mixer.music.stop()
   current_song=(current_song+1)%len(playlist)
   pygame.mixer.music.load(playlist[current_song])
   pygame.mixer.music.play(-1)
def play_previous():
   global current_song
   pygame.mixer.music.stop()
   current_song=(current_song-1)%len(playlist)
   pygame.mixer.music.load(playlist[current_song])
   pygame.mixer.music.play(-1)
while True:
    
    # screen.fill(black)
   #  screen.blit(image,image_rect)
    pygame.display.flip()
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the program
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key in key:
                action=key[event.key]
                if action =="pause":
                    if paused:
                     pygame.mixer.music.unpause()
                     paused=False
                    
                    else:
                     pygame.mixer.music.pause()
                     paused = True
                elif action=="v_up":
                   volume=min(volume+0.1,1)
                   pygame.mixer.music.set_volume(volume)
                elif action=="v_down":
                   volume=max(volume-0.1,0)
                   pygame.mixer.music.set_volume(volume)
                elif action=="next":
                   play_next()
                elif action=="previous":
                   play_previous()
            pygame.display.update()