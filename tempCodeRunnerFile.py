er(parent1,parent2):
#     ''' The oﬀsprings are created according to the equation:
#             Off_spring A = Best Parent  + β ∗ ( Best Parent − Worst Parent)
#             Off_spring B = Worst Parent - β ∗ ( Best Parent − Worst Parent)
#                 Where β is a random number between 0 and 1.
#         Input: 2 Parents
#         Output: 2 Children (1d Array)'''
#     ff1=fitness_fuction(parent1)
#     ff2=fitness_fuction(parent2)
#     diff=parent1 - parent2
#     beta=np.random.rand()
#     if ff1>ff2:
#         child1=parent1 + beta * diff
#         child2=parent2 - beta * diff
#     else:
#         child2=parent1 + beta * diff
#         child1=parent2 - beta * diff
#     return child1,child2

# for i in population[:30]:
#     for j in population[:30]:
#         print(Arithmetic_crossover(i,j))