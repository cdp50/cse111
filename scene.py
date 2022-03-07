# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    
    
    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_grid(canvas, width, height, interval, color="white"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="sky blue")
    draw_oval(canvas, 200, 450, 100, 400, width=0, fill="white")
    draw_oval(canvas, 550, 400, 450, 350, width=0, fill="white")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0, scene_width, scene_height * 2 / 3, width=0, fill="darkOrange2")
    draw_polygon(canvas,0, 100, 800, 100, 400, scene_height * 2 / 3, width=0, fill="gray25")
    draw_rectangle(canvas, 0, 0, scene_width, 100, width=0, fill="gray25")
    draw_polygon(canvas,365, 0, 390, 0, 400, scene_height * 2 / 3, width=0, fill="goldenrod1")
    draw_polygon(canvas,410, 0, 435, 0, 400, scene_height * 2 / 3, width=0, fill="goldenrod1")


# Call the main function so that
# this program will start executing.
main()