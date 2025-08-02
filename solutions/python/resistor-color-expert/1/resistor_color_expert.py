def resistor_label(colors):
    color_code = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    tolerance = {'grey' : '±0.05%', 'violet' : '±0.1%', 'blue' : '±0.25%', 'green' : '±0.5%', 'brown' : '±1%', 'red' : '±2%', 'gold' : '±5%', 'silver' : '±10%'}
    if len(colors) == 1:
        return str(color_code.index(colors[0])) + ' ohms'
    if len(colors) == 4:
        resistor_number = int(str(color_code.index(colors[0])) + str(color_code.index(colors[1])))
        multiple = 10 ** color_code.index(colors[2])
        resistance = resistor_number * multiple
        if resistance >= 1000000000:
            if resistance / 1000000000 == resistance // 1000000000:
                return str(resistance//1000000000) + ' gigaohms ' + tolerance[colors[-1]]
            return str(resistance/1000000000) + ' gigaohms ' + tolerance[colors[-1]]
        if resistance >= 1000000:
            if resistance / 1000000 == resistance // 1000000:
                return str(resistance//1000000) + ' megaohms ' + tolerance[colors[-1]]
            return str(resistance/1000000) + ' megaohms ' + tolerance[colors[-1]]
        if resistance >= 1000:
            if resistance / 1000 == resistance // 1000:
                return str(resistance//1000) + ' kiloohms ' + tolerance[colors[-1]]
            return str(resistance/1000) + ' kiloohms ' + tolerance[colors[-1]]
        return str(resistance) + ' ohms ' + tolerance[colors[-1]]
    if len(colors) == 5:
        resistor_number = int(str(color_code.index(colors[0])) + str(color_code.index(colors[1])) + str(color_code.index(colors[2])))
        multiple = 10 ** color_code.index(colors[3])
        resistance = resistor_number * multiple
        if resistance >= 1000000000:
            if resistance / 1000000000 == resistance // 1000000000:
                return str(resistance//1000000000) + ' gigaohms ' + tolerance[colors[-1]]
            return str(resistance/1000000000) + ' gigaohms ' + tolerance[colors[-1]]
        if resistance >= 1000000:
            if resistance / 1000000 == resistance // 1000000:
                return str(resistance//1000000) + ' megaohms ' + tolerance[colors[-1]]
            return str(resistance/1000000) + ' megaohms ' + tolerance[colors[-1]]
        if resistance >= 1000:
            if resistance / 1000 == resistance // 1000:
                return str(resistance//1000) + ' kiloohms ' + tolerance[colors[-1]]
            return str(resistance/1000) + ' kiloohms ' + tolerance[colors[-1]]
        return str(resistance) + ' ohms ' + tolerance[colors[-1]]