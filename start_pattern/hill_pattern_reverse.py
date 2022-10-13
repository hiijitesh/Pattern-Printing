
# The below code is modification right_angle_triangle_pattern code

'''
 * * * * * * *
  * * * * * *
   * * * * *
    * * * *
     * * *
      * *
       *
'''
n = 7

for row in range(n):
    for col in range(row+1):
        print(" ", end="")
    for col in range(row, n):
        print("* ", end="")

    print()
