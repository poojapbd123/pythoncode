months = ('jan frb mar apr may jun jul ' + 'aug sep oct nov dec ').split()
month2mm = {}
for i, month in enumerate(months):
    month2mm[month] = i + 1
    
date = input()
date = date.replace(',', ' ')
day, months, year = date.split()

dd, yyyy = int(day), int(year)
mon = month[:3].lower()
mm = month2mm[mon]
print((yyyy, mm, dd))

print("==================")


    