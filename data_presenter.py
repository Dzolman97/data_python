open_cupcake = open("CupcakeInvoices.csv")

# for data in open_cupcake:
#    print(data)


# for value in open_cupcake:
#    if "Chocolate" in value:
#       print("Chocoalte")
#    elif "Vanilla" in value:
#       print("Vanilla")
#    elif "Strawberry" in value:
#       print("Strawberry")

total = 0

for line in open_cupcake:
   results = line.rstrip('\n').split(',')
   newResults = float(results[-1]) * float(results[-2])
   total = total + newResults
   
print(round(total, 2))

open_cupcake.close()