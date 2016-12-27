Word Frequency
=======
Write a bash script to calculate the frequency of each word in a text file words.txt.

For simplicity sake, you may assume:

words.txt contains only lowercase characters and space ' ' characters.
Each word must consist of lowercase characters only.
Words are separated by one or more whitespace characters.
For example, assume that words.txt has the following content:
```
the day is sunny the the
the sunny is is
```
Your script should output the following, sorted by descending frequency:
```
the 4
is 3
sunny 2
day 1
```

这道题给我们一段脚本，然后让我们输出统计每个单词的出现的次数。

解法：我们可以首先用grep将单词都分解，然后进行排序，再用uniq进行统计，然后用sort对出现的次数再排序依次，最后用awk输出。
```
# Read from the file words.txt and output the word frequency list to stdout.
grep -oE '[a-z]+' words.txt | sort | uniq -c | sort -nr| awk '{print $2" "$1}'
```
