from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].replace('\n', '')
    for i in range(len(lines)):
        #add line to edge matrix
        if ((lines[i]) == 'line'):
            p = (lines[i+1]).split(' ')
            for j in range(len(p)):
                p[j] = int(p[j].strip())
            add_edge(points, p[0], p[1], p[2], p[3], p[4], p[5])
        #make transformation matrix into an identity matrix
        elif ((lines[i]) == 'ident'):
            ident(transform)
        #make transformation matrix into scale matrix and then scales the points
        elif ((lines[i]) == 'scale'):
            factors = (lines[i+1]).split(' ')
            for j in range(len(factors)):
                factors[j] = int(factors[j].strip())
            print(factors)
            s = make_scale(factors[0], factors[1], factors[2])
            matrix_mult(s, transform)
        #make transformation matrix into translate matrix and then translates the points
        elif ((lines[i]) == 'move'):
            nums = (lines[i+1]).split(' ')
            for j in range(len(nums)):
                nums[j] = int(nums[j].strip())
            t = make_translate(nums[0], nums[1], nums[2])
            matrix_mult(t, transform)
        #make transformation matrix into rotation matrix and then rotates the points
        elif ((lines[i]) == 'rotate'):
            rotations = (lines[i+1]).split(' ')
            axis = rotations[0]
            angle = int(rotations[1].strip())
            if (axis == 'x'):
                matrix_mult(make_rotX(angle), transform)
            elif (axis == 'y'):
                matrix_mult(make_rotY(angle), transform)
            else:
                matrix_mult(make_rotZ(angle), transform)
        #multiplies the tranformation matrix with the edge matrix
        elif ((lines[i]) == 'apply'):
            matrix_mult(transform, points)
        elif ((lines[i]) == 'display'):
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif ((lines[i]) == 'save'):
            fileName = (lines[i+1]).strip()
            save_extension(screen, fileName)
        elif ((lines[i]) == 'quit'):
            break
