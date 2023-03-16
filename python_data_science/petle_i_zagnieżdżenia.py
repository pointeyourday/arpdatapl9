accounts = [
    ("A001", "100600", 250.50),
    ("B001", "200800", 199.97),
    ("A002", "600100", 213.90)
]

# Dla przykładu powyżej
#       0       1       2
#   0   [0][0]  [0][1]  [0][2]
#   1   [1][0]  [1][1]  [1][2]
#   2   [2][0]  [2][1]  [2][2]


print(accounts)
print(accounts[-1])
print(accounts[-1][2])
print(accounts[0], accounts[1])
print(accounts[0][2], accounts[1][2])