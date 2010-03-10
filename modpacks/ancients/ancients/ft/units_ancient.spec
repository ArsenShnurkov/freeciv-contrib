[spec]

; Format and options of this spec file:
options = "+spec3"

[info]

artists = "
    The tiles were crudely hacked from the HiRes Civ II Modpack
    of Tim Smith by F. Mach
    Submissions of improved tiles will be welcome!
    <ft@uliq.net>
"

[file]
gfx = "ancients/ft/units_ancient"

[grid_main]

x_top_left = 1
y_top_left = 39
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"

  0,  0, "u.militia"
  0,  1, "u.levy"
  0,  2, "u.skirmishers"
  0,  3, "u.archers"
  0,  4, "u.spearphalanx"
  0,  5, "u.pikephalanx"
  0,  6, "u.legionaires"
  0,  7, "u.auxiliaries"
  0,  8, "u.marines"
  0,  9, "u.guerillas"
  
  1,  0, "u.warband"
  1,  1, "u.men_at_arms"
  1,  2, "u.halberdiers"
;  0, 13, "u.blank" (removed, dont know what this should be?!)
  1,  3, "u.settlers"
  1,  4, "u.worker"
  1,  5, "u.lightcavalry"
;  1,  6, "u.hunne-archers" (currently unused)
  1,  7, "u.heavycavalry"
; 1,  8, "u.early_knights" (currently unused)  
  1,  9, "u.knights"
  
  2,  0, "u.cataphracts" 
  2,  1, "u.earlylancers"
  2,  2, "u.laterchariots"
; 2,  3, "u.elitechariots" (currently unused)
  2,  4, "u.earlychariots"
  2,  5, "u.elephants"
;  2,  6, "u.elite_elephants" (currently unused)
  2,  7, "u.crusaders"
;  2,  8, "u.diplomat2" (currently unused)
  2,  9, "u.spy"
  
  3,  0, "u.explorer"
  3,  1, "u.diplomat"    
  3,  2, "u.boats"
  3,  3, "u.lighttransport"
  3,  4, "u.heavytransport"
  3,  5, "u.warships"
  3,  6, "u.longboats"
  3,  7, "u.triremes"
;  3,  8, "u.frigate" (currently unused)
;  3,  9, "u.tradeship" (currently unused)

;  4,  0, "u.bishop" (currently unused)
;  4,  1, "u.earlycatapult" (currently unused) 
;  4,  2, "u.ballista" (currently unused)  
  4,  3, "u.catapult"
  4,  4, "u.onager"
;  4,  5, "u.primitivcatapult" (currently unused)
  4,  6, "u.fanatics"
  4,  7, "u.caravan"
  4,  8, "u.freight"
;  4,  9, "u.roman" (currently unused)
}
