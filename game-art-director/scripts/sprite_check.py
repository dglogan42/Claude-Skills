#!/usr/bin/env python3
"""usage: sprite_check.py sheet.png TILE [palette.txt (one hex per line)]"""
import sys as _s
if len(_s.argv)>1 and _s.argv[1] in ('-h','--help') or (len(_s.argv)<2 and False):
    print('Usage: python sprite_check.py IMAGE TILE_PX [palette.txt]'); _s.exit(0)
import sys
from PIL import Image
img=Image.open(sys.argv[1]).convert("RGBA"); t=int(sys.argv[2]); W,H=img.size
pal=None
if len(sys.argv)>3:
    pal={l.strip().lstrip('#').lower() for l in open(sys.argv[3]) if l.strip()}
issues=0
if W%t or H%t: print(f"GRID: sheet {W}x{H} not a multiple of {t}"); issues+=1
px=img.load(); off={}; semi=0
for y in range(H):
    for x in range(W):
        r,g,b,a=px[x,y]
        if 0<a<255: semi+=1
        if a and pal is not None:
            h=f"{r:02x}{g:02x}{b:02x}"
            if h not in pal: off[h]=off.get(h,0)+1
if semi: print(f"ALPHA: {semi} semi-transparent pixels"); issues+=1
if off: print(f"PALETTE: {len(off)} off-palette colours, e.g. {sorted(off,key=off.get)[-5:]}"); issues+=1
print(f"tiles: {W//t}x{H//t}; issues: {issues}"); sys.exit(1 if issues else 0)
