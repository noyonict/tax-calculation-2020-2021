
def calculate_tax(income, gender='Male', age=35, citizen='Bangladesh', freedom_fighter=False, disabled_person=False):
    tax = 0
    initial_value = 300000

    if gender == 'Female' or age > 65:
        initial_value = 350000

    if freedom_fighter:
        initial_value = 475000

    if disabled_person:
        initial_value = 450000

    if citizen != 'Bangladesh':
        return (income * 30) / 100

    if income > initial_value:
        tax_0_extra = income - initial_value

        if tax_0_extra > 100000:
            tax += (100000 * 5) / 100
            tax_5_extra = tax_0_extra - 100000

            if tax_5_extra > 300000:
                tax += (300000 * 10) / 100
                tax_10_extra = tax_5_extra - 300000

                if tax_10_extra > 400000:
                    tax += (400000 * 15) / 100
                    tax_15_extra = tax_10_extra - 400000

                    if tax_15_extra > 500000:
                        tax += (500000 * 20) / 100
                        tax_20_extra = tax_15_extra - 500000

                        if tax_20_extra > 0:
                            tax += (500000 * 25) / 100
                    else:
                        tax += (tax_15_extra * 20) / 100

                else:
                    tax += (tax_10_extra * 15) / 100

            else:
                tax += (tax_5_extra * 10) / 100
        else:
            tax += (tax_0_extra * 5) / 100

    return tax


if __name__ == '__main__':
    print(calculate_tax(1300000))
