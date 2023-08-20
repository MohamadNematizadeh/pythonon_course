
colors = ["BNV","bnv2","MVM","bnz","MVM3","bnz2","Tesla2"]
new_color = ""

print('color =', colors)

co = colors.copy()
print('copy',co)

colors.insert(2,'Tesla')
print('insert',colors)


colors.extend(['Toyota'])
print('extend',colors)