# dobros = [i * 2 for i in range(10)]
# print(dobros)
dobros2 = [i *2 for i in range(1, 21) if i % 2 == 0]
print(dobros2)

# MESMA SOLUÇÃO DO APRESENTADO ACIMA:
dobros2 = []

for i in range(1, 21):
    # print(i*2)
    if i % 2 == 0:
        dobros2.append(i*2)

print(dobros2)