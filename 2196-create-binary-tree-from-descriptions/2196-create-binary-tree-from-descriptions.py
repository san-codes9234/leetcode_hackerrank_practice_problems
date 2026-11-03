class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for p, c, isLeft in descriptions:
            if p not in nodes: nodes[p] = TreeNode(p)
            if c not in nodes: nodes[c] = TreeNode(c)
            if isLeft:
                nodes[p].left  = nodes[c]
            else:
                nodes[p].right = nodes[c]
            children.add(c)

        # Root = only node that is never a child
        for val, node in nodes.items():
            if val not in children:
                return node

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna