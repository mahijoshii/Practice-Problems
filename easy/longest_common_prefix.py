class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:
            prefix = strs[0]
            for word in strs[1:]:
                while not word.startswith(prefix):
                    prefix = prefix[:-1] # loop through and remove last character until equal
                    if prefix == "":
                        return ""
            return prefix