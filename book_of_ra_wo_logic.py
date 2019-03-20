import random

#parami
laukums = [[0] * 5 for y in range(3)]
simboli = []
gramata_rate = 2 #*
muzhiks_rate = 3 #M
pharaoh_rate = 5 #F
vabole_statuja_rate = 6 #V, S
ak_rate = 12 #A, K
jq10_rate = 18 #J, Q, X
if gramata_rate + muzhiks_rate + pharaoh_rate + 2 * vabole_statuja_rate + 2 * ak_rate + 3 * jq10_rate != 100:
        print("Uzmanību, kļūda spēles loģikā!!!\n")

#kopa
simboli.extend(["*"] * gramata_rate)
simboli.extend(["M"] * muzhiks_rate)
simboli.extend(["F"] * pharaoh_rate)
simboli.extend(["V"] * vabole_statuja_rate)
simboli.extend(["S"] * vabole_statuja_rate)
simboli.extend(["A"] * ak_rate)
simboli.extend(["K"] * ak_rate)
simboli.extend(["J"] * jq10_rate)
simboli.extend(["Q"] * jq10_rate)
simboli.extend(["X"] * jq10_rate)

#spins
for x in range(5):
        #nakama rinda nelauj viena kolonna but diviem vienadiem simboliem
        while laukums[0][x] == laukums[1][x] or laukums [0][x] == laukums [2][x] or laukums [1][x] == laukums [2][x]:
                for y in range(3):
                        laukums[y][x] = random.choice(simboli)   

for rinda in laukums:
    print('  '.join([str(simbols) for simbols in rinda]))

