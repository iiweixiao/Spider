import time
from datetime import datetime

time_now = int(time.time())              # 获取当前时间的时间戳
print(time_now)
dt_now = datetime.fromtimestamp(time_now)

print(type(dt_now), dt_now)