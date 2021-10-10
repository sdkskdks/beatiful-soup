def permutation(string):
   if len(string) == 1:
     return [string]

   res_list = [] # resulting list
   for char in string:
     remaining_elements = [x for x in string if x != char]
     sublist_permutation = permutation(remaining_elements) # sublist permutations

     for elem in sublist_permutation:
       res_list.append(char + ''.join(elem))

   return res_list

print(permutation(['a', 'b', 'c']))
print(permutation('abc')) # works the same as above
