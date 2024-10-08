import sys

from collections import Counter
import statistics as st


N = int(sys.stdin.readline())
numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()

# 산술평균
print(round(st.mean(numbers)))

# 중앙값
print(st.median(numbers))

# 최빈값

cnt = Counter(numbers).most_common()
mode = []

for i in cnt:
    if i[1] == cnt[0][1]:
        mode.append(i[0])
    else:
        break
if len(mode) == 1:
    print(mode[0])
else:
    mode.sort()
    print(mode[1])

# 범위
print(max(numbers)-min(numbers))