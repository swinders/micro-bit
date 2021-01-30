// GAGFEC
// 
// CGC
// 
// 1st four are 1/2
input.onButtonPressed(Button.A, function () {
    music.changeTempoBy(120)
    for (let index = 0; index < 2; index++) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.playTone(294, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(262, music.beat(BeatFraction.Whole))
    }
    for (let index = 0; index < 2; index++) {
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(349, music.beat(BeatFraction.Whole))
        music.playTone(392, music.beat(BeatFraction.Double))
    }
    for (let index = 0; index < 2; index++) {
        music.playTone(392, music.beat(BeatFraction.Half))
        music.playTone(440, music.beat(BeatFraction.Half))
        music.playTone(392, music.beat(BeatFraction.Half))
        music.playTone(349, music.beat(BeatFraction.Half))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(262, music.beat(BeatFraction.Whole))
    }
    for (let index = 0; index < 2; index++) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.playTone(196, music.beat(BeatFraction.Whole))
        music.playTone(262, music.beat(BeatFraction.Whole))
    }
})
