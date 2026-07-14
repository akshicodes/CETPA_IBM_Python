#Smart Retail Analyser

#input from user
print("-----Welcome to GUDDU STORE-----")
cust_name= input("Enter customer name: ")
cust_age= int(input("Enter customer age: "))
product_name= input("Enter the product name: ")
quantity= int(input("Enter quantity: "))
membership= input("Is the customer a member? (yes/no): ").lower()
price= float(input("Enter the price per unit: "))
payment_method= input("Enter the payment method: ").lower()

#Data types of the inputs
print("\n-----Data Types of the Inputs-----")
print("Type of cust_name:", type(cust_name))
print("Type of cust_age:", type(cust_age))
print("Type of product_name:", type(product_name))
print("Type of quantity:", type(quantity))
print("Type of membership:", type(membership))
print("Type of price:", type(price))
print("Type of payment_method:", type(payment_method))

#Data Type Conversion
 
quantity_float= float(quantity)
price_int= int(price)
age_str= str(cust_age)  
price_str= str(price)

print("\n-----Data Type Conversion-----")  
print("Quantity as float:", quantity_float)
print("Price as integer:", price_int)
print("Age as string:", age_str)
print("Price as string:", price_str)

print( "Type of quantity_float:", type(quantity_float))
print("Type of price_int:", type(price_int))
print("Type of age_str:", type(age_str))
print("Type of price_str:", type(price_str))

#arithmetic operations
total_cost= quantity * price

#user defined function 1
# to calculate discount based on membership
def calculate_discount(total_cost, membership):
    if membership == "yes":
        discount = total_cost * 0.1  # 10% discount for members
    else:
        discount = total_cost * 0.05  # 5% discount for non-members
    return discount


#user defined function 2
#to calculate gst
def calculate_gst(total_cost):
    gst = total_cost * 0.18  # 18% GST
    return gst

#user defined function 3
#sales insights
def sales_insights(final_cost):
    if final_cost >= 8000:
        insights = "High Value Sale"
    elif final_cost >= 3000:
        insights = "Medium Value Sale"
    else:
        insights = "Low Value Sale"
    return insights

discount= calculate_discount(total_cost, membership)
gst= calculate_gst(total_cost)
    
final_cost = total_cost - discount + gst
    
#customer status
if final_cost >= 10000:
    category = "Diamond Customer"
elif final_cost >= 5000:
    category = "Gold Customer"
elif final_cost >= 2000:
    category = "Silver Customer"
else:
    category = "Regular Customer"

#validating membership and reward 
if membership == "yes":
    if final_cost >= 5000:
        reward= "Free Gift Voucher"
    else:
        reward= "100 Reward Points"
else:
    if final_cost >= 5000:
        reward= "Invite for membership"
    else:
        reward= "Thank you for shopping with us"

#validating mode of payment
if payment_method == "cash":
    print("Payment Status: Cash Received")
elif payment_method == "card":
    print("Payment Status: Card Verified")
elif payment_method == "upi":
    print("Payment Status: Instant Payment Received")
else:
    print("Invalid Payment Method")

#function calls and output
  

# print("\n-----Calculating Total Cost and Discount-----")

print("\n======Smart Retail Sales Report======")
print('\n ----BILL DETAILS-GUDDU STORE-----')

print("Customer Name:", cust_name)
print("Customer Age:", cust_age)
print("Product Name:", product_name)
print("Quantity:", quantity)
print("Price per Unit:", price)
print("Payment Method:", payment_method)
print("Membership Status:", membership)
discount= calculate_discount(total_cost, membership)
gst= calculate_gst(total_cost)
print("Total Cost:", total_cost)
print("Discount:", discount)
print("GST:", gst)
print("Final Cost:", final_cost)
print("Customer Status:", category)
print("Reward:", reward)
print("Payment Method:", payment_method)

print("Business Insights: The customer is a", category, "and has made a purchase of", final_cost, "which is considered a", sales_insights(final_cost))


print("\n-----Sales Insights-----")
final_cost = total_cost - discount + gst
print("Sale Category:", sales_insights(final_cost))













