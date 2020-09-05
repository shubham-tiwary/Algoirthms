def find_rotated_min(array,left,right):
  '''
  Function to find minimum element in an increasing sequence 
  rotated unknown number of times in O(logn) time
  '''
  # When search is exhausted, condition not met, array is not rotated then 1st element is smallest
  if right<left:
    return array[0]
  # Only one element is left to check then that element is smallest
  if left == right:
    return array[left]
  mid = (left+right)//2
  if (mid>left and array[mid]<array[mid-1]):
    return array[mid]
  if (mid<right and array[mid+1]<array[mid]):
    return array[mid+1]
  if (array[right]>array[mid]):
    return find_rotated_min(array,left,mid-1)
  return find_rotated_min(array,mid+1,right)

A = [12,23,33,34,56,79,5,8,9,10]
print(find_rotated_min(A,0,len(A)-1))
