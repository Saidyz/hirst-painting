import colorgram
import turtle as tt
import random

colors = colorgram.extract('image.jpg', 20)  #returns Color objects

colors_list = []
def extrat_color():
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb = (r, g ,b )
        colors_list.append(rgb)
extrat_color()  # the function is just for generating colors from the image using the colorgram packg..
# print(colors_list)  

colors_list =[ (237, 37, 114), (144, 26, 67), (238, 71, 36), (221, 163, 55), (15, 140, 88), (175, 163, 48), (32, 122, 187), (50, 189, 228), (172, 44, 94), (242, 219, 56), (80, 24, 74), (127, 190, 92), (12, 224, 0), (23, 171, 123), (191, 67, 40), (206, 132, 164)]
print(random.choice(colors_list))
tt.colormode(255)

sido = tt.Turtle()
sido.penup()


def drawing_dotted_line():
    """"""
    for _ in range(10):
        color = random.choice(colors_list)
        sido.color(color)
        sido.dot(20,color)
        sido.fd(50)

def spot():
    """"""
    pass

x0 = -250
y0 = -300

for s in range(10):
    sido.teleport(y0, x0)
    drawing_dotted_line()
    x0+=50









screen = tt.Screen()
screen.exitonclick()