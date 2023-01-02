from os import walk  # a useful library that we can access the os module functions
import pygame.image
import pygame


def import_folder(path):
    surface_list = []  # to get a list of strings (each file)

    for _, __ , img_files in walk(path):  # walk uses 3 pieces of info
        image_scale = 2.2
        for image in img_files:
            full_path = path + '/' + image  # so we have all code needed from code to img
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(pygame.transform.rotozoom(img_surface, 0, image_scale))  # rescaling the img and loading

    return surface_list

# this function allows us to access any of the folders and import their images
