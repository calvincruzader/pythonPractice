import decimal 

print("rounding issues in decimals due to hardware limitations of representation rational numbers.")
print("1 / 3 = {:f}".format(1/3)) 

print("Thus, we import the decimal Python module to have more precision than usual.")

print("decimal.Decimal(1 / 3) = {:f}".format(decimal.Decimal(1 / 3)))