class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
         # Step 1: sort
        people.sort(key=lambda x: (-x[0], x[1]))
        
        # Step 2: insert
        queue = []
        for p in people:
            queue.insert(p[1], p)
        
        return queue
        