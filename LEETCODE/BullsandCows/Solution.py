class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        secret_count = {}

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] in secret_count:
                    secret_count[secret[i]] += 1
                else:
                    secret_count[secret[i]] = 1

        for i in range(len(guess)):
            if secret[i] != guess[i] and guess[i] in secret_count and secret_count[guess[i]] > 0:
                cows += 1
                secret_count[guess[i]] -= 1

        return f"{bulls}A{cows}B"