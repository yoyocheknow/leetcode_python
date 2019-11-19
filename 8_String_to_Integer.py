# -*- coding:utf-8 -*-


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_list = []
        Max_int = 2 ** 31 - 1
        Min_int = -1 * (2 ** 31)

        start, sign, temp_i, res = False, 1, 0, 0
        for i in range(len(str)):
            try:
                temp_i = int(str[i])
            except:
                if (i == 0 or len(int_list) == 0) and str[i] == '-' and not start:
                    sign = -1
                    start = True
                elif (i == 0 or len(int_list) == 0) and str[i] == '+' and not start:
                    sign = 1
                    start = True
                else:
                    if len(int_list) == 0 and str[i] == ' ' and not start:
                        continue
                    elif len(int_list) == 0:
                        return 0
                    else:
                        break
                continue

            int_list.append(temp_i)
        mi = len(int_list)
        for i in range(len(int_list)):
            res += int_list[i] * (10 ** (mi - 1))
            mi -= 1
        res = res * sign
        if res > Max_int:
            return Max_int
        if res < Min_int:
            return Min_int
        return res


if __name__ == "__main__":
    r = Solution().myAtoi("-2 34")
    print r