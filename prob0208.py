"""
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
medium

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。
"""


class Node:
    def __init__(self, val):
        # val 是否有字符串以当前结尾
        self.val = val
        self.children = {}
        for c in range(ord('a'), ord('z')+1):
            self.children[chr(c)] = None


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(True)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            if node.children[w]:
                node = node.children[w]
            else:
                tmp = Node(False)
                node.children[w] = tmp
                node = node.children[w]
        node.val = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            if not node.children[w]:
                return False
            node = node.children[w]

        return node.val

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            if not node.children[w]:
                return False
            node = node.children[w]
        return True

if __name__ == '__main__':

    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))


