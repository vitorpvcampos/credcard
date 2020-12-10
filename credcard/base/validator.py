import re
from django.core.exceptions import ValidationError


def validate_cpf(cpf):
    cpf = ''.join(re.findall('\d', str(cpf)))

    if (not cpf) or (len(cpf) < 11):
        raise ValidationError(f"{cpf} is not a valid CPF.")

    cpf_number = list(map(int, cpf))
    print(cpf_number)
    new_cpf_number = cpf_number[:9]

    while len(new_cpf_number) < 11:
        r = sum([(len(new_cpf_number) + 1 - i) * v for i, v in enumerate(new_cpf_number)]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        new_cpf_number.append(f)

    if new_cpf_number == cpf_number:
        return cpf
    raise ValidationError(f"{cpf} is not a valid CPF.")
