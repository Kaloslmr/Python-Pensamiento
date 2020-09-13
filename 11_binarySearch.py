objective = None
epsilon = 0.001
low = 0.0
steps = 0
result=0.0

while objective == None:
  objective_string = input('Which number do you wanna get the square root? ')
  if(objective_string.isdigit()):
    objective = int(objective_string)

high = max(1.0, objective)

while abs(result**2-objective) >= epsilon:
  if result**2 < objective:
    low = result
  else:
    high = result
  if (high+low)/2!=result:
    result=(high + low) / 2
  else:
    break
  steps+=1
  print(f'{steps}: high={high}, low={low}, result={result}')


print(f'square of {objective} is equal to {result}')