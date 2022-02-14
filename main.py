unit_price = 49.95
quantity = 32
sales_tax_rate = 0.085
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax

s_subtotal = "$" + f"{subtotal:,.2f}"
s_sales_tax = "$" + f"{sales_tax:,.2f}"
s_total = "$" + f"{total:,.2f}"

output = f"""
Subtotal:      {s_subtotal:>9}
Sales Tax:    {s_sales_tax:>9}
Subtotal:      {s_total:>9}
"""

print(output)
