number_of_elements = int(input('Enter number of elements:'))
elements =[]
for i in  range(1, number_of_elements+1):
    num=input(f'Enter element number  {i}: ')
    elements.append(num)

print(elements)

maxx ,min = max(elements),min(elements)
print(f'The pair with maximum difference is {maxx, min}')