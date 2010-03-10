
[spec]

; Format and options of this spec file:
options = "+spec3"

[info]

artists = "
    Tim F. Smith <yoohootim@hotmail.com>
    Franz Mach <ft@uliq.net>
"

[file]
gfx = "ancients/ft/dither"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 32
pixel_border = 1

tiles = { "row", "column","tag"
  0,    2,  "t.multi_dither_tile_0x0"
  1,    1,  "t.multi_dither_tile_0x1"
  2,    0,  "t.multi_dither_tile_0x2"
  1,    3,  "t.multi_dither_tile_1x0"
  2,    2,  "t.multi_dither_tile_1x1"
  3,    1,  "t.multi_dither_tile_1x2"
  2,    4,  "t.multi_dither_tile_2x0"
  3,    3,  "t.multi_dither_tile_2x1"
  4,    2,  "t.multi_dither_tile_2x2"
  
  1,    0,  "tx.darkness_nw"
  2,    1,  "tx.darkness_w"
  3,    0,  "tx.darkness_sw"
  3,    2,  "tx.darkness_s"
  3,    4,  "tx.darkness_se"
  2,    3,  "tx.darkness_e"
  1,    4,  "tx.darkness_ne"
  1,    2,  "tx.darkness_n"
}

