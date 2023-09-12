import sys
input = sys.stdin.readline

n, m = map(int, input().split())
known_list = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & known_list:
            known_list = known_list.union(party)

count = 0

for party in parties:
    if not party & known_list:
        count += 1

print(count)