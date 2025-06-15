import os


def print_tree(startpath, prefix=""):
    for item in os.listdir(startpath):
        if item == ".git" or item == "migrations" or item == "node_modules":
            continue
        path = os.path.join(startpath, item)
        if os.path.isdir(path):
            print(prefix + "├── " + item)
            print_tree(path, prefix + "│   ")
        else:
            print(prefix + "├── " + item)


print_tree(".")
