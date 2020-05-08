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
# ŠÇ—E
def calc_manager(base, post):
    salary = base + post
    social = round10(salary * social_rate)
    tax = (salary - social) * tax_rate
    bank = salary - social - tax
    return int(bank)

if __name__ == "__main__":
    bank_terao = calc_manager(350000, 80000)
    bank_waka = calc_manager(375000, 40000)

    print(f'›”ö“N—Y‚³‚ñ‚ÌUŠz={bank_terao}')
    print(f'á—ÑmŒp‚³‚ñ‚ÌUŠz={bank_waka}')
