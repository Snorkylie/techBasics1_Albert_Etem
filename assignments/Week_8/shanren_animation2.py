#Some of the code is stolen from a project I did with my friends ehem. Then there is ssome from the snippet which is the dino.py

#  World of Shanren: Rose Swordmage


# importing required library
import pygame
import random
import math
import sys
import os


SCREEN_WIDTH  = 900
SCREEN_HEIGHT = 650
BACKGROUND_COLOR = (10, 5, 25)   # <- AI


class Particle:
    def __init__(self, x, y, colour):
        self.x = x + random.uniform(-10, 10)
        self.y = y + random.uniform(-5, 5)
        self.vx = random.uniform(-0.8, 0.8)
        self.vy = random.uniform(-2.0, -0.4)
        self.colour = colour
        self.radius  = random.randint(3, 7)
        self.alpha   = 255
        self.fade    = random.randint(8, 18)

    def update(self):
        # Position updaten
        self.x += self.vx
        self.y += self.vy
        self.alpha = max(0, self.alpha - self.fade)

    def alive(self):
        return self.alpha > 0   # True

#AI did the surface before the class
    def draw(self, screen):
        # Kleine eigene Surface mit Alpha-Kanal, damit Transparenz funktioniert
        surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, (*self.colour, self.alpha), (self.radius, self.radius), self.radius)
        screen.blit(surf, (int(self.x - self.radius), int(self.y - self.radius)))

class RoseSwordmage:
    _base_image = None

    @classmethod
    def load_image(cls, path, height=160):
        """Lädt und skaliert das Bild einmal für die ganze Klasse."""  # <- AI
        raw   = pygame.image.load(path).convert_alpha()    # ← from Snippet: convert_alpha() für PNG
        ratio = height / raw.get_height()
        w     = int(raw.get_width() * ratio)
        cls._base_image = pygame.transform.scale(raw, (w, height))   # <- from Snippet: transform.scale

    def __init__(self, tint_colour, particle_colour, instance_id):

        scale  = random.uniform(0.80, 1.30)
        bw, bh = self._base_image.get_size()
        scaled = pygame.transform.scale(                    # <- from Snippet: transform.scale
            self._base_image, (int(bw * scale), int(bh * scale))
        )

        # Farbton-Overlay on the scaled picture  <- from the Snippet-comment: tint
        self.image = scaled.copy()
        tint_surf  = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        tint_surf.fill((*tint_colour, 55))
        self.image.blit(tint_surf, (0, 0))           # <- from Snippet: blit

        self.w = self.image.get_width()
        self.h = self.image.get_height()

        self.tint_colour     = tint_colour
        self.particle_colour = particle_colour

        # circle-Parameter <- AI
        self.cx = random.randint(180, SCREEN_WIDTH  - 180)
        self.cy = random.randint(180, SCREEN_HEIGHT - 180)
        self.orbit_r = random.randint(80, 200)       # Radius of circle

        self.angle = (2 * math.pi / 5 * instance_id) + random.uniform(0, 0.5)
        self.speed = random.uniform(0.008, 0.025)
        if random.random() < 0.5:
            self.speed *= -1

        # helping me with the circles and radius made by AI
        self.x = self.cx + self.orbit_r * math.cos(self.angle)
        self.y = self.cy + self.orbit_r * math.sin(self.angle)

        # Down here selfmade aka stolen from another project we had with friends xD
        self.pulse_phase = random.uniform(0, 2 * math.pi)
        self.pulse_speed = random.uniform(0.04, 0.09)

        # particles also stolen from project and helped by AI
        self.particles    = []
        self.ptimer       = 0
        self.prate        = random.randint(2, 5)     # Neuer Partikel alle N Frames

    def update(self):

        self.angle += self.speed
        # math.cos/sin making the circle path
        self.x = self.cx + self.orbit_r * math.cos(self.angle)
        self.y = self.cy + self.orbit_r * math.sin(self.angle)


        self.ptimer += 1
        if self.ptimer >= self.prate:
            self.ptimer = 0
            hand_x = self.x + self.w * 0.72
            hand_y = self.y + self.h * 0.28
            self.particles.append(Particle(hand_x, hand_y, self.particle_colour))

        # disabling dead particles
        for p in self.particles:
            p.update()
        self.particles = [p for p in self.particles if p.alive()] #didn't work with just p.alive] so changed it to p.alive()]

    def draw(self, screen):
        """drawing particles, Glow-Ring and the charakter."""  # <- AI

        for p in self.particles:
            p.draw(screen)

        # Pulsierender Glow-Ring <- Ai
        pulse   = math.sin(pygame.time.get_ticks() * 0.001 * 60 * self.pulse_speed + self.pulse_phase)
        glow_r  = int(self.w * 0.55 + pulse * 8)
        gsurf   = pygame.Surface((glow_r * 2, glow_r * 2), pygame.SRCALPHA)
        pygame.draw.circle(gsurf, (*self.tint_colour, 35), (glow_r, glow_r), glow_r)
        cx_px   = int(self.x + self.w / 2)
        cy_px   = int(self.y + self.h / 2)
        screen.blit(gsurf, (cx_px - glow_r, cy_px - glow_r))  # <- from Snippet: blit

        # Charakter-Sprite from Snippet aka dino.py
        # blit = copy image to screen at a specific location (afrom dino.py Snippet-Kommentar)
        screen.blit(self.image, (int(self.x), int(self.y)))

    def draw_orbit(self, screen):
        """drawing the circle path (debugging / O-Taste)."""  # <- AI
        pygame.draw.circle(screen, (*self.tint_colour, 40),
                           (int(self.cx), int(self.cy)), self.orbit_r, 1)

