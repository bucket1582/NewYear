from math import cos, sin, pi
from time import time
from random import random, uniform
import turtle as t

g = 0.15

class Firework:
    fireworks = []
    def __init__(self, launchPos, launchSpeed, launchAngle, explosionTime, color, child):
        global g
        self.p = launchPos
        self.v = [launchSpeed * cos(launchAngle), launchSpeed * sin(launchAngle)]
        self.t = explosionTime
        self.initT = time()
        self.c = color
        self.n = child
        Firework.fireworks.append(self)

    def _process(self):
        self.v[1] -= g
        self.p[0] = self.p[0] + self.v[0]
        self.p[1] = self.p[1] + self.v[1]
        if time() - self.initT >= self.t:
            self.explode(6)
            try:
                Firework.fireworks.remove(self)
            except:
                pass
        if self.p[1] < 0 or self.p[0] < 0 or self.p[0] > 1920 or self.p[1] > 1080:
            try:
                Firework.fireworks.remove(self)
            except:
                pass

    def explode(self, count):
        for i in range(count):
            c1 = random()
            c2 = random()
            if c1 + c2 > 1.5:
                c3 = random()
            else:
                c3 = min(1.5 - (c1 + c2), 1)
            if self.n > 0:
                Firework(self.p.copy(), 30, uniform(-pi, pi), self.t/2, (random(), random(), random()), self.n-1)

    @staticmethod
    def processing():
        for i in Firework.fireworks:
            i._process()
