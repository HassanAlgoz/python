from dataclasses import dataclass
from typing import Union, List


def breadth_first_search(tree):
    frontier = []
    def traverse(current):
        while (node := frontier.pop()):
            print(node.get('value', None))
            traverse(node)
            for node in node.get('children', []):
                frontier.append(node)
    frontier.append(tree)
    traverse(tree)

def depth_first_search(tree):
    frontier = []
    def traverse(current):
        while (node := frontier.pop()):
            for node in node.get('children', []):
                frontier.append(node)
            traverse(node)
            print(current.get('value', None))
    traverse(tree)


tree = dict(value='0', children=[
    dict(value='01', children=[dict(value='011'), dict(value='012'), dict(value='013')]),
    dict(value='02', children=[dict(value='021'), dict(value='022'), dict(value='023')]),
])

print("BFS:")
breadth_first_search(tree)

# print('=' * 50)

# print("DFS:")
# depth_first_search(tree)