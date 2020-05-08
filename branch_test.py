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
# ˆê”ÊĞˆõ
def calc_general(base, over):
    over_price = trunc10(base / 160.0 * 1.25)
    salary = base + over_price * over
    social = round10(salary * social_rate)
    tax = (salary - social) * tax_rate
    bank = salary - social - tax
    return int(bank)

if __name__ == "__main__":
    bank_terada = calc_general(320000, 30)
    bank_hiro = calc_general(295000, 20)
    bank_suga = calc_general(220000, 35)

    print(f'›“c”¿‚³‚ñ‚ÌUŠz={bank_terada}')
    print(f'L“cN”‚³‚ñ‚ÌUŠz={bank_hiro}')
    print(f'›À—mˆê˜Y‚³‚ñ‚ÌUŠz={bank_suga}')
