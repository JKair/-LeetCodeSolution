Implement Trie (Prefix Tree)
=======
Implement a trie with insert, search, and startsWith methods.

这道题让我们实现前缀树。

解法：所谓Trie是一种数据结构，很重要的结构之一，用在搜索方面是可以节省很多空间的数。

本题的前缀树核心思想就是利用字符串的前缀一样的情况，不重复存储前缀，在产生不同的时候才开一个分叉，字母的话是26叉树，同理，我们所有的数也可以是10叉数。具体介绍的话，请详看[这篇文章](http://blog.csdn.net/hackbuteer1/article/details/7964147)。前缀树和后缀树本质上是差不多的。

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

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    void insert(string word) {
        TrieNode *temp = root;
        for (auto w : word) {
            int i = w - 'a';
            if (!temp->child[i]) temp->child[i] = new TrieNode();
            temp = temp->child[i];
        }
        temp->isWord = true;
    }

    // Returns if the word is in the trie.
    bool search(string word) {
        TrieNode *temp = root;
        for (auto w : word) {
            int i = w - 'a';
            if (!temp->child[i]) return false;
            temp = temp->child[i];
        }

        return temp->isWord;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(string prefix) {
        TrieNode *temp = root;
        for (auto p : prefix) {
            int i = p - 'a';
            if (!temp->child[i]) return false;
            temp = temp->child[i];
        }

        return true;
    }

private:
    TrieNode* root;
};

// Your Trie object will be instantiated and called as such:
// Trie trie;
// trie.insert("somestring");
// trie.search("key");
```
