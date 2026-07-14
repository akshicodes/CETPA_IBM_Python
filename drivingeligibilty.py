#age checker for driving license
while True:
        

        print("Do you want to apply for a driving license or get Learning's Permit Eligibilty?")
        license_fee = input("Have you paid the license fee? (yes/no): ").strip().lower()
       


        if license_fee == "no":
            print("Please pay the license fee before applying.")
             
            
            
        else:
            age = int(input("Enter your age: "))
            def driving_license_eligibility(age):
                if age >= 18:
                    return "You are eligible to apply for a driving license."
                else:
                    return "You are not eligible for a driving license yet."

            def learning_permit_eligibility(age):
                if age >= 16:
                    return "You are eligible to apply for a Learning's Permit."
                else:
                    return "You are not eligible for a Learning's Permit yet."

            if age >= 18 :
                driving_license_message = driving_license_eligibility(age)
                print(driving_license_message)
                 

            else:
                learning_permit_message = learning_permit_eligibility(age)
                print(learning_permit_message)
                 

   
       








