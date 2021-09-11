"""
Ques 2. Merge sort
T.C. = O(n log n)
S.C. = O(n) => Space used by list 
"""
# class Solution:
#     def merge(self,arr, l, m, r): 
#         temp = list()
#         p1 = l
#         p2 = m + 1
        
#         while p1 <= m and p2 <= r:
#             if(arr[p1] < arr[p2]):
#                 temp.append(arr[p1])
#                 p1 += 1 
#             else:
#                 temp.append(arr[p2])
#                 p2 += 1 
                
#         while p1 <= m:
#             temp.append(arr[p1])
#             p1 += 1
        
#         while p2 <= r:
#             temp.append(arr[p2])
#             p2 += 1 
            
#         idx = 0
#         while idx < len(temp):
#             arr[l + idx] = temp[idx]
#             idx += 1
        
#     def mergeSort(self,arr, l, r):
#         if(l >= r):
#             return             
#         mid = (l + r) // 2 
#         self.mergeSort(arr, l, mid)
#         self.mergeSort(arr, mid + 1, r)
#         self.merge(arr, l, mid, r )