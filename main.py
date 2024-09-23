# Devon Taylor
# U2L1
# DS - Multiplication Table
# 9/23/24


# ONE LINE - NO MORE, NO LESS
table = [i*e for i in range(1, 11) for e in range(1, 11)]


########### NO TOUCHY ###########
for i, num in enumerate(table):
    if i % 10 == 0:
        print()
    
    print(num, end="\t")
print()
#################################