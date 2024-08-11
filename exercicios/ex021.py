import playsound
pygame.init()
pygame.mixer.load('ex021-audio.mp3')
pygame.mixer.play()
pygame.event.wait()
