# �Љ�ی�����
social_rate = 0.15

# �����ŗ�
tax_rate = 0.1

# 10�~�P�ʎl�̌ܓ�
def round10(v):
r = int(v / 10 + 0.5) * 10
return r

# 10�~�P�ʐ؂�̂�
def trunc10(v):
    t = int(v / 10) * 10
    return t

if __name__ == "__main__":
# ��ʎЈ�
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

    print(f'���c��������̐U���z={bank_terada}')
    print(f'�L�c�N������̐U���z={bank_hiro}')
    print(f'�����m��Y����̐U���z={bank_suga}')
