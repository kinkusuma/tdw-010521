def pattern(size):
  size += 1
  for i in range(1, size):
    for j in range(1, size):
      if i == 1 or i == size-1:
        print('+ ', end='')
      else:
        if j%3 == 0:
          print('+ ', end='')
        else:
          print('= ', end='')
    print('\n')

pattern(8)

"""
output:

+ + + + + + + + 

= = + = = + = = 

= = + = = + = = 

= = + = = + = = 

= = + = = + = = 

= = + = = + = = 

= = + = = + = = 

+ + + + + + + + 

"""