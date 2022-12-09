class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        resInd = 0
        for idx,c in enumerate(strs[0]):
            
            resInd = idx
            
            for i in range(1, len(strs)):
                
                if len(strs[i]) - 1 < idx or strs[i][idx] != c:
                    return strs[0][:idx]
        
        return strs[0]