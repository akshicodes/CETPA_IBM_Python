'''
->Inputs:
Applicant Name, Applicant Age, Applicant Gender, Monthly Salary, Credit Score, EMIs, Loan Amt Requirment, Loan Purpose(Home, Car, Education, Personal, Business), Loan Tenure(1-30 years)

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

5. if salary is greater than 60k, credit score is 690 so loam approved with higher interest rate

-> Loan Category:
based on salary:
60k-80k: bronze
80k-1L: silver
1L-2L: gold
2L+: platinum


-> If all the above criteria are met, the applicant is eligible for the loan, otherwise they are not eligible.'''