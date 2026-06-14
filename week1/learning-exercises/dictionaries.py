drug = {
    "name": "Metformin",
    "class": "Biguanide",
    "indication": "Type 2 Diabetes",
    "approval_year": 1994,
    "dosage_mg": 500.0,
    "side_effects": ["nausea", "diarrhoea", "stomach pain"]
}

print(drug["name"])
print(drug["side_effects"])
print(drug["side_effects"][0])

drugs = [
    {
        "name": "Metformin",
        "class": "Biguanide",
        "indication": "Type 2 Diabetes",
        "approval_year": 1994
    },
    {
        "name": "Atorvastatin",
        "class": "Statin",
        "indication": "High Cholesterol",
        "approval_year": 1996
    },
    {
        "name": "Ibuprofen",
        "class": "NSAID",
        "indication": "Pain Relief",
        "approval_year": 1974
    }
]

for drug in drugs:
    if drug["approval_year"] > 1990:
        print(f"{drug['name']} - approved {drug['approval_year']}")

#Go through every key-value pair in the drug dictionary, 
#for each pair give me the key in a variable called key and the value in a variable called value."
# this only prints the last value in the dictionary because the for loop overwrites the value of drug each time.
for key, value in drug.items():
    print(f"{key}: {value}")