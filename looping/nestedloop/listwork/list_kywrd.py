food=list(("biriyani","alfaham","sadhya","porotta","pathiri"))
print(food)
new_food=list(("biriyani","alfaham","sadhya","porotta","biriyani","pathiri"))
print(new_food)
print(type(food))
print(len(food))
print(food[0])
print(food[1])
print(food[2])
print(food[3])
print(food[4])

food[2]="Mandhi"
food[4]="puttu kadala"
#append----to add to the last index
food.append("fried rice")
print(food)
