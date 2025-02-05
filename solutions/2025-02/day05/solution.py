class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        # Confirming that there are of equal length
        if len(s1) != len(s2):
            return False
        
        # If they are the same, return true
        if s1 == s2:
            return True
        
        # ensuring that they have same letter counts
        d1, d2 = {}, {}

        for i in range(len(s1)):
            d1[s1[i]] = 1 + d1.get(s1[i], 0)
            d2[s2[i]] = 1 + d2.get(s2[i], 0)

        if d1 != d2:
            return False

        # At this stage, we know we have same length, and letter composition
        # We need at most two letter displacement
        dis_count = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dis_count += 1
                if dis_count > 2:
                    return False
        return True