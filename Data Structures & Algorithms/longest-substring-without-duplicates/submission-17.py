class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            best_lenght = 1 if s else 0

            l = 0
            seen = {}
            # only start comparing in the second element
            for r in range(len(s)):
                if s[r] in seen:
                    # found a duplicate

                    if l <= seen[s[r]]:
                        # if the duplicate is to the right of l, move l to position right after duplicate
                        # duplicate posistion is where it was last seen
                        l = seen[s[r]] + 1
                    else:
                        # else ignore this duplicate it is not in the substring
                        pass
                else:
                    # if not a duplicate (we have never seen it)
                    # continue to the next iteration
                    pass

                # Execute every iteration:

                # current length of the substring
                length = r - l + 1
                # we want to keep track of the best length
                if best_lenght < length:
                    # the new champion arises
                    best_lenght = length
                print(length)
                # mark current char as seen and save its index
                # if it was already there it means then we are just updating the latest index,
                # which should be also fine
                seen[s[r]] = r
            return best_lenght
