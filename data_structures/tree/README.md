# Tree


### Binary Search Tree

  * Construct : build a balanced Binary Search Tree from an array
    - If the array is unordered, shuffle the elements before build to BST, insert one by one, to make a balanced tree.
    - If the array is sorted, works link binary search
![    ](../../resources/optimal-binary-search-tree-from-sorted-array.gif)



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
  * Predecessor: make BinarySearchTree supports the iterator protocol
  ```python
  t = BinarySearchTree()
  t.insert(32)
  t.insert(25)
  t.insert(43)
  #...
  for v in t:
    print v
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


### Red-Black Trees
Red-black tree is a type of self-balancing binary search tree[3]. 2 By using color changing and rotation, red-black tree provides a very simple and straightforward way to keep the tree balanced.
Every node is either red or black.
  * The root is black.
  * Every leaf (NIL) is black.
  * If a node is red, then both its children are black.
  * For each node, all paths from the node to descendant leaves contain the same number of black nodes.

### AVL Trees
An **AVL tree** is a binary search tree that is height balanced: for each node `x`, the heights of the left and right subtrees of `x` differ by at most 1.
  * Insert
  * Delete

### Tries

#### references:
  * http://stackoverflow.com/questions/29799667/using-generators-to-perform-an-inorder-tree-traversal-on-a-bst
  * https://github.com/liuxinyu95/AlgoXY
