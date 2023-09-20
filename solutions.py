#Maximum Ice Cream Bars#
class Solution(object):
    def maxIceCream(self, costs, coins):
        sum_ = 0
        costs.sort()
        for i in range(len(costs)):
            if costs[i] == coins:
                return 1
            sum_ += costs [i]
            if sum_ > coins:
                return i
        return len(costs)
#Distribute Candies to People#
class Solution(object):
    def distributeCandies(self, candies, num_people):
        l = [0] * num_people
        i = 1
        while candies > 0:
            if candies > i:
                l[(i - 1) % num_people] += i
            else:
                l[(i - 1) % num_people] += candies
            candies -= i
            i += 1
        return l
#Valid Anagrams#
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict1 = dict({})
        for i in s:
            if dict1.get(i) == None:
                dict1[i] = 1
            else:
                dict1[i] +=1
        for i in t:
            if dict1.get(i) == None:
                dict1[i] = 1
            else:
                dict1[i] -= 1
        for i in dict1:
            if dict1[i] != 0:
                return False
            else:
                continue
        return True
#Maximum Number of Words Found in Sentences#
class Solution(object):
    def mostWordsFound(self, sentences):
        answer = 0
        for i in sentences:
            array = i.split()
            if len(array) > answer:
                answer = len(array)
            else:
                continue
        return answer
