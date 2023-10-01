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
hx, hy = -1, -1
hide_cursor()

def handle_events():

    global running
    global hx, hy
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            hx, hy = event.x, TUK_HEIGHT - 1 - event.y

def draw_hand():
    global hx, hy

    hand_arrow.draw(hx, hy)

def draw_hand_character(px, py):
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, 640, 512)
    hand_arrow.draw(px, py)
    update_canvas()


def draw_all(p1, p2):

    global frame
    global hx, hy

    x1, y1 = hx, hy
    x2, y2 = p1, p2

    for i in range(0, 100, 4):
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

        if not running:
            break

        update_canvas()
        delay(0.05 * t)



while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.draw(x, y)
    frame = (frame + 1) % 8
    character.clip_draw(frame * 100, 0, 100, 100, TUK_WIDTH // 2, TUK_HEIGHT // 2, 150, 150)

    if hx and hy > 0:
        draw_hand()

    update_canvas()
    handle_events()

    if not running:
        break
    delay(0.05)

close_canvas()
