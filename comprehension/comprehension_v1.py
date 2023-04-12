# dobros = [i * 2 for i in range(10)]
# print(dobros)
dobros = [i * 2 for i in range(1, 21, 2)]
print(dobros)

# MESMA SOLUÇÃO DO APRESENTADO ACIMA:
dobros = []

for i in range(1, 21, 2):
    # print(i*2)
    dobros.append(i*2)

print(dobros)