import sys

while True :
    n_time = []
    c = ''
    time = raw_input('Type the time in the format"hh:mm:ss(AM/PM)":\n').strip()
    for i in time:
        if (not i.isdigit()) and (not i == ':'):
            n_time.append(i)
    t = ''.join(n_time)
    if t == 'PM':
        if int(time[0:2]) == 12:
            c = int(time[0:2])
        else:
            c = int(time[0:2]) + 12   
    elif t == 'AM':
        if int(time[0:2]) == 12:
            c = '00'
        else:
            c = int(time[0:2])
        
    print str(c)+ time[2:8]
