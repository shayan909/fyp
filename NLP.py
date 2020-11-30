symptoms = {"fever": {"question": {"duration": "How long you're having it?", "severity": "What is the temperature?"}},
            "cough": {"question": {"duration": "How long you're having cough?", "severity": "is it dry or wet?"}}}

symplst = ["fever","cough"]
symp_details = {}
my_symp = {}

for x in symplst:
    #if x in symptoms.keys():
        print(symptoms[x]["question"]["duration"])
        symp_details["duration"] = input()
        print(symp_details)
        print(symptoms[x]["question"]["severity"])
        symp_details["severity"] = input()
        my_symp[x] = symp_details
        print(my_symp)
   # else:
        print("no match")

