"""

GAGFEC

CGC

1st four are 1/2

"""

def on_button_pressed_a():
    music.change_tempo_by(120)
    for index in range(2):
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
    for index2 in range(2):
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.DOUBLE))
    for index3 in range(2):
        music.play_tone(392, music.beat(BeatFraction.HALF))
        music.play_tone(440, music.beat(BeatFraction.HALF))
        music.play_tone(392, music.beat(BeatFraction.HALF))
        music.play_tone(349, music.beat(BeatFraction.HALF))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
    for index4 in range(2):
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(196, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)
