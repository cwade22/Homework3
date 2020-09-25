SENTINEL = -1
result = []
while True: 
    gallons = float(input('Enter the gallons used ( -1 to end ): '))
    if gallons == SENTINEL : break
    miles = float(input('Enter the miles driven: '))
    mpg = miles / gallons 
    print(f'The miles/gallon for this tank was {mpg}')
    result.append(mpg) #add the mpg result to the result list above
    
print('The overall average miles/gallon was',sum(result)/len(result))
