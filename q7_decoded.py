"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def decoded_count(message):

    if not message:
        return 0
    
    dp = [0 for x in range(len(message)+1)]

    # base case for string of length 0 number of decodings =1
    dp[0] = 1

    # number of ways to decode message of length 1 = 1
    dp[1] = 0 if message[0]=='0' else 1

    for i in range(2, len(message)+1):
        # check one step before the third character
        if 0< int(message[i-1:i]) < 9:
            dp[i] += dp[i-1]
        
        # check two steps before the third character
        if 10 <= int(message[i-2:i]) < 27:
            dp[i] += dp[i-2]

    return dp[len(message)]

assert decoded_count("81") == 1
assert decoded_count("11") == 2
assert decoded_count("111") == 3
assert decoded_count("1111") == 5
assert decoded_count("1311") == 4