import json

with open('intents.json') as file:
    data = json.load(file)


symplst = ["fever","chest pain"]
my_symp = {}

for x in symplst:
        symp_details = {}

        print(data["symptoms"][x]["question"]["duration"])
        symp_details["duration"] = input()
        print(symp_details)
        print(data["symptoms"][x]["question"]["severity"])
        symp_details["severity"] = input()
        my_symp[x] = symp_details

print(my_symp)



#print(data['symptoms']['fever']['question']['duration'])


