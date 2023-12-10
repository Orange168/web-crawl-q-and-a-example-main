
import re

# re.match() 示例
def match_example():
    pattern = r'Hello'
    string = 'Hello, how are you?'

    match = re.match(pattern, string)

    if match:
        print("re.match() - Match found:", match.group())
    else:
        print("re.match() - No match")

# re.findall() 示例
def findall_example():
    pattern = r'\d+'
    string = 'There are 10 apples and 20 oranges.'

    matches = re.findall(pattern, string)

    print("re.findall() - All matches:", matches)

# re.finditer() 示例
def finditer_example():
    pattern = r'\w+'
    string = 'This is a sample text.'

    iterator = re.finditer(pattern, string)

    print("re.finditer() - Matches found:")
    for match in iterator:
        print("  -", match.group())

# re.sub() 示例
def sub_example():
    pattern = r'\s+'
    string = 'This     is    a     test.'

    replaced_string = re.sub(pattern, ' ', string)

    print("re.sub() - Replaced string:", replaced_string)

# re.split() 示例
def split_example():
    pattern = r'\s+'
    string = 'Splitting   this  string.'

    splitted_list = re.split(pattern, string)

    print("re.split() - Splitted list:", splitted_list)

# 执行示例函数
def run_examples():
    match_example()
    findall_example()
    finditer_example()
    sub_example()
    split_example()

# 运行示例
if __name__ == "__main__":
    run_examples()
