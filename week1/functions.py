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

def describe_drug(drug):
    print(f"Name: {drug['name']}")
    print(f"Indication: {drug['indication']}")
    print(f"Approved: {drug['approval_year']}")

for drug in drugs:
    describe_drug(drug)
 