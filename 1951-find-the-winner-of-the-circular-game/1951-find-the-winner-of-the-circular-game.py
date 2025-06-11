class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        people = list(range(1, n + 1))
        idx = 0  # Starting index

        while len(people) > 1:
            idx = (idx + k - 1) % len(people)  # Find the index to eliminate
            people.pop(idx)  # Remove that person

        return people[0] 

        