# Function to concatenate multiple strings using *args
def join_strings(*args):
    sum_sentence = args[0]
    for item in args[1:]:
        sum_sentence += " " + item
    return sum_sentence

if __name__ == "__main__":
    result = join_strings("Hello", "world", "this", "is", "Python!")
    print(result)  # Hello world this is Python!

    result = join_strings("Python", "is", "fun!")
    print(result)  # Python is fun!