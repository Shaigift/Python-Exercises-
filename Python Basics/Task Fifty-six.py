day = int(input('Give number of days: ')) * 3600 * 24
month = int(input('Give number of months')) * 3600 * 24 * 7
hour = float(int(input('Give number of hours'))) * 3600
minute = float(int(input('Give number of minute'))) * 60

time = day + hour + month + minute

print('The amount of seconds', time)