import pygame

CHARACTERS = {
    # Add path to sprites
    1: "PATH_TO_CHARACTER1",
    2: "PATH_TO_CHARACTER2",
    3: "PATH_TO_CHARACTER3",
    4: "PATH_TO_CHARACTER4",
}

BACKGROUNDS = {
    # Add path to backgrounds
    1: "PATH_TO_BACKGROUND",
    2: "PATH_TO_BACKGROUND2",
}


def load_image(image_path: str) -> pygame.Surface:
    return pygame.image.load(image_path)


# Call load_image here for each image
# MASTER_SPRITE = load_image(CHARACTERS["INDEX_OF_MASTER_SPRITE"])