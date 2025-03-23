def boredom(staff):
    dept = {'accounts': 1, 'finance': 2, 'canteen': 10, 'regulation': 3, 'trading': 6, 'change': 6, 'IS': 8, 'retail': 5, 'cleaning': 4, 'pissing about': 25}
    bore = 0
    for employee in staff:
        department = staff[employee]
        if department in dept:
            bore += dept[department]
            
    if bore <= 80:
        return 'kill me now'
    elif bore > 80 and bore < 100:
        return 'i can handle this'
    else:
        return 'party time!!'
    

print(boredom({ "tim": "IS", "jim": "finance",
      "randy": "pissing about", "sandy": "cleaning", "andy": "cleaning",
      "katie": "cleaning", "laura": "pissing about", "saajid": "regulation",
      "alex": "regulation", "john": "accounts", "mr": "canteen" }))

# n = sum(lookup[s] for s in staff.values())
#     if n <= 80:
#         return "kill me now"
#     if n < 100:
#         return "i can handle this"
#     return "party time!!"