# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    files_cache = {}
    for file_path in files:
        file_split = file_path.split("/")
        file_key = file_split[-1]
        if file_key not in files_cache:
            files_cache[file_key] = file_path
    for query in queries:
        if query in files_cache:
            result.append(files_cache[query])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
