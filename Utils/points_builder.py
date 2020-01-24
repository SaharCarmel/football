import matplotlib.pyplot as plt
import matplotlib as mlb
import numpy as np

def castYtofield(y):
    return (y/100)

def castXtofield(x):
    return x/60

fig = plt.figure()
x = np.array([-1 , 1])
y = np.array([-0.45, 0.45])
# plt.scatter(x,y)
plt.vlines(castXtofield(60-16.5), ymax=0.2, ymin=-0.2)
plt.vlines(castXtofield(-60+16.5), ymax=0.2, ymin=-0.2)
# 16 meter
plt.hlines(0.2, castXtofield(-60), castXtofield(-60+16.5))
plt.hlines(-0.2, castXtofield(-60), castXtofield(-60+16.5))
plt.hlines(0.2, castXtofield(60), castXtofield(60-16.5))
plt.hlines(-0.2, castXtofield(60), castXtofield(60-16.5))
## inner
plt.vlines(castXtofield(60-5.5), castYtofield(7.32/2+5.5), castYtofield(-7.32/2-5.5))
plt.vlines(castXtofield(-60+5.5), castYtofield(7.32/2+5.5), castYtofield(-7.32/2-5.5))
plt.hlines(castYtofield(7.32/2+5.5), castXtofield(-60), castXtofield(-60+5.5))
plt.hlines(-castYtofield(7.32/2+5.5), castXtofield(-60), castXtofield(-60+5.5))
plt.hlines(castYtofield(7.32/2+5.5), castXtofield(60), castXtofield(60-5.5))
plt.hlines(-castYtofield(7.32/2+5.5), castXtofield(60), castXtofield(60-5.5))
# Boundries
plt.hlines(-0.45,1,-1)
plt.hlines(0.45,1,-1)
plt.vlines(1,0.45,-0.45)
plt.vlines(0,0.45,-0.45)
plt.vlines(-1,0.45,-0.45)
# plt.grid()
points = plt.ginput(3, show_clicks=True)
print(points)
plt.show()