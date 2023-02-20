class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        temp = queryIP.split('.')
        if len(temp) == 4:
            for num in temp:
                if num == '':
                    return 'Neither'
                for i in range(len(num)):
                    if not 48 <= ord(num[i]) <= 57 or (i == 0 and num[i] == '0' and len(num) > 1):
                        
                        return 'Neither'
                if not 0 <= int(num) <= 255:
                    return 'Neither'
            return 'IPv4'
        temp = queryIP.split(':')
        if len(temp) == 8:
            for num in temp:
                if not 1 <= len(num) <= 4:
                        return 'Neither'
                for i in num:
                    if not (65 <= ord(i) <= 70 or 97 <= ord(i) <= 102 or 48 <= ord(i) <= 57 ):
                        return 'Neither'
            return 'IPv6'
        return 'Neither'
                    