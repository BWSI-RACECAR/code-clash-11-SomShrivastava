"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #11 -  Increasing Subsequence (increasingsubsequence.py)


Author: Ali Qattan

Difficulty Level: 9/10


Prompt:Alex was preparing for the Grand Prix race. As part of their training
, they had to work on their RACECAR. The car was equipped with a unique engine
that required a specific sequence of instructions to achieve the maximum speed. 
Alex received a series of random numbers, representing the instructions for the
car's engine, but they were in no particular order. Each number indicated the 
intensity of a specific action required to optimize the RACECAR's performance. 
However, Alex knew that only by arranging the instructions in increasing order 
would they be able to unlock the car's true potential and achieve the longest 
sequence of increasing intensities. Realizing the significance of arranging the
instructions correctly, Alex decided to write a Python function to determine the 
length of the longest increasing subsequence of instructions. This function would 
take an array of integers as input and return the length of the longest increasing 
subsequence.


Test Cases: 
Input: [9, 7, 5, 3, 1] Output: 1

Input: [1, 3, 5, 7, 9] Output: 5

Input: [3, 1, 4, 1, 5, 9, 2, 6, 5], Output: 4


"""
class Solution:
    def find_longest_increasing_subsequence(self, arr):
        length = len(arr)
        if length == 0:
            return 0

        lis = [1] * length

        for i in range(1, length):
            for j in range(i):
                if arr[i] > arr[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        return max(lis)


def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.find_longest_increasing_subsequence(array)
    print(ans)

if __name__ == "__main__":
    main()
