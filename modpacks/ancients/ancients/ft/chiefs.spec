[spec]

; Format and options of this spec file:
options = "+spec3"

[info]

artists = "
    Falk Hueffner <falk.hueffner@student.uni-tuebingen.de>
    Jeff Mallatt <jjm@codewell.com> (occupation indicator)
    Franz Mach <ft@uliq.net> (Modifications for use with ft-Tileset)
"

[file]
gfx = "ancients/ft/chiefs"

[grid_main]

x_top_left = 1
y_top_left = 39
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"

; Unit hit-point bars: approx percent of hp remaining
0,  0, "unit.hp_100"
0,  1, "unit.hp_90"
0,  2, "unit.hp_80"
0,  3, "unit.hp_70"
0,  4, "unit.hp_60"
0,  5, "unit.hp_50"
1,  0, "unit.hp_40"
1,  1, "unit.hp_30"
1,  2, "unit.hp_20"
1,  3, "unit.hp_10"
1,  4, "unit.hp_0"

}

