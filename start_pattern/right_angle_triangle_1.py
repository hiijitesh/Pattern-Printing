
'''
 *******
  ******
   *****
    ****
     ***
      **
       *
    '''

n = 7

for row in range(n):
    for col in range(row+1):
        print(" ", end="")
    for col in range(row, n):
        print("*", end="")

    print()
########################################################################################

'''
*******
******
*****
****
***
**
*
'''

for row in range(n):
    for col in range(row+1):
        print("", end="")
    for col in range(row, n):
        print("*", end="")

    print()


########################################################################################


'''
 * * * * * * *
  * * * * * *
   * * * * *
    * * * *
     * * *
      * *
       *
'''



for row in range(n):
    for col in range(row+1):
        print(" ", end="")
    for col in range(row, n):
        print("* ", end="")

    print()
