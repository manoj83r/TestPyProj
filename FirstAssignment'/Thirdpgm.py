costOfProd = input('Enter the cost of the product:')
quantity = input('Enter the total number of items bought:')
costOfProd = float(costOfProd)
quantity = int(quantity)
totalCost = costOfProd * quantity
if totalCost > 1000:
    print("Total cost before Discount:", str(totalCost))
    discountedCost = totalCost * 0.9
    print("Total cost after Discount:", str(discountedCost))
else:
    print("Total cost:", str(totalCost))
    print("Sorry there is no discount")

