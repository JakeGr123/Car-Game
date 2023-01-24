import pygame

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)



def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)
    
def blit_rotate_center1(win1, image, top_left, angle):
    rotated_image1 = pygame.transform.rotate(image, angle)
    new_rect1 = rotated_image1.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win1.blit(rotated_image1, new_rect1.topleft)
