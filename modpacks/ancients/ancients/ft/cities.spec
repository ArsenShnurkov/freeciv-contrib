
; The names for city tiles are not free and must follow the following rules.
; The names consists of style name, _ , size. The style name is as specified
; in cities.ruleset file. The size indicates which size city must
; have to be drawn with a tile. E.g. european_4 means that the tile is to be
; used for cities of size 4+ in european style. Obviously the first tile
; must be style_name_0. The sizes must be in ascending order.
; There must also be a style_name_wall tile used to draw the wall and
; an occupied tile to indicate a miltary units in a city.
; The maximum size supported now is 31, but there can only be MAX_CITY_TILES
; normal tiles. The constant is defined in common/city.h and set to 8 now.
;

[spec]

; Format and options of this spec file:
options = "+spec3"

[info]

artists = "
    Franz Mach <ft@uliq.net>
"

[file]
gfx = "ancients/ft/cities"

[grid_main]

x_top_left = 1
y_top_left = 50
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"

; default tiles

 1,  2, "cd.city"

; used by all city styles

12,  3, "city.disorder"
;12, 4, "city.disorder"

;
; city tiles
;

 0,  0, "city.precolumbian_city_0"
 0,  1, "city.precolumbian_city_3"
 0,  2, "city.precolumbian_city_5"
 0,  3, "city.precolumbian_city_8"
 0,  4, "city.precolumbian_city_12"

 1,  0, "city.classical_city_0"
 1,  1, "city.classical_city_3"
 1,  2, "city.classical_city_5"
 1,  3, "city.classical_city_8"
 1,  4, "city.classical_city_12"

 2,  0, "city.asian_city_0"
 2,  1, "city.asian_city_3"
 2,  2, "city.asian_city_5"
 2,  3, "city.asian_city_8"
 2,  4, "city.asian_city_12"

 3,  0, "city.european_city_0"
 3,  1, "city.european_city_3"
 3,  2, "city.european_city_5"
 3,  3, "city.european_city_8"
 3,  4, "city.european_city_12"

 4,  0, "city.babylonian_city_0"
 4,  1, "city.babylonian_city_3"
 4,  2, "city.babylonian_city_5"
 4,  3, "city.babylonian_city_8"
 4,  4, "city.babylonian_city_12"

 5,  0, "city.arabian_city_0"
 5,  1, "city.arabian_city_3"
 5,  2, "city.arabian_city_5"
 5,  3, "city.arabian_city_8"
 5,  4, "city.arabian_city_12"

 6,  0, "city.african_city_0"
 6,  1, "city.african_city_3"
 6,  2, "city.african_city_5"
 6,  3, "city.african_city_8"
 6,  4, "city.african_city_12"

 7,  0, "city.industrial_city_0"
 7,  1, "city.industrial_city_3"
 7,  2, "city.industrial_city_5"
 7,  3, "city.industrial_city_8"
 7,  4, "city.industrial_city_12"

 8,  0, "city.modern_city_0"
 8,  1, "city.modern_city_3"
 8,  2, "city.modern_city_5"
 8,  3, "city.modern_city_8"
 8,  4, "city.modern_city_12"

 9,  0, "city.postmodern_city_0"
 9,  1, "city.postmodern_city_3"
 9,  2, "city.postmodern_city_5"
 9,  3, "city.postmodern_city_8"
 9,  4, "city.postmodern_city_12"

10,  0, "city.asiaminor_city_0"
10,  1, "city.asiaminor_city_3"
10,  1, "city.asiaminor_city_5"
10,  1, "city.asiaminor_city_8"
10,  1, "city.asiaminor_city_12"

10,  2, "city.minor_city_0"
10,  3, "city.minor_city_3"
10,  3, "city.minor_city_5"
10,  3, "city.minor_city_8"
10,  3, "city.minor_city_12"

10,  4, "city.minorhill_city_0"
10,  4, "city.minorhill_city_3"
10,  4, "city.minorhill_city_5"
10,  4, "city.minorhill_city_8"
10,  4, "city.minorhill_city_12"

11,  0, "city.celtic_city_0"
11,  1, "city.celtic_city_3"
11,  2, "city.celtic_city_5"
11,  3, "city.celtic_city_8"
11,  4, "city.celtic_city_12"

10,  0, "city.tropical_city_0"
11,  1, "city.tropical_city_3"
11,  2, "city.tropical_city_5"
11,  3, "city.tropical_city_8"
11,  4, "city.tropical_city_12"

}

[grid_specials]

x_top_left = 375
y_top_left = 675
dx = 64
dy = 60
pixel_border = 1

