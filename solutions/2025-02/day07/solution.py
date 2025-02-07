class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        cur_win = set()  # track characters in the current window

        while r < len(s):
            if s[r] not in cur_win:
                cur_win.add(s[r])
                longest = max(longest, r - l + 1)
                r += 1  # expand the window
            else:
                cur_win.remove(s[l])
                l += 1  # shrink the window

        return longest