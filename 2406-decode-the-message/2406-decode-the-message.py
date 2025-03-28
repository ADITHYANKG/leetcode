class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        index = 0

        # Build the substitution map
        for char in key:
            if char != " " and char not in mapping:
                mapping[char] = alphabet[index]
                index += 1
        
        # Decode the message
        decoded_message = ""
        for char in message:
            if char == " ":
                decoded_message += " "
            else:
                decoded_message += mapping[char]

        return decoded_message  
                

