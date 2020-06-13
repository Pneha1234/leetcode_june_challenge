class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 1. Descending order by height 
        # 2. same hight ascending order by the number of people in front 
        people.sort(key=lambda p:(-p[0], p[1]))
        replace_people = []
        
        # Insert into the corresponding position according to the number of people in front
        for p in people:
            replace_people.insert(p[1], p)
            
        return replace_people