#stars made from Ai for the background
def make_stars(n=120):
    """Erstellt eine Liste zufälliger Sterne: (x, y, radius, basis-alpha)."""
    return [(random.randint(0, SCREEN_WIDTH),
             random.randint(0, SCREEN_HEIGHT),
             random.randint(1, 3),
             random.randint(80, 200)) for _ in range(n)]


def draw_background(screen, stars, tick):
    screen.fill(BACKGROUND_COLOR)  # ← aus Snippet: screen.fill mit Hintergrundfarbe

    for sx, sy, sr, base_a in stars:
        # Twinkle-Effect  <- AI
        alpha = max(60, min(255, int(base_a + 55 * math.sin(tick * 0.002 + sx))))
        surf = pygame.Surface((sr * 2, sr * 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, (255, 255, 255, alpha), (sr, sr), sr)
        screen.blit(surf, (sx - sr, sy - sr))  # ← aus Snippet: blit


def main():
    # activate the pygame library  <- from the Code-Snippet
    pygame.init()

    # create the display surface object of specific dimension  <- Snippet
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # set the pygame window name  <- Snippet
    pygame.display.set_caption("World of Shanren – Rose Swordmage")

    # Bild loading from the Snippet
    # use convert_alpha() for png images  <- Snippet-comment
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "character2.png")
    if not os.path.exists(image_path):
        print(f"FEHLER: Bild nicht gefunden → {image_path}")
        sys.exit(1)
    RoseSwordmage.load_image(image_path, height=160)

    # every instanz is a 50/50 between me and Ai, got bored in the middle that is why
    TINTS = [(255, 100, 150), (200, 100, 255), (255, 80, 80), (100, 180, 255), (255, 200, 80)]
    PCOLS = [(255, 80, 130), (180, 80, 255), (255, 60, 60), (80, 160, 255), (255, 180, 50)]
    characters = [
        RoseSwordmage(TINTS[i], PCOLS[i], i)
        for i in range(5)
    ]

    stars = make_stars(140)

    #HUD quickly with AI
    font_big = pygame.font.SysFont("consolas", 22, bold=True)
    font_small = pygame.font.SysFont("consolas", 14)

    show_orbits = False  # O-Taste

    # Init the clock  <- from the Code-Snippet
    clock = pygame.time.Clock()

    tick = 0
    flag = True  # <- from the Code-Snippet: flag steuert die Hauptschleife

    while flag:

        # ticking the clock  <-  Code-Snippet
        clock.tick(60)

        tick += 1  # <- AI: is needed for the flickering effect

    # events from the code snippet
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False  # <- Code-Snipped

            #Keyboard Ai
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    flag = False
                if event.key == pygame.K_o:
                    show_orbits = not show_orbits  # toggeling circle path on and off

        # Alle Charaktere auf ihrer Kreisbahn weiterbewegen
        for ch in characters:
            ch.update()

        # drawing is from the Snippet
        # paint the screen with background color  <- Snippet-Kommentar
        draw_background(screen, stars, tick)  # enthält screen.fill  <-Snippet

        # Orbit toggling  <- AI
        if show_orbits:
            for ch in characters:
                ch.draw_orbit(screen)

        # Using blit to copy image to screen  <- from Snippet-Kommentar
        for ch in characters:
            ch.draw(screen)  # intern: screen.blit(self.image, ...)  <- Snippet

        # HUD made by AI
        screen.blit(font_big.render("World of Shanren", True, (255, 150, 200)), (20, 15))
        screen.blit(font_small.render("O = Orbits anzeigen  |  ESC = Beenden", True, (160, 130, 160)),
                    (20, SCREEN_HEIGHT - 28))

        # refresh the display  <- aus dem Code-Snippet
        pygame.display.flip()

    # closing from the Snippet
    pygame.quit()
    exit(0)


if __name__ == "__main__":
    main()