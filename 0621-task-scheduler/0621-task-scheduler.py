class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0 for _ in range(26)]
        for t in tasks:
            freq[ord(t) - ord('A')] += 1
        
        pq = [-f for f in freq if f>0]
        heapq.heapify(pq)

        interval = 0
        while pq:
            cycle = n+1
            temp = []
            task_count = 0
            while(cycle>0 and pq):
                current_freq = -heapq.heappop(pq)
                if(current_freq>1):
                    temp.append(-(current_freq-1))
                task_count += 1
                cycle -=1
            for t in temp:
                heapq.heappush(pq, t)
            
            interval += task_count if not pq else n+1
        
        return interval