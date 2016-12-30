Add and Search Word - Data structure design
=========
Design a data structure that supports the following two operations:
```
void addWord(word)
bool search(word)
```
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:
```
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```

这道题如果你之前做过前缀树的话，应该会变得很简单。

解法：我们构建一棵前缀树之后，进行查找，最主要在于处理`.`上，如果遇到的话，我们就扫一遍当前那个节点下所有的情况。

```
class TrieNode {
public:
    TrieNode *child[26];
    bool isWord;
    // Initialize your data structure here.
    TrieNode() : isWord(false) {
        for (auto &i : child) i = NULL;
    }
};

class WordDictionary {
private:
    TrieNode *root;
public:
    WordDictionary() {
        root = new TrieNode();
    }
    // Adds a word into the data structure.
    void addWord(string word) {
        TrieNode *temp = root;
        for (auto w : word) {
            int i = w - 'a';
            if (!temp->child[i]) temp->child[i] = new TrieNode();
            temp = temp->child[i];
        }
        temp->isWord = true;
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    bool search(string word) {
        return search(word, root, 0);
    }

    bool search(string &word, TrieNode *temp, int i) {
        if (i == word.size()) return temp->isWord;
        if (word[i] == '.'){
            for (auto p : temp->child) {
                if (p && search(word, p, i + 1)) return true;
            }
        } else {
            return temp->child[word[i] - 'a'] && search(word, temp->child[word[i] - 'a'], i + 1);
        }

        return false;
    }
};

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary;
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");
```

相似题目[Implement Trie (Prefix Tree)](./Implement Trie \(Prefix Tree\).md)
