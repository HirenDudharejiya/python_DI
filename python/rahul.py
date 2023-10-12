def pythagorean_triplet(a, b, c):
    a_sq = a * a
    b_sq = b * b
    c_sq = c * c
    
    smallest_squares_sum = a_sq + b_sq
    if(a_sq + b_sq == c_sq ):
        print(True)
    else:
        print(False)
    
    # return smallest_squares_sum == c_sq

print(pythagorean_triplet(3, 4, 5))
print(pythagorean_triplet(5, 12, 13))
print(pythagorean_triplet(8, 15, 17))
print(pythagorean_triplet(7, 24, 25)) 
print(pythagorean_triplet(1,2,3))