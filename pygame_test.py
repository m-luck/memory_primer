import pygame
pygame.init()

#
# For demo purposes, the button is the whole window
#

button = pygame.display.set_mode((400, 320))

#
# Create 12-point text in white saying "Hello, World!"
#
font = pygame.font.Font(pygame.font.get_default_font(), 12)
text = font.render("Hello, World!", True, (0xff, 0xff, 0xff))

#
# Use the text's rect to get width / height
# Then center that rect on the target surface
#
text_rect = text.get_rect()
text_rect.center = button.get_rect().center
button.blit(text, text_rect)

pygame.display.flip()
