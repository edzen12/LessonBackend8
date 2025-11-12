# заменить встречающиеся буквы Т на U и сохранить строку
def dna_to_rna(dna):
    n = ''
    i = 0
    for i in dna:
        if i == 'T':
            n += 'U'
        else:
            n+=i
    print(n)
# dna_to_rna('TREGTHRNYT') # U

def remove_exclamation_marks(s):
    n = ''
    i = 0
    for i in s:
        if i == '!':
            n += ''
        else:
            n+=i
    return n

# print(remove_exclamation_marks('egfr!fef!fereb!'))


def get_age(age):
    if int(age[0]) >0 and int(age[0]) <10:
        return int(age[0])

# print(get_age("2 years old"))



def powers_of_two(n):
    g = []
    for i in range(int(n)+1):
        k = 2 ** i
        g.append(k)
    return g

print(powers_of_two(3))