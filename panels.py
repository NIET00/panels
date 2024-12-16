# TIMES PANEL FITS IN CASE BEFORE AND AFTER ROTATION
def get_fits(x,y,a,b):
    return(max(times_panel_fits(x,y,a,b), times_panel_fits(x,y,b,a,True)))


def times_panel_fits(roofX, roofY, panelX, panelY, rotate_panel=False):
    # TIMES PANEL FITS WITHOUT ROTATION
    vertical_fit = roofY // panelY
    horizontal_fit = roofX // panelX
    first_fit = vertical_fit * horizontal_fit

    # CALCULATE REMAINING SPACE
    if not rotate_panel:
        rem = roofX % panelX
    else:
        rem = roofY % panelY

    # TIMES PANEL FITS IN REMAINING SPACE
    rotated_horizontal_fit = rem // panelY
    rotated_vertical_fit = roofY // panelX
    second_fit = rotated_horizontal_fit * rotated_vertical_fit

    return first_fit + second_fit

# GET SIZE OF ROOF AND PANELS
while True:
    try:
        x, y = sorted(map(float, input("Enter the roof size, separated by a space (e.g. 3 5): ").split()), reverse=True)
        a, b = sorted(map(float, input("Enter the panel size, separated by a space (e.g. 3 5): ").split()), reverse=True)
        if x > 0 and y >0 and a > 0 and b > 0:
            break
        else:
            print("Make sure the size of the roof and panels are positive values.")
    except Exception as e:
        print("Make sure you enter two numbers separated by a space.")

print(get_fits(x,y,a,b))
