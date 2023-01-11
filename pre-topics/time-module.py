# ------------------ Time Module -------------- #
import time

# Get current time

# return struct time object
gm_time = time.gmtime()
print(gm_time)
# time.struct_time(tm_year=2023, tm_mon=1, tm_mday=6, tm_hour=18, tm_min=47, tm_sec=28, tm_wday=4, tm_yday=6, tm_isdst=0)

asc_time = time.asctime()
print(asc_time) # Fri Jan  6 18:49:55 2023

print(time.time()) # 1673124689.5367749
time3 = time.ctime(time.time()) # same format as asctime()
print(time3)

str_time =  time.strftime("%a, %d, %b %H:%M:%S %Y", time.localtime())
print(str_time)
str_time2 = time.strftime("%a, %d, %b %H:%M:%S %Y", time.gmtime())
print(str_time2)

# time measurement
time.sleep(5)
print('wait for 5s')

# time difference
current_time = time.time()
time.sleep(2)
new_current_time = time.time()
time_passed = new_current_time - current_time
print('Time passed', time_passed)

start = time.perf_counter()
time.sleep(3)
end = time.perf_counter()
total_time = end - start
print(f"Time passed {total_time} seconds.")


