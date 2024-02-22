class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if(n==1):
            return 1
        disqualified = set()
        judge_candidates = defaultdict(int)

        total = 0
        for relation in trust:
            disqualified.add(relation[0])
            judge_candidates[relation[1]] += 1
        
        for candidate in judge_candidates:
            if(candidate not in disqualified and judge_candidates[candidate]==n-1):
                return candidate
        
        return -1

        