import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Shiritori!")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            screen.fill("silver")


    #screen.fill("silver")
    #pygame.key.set_text_input_rect(pygame.Rect(240, 320, 40, 20))
    
    pygame.key.start_text_input()
    #pygame.key.set_text_input_rect(pygame.Rect(240, 320, 40, 20))
    pygame.display.flip()
    clock.tick(60)
pygame.quit


# def main():
#     msg = input("Type: ")
#     print(msg)

# if __name__ == "__main__":
#     main()