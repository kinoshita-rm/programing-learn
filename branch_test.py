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

# �A���o�C�g
def calc_part(unit, time):
    salary = unit * time
    tax = salary * tax_rate
    bank = salary - tax
    return int(bank)

if __name__ == "__main__":
    bank_kiku = calc_part(1200, 90)
    bank_yama = calc_part(1000, 120)

    print(f'�e�n�͂���̐U���z={bank_kiku}')
    print(f'�R�݊��ނ���̐U���z={bank_yama}')
