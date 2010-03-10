
[spec]

; Format and options of this spec file:
options = "+spec3"

[info]

artists = "
    Tatu Rissanen <tatu.rissanen@hut.fi>
    Jeff Mallatt <jjm@codewell.com> (miscellaneous)
    Franz Mach <ft@uliq.net> (Modifications for using with the ft-Tiles)
"

[file]
gfx = "ancients/ft/tiles"

[grid_main]

x_top_left = 1
y_top_left = 39
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
; Unit activity letters:  (note unit icons have just "u.")

  1,  8, "unit.auto_attack", "unit.auto_settler"
  2,  9, "unit.stack"
  2,  3, "unit.connect"
  1,  9, "unit.auto_explore"

  0,  3, "unit.transform"
  0,  4, "unit.sentry"
  0,  5, "unit.goto"
  0,  6, "unit.mine"
  0,  7, "unit.pollution"
  0,  8, "unit.road"
  0,  9, "unit.irrigate"

  1,  3, "unit.fortifying", "unit.fortress"
  1,  4, "unit.airbase"
  1,  5, "unit.pillage"
  3,  9, "unit.fortified"
  1,  6, "unit.fallout"
  1,  7, "unit.patrol"
 
  0, 10, "unit.loaded" 
  3, 10, "unit.lowfuel"
  4, 10, "unit.tired"

; Unit hit-point bars: approx percent of hp remaining
; -> in "chiefs.spec"

; Numbers: city size:

  4,  0, "city.size_0"
  4,  1, "city.size_1"
  4,  2, "city.size_2"
  4,  3, "city.size_3"
  4,  4, "city.size_4"
  4,  5, "city.size_5"
  4,  6, "city.size_6"
  4,  7, "city.size_7"
  4,  8, "city.size_8"
  4,  9, "city.size_9"
  5,  1, "city.size_10"
  5,  2, "city.size_20"
  5,  3, "city.size_30"
  5,  4, "city.size_40"
  5,  5, "city.size_50"
  5,  6, "city.size_60"
  5,  7, "city.size_70"
  5,  8, "city.size_80"
  5,  9, "city.size_90"

; Numbers: city tile food/shields/trade y/g/b

  6,  0, "city.t_food_0"
  6,  1, "city.t_food_1"
  6,  2, "city.t_food_2"
  6,  3, "city.t_food_3"
  6,  4, "city.t_food_4"
  6,  5, "city.t_food_5"
  6,  6, "city.t_food_6"
  6,  7, "city.t_food_7"
  6,  8, "city.t_food_8"
  6,  9, "city.t_food_9"

  7,  0, "city.t_shields_0"
  7,  1, "city.t_shields_1"
  7,  2, "city.t_shields_2"
  7,  3, "city.t_shields_3"
  7,  4, "city.t_shields_4"
  7,  5, "city.t_shields_5"
  7,  6, "city.t_shields_6"
  7,  7, "city.t_shields_7"
  7,  8, "city.t_shields_8"
  7,  9, "city.t_shields_9"

  8,  0, "city.t_trade_0"
  8,  1, "city.t_trade_1"
  8,  2, "city.t_trade_2"
  8,  3, "city.t_trade_3"
  8,  4, "city.t_trade_4"
  8,  5, "city.t_trade_5"
  8,  6, "city.t_trade_6"
  8,  7, "city.t_trade_7"
  8,  8, "city.t_trade_8"
  8,  9, "city.t_trade_9"

; Unit upkeep in city dialog:
; These should probably be handled differently and have
; a different size...

  2,  4, "upkeep.food"
  2,  5, "upkeep.food2"
  2,  6, "upkeep.unhappy"
  2,  7, "upkeep.unhappy2"
  2,  8, "upkeep.shield"
  1, 10, "upkeep.gold"
  2, 10, "upkeep.gold2"
}

[grid_explode]

x_top_left = 1
y_top_left = 39
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
  3,  0, "explode.unit_0"
  3,  1, "explode.unit_1"
  3,  2, "explode.unit_2"
  3,  3, "explode.unit_3"
  3,  4, "explode.unit_4"
  3,  5, "explode.unit_5"
  3,  6, "explode.unit_6"
  3,  7, "explode.unit_7"
}

[grid_nuke]
x_top_left = 1
y_top_left = 39
dx = 192
dy = 144
pixel_border = 0

tiles = { "row", "column", "tag"
0, 0, "explode.nuke"
}
