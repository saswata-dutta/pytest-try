from myapp.view import world

def hello():
    return f"hello {world()}"

if __name__ == "__main__":
    print(hello())
