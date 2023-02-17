"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1: 输入: s = "anagram", t = "nagaram" 输出: true

示例 2: 输入: s = "rat", t = "car" 输出: false

说明: 你可以假设字符串只包含小写字母
"""

def solution(s: str, t: str) -> bool:
    # 构建哈希表
    record = [0] * 26
    for i in s:
        record[ord(i) - ord("a")] += 1

    for j in t:
        record[ord(j) - ord("a")] -= 1

    return record == [0] * 26


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    result = solution(s, t)
    print(result)
