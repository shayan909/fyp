symptoms = {"fever": {"question": {"duration": "How long you're having it?", "severity": "What is the temperature?"}}}

symplst = ["fever"]
symp_details = {}

for x in symplst:
    if x in symptoms.keys():
        print(symptoms[x]["question"]["duration"])
        symp_details["duration"] = input()
        print(symp_details)
        print(symptoms[x]["question"]["severity"])
        symp_details[x] = input()
    else:
        print("no match")

