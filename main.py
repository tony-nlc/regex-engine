class RegexEngine:
    def __init__(self, pattern):
        self.pattern = pattern

    def match(self, text):
        if self.pattern.startswith('^'):
            return self._match_helper(1, 0, text)
        else:
            for i in range(len(text) + 1):
                print(self._match_helper(0, i, text))
                if self._match_helper(0, i, text):
                    return True
            return False

    def _match_helper(self, pat_idx, txt_idx, text):
        
        if pat_idx == len(self.pattern):
            return txt_idx == len(text) or (self.pattern[-1] == '$' and txt_idx == len(text))
        
        first_match = (txt_idx < len(text) and 
                       (self.pattern[pat_idx] == text[txt_idx] or self.pattern[pat_idx] == '.'))
        if (pat_idx + 1) < len(self.pattern) and self.pattern[pat_idx + 1] == '*':
            return (self._match_helper(pat_idx + 2, txt_idx, text) or
                    (first_match and self._match_helper(pat_idx, txt_idx + 1, text)))
        
        elif (pat_idx + 1) < len(self.pattern) and self.pattern[pat_idx + 1] == '+':
            return first_match and (self._match_helper(pat_idx + 2, txt_idx + 1, text) or
                                    self._match_helper(pat_idx, txt_idx + 1, text))
        
        elif (pat_idx + 1) < len(self.pattern) and self.pattern[pat_idx + 1] == '?':
            return (self._match_helper(pat_idx + 2, txt_idx, text) or
                    (first_match and self._match_helper(pat_idx + 2, txt_idx + 1, text)))
        
        else:
            return first_match and self._match_helper(pat_idx + 1, txt_idx + 1, text)



engine2 = RegexEngine("^abcd.?")
print(engine2.match("abcd"))   # True
print(engine2.match("abcde"))  # True
print(engine2.match("ababc")) # False
