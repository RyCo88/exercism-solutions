def value(colors):
    color_code = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white",]
    code = ''
    for i in colors[:2]:
        code += str(color_code.index(i))
    return int(code)
