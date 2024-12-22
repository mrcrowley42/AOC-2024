with open("inputs/day22_input.txt") as file:
    input = list(map(int, file.read().splitlines()))


def mix_prune(secret, num):
    return (secret ^ num) % 16777216


def next_number(secret):
    secret = mix_prune(secret, secret * 64)
    secret = mix_prune(secret, secret // 32)
    secret = mix_prune(secret, secret * 2048)

    return secret


scores = 0
for secret in input:
    for i in range(2000):
        secret = next_number(secret)
    scores += secret

print(scores)


total_for_sequences = dict()

for line in input:
    secret = line
    sequence = [secret % 10]
    for i in range(2000):
        secret = next_number(secret)
        price = secret % 10
        sequence.append(price)
    seen = set()
    for i in range(len(sequence)-4):
        subseq = sequence[i:i+5]
        diffs = tuple([subseq[j+1] - subseq[j] for j in range(len(subseq)-1)])
        if diffs in seen:
            continue
        seen.add(diffs)
        total_for_sequences[diffs] = total_for_sequences.get(diffs, 0) + subseq[-1]

print(max(total_for_sequences.values()))
