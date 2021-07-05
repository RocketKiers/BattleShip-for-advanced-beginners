

name = 'rocket'

def render(width_board, height_board, shots):
    header = "+" + "-" * width_board + "+"
    print(header)
    set_shots = set(shots)


    for y in range(height_board):
        row = []
        for x in range(width_board):
            if (x,y) in set_shots:
                ch = "x"
            else:
                ch = " "
            row.append(ch)
        print("|" + "".join(row) + "|")
        #to do: deal with bad input

    print(header)

if name == "rocket":
    shots = []

    while True:
        inp_p1 = input("Where do you want to shoot? example = 4,1 \n")
        xstr,ystr = inp_p1.split(",")
        x = int(xstr)
        y = int(ystr)

        shots.append((x,y))
        render(15,15, shots)