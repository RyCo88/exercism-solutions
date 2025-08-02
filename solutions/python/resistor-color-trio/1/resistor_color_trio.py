def label(colors):
    color_code = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    if colors[2] == 'black':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + ' ohms'
    if colors[2] == 'brown':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + '0 ohms'
    if colors[2] == 'red':
        resist_number = str(color_code.index(colors[0]))
        return str(int(resist_number)) + ' kiloohms'
    if colors[2] == 'orange':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + ' kiloohms'
    if colors[2] == 'yellow':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + '0 kiloohms'
    if colors[2] == 'green':
        resist_number = str(color_code.index(colors[0]))
        return str(int(resist_number)) + ' megaohms'
    if colors[2] == 'blue':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + ' megaohms'
    if colors[2] == 'violet':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + '0 megaohms'
    if colors[2] == 'grey':
        resist_number = str(color_code.index(colors[0]))
        return str(int(resist_number)) + ' gigaohms'
    if colors[2] == 'white':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + ' gigaohms'