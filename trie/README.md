# Trie

A Trie is a special form of a Nary tree. Typically, a trie is used to store strings. Each Trie node represents a string 
(a prefix). Each node might have several children nodes while the paths to different children nodes represent different 
characters. And the strings the child nodes represent will be the origin string represented by the node itself plus the 
character on the path. - Leetcode

```text
     head
     /  \
    a    b
   /    /  \
 am    ba  be
      /
    bad
```



* [Trie (Prefix Tree)](#trie-prefix-tree)

## Trie (Prefix Tree)