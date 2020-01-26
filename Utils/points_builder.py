import matplotlib.pyplot as plt
import matplotlib as mlb
import numpy as np

def castYtofield(y):
    return (y/100)

def castXtofield(x):
    return x/60

def plotField():
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
    return fig


## getting attackers
attacking_players = int(input("Num of attacking players: "))
defending_players = int(input("Num of defending players: "))
fig = plotField()
plt.title("Place attackers")
attacking_points = plt.ginput(attacking_players, show_clicks=True)
attacking_points = np.array(attacking_points).transpose()
plt.close()

## getting defenders
fig = plotField()
plt.title("Place defenders")
plt.scatter(attacking_points[0], attacking_points[1], marker="+", c="blue")
defending_points = plt.ginput(defending_players, show_clicks=True)
defending_points = np.array(defending_points).transpose()
plt.close()

## getting ball
fig = plotField()
plt.title("Place ball")
plt.scatter(attacking_points[0], attacking_points[1], marker="+", c="blue")
plt.scatter(defending_points[0], defending_points[1], marker="_", c="red")
ball_point = plt.ginput(1, show_clicks=True)

plt.close()
fig = plotField()
plt.scatter(attacking_points[0], attacking_points[1], marker="+", c="blue")
plt.scatter(defending_points[0], defending_points[1], marker="_", c="red")
plt.scatter(ball_point[0][0], ball_point[0][1], marker="o", c="green")
plt.show()
fig.savefig("corner_2_vs_1_keeper.jpg")


print("Ball")
print("builder.SetBallPosition({:.4f}, {:.4f})".format(ball_point[0][0],ball_point[0][1]))

def_roles = ["GK", "LB", "CB", "RB"]
atk_roles = ["LM", "CM", "RM", "CF"]
print("Defending team")
for item, role in zip(defending_points.transpose(), def_roles):
    print("builder.AddPlayer({:.4f}, {:.4f}, e_PlayerRole_{})".format(item[0], item[1], role))

print("Attacking team")
for item, role in zip(attacking_points.transpose(), atk_roles):
    print("builder.AddPlayer({:.4f}, {:.4f}, e_PlayerRole_{})".format(item[0], item[1], role))


