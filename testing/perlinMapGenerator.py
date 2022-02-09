from copyreg import pickle
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
from random import randint

def generateMap():
    randomSeed = randint(0, 999)
    noise = PerlinNoise(octaves=3, seed=randomSeed)
    xpix, ypix = 35, 22
    pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

    return pic
