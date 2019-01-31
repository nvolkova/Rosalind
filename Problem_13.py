# Problem 13: Calculating Expected Offspring
file = open("/Users/nvolkova/Downloads/rosalind_iev.txt", "r")
dominants, dominant_hetero, dominant_homo, hetero, hetero_homo, homo = [int(x) for x in next(file).split()]
exp_no_offspring = 2 * (dominants + dominant_hetero + dominant_homo + 0.75 * hetero + 0.5 * hetero_homo)
print(exp_no_offspring)

