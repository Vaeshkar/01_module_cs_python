university = {
  "name":"WBS University",
  "departments": {
    "Computer Science": {
      "professors": [
        {"name":"Malan", "specialty":"CS50"},
        {"name":"Lee", "specialty":"Cybersecurity"}
      ],
      "courses": ["Algorithms", "Machine Learning"]
    },
    "Mathematics": {
      "professors": [
        {"name":"Johnson", "specialty":"Statistics"},
        {"name":"Patel", "specialty":"Algebra"}
      ],
      "courses": ["Calculus", "Linear Algebra"]
    }
  }
}

print("\nPrint Professors and Specialties:")
for dept in university["departments"]:
  for prof in university["departments"][dept]["professors"]:
    print(f"{prof['name']} – {prof['specialty']}")