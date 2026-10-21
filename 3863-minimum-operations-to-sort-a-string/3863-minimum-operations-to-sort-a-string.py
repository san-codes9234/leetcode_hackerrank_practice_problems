class Solution:
    def minOperations(self, s: str) -> int:
        target = "".join(sorted(s))
        
        # 0 Operations: already fully sorted
        if s == target:
            return 0
            
        # Impossible to sort: length <= 2 and not sorted
        if len(s) <= 2:
            return -1
            
        # 1 Operation: an extreme is already in its correct sorted position
        # Meaning we can safely exclude that extreme and sort the remaining unsorted block
        if s[0] == target[0] or s[-1] == target[-1]:
            return 1
            
        # 3 Operations: The bottleneck case
        # Prefix -> Suffix sort works IF the absolute minimum can be moved to index 0 via the prefix.
        # Suffix -> Prefix sort works IF the absolute maximum can be moved to index N-1 via the suffix.
        # If neither is possible (meaning min is ONLY at the end, and max is ONLY at the start):
        if min(s[:-1]) != target[0] and max(s[1:]) != target[-1]:
            return 3
            
        # 2 Operations: all other cases can be solved via (Prefix -> Suffix) or (Suffix -> Prefix)
        return 2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna