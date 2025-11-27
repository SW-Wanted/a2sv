class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child_i = 0; cookie_i = 0; content_children = 0
        
        while child_i < len(g) and cookie_i < len(s):
            if s[cookie_i] >= g[child_i]:
                content_children += 1
                child_i += 1
            cookie_i += 1
            
        return content_children