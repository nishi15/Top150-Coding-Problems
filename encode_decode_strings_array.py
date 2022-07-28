'''
Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

'''

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        enc_str = ""
        for word in strs:
            enc_str += str(len(word))+"#"+word

        return enc_str 

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    
    def decode(self, str):
        # write your code here
        decoded_arr = []
        i =0 
        while i < (len(str)):
            try:
                if isinstance(int(str[i]),int):
                    word_len = int(str[i])
            except:
                pass

            if str[i] == "#":
                decoded_arr.append(str[i+1:word_len+i+1])
                i = word_len+i+1
            else:
                i =i +1

            


        return decoded_arr


if __name__ == "__main__":
    sol = Solution()
    enc = sol.encode(["we", "sa#id", ":q2","yes"])
    print(enc)
    res = sol.decode(enc)
    print(res)