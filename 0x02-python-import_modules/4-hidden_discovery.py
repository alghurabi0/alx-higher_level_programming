#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    info = dir(hidden_4)
    for name in info:
        if name[:2] != '__':
            print(name)
