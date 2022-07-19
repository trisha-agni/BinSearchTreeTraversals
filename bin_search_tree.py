class BinTreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class BSTree:
  def __init__(self, the_list):
    the_list.sort()
    print('Creating binary search tree from sorted list: {}'.format(the_list))
    self.root = self._create_tree(the_list, 0, len(the_list)-1)

  def _create_tree(self, the_list, l_idx, r_idx):
    if r_idx < l_idx:
      return None
    mid = l_idx + (r_idx-l_idx)//2
    root = BinTreeNode(the_list[mid])
    root.left = self._create_tree(the_list, l_idx, mid-1)
    root.right = self._create_tree(the_list, mid+1, r_idx)
    return root
