class Tree(object):
    '''
    This Class defines binary tree. The only variable in this class
    is the root of the tree.
    '''
    def __init__(self, root):
        self.root = root

    def get_value_root(self):
        if self.root is not None:
            return self.root.value
        else:
            return None

    def get_depth(self):
        if self.root is None:
            return 0
        else:
            return 1 + max(Tree(self.root.left).get_depth(), Tree(self.root.right).get_depth())

    def print_tree(self):
        '''
        This function visualizes the binary tree. The result is saved in
        a list of list.
        Variables :
        "result" : the list of the list that visualizes the binary tree
        "new_level": all the tree nodes in the current level
        "old_level": all the tree nodes in the previous level
        "current_depth": the depth of the current level. The depth of the root is 1.
        '''
        result = []

        if self.get_value_root() is None:
            print('|')
            return ['|']

        depth = self.get_depth()
        space = 2 ** (depth - 1) - 1

        new_level = [self.root]
        level_string = ['|'] * space
        level_string.append(str(self.get_value_root()))
        level_string.extend(['|'] * space)
        result.append(level_string)
        current_depth = 1

        while current_depth < depth:
            old_level = new_level
            new_level = []

            for i in old_level:
                if i is None:
                    new_level.append(None)
                    new_level.append(None)
                else:
                    new_level.append(i.left)
                    new_level.append(i.right)

            space = int((float(space) + 1.0) / 2.0) - 1

            if Tree(new_level[0]).get_value_root() is None:
                level_string = ['|'] * space
                level_string.append('|')
                level_string.extend(['|'] * space)
            else:
                level_string = ['|'] * space
                level_string.append(str(Tree(new_level[0]).get_value_root()))
                level_string.extend(['|'] * space)

            for i in new_level[1:]:
                if i is None:
                    level_string.append('|')
                    level_string.extend(['|'] * space)
                    level_string.append('|')
                    level_string.extend(['|'] * space)
                else:
                    level_string.append('|')
                    level_string.extend(['|'] * space)
                    level_string.append(str(Tree(i).get_value_root()))
                    level_string.extend(['|'] * space)

            result.append(level_string)
            current_depth += 1

        return result


class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


if __name__ == '__main__':
    a = Node(2, None, None)
    b = Tree(a)

    print(b.get_value_root())
