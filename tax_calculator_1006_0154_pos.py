# 代码生成时间: 2025-10-06 01:54:19
import scrapy
def calculate_tax(income, deductions, tax_rate):
    """Calculates the tax based on income, deductions, and tax rate.

    Args:
        income (float): The total income.
        deductions (float): The total deductions.
        tax_rate (float): The tax rate as a percentage.

    Returns:
        float: The calculated tax amount.
        None: If any input is invalid.
    """
    if not isinstance(income, (int, float)) or not isinstance(deductions, (int, float)) or not isinstance(tax_rate, (int, float)):
        print("Invalid input: Income, deductions, and tax rate must be numbers.")
        return None
    if income < 0 or deductions < 0 or tax_rate < 0:
        print("Invalid input: Income, deductions, and tax rate cannot be negative.")
        return None
    if tax_rate > 100:
        print("Invalid input: Tax rate cannot exceed 100%.")
        return None
    taxable_income = income - deductions
    tax_amount = taxable_income * (tax_rate / 100)
    return tax_amount

# Example usage:
if __name__ == "__main__":
    income = float(input("Enter your total income: "))
    deductions = float(input("Enter your total deductions: "))
    tax_rate = float(input("Enter the tax rate (e.g., 20 for 20%): "))
    tax = calculate_tax(income, deductions, tax_rate)
    if tax is not None:
        print(f"The calculated tax amount is: ${{:.2f}}".format(tax))
    else:
        print("Tax calculation failed.")