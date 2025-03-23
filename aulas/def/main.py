def calc_tax(wage):
    percent = 27.5 / 100 * wage
    if wage <= 2500:
        return "Você é isento de imposto de renda"
    elif wage > 2500:
        tax = wage - percent
        print(f"Você foi taxado no IR, agora você tem {tax:.1f}")
calc_tax(5500)