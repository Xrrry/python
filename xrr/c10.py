def curve_pre():
    def curve():
        print('123')
    return curve


f = curve_pre()
f()
