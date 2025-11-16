class Node:
    def __init__(self, char, weight, left=None, right=None):
        self.char = char
        self.weight = weight
        self.left = left
        self.right = right

    def __lt__(self, other):
        return other.weight > self.weight

    def getCode(self, char, parentPath):
        if self.char == char:
            return parentPath

        if self.left:
            left_path = self.left.getCode(char, parentPath + "0")
            if left_path:
                return left_path

        if self.right:
            right_path = self.right.getCode(char, parentPath + "1")
            if right_path:
                return right_path


        return None



def countTable(msg: str) -> dict[str, int]:
    dict_table = {}
    for char in msg:
        if char in dict_table:
            dict_table[char] += 1
        else:
            dict_table[char] = 1

    return dict_table

def huffman(nodes: list[Node]) -> Node:
    while len(nodes) > 1:
        nodes.sort()

        left = nodes.pop(0)
        right = nodes.pop(0)

        parent = Node(None, left.weight + right.weight, left, right)

        nodes.append(parent)

    return nodes[0]

def encode(msg: str) -> tuple[str, dict[str, str]]:
    count_table = countTable(msg)

    nodes = []

    for char, weight in count_table.items():
        nodes.append(Node(char, weight))

    no = huffman(nodes)

    code_table = {}
    for i in count_table.keys():
        code_table[i] = no.getCode(i, "")

    encoded_msg = ""

    for i in msg:
        encoded_msg += code_table[i]

    return encoded_msg, code_table

def decode(encoded: str, table: dict[str, str]) -> str:
    left = 0
    values = table.values()

    decoded_msg = ""

    for i in range(len(encoded)):
        cur = encoded[left:i+1]
        for key, values in table.items():
            if values == cur:
                decoded_msg += key
                left = i + 1
                break

    return decoded_msg


def encode_file(filepath):
    with open(filepath, "r") as f_read:
        content = f_read.read()
        encoded_str, table = encode(content)
        with open("encoded.huff", "w") as f_write:
            f_write.write(f'{len(table)}\n')
            for key, values in table.items():
                f_write.write(key + ":" + values + "\n")
            f_write.write(encoded_str)


def decode_file(filepath):
    with open(filepath, "r") as f_read:
        ln = f_read.readline()
        table = {}
        for _ in range(int(ln)):
            line = f_read.readline()
            key, value = line.split(":")
            table[key] = value[0:len(value) - 1]
        content = f_read.read()
        decoded_str = decode(content, table)
        with open("decoded.txt", "w") as f:
            f.write(decoded_str)

string, table = encode("Hello fsdfdfsdfsdfsdfsdfsdfsdfdsfsdfdsfWorld")

decoded_string = decode(string, table)
print(decoded_string)


encode_file("file.txt")
decode_file("encoded.huff")

