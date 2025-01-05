class TreeNode:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display_tree(self, level=0):
        indent = " " * (level * 4)
        print(f"{indent}{self.name}: {self.data}")
        for child in self.children:
            child.display_tree(level + 1)

# Example usage
root = TreeNode("Waste Management System")

city_a = TreeNode("City A", {"priority": 3, "orders": 10})
city_b = TreeNode("City B", {"priority": 1, "orders": 5})
city_c = TreeNode("City C", {"priority": 2, "orders": 8})

root.add_child(city_a)
root.add_child(city_b)
root.add_child(city_c)

recycling_a = TreeNode("Recycling", {"facilities": 2})
waste_collection_a = TreeNode("Waste Collection", {"trucks": 5})
city_a.add_child(recycling_a)
city_a.add_child(waste_collection_a)

recycling_b = TreeNode("Recycling", {"facilities": 1})
waste_collection_b = TreeNode("Waste Collection", {"trucks": 3})
city_b.add_child(recycling_b)
city_b.add_child(waste_collection_b)

recycling_c = TreeNode("Recycling", {"facilities": 3})
waste_collection_c = TreeNode("Waste Collection", {"trucks": 4})
city_c.add_child(recycling_c)
city_c.add_child(waste_collection_c)

root.display_tree()
