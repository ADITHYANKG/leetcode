class Solution:
    def maximum69Number (self, num: int) -> int:
          # Convert the number to a list of characters for easy manipulation
        num_str = list(str(num))

        # Find the first occurrence of '6' and change it to '9'
        for i in range(len(num_str)):
            if num_str[i] == '6':
                num_str[i] = '9'
                break

        # Convert the modified list back to an integer and return it
        return int(''.join(num_str))