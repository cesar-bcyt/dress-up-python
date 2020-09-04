import pygame
from collections import defaultdict
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

_assets = {
    'ui': {
        'background': './assets/Keri-Dressup-RenPy-Template/game/Dressup_Screen/background.png',
        'hover': './assets/Keri-Dressup-RenPy-Template/game/Dressup_Screen/hover.png',
        'idle': './assets/Keri-Dressup-RenPy-Template/game/Dressup_Screen/idle.png',
        'selected': './assets/Keri-Dressup-RenPy-Template/game/Dressup_Screen/selected.png',
    },
    'base': {
        'base1_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Base/base1.png',
        'base2_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Base/base2.png',
        'base3_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Base/base3.png',
        'base4_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Base/base4.png',
        'base5_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Base/base5.png',
    },
    'bottoms': {
        'bottom1_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom1_1.png',
        'bottom1_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom1_2.png',
        'bottom1_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom1_3.png',
        'bottom1_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom1_4.png',
        'bottom1_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom1_5.png',
        'bottom1_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom1_6.png',

        'bottom2_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom2_1.png',
        'bottom2_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom2_2.png',
        'bottom2_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom2_3.png',
        'bottom2_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom2_4.png',
        'bottom2_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom2_5.png',
        'bottom2_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom2_6.png',

        'bottom3_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom3_1.png',
        'bottom3_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom3_2.png',
        'bottom3_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom3_3.png',
        'bottom3_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom3_4.png',
        'bottom3_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom3_5.png',
        'bottom3_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom3_6.png',

        'bottom4_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom4_1.png',
        'bottom4_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom4_2.png',
        'bottom4_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom4_3.png',
        'bottom4_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom4_4.png',
        'bottom4_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom4_5.png',
        'bottom4_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom4_6.png',

        'bottom5_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom5_1.png',
        'bottom5_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom5_2.png',
        'bottom5_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom5_3.png',
        'bottom5_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom5_4.png',
        'bottom5_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom5_5.png',
        'bottom5_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/bottom5_6.png',
    },
    'eyebrows': {
        'eyebrows1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyebrows/eyebrows1_1.png',
        'eyebrows2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyebrows/eyebrows2_1.png',
        'eyebrows3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyebrows/eyebrows3_1.png',
        'eyebrows4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyebrows/eyebrows4_1.png',
        'eyebrows5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyebrows/eyebrows5_1.png',
    },
    'eyes': {
        'eyes1_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes1_1.png',
        'eyes1_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes1_2.png',
        'eyes1_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes1_3.png',
        'eyes1_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes1_4.png',
        'eyes1_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes1_5.png',
        'eyes1_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes1_6.png',
        'eyes1_7': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes1_7.png',
        'eyes1_8': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes1_8.png',
        'eyes1_9': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes1_9.png',
        'eyes1_10': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes1_10.png',

        'eyes2_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes2_1.png',
        'eyes2_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes2_2.png',
        'eyes2_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes2_3.png',
        'eyes2_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes2_4.png',
        'eyes2_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes2_5.png',
        'eyes2_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes2_6.png',
        'eyes2_7': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes2_7.png',
        'eyes2_8': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes2_8.png',
        'eyes2_9': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes2_9.png',
        'eyes2_10': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes2_10.png',

        'eyes3_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes3_1.png',
        'eyes3_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes3_2.png',
        'eyes3_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes3_3.png',
        'eyes3_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes3_4.png',
        'eyes3_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes3_5.png',
        'eyes3_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes3_6.png',
        'eyes3_7': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes3_7.png',
        'eyes3_8': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes3_8.png',
        'eyes3_9': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes3_9.png',
        'eyes3_10': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/eyes3_10.png',
    },
    'hair': {
        'hair1_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_1.png',
        'hair1_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_2.png',
        'hair1_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_3.png',
        'hair1_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_4.png',
        'hair1_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_5.png',
        'hair1_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_5.png',
        'hair1_7': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_7.png',
        'hair1_8': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_8.png',
        'hair1_9': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_9.png',
        'hair1_10': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_10.png',
        'hair1_11': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_11.png',
        'hair1_12': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_12.png',
        'hair1_13': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_13.png',
        'hair1_14': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_14.png',
        'hair1_15': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair1_15.png',

        'hair2_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_1.png',
        'hair2_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_2.png',
        'hair2_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_3.png',
        'hair2_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_4.png',
        'hair2_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_5.png',
        'hair2_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_5.png',
        'hair2_7': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_7.png',
        'hair2_8': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_8.png',
        'hair2_9': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_9.png',
        'hair2_10': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_10.png',
        'hair2_11': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_11.png',
        'hair2_12': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_12.png',
        'hair2_13': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_13.png',
        'hair2_14': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_14.png',
        'hair2_15': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair2_15.png',

        'hair3_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_1.png',
        'hair3_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_2.png',
        'hair3_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_3.png',
        'hair3_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_4.png',
        'hair3_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_5.png',
        'hair3_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_5.png',
        'hair3_7': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_7.png',
        'hair3_8': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_8.png',
        'hair3_9': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_9.png',
        'hair3_10': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_10.png',
        'hair3_11': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_11.png',
        'hair3_12': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_12.png',
        'hair3_13': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_13.png',
        'hair3_14': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_14.png',
        'hair3_15': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair3_15.png',

        'hair4_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_1.png',
        'hair4_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_2.png',
        'hair4_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_3.png',
        'hair4_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_4.png',
        'hair4_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_5.png',
        'hair4_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_5.png',
        'hair4_7': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_7.png',
        'hair4_8': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_8.png',
        'hair4_9': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_9.png',
        'hair4_10': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_10.png',
        'hair4_11': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_11.png',
        'hair4_12': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_12.png',
        'hair4_13': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_13.png',
        'hair4_14': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_14.png',
        'hair4_15': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair4_15.png',

        'hair5_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_1.png',
        'hair5_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_2.png',
        'hair5_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_3.png',
        'hair5_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_4.png',
        'hair5_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_5.png',
        'hair5_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_5.png',
        'hair5_7': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_7.png',
        'hair5_8': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_8.png',
        'hair5_9': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_9.png',
        'hair5_10': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_10.png',
        'hair5_11': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_11.png',
        'hair5_12': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_12.png',
        'hair5_13': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_13.png',
        'hair5_14': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_14.png',
        'hair5_15': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/hair5_15.png',
    },
    'tops': {
        'top1_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top1_1.png',
        'top1_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top1_2.png',
        'top1_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top1_3.png',
        'top1_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top1_4.png',
        'top1_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top1_5.png',
        'top1_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top1_6.png',

        'top2_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top2_1.png',
        'top2_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top2_2.png',
        'top2_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top2_3.png',
        'top2_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top2_4.png',
        'top2_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top2_5.png',
        'top2_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top2_6.png',

        'top3_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top3_1.png',
        'top3_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top3_2.png',
        'top3_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top3_3.png',
        'top3_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top3_4.png',
        'top3_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top3_5.png',
        'top3_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top3_6.png',

        'top4_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top4_1.png',
        'top4_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top4_2.png',
        'top4_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top4_3.png',
        'top4_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top4_4.png',
        'top4_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top4_5.png',
        'top4_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top4_6.png',

        'top5_1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top5_1.png',
        'top5_2': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top5_2.png',
        'top5_3': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top5_3.png',
        'top5_4': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top5_4.png',
        'top5_5': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top5_5.png',
        'top5_6': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/top5_6.png',
    },
    'mouths': {
        'mouth1': './assets/Keri-Dressup-RenPy-Template/game/Create_Character/Mouth/mouth1_1.png',
    },
    'cursor': {
        'normal': './assets/cursor/normal.png',
        'clicked': './assets/cursor/clicked.png',
    }
}

