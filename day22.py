with open("inputs/day22_input.txt") as file:
    input = list(map(int, file.read().splitlines()))


def mix_prune(secret, num):
    return (secret ^ num) % 16777216


def next_number(secret):
    secret = mix_prune(secret, 64 * secret)
    secret = mix_prune(secret, secret // 32)
    secret = mix_prune(secret, secret * 2048)

    return secret


scores = 0
for secret in input:
    for i in range(2000):
        secret = next_number(secret)
    scores += secret

print(scores)



# for line in input:
#     secret = line
#     prices = [int(str(secret)[-1]),]
#     for i in range(10):
#         secret = next_number(secret)
#         price = int(str(secret)[-1])
#         prices.append(price)
#         print(prices)
#         # print(secret)
#     scores += secret
    
# print(scores)