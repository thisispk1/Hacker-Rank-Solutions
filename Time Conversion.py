def timeConversion(s):
    if s.endswith('PM') or s.endswith('pm'):
        x=s.split(':')
        y=int(x[0])
        y=y+12
        x[0]=str(y)
        x=str(':'.join(x))
        return(x[:8])
    elif s.endswith('AM') or s.endswith('am'):
        if s.startswith('12'):
            x=s.split(':')
            y=int(x[0])
            y=y-12
            x[0]=str(y)
            x=str(':'.join(x))
            return(x[:8])
        else:
            return(s[:8])
t=str(input('t='))
timeConversion(t)
