class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if sum(skill)%(len(skill)/2)!=0:
            return -1
        balanced_skill=(sum(skill)*2)/len(skill)

        # sort

        skill.sort()

        left=0
        right=len(skill)-1
        chem=0

        while left<right:
            if skill[left]+skill[right]==balanced_skill:
                chem+=(skill[left]*skill[right])
                left+=1
                right-=1
            else:
                return -1
        return chem
        