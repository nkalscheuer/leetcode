def removeKeys(s: string, held_set: dict, start: int, end: int):
    current = start
    while current <= end:
        del held_set[s[current]]
        current += 1
    
def recLengthOfLongestSubstring(s: str, held_set: dict, current_start: int, current: int,  max_sub: int) -> int:
    # First check if we've gone over the whole string:
    if current >= len(s):
        return max_sub
    #check if the next character is in the working set
    if s[current] in held_set.keys():
        # Get next char's current point in substring and skip over it
        old_point = held_set[s[current]]
        removeKeys(s, held_set, current_start, old_point)
        held_set[s[current]] = current
        current_start = old_point + 1 # Does not include old point
        # Size would only either stay the same or get smaller, so need to check for max
        return recLengthOfLongestSubstring(s, held_set, old_point + 1, current + 1, max_sub)
    else:
        # Character is not repeating, so add it to substring
        held_set[s[current]] = current
        if len(held_set) > max_sub:
            max_sub = len(held_set)
        return recLengthOfLongestSubstring(s, held_set, current_start, current + 1, max_sub)
        
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = dict()
        return recLengthOfLongestSubstring(s, substr, 0, 0, 0)
    