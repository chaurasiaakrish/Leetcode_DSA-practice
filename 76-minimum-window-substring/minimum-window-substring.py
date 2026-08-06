class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Edge case
        if len(s) < len(t):
            return ""

        # Frequency map of t
        t_freq = {}
        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0) + 1

        # Sliding window frequency
        s_freq = {}

        left = 0

        min_len = float("inf")
        ans = ""

        # Expand the window
        for right in range(len(s)):

            # Add current character
            s_freq[s[right]] = s_freq.get(s[right], 0) + 1

            # Check if current window is valid
            valid = True

            for ch in t_freq:

                # If any required character is missing
                # or appears fewer times than required
                if s_freq.get(ch, 0) < t_freq[ch]:
                    valid = False
                    break

            # If valid, try shrinking
            while valid:

                # Update answer
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left:right + 1]

                # Remove left character
                s_freq[s[left]] -= 1

                if s_freq[s[left]] == 0:
                    del s_freq[s[left]]

                left += 1

                # Check validity again after shrinking
                valid = True

                for ch in t_freq:
                    if s_freq.get(ch, 0) < t_freq[ch]:
                        valid = False
                        break

        return ans