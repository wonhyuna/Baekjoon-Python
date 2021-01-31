h, m = map(int, input().split())

total = h * 60 + m
alarm = total - 45
if alarm < 0:
    alarm += 24 * 60

hour = alarm // 60
minute = alarm % 60

print(hour, minute)