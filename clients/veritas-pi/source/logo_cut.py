# Cut a logo off a white background, keeping gold fully opaque. Usage: logo_cut.py in.png out.png [dark]
import sys
from PIL import Image
import numpy as np
a=np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(float)
al=np.clip(((255-a.min(axis=2))/255.0-0.06)*1.7,0,1)
safe=np.maximum(al,1e-3)[...,None]
c=np.clip((a-255*(1-safe))/safe,0,255)
arr=np.dstack([c,al*255])
im=Image.fromarray(arr.astype(np.uint8),'RGBA'); bb=im.getchannel('A').point(lambda v:255 if v>24 else 0).getbbox()
arr=arr[bb[1]:bb[3],bb[0]:bb[2]]
if len(sys.argv)>3:   # dark-background version: navy lettering right of the gold divider becomes off-white
    H,W,_=arr.shape; r,g,b,A=[arr[...,i] for i in range(4)]
    gold=(r>150)&(b<120)&(A>150); div=int(np.argmax(gold.sum(axis=0)[:W//2]))
    navy=(b>=r-5)&(r<120)&(np.arange(W)[None,:]>div+4)
    arr[navy,0:3]=[246,244,238]
Image.fromarray(arr.astype(np.uint8),'RGBA').save(sys.argv[2])
