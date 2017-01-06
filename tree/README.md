# Tree


### Binary Search Tree

  * insert : use the following algorithm, to insert a key `k`
    - If the tree is empty, construct a leaf node with key = `k`
    - If `k` is equal to the key of root node, overwrite the `payload`
    - If `k` is less then the key of root node, insert it into the left child
    - If `k` is greater than the key of root node, insert it into the right child
  * traverse : use `yield` generators to perform inorder traversal
  ```python
  t.insert(1)
  t.insert(15)
  t.insert(7)
  for v in t.traverse():
      # do somethins
      pass
  ```

#### references:
  * http://stackoverflow.com/questions/29799667/using-generators-to-perform-an-inorder-tree-traversal-on-a-bst

### Tries


### Red-Black Trees

### AVL Trees
