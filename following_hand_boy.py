from pico2d import *
from random import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND_FULL.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

def handle_events():

    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def draw_all(p1, p2):

    global frame
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    for i in range(0, 100, 5):
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        frame = (frame + 1) % 8

        t = i / 100
        x = (1 - t) * x1 + t * x2   # 1 - t : t 의 비율로 x1, x2를 섞고 더한다
        y = (1 - t) * y1 + t * y2
        if x1 < x2:
            character.clip_draw(frame * 100, 100, 100, 100, x, y, 150, 150)
        elif x2 < x1:
            character.clip_draw(frame * 100, 0, 100, 100, x, y, 150, 150)
        hand_arrow.draw(x2, y2)


        handle_events()
        if not running:
            break

        update_canvas()
        delay(0.08 * t)

hand_points = [(randint(0, 1280), randint(0, 1024)) for i in range(10)]

while running:
    for i in range(0, len(hand_points) - 1):
        draw_all(hand_points[i], hand_points[i + 1])

    handle_events()

close_canvas()