assets = {}
for key in _assets.keys():
    assets[key] = {}
    # assets[key] = defaultdict(lambda: s )
    for asset, path in _assets[key].items():
        assets[key][asset] = pygame.image.load(resource_path(path))
        if key == 'cursor':
            assets[key][asset] = pygame.transform.scale(assets[key][asset], (84, 86))

ui = {
    (267+97*0, 112, 80, 80): ('set_part', 'base', 'base1'),
    (267+97*1, 112, 80, 80): ('set_part', 'base', 'base2'),
    (267+97*2, 112, 80, 80): ('set_part', 'base', 'base3'),
    (267+97*3, 112, 80, 80): ('set_part', 'base', 'base4'),
    (267+97*4, 112, 80, 80): ('set_part', 'base', 'base5'),

    (267+97*0, 232, 80, 80): ('set_part', 'hair', 'hair1'),
    (267+97*1, 232, 80, 80): ('set_part', 'hair', 'hair2'),
    (267+97*2, 232, 80, 80): ('set_part', 'hair', 'hair3'),
    (267+97*3, 232, 80, 80): ('set_part', 'hair', 'hair4'),
    (267+97*4, 232, 80, 80): ('set_part', 'hair', 'hair5'),

    (267+97*0, 352, 80, 80): ('set_color', 'hair', '1'),
    (267+97*1, 352, 80, 80): ('set_color', 'hair', '2'),
    (267+97*2, 352, 80, 80): ('set_color', 'hair', '3'),
    (267+97*3, 352, 80, 80): ('set_color', 'hair', '4'),
    (267+97*4, 352, 80, 80): ('set_color', 'hair', '5'),

    (267+97*0, 445, 80, 80): ('set_color', 'hair', '6'),
    (267+97*1, 445, 80, 80): ('set_color', 'hair', '7'),
    (267+97*2, 445, 80, 80): ('set_color', 'hair', '8'),
    (267+97*3, 445, 80, 80): ('set_color', 'hair', '9'),
    (267+97*4, 445, 80, 80): ('set_color', 'hair', '10'),

    (267+97*0, 538, 80, 80): ('set_color', 'hair', '11'),
    (267+97*1, 538, 80, 80): ('set_color', 'hair', '12'),
    (267+97*2, 538, 80, 80): ('set_color', 'hair', '13'),
    (267+97*3, 538, 80, 80): ('set_color', 'hair', '14'),
    (267+97*4, 538, 80, 80): ('set_color', 'hair', '15'),

    (267+97*0, 674, 80, 80): ('set_part', 'eyes', 'eyes1'),
    (267+97*1, 674, 80, 80): ('set_part', 'eyes', 'eyes2'),
    (267+97*2, 674, 80, 80): ('set_part', 'eyes', 'eyes3'),

    (267+97*0, 794, 80, 80): ('set_color', 'eyes', '1'),
    (267+97*1, 794, 80, 80): ('set_color', 'eyes', '2'),
    (267+97*2, 794, 80, 80): ('set_color', 'eyes', '3'),
    (267+97*3, 794, 80, 80): ('set_color', 'eyes', '4'),
    (267+97*4, 794, 80, 80): ('set_color', 'eyes', '5'),

    (267+97*0, 887, 80, 80): ('set_color', 'eyes', '6'),
    (267+97*1, 887, 80, 80): ('set_color', 'eyes', '7'),
    (267+97*2, 887, 80, 80): ('set_color', 'eyes', '8'),
    (267+97*3, 887, 80, 80): ('set_color', 'eyes', '9'),
    (267+97*4, 887, 80, 80): ('set_color', 'eyes', '10'),

    (952+97*0, 112, 80, 80): ('set_part', 'tops', 'top1'),
    (952+97*1, 112, 80, 80): ('set_part', 'tops', 'top2'),
    (952+97*2, 112, 80, 80): ('set_part', 'tops', 'top3'),
    (952+97*3, 112, 80, 80): ('set_part', 'tops', 'top4'),
    (952+97*4, 112, 80, 80): ('set_part', 'tops', 'top5'),

    (952+97*0, 232, 80, 80): ('set_part', 'bottoms', 'bottom1'),
    (952+97*1, 232, 80, 80): ('set_part', 'bottoms', 'bottom2'),
    (952+97*2, 232, 80, 80): ('set_part', 'bottoms', 'bottom3'),
    (952+97*3, 232, 80, 80): ('set_part', 'bottoms', 'bottom4'),
    (952+97*4, 232, 80, 80): ('set_part', 'bottoms', 'bottom5'),

    (1232+585*0, 522, 80, 80): 'top_left_arrow',
    (1232+585*1, 522, 80, 80): 'top_right_arrow',

    (1232+585*0, 853, 80, 80): 'bottom_left_arrow',
    (1232+585*1, 853, 80, 80): 'bottom_right_arrow',

    (1661, 14, 236, 80): 'save_picture',
}

def hovers(pos, box):
    return box[0] <= pos[0] <= box[0]+box[2] and box[1] <= pos[1] <= box[1]+box[3]

def flash_text(screen, text, position):
    text_surface = font.render(text, 1, (128, 128, 128))
    surf_size = text_surface.get_size()
    pos = (position[0]-surf_size[0]//2, position[1]-surf_size[1]//2)
    timer = 100
    while True:
        screen.blit(text_surface, pos)
        timer -= 1
        if timer <= 0:
            raise StopIteration
        else:
            yield

def flash_animation(screen):
    alpha = 255
    surface = pygame.Surface((1920, 1080), pygame.SRCALPHA)
    while True:
        surface.fill((255, 255, 255, alpha))
        screen.blit(surface, (0, 0))
        alpha -= 10
        if alpha <= 0:
            raise StopIteration
        else:
            yield

class Character():
    def __init__(self):
        self.base = 'base1_1'
        self.bottoms = 'bottom1_1'
        self.eyebrows = 'eyebrows1'
        self.eyes = 'eyes1_1'
        self.hair = 'hair1_1'
        self.tops = 'top1_1'
        self.mouths = 'mouth1'
        self._divisor = 2.5
        self.parts = ['base', 'mouths', 'eyes', 'hair', 'bottoms', 'tops', 'eyebrows']
        self.update_surfaces()

    def save_picture(self):
        surface = pygame.Surface((948, 1920))
        surface.fill((255, 255, 255))
        for part in self.parts:
            surface.blit(assets[part][getattr(self, part)], (0, 0))
        pygame.image.save(surface, 'Character.png')

    def set_part(self, part_category, part_name):
        prev = getattr(self, part_category).split('_')
        new = '_'.join((part_name, prev[1]))
        setattr(self, part_category, new)
        self.update_surfaces()

    def cycle_bottom_color(self, diff):
        prev = self.bottoms.split('_')
        new_color = (int(prev[1])+diff) % 6
        if new_color <= 0:
            new_color = 6
        self.bottoms = '_'.join((prev[0], str(new_color) ))
        self.update_surfaces()

    def cycle_top_color(self, diff):
        prev = self.tops.split('_')
        new_color = (int(prev[1])+diff) % 6
        if new_color <= 0:
            new_color = 6
        self.tops = '_'.join((prev[0], str(new_color) ))
        self.update_surfaces()

    def set_color(self, part_category, color):
        prev = getattr(self, part_category).split('_')
        new = '_'.join((prev[0], color))
        setattr(self, part_category, new)
        self.update_surfaces()

    def update_surfaces(self):
        for part in self.parts:
            setattr(self,
                    '_'+part,
                    pygame.transform.scale(assets[part][getattr(self, part)], (int(948/self._divisor), int(1920/self._divisor))))

    def draw(self, screen):
        screen.blit(self._base, (1380, 295))
        screen.blit(self._mouths, (1380, 295))
        screen.blit(self._eyebrows, (1380, 295))
        screen.blit(self._eyes, (1380, 295))
        screen.blit(self._hair, (1380, 295))
        screen.blit(self._bottoms, (1380, 295))
        screen.blit(self._tops, (1380, 295))

character = Character()

pygame.init()
pygame.font.init()
pygame.mouse.set_visible(False)
font = pygame.font.SysFont('Arial', 50)
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
background = assets['ui']['background']
idle = assets['ui']['idle']
done = False
clicked = False
animations = []
text = None
# flash = flash_animation(screen)
animations.append(flash_text(screen, 'Presiona q para salir', (1920//2, 1080-60)))

while not done:
    clock.tick(80)
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(idle, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_corrected = (mouse_pos[0]+15, mouse_pos[1]+15)
    for box in ui.keys():
        if hovers(mouse_pos_corrected, box) and not clicked:
            screen.blit(assets['ui']['hover'], box[:2], box)
        if hovers(mouse_pos_corrected, box) and clicked and type(ui[box]) is tuple:
            getattr(character, ui[box][0])(ui[box][1], ui[box][2])
        if hovers(mouse_pos_corrected, box) and type(ui[box]) is str and clicked:
            clicked = False
            if ui[box] == 'bottom_left_arrow':
                character.cycle_bottom_color(-1)
            elif ui[box] == 'bottom_right_arrow':
                character.cycle_bottom_color(1)
            elif ui[box] == 'top_left_arrow':
                character.cycle_top_color(-1)
            elif ui[box] == 'top_right_arrow':
                character.cycle_top_color(1)
            elif ui[box] == 'save_picture':
                character.save_picture()
                animations.append(flash_animation(screen))
                animations.append(flash_text(screen, 'Imagen guardada: Character.png', (1920//2, 1080-60)))

        if type(ui[box]) is tuple:
            for part in character.parts:
                if ui[box][0] == 'set_part':
                    if part == ui[box][1] and getattr(character, part).split('_')[0] == ui[box][2]:
                        screen.blit(assets['ui']['selected'], box[:2], box)
                elif ui[box][0] == 'set_color':
                    if part == ui[box][1] and getattr(character, part).split('_')[1] == ui[box][2]:
                        screen.blit(assets['ui']['selected'], box[:2], box)

    character.draw(screen)
    if clicked:
        screen.blit(assets['cursor']['clicked'], mouse_pos)
    else:
        screen.blit(assets['cursor']['normal'], mouse_pos)
    for animation in animations:
        try:
            next(animation)
        except:
            animations.remove(animation)
    pygame.display.update()
