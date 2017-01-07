# Tree


### Binary Search Tree

  * Insert : use the following algorithm, to insert a key `k`
    - If the tree is empty, construct a leaf node with key = `k`
    - If `k` is equal to the key of root node, overwrite the `payload`
    - If `k` is less then the key of root node, insert it into the left child
    - If `k` is greater than the key of root node, insert it into the right child
  * Traverse : use `yield` generators to perform inorder traversal
  ```python
  t.insert(1)
  t.insert(15)
  t.insert(7)
  for v in t.traverse():
      # do somethings
      pass
  ```
  * Search: According to the definition of binary search tree, search a key in a tree can be realized as the following.
    - If the tree is empty, the searching fails;
    - If the key of the root is equal to the value to be found, the search succeed. The root is returned as the result;
    - If the value is less than the key of the root, search in the left child.
    - Else, which means that the value is greater than the key of the root, search in the right child.


  * Delete: delete an element in Binary Search Tree by `key`, and  keep the BST property.
    - If node have two children
      - use minimum element(`min_on_right`) of its right sub tree to replace `node.key` and `node.payload`
    - Otherwise, node have one or without any child
      - if have left child or right child, use the child replace the `node`
      - if without any child, set `node` to None
      - if the `node` is root, need update `self._root`

#### references:
  * http://stackoverflow.com/questions/29799667/using-generators-to-perform-an-inorder-tree-traversal-on-a-bst

### Tries


### Red-Black Trees

### AVL Trees
