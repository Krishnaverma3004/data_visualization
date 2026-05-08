# -------------------------------------------------------
# Function to check if input contains only digits
# Returns True if valid positive number
# -------------------------------------------------------
def is_number(value):
    if value == "":
        return False
    
    for ch in value:
        if ch < '0' or ch > '9':
            return False
    
    return True


# -------------------------------------------------------
# E-Commerce Cart System (Improved)
# - Removes duplicate product prices
# - Applies 10% discount if total > 5000
# - Adds 18% GST
# - Displays final payable amount (3 decimal places)
# -------------------------------------------------------
def ecommerce_cart():

    data = input("Enter product prices separated by space: ").split()

    prices = []

    # Validate and remove duplicates
    for item in data:
        if is_number(item):
            price = int(item)

            if price not in prices:
                prices.append(price)

    if len(prices) == 0:
        print("No valid product prices entered.")
        return

    # Calculate total
    total = 0
    for price in prices:
        total = total + price

    print("\nTotal before discount and GST:", format(total, ".3f"))

    # Apply 10% discount if applicable
    if total > 5000:
        discount = total * 0.10
        total = total - discount
        print("Discount Applied (10%):", format(discount, ".3f"))
    else:
        discount = 0
        print("No discount applied.")

    # Apply 18% GST
    gst = total * 0.18
    total = total + gst

    print("GST Added (18%):", format(gst, ".3f"))

    # Final Payable Amount
    print("Final Payable Amount:", format(total, ".3f"))

'''output:
    Enter product prices separated by space: 1000 2000 3000 200
    Total before discount and GST: 6000.000
    Discount Applied (10%): 600.000
    GST Added (18%): 972.000
    Final Payable Amount: 6372.000
    ''' 