tiles = { "row", "column", "tag"

 0, 0, "tx.fortress_back"
 0, 1, "tx.fortress"
 0, 2, "tx.airbase"
 0, 3, "tx.airbase_full"
}

[grid_flags]

x_top_left = 408
y_top_left = 640
dx = 14
dy = 33
pixel_border = 1

tiles = { "row", "column", "tag"

 0, 0, "city.precolumbian_occupied_0"
 0, 1, "city.celtic_occupied_0"
 0, 2, "city.babylonian_occupied_0"
 0, 3, "city.classical_occupied_0"
 0, 4, "city.asian_occupied_0", "city.tropical_occupied_0"
 0, 5, "city.arabian_occupied_0"
 0, 6, "city.european_occupied_0"
 0, 7, "city.african_occupied_0"
 0, 8, "city.industrial_occupied_0", "city.modern_occupied_0"
 0, 9, "city.minor_occupied_0"
 0,10, "city.minorhill_occupied_0"
 0,11, "city.asiaminor_occupied_0"
 0,12, "city.postmodern_occupied_0"
}

[grid_walls]

x_top_left = 375
y_top_left = 50
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"

; city tiles

 0,  0, "city.precolumbian_wall_0"
 0,  1, "city.precolumbian_wall_3"
 0,  2, "city.precolumbian_wall_5"
 0,  3, "city.precolumbian_wall_8"
 0,  4, "city.precolumbian_wall_12"

 1,  0, "city.classical_wall_0"
 1,  1, "city.classical_wall_3"
 1,  2, "city.classical_wall_5"
 1,  3, "city.classical_wall_8"
 1,  4, "city.classical_wall_12"

 2,  0, "city.asian_wall_0"
 2,  1, "city.asian_wall_3"
 2,  2, "city.asian_wall_5"
 2,  3, "city.asian_wall_8"
 2,  4, "city.asian_wall_12"

 3,  0, "city.european_wall_0"
 3,  1, "city.european_wall_3"
 3,  2, "city.european_wall_5"
 3,  3, "city.european_wall_8"
 3,  4, "city.european_wall_12"

 4,  0, "city.babylonian_wall_0"
 4,  1, "city.babylonian_wall_3"
 4,  2, "city.babylonian_wall_5"
 4,  3, "city.babylonian_wall_8"
 4,  4, "city.babylonian_wall_12"

 5,  0, "city.arabian_wall_0"
 5,  1, "city.arabian_wall_3"
 5,  2, "city.arabian_wall_5"
 5,  3, "city.arabian_wall_8"
 5,  4, "city.arabian_wall_12"

 6,  0, "city.african_wall_0"
 6,  1, "city.african_wall_3"
 6,  2, "city.african_wall_5"
 6,  3, "city.african_wall_8"
 6,  4, "city.african_wall_12"

 7,  0, "city.industrial_wall_0"
 7,  1, "city.industrial_wall_3"
 7,  2, "city.industrial_wall_5"
 7,  3, "city.industrial_wall_8"
 7,  4, "city.industrial_wall_12"

 8,  0, "city.modern_wall_0"
 8,  1, "city.modern_wall_3"
 8,  2, "city.modern_wall_5"
 8,  3, "city.modern_wall_8"
 8,  4, "city.modern_wall_12"

 9,  0, "city.postmodern_wall_0"
 9,  1, "city.postmodern_wall_3"
 9,  2, "city.postmodern_wall_5"
 9,  3, "city.postmodern_wall_8"
 9,  4, "city.postmodern_wall_12"

10,  0, "city.asiaminor_wall_0"
10,  1, "city.asiaminor_wall_3"
10,  1, "city.asiaminor_wall_5"
10,  1, "city.asiaminor_wall_8"
10,  1, "city.asiaminor_wall_12"

10,  2, "city.minor_wall_0"
10,  3, "city.minor_wall_3"
10,  3, "city.minor_wall_5"
10,  3, "city.minor_wall_8"
10,  3, "city.minor_wall_12"

10,  4, "city.minorhill_wall_0"
10,  4, "city.minorhill_wall_3"
10,  4, "city.minorhill_wall_5"
10,  4, "city.minorhill_wall_8"
10,  4, "city.minorhill_wall_12"

11,  0, "city.celtic_wall_0"
11,  1, "city.celtic_wall_3"
11,  2, "city.celtic_wall_5"
11,  3, "city.celtic_wall_8"
11,  4, "city.celtic_wall_12"

10,  0, "city.tropical_wall_0"
11,  1, "city.tropical_wall_3"
11,  2, "city.tropical_wall_5"
11,  3, "city.tropical_wall_8"
11,  4, "city.tropical_wall_12"

}

