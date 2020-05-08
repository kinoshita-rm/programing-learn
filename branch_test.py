# Ğ‰ï•ÛŒ¯—¿—¦
social_rate = 0.15

# Š“¾Å—¦
tax_rate = 0.1

# 10‰~’PˆÊlÌŒÜ“ü
def round10(v):
r = int(v / 10 + 0.5) * 10
return r

# 10‰~’PˆÊØ‚èÌ‚Ä
def trunc10(v):
    t = int(v / 10) * 10
    return t

if __name__ == "__main__":

# ƒAƒ‹ƒoƒCƒg
def calc_part(unit, time):
    salary = unit * time
    tax = salary * tax_rate
    bank = salary - tax
    return int(bank)

if __name__ == "__main__":
    bank_kiku = calc_part(1200, 90)
    bank_yama = calc_part(1000, 120)

    print(f'‹e’nÍ‚³‚ñ‚ÌUŠz={bank_kiku}')
    print(f'RŠİŠ¹“Ş‚³‚ñ‚ÌUŠz={bank_yama}')
