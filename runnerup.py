"""
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given  scores. 
Store them in a list and find the score of the runner-up.


Input Format
The first line contains n. The second line contains an array A[] of n 
integers each separated by a space.

Constraints
2 <= n <= 10
-100 <= A[i] <= 100

Output Format
Print runner-up score
"""

"""
Sample Input 0
5
2 3 6 6 5

Sample Output 0

5
"""

"""
Explanation 0

Given list is . The maximum score is , second maximum is . 
Hence, we print  as the runner-up score.
"""

"""
Question
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
"""
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    x = max(arr)
    y = -100
    for i in range(0,n):
        if arr[i]<x and arr[i] > y:
            y = arr[i]
    
    print(y)

"""
Sudo
With Given input n
Rearrange it in arr from Highest to lowest 
Print second highest number
"""