#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    nameList = dir(hidden_4)

    for i in nameList:
        if i[:2] != "__":
            print(i)
