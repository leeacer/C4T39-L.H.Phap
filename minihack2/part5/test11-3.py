county = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
population = [150300, 247100, 333300, 266800, 420900, 318000]
maxium = population.index(max(population))
minium = population.index(min(population))

print("Largest population is:", county[maxium], max(population)) 
print("Smallest population is:", county[minium], min(population)) 