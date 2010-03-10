
[spec]

; Format and options of this spec file:
options = "+spec3"

[info]

artists = "
    Tim F. Smith <yoohootim@hotmail.com>
    Daniel Speyer <dspeyer@users.sf.net>
    Franz Mach <ft@uliq.net>
"

[file]
gfx = "ancients/ft/terrain1"

[grid_main]

x_top_left = 1
y_top_left = 39
dx = 64
dy = 32
pixel_border = 1

tiles = { "row", "column","tag"

; terrain
  0,    0, "t.desert1"
  0,    1, "t.desert2"
  1,    0, "t.plains1"
  1,    1, "t.plains2"
  2,    0, "t.grassland1"
  2,    1, "t.grassland2"
  3,    0, "t.forest1"
  3,    1, "t.forest2"
  4,    0, "t.hills1"
  4,    1, "t.hills2"
  5,    0, "t.mountains1"
  5,    1, "t.mountains2"
  6,    0, "t.tundra1"
  7,    0, "t.arctic1"
  8,    0, "t.swamp1"
  9,    0, "t.jungle1"
  10,   0, "t.ocean1"

; Terrain special resources:

 0,   2, "ts.oasis"
 0,   3, "ts.oil"
 1,   2, "ts.buffalo"
 1,   3, "ts.wheat"

 7,   4, "ts.grassland_resources", "ts.river_resources"

 3,   2, "ts.pheasant"
 3,   3, "ts.silk"

 4,   2, "ts.coal"
 4,   3, "ts.wine"

 5,   2, "ts.gold"
 5,   3, "ts.iron"

 6,   2, "ts.tundra_game"
 6,   3, "ts.furs"

 7,   2, "ts.arctic_ivory"
 7,   3, "ts.arctic_oil"

 8,   2, "ts.peat"
 8,   3, "ts.spice"

 9,   2, "ts.gems"
 9,   3, "ts.fruit"
 2,   4, "ts.seals"
 9,   5, "ts.forest_game"

 10,  2, "ts.fish"
 10,  3, "ts.whales"
 2,  3, "ts.horses"

;roads
 2, 5, "r.road_n"
 2, 6, "r.road_ne"
 2, 7, "r.road_e"
 4, 5, "r.road_se"
 4, 6, "r.road_s"
 4, 7, "r.road_sw"
 6, 5, "r.road_w"
 6, 6, "r.road_nw"

;rails
 3, 5, "r.rail_n"
 3, 6, "r.rail_ne"
 3, 7, "r.rail_e"
 5, 5, "r.rail_se"
 5, 6, "r.rail_s"
 5, 7, "r.rail_sw"
 7, 5, "r.rail_w"
 7, 6, "r.rail_nw"

 0, 7, "r.road_isolated"
 1, 7, "r.rail_isolated"

;add-ons
 2, 4, "tx.oil_mine"
 4, 4, "tx.farmland"
 3, 4, "tx.irrigation"
 5, 4, "tx.mine"
 6, 4, "tx.pollution"
 8, 4, "tx.village"
 9, 4, "tx.fallout"
 
;extra 
 10, 5, "t.dither_tile"
 10, 5, "tx.darkness"
  9, 5, "tx.fog"
;  9, 6, "t.black_tile"
  9, 6, "mask.tile"
 10, 6, "t.coast_color"

 8, 5, "user.attention"
}
