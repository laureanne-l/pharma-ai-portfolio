drug_name = "Metformin"
drug_class = "Biguanide"
indication = "Type 2 diabetes"
approval_year = 1994
dosage_mg = 500.0
is_approved = True

print(f"Drug: {drug_name}")
print(f"Class: {drug_class}")
print(f"Indication: {indication}")
print(f"Approved: {approval_year}")
print(f"Dosage: {dosage_mg} mg")
print(f"Currently Approved: {is_approved}")

print(type(drug_name))
print(type(approval_year))
print(type(dosage_mg))
print(type(is_approved))

print(approval_year + 10)
print(drug_name + " is a medication")