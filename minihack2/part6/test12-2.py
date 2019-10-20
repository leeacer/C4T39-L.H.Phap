area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09] 
population = [150300, 247100, 333300, 266800, 420900, 318000]
res_list = [] 
for i in range(0, len(area)): 
	res_list.append(population[i] // area[i]) 
average = sum(res_list) // len(area)
print("The average population density is:", average)