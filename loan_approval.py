'''
->Inputs:
Applicant Name, Applicant Age, Applicant Gender, Monthly Salary, Credit Score, EMIs, Loan Purpose(Home, Car, Education, Personal, Business), Loan Tenure(1-30 years)

->Eligibilty Criteria:
1. age must be between 21 and 60 years

2. monthly salary must be at least greater than 60k

3. Credit score:
>750: excellent
700-749: good
650-699: average
<650: reject

4. EMIs must be less than 50% of the monthly salary

5. Loan Amount Requirement:
- Home: 5-50 lakhs
- Car: 3-20 lakhs
- Education: 1-10 lakhs
- Personal: 1-15 lakhs
- Business: 5-100 lakhs

6. Loan Tenure: 1-30 years


-> Loan Decision:
1. approved only when all the above criteria are met

2.if salary is less than 60k, then rejected

3.if salary is greater than 60k but credit score is less than 650, then rejected

4. if salary is greater than 60k and credit score is greater than 650 but EMIs are more than 50% of the monthly salary, then rejected

5. if salary is greater than 60k, credit score is 690 so loan approved with higher interest rate

-> Interest Rate

Based on credit score:
750+ -> 8%
700–749 -> 	9%
650–699 ->	10.5%
Below 650-> 	Not Eligible

-> Loan Category:
based on salary:
60k-80k: bronze
80k-1L: silver
1L-2L: gold
2L+: platinum


-> If all the above criteria are met, the applicant is eligible for the loan, otherwise they are not eligible.'''



import pandas as pd


# role selection
user_role = input("Are you running this as a Bank Manager or Applicant? ").strip().lower()

if user_role in ["bank manager", "manager"]:
    show_all_records = input("\nDo you want to see all loan records in the CSV file? (yes/no): ").strip().lower()

    if show_all_records in ["yes", "y"]:
        print("\nAll loan records:")
        csv_file = "loan_applications.csv"
        print(pd.read_csv(csv_file).to_string(index=False))

else:
    print("\nProceeding as an Applicant...\n")


#input from user
applicant_name = input("Enter Applicant Name: ").title()
applicant_age = int(input("Enter Applicant Age: "))
applicant_gender = input("Enter Applicant Gender (M/F): ").upper()
monthly_salary = float(input("Enter Monthly Salary: "))
credit_score = int(input("Enter Credit Score: "))
emis = float(input("Enter EMIs: ")) 
loan_amt=float(input("Enter Loan Amount: "))
loan_purpose = input("Enter Loan Purpose (Home, Car, Education, Personal, Business): ").strip().lower()
loan_purpose_display = loan_purpose.title()
loan_tenure = int(input("Enter Loan Tenure (1-30 years): "))

loan_status = "Loan Rejected"
rejection_reason = ""
credit_rating = "N/A"
interest_rate = "N/A"
loan_category = "N/A"


if applicant_age < 21 or applicant_age > 60:
    rejection_reason = "Applicant age must be between 21 and 60 years."
    
    

elif monthly_salary < 60000:
    rejection_reason = "Monthly salary must be at least ₹60,000."
    
elif credit_score < 650:
    rejection_reason = "Credit score below 650."

elif emis > (0.5 * monthly_salary):
    rejection_reason = "Applicant is not eligible for the loan due to EMIs criteria."
     
elif loan_purpose not in ["home", "car", "education", "personal", "business"]:
    rejection_reason = "Invalid loan purpose entered."

    #loan amount criteria on the basis of loan purpose

elif loan_purpose == "home" and not (500000 <= loan_amt <= 5000000):
    rejection_reason = "Home loan amount must be between ₹5,00,000 and ₹50,00,000."

elif loan_purpose == "car" and not (300000 <= loan_amt <= 2000000):
    rejection_reason = "Car loan amount must be between ₹3,00,000 and ₹20,00,000."

elif loan_purpose == "education" and not (100000 <= loan_amt <= 1000000):
    rejection_reason = "Education loan amount must be between ₹1,00,000 and ₹10,00,000."

elif loan_purpose == "personal" and not (100000 <= loan_amt <= 1500000):
    rejection_reason = "Personal loan amount must be between ₹1,00,000 and ₹15,00,000."

elif loan_purpose == "business" and not (500000 <= loan_amt <= 10000000):
    rejection_reason = "Business loan amount must be between ₹5,00,000 and ₹1,00,00,000."
     
elif loan_tenure < 1 or loan_tenure > 30:
    rejection_reason = "Applicant is not eligible for the loan due to Loan Tenure criteria."
     
else:
    loan_status = "Loan Approved"
    

    #Determine interest rate based on credit score
    if credit_score >= 750:
        credit_rating = "Excellent"
        interest_rate = 8

    elif credit_score >= 700:
        credit_rating = "Good"
        interest_rate = 9

    else:
        credit_rating = "Average"
        interest_rate = 10.5

    #Loan Category on the basis of monthly salary
    if monthly_salary >= 200000:
        loan_category = "Platinum"

    elif monthly_salary >= 100000:
        loan_category = "Gold"

    elif monthly_salary >= 80000:
        loan_category = "Silver"

    else:
        loan_category = "Bronze"

loan_record = {
    "Applicant Name": applicant_name,
    "Applicant Age": applicant_age,
    "Applicant Gender": applicant_gender,
    "Monthly Salary": monthly_salary,
    "Credit Score": credit_score,
    "Credit Rating": credit_rating,
    "Monthly EMIs": emis,
    "Loan Amount": loan_amt,
    "Loan Purpose": loan_purpose_display,
    "Loan Tenure": loan_tenure,
    "Loan Category": loan_category,
    "Interest Rate": interest_rate,
    "Loan Status": loan_status,
    "Rejection Reason": rejection_reason,
}

loan_df = pd.DataFrame([loan_record])
csv_file = "loan_applications.csv"

loan_df.to_csv(csv_file, index=False)
print("\nLoan application summary saved to 'loan_applications.csv'.")

if loan_status == "Loan Approved":
    print("\nLoan application summary:")
    print(f"\nCongratulations {applicant_name}! Loan Approved")
    


    print("----------- Applicant Details -----------")
    print(f"Applicant Name   : {applicant_name}")
    print(f"Age              : {applicant_age}")
    print(f"Gender           : {applicant_gender}")
    print(f"Monthly Salary   : ₹{monthly_salary:,.2f}")
    print(f"Credit Score     : {credit_score}")
    print(f"Credit Rating    : {credit_rating}")
    print(f"Monthly EMIs     : ₹{emis:,.2f}")
    print(f"Loan Amount      : ₹{loan_amt:,.2f}")
    print(f"Loan Purpose     : {loan_purpose.title()}")
    print(f"Loan Tenure      : {loan_tenure} Years")
    print("-----------------------------------------")
    print(f"Loan Category    : {loan_category}")
    print(f"Interest Rate    : {interest_rate}%")

    print(
        f"Expected: {loan_status}, Credit Rating = {credit_rating}, Loan Category = {loan_category}"
    )

    if 650 <= credit_score <= 699:
        print("Note -> Loan approved with a higher interest rate due to an average credit score.")
else:
    print(f"\nLOAN REJECTED: {rejection_reason}")




