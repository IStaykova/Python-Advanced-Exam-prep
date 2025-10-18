def classify_books(*args, **kwargs):
    fiction_books = {}
    non_fiction_book = {}

    reversed_kwargs = {v: k for k, v in kwargs.items()}

    for genre, name in args:
            if genre == "fiction":
                fiction_books[name] = reversed_kwargs[name]
            else:
                non_fiction_book[name] = reversed_kwargs[name]

    sorted_fiction_books = sorted(
        fiction_books.items(), key=lambda x: x[1]
    )
    sorted_non_fiction_books = sorted(
        non_fiction_book.items(), key=lambda  x: x[1], reverse=True
    )
    result = []
    if sorted_fiction_books:
        result.append("Fiction Books:")
        for name, code in sorted_fiction_books:
            result.append(f"~~~{code}#{name}")
    if sorted_non_fiction_books:
        result.append("Non-Fiction Books:")
        for name, code in sorted_non_fiction_books:
            result.append(f"***{code}#{name}")
    return "\n".join(result)


print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
print("-------------------------")
print(classify_books(
    ("non_fiction", "The Art of War"),
    ("fiction", "The Great Gatsby"),
    ("non_fiction", "A Brief History of Time"),
    ("fiction", "Brave New World"),
    FF1234HH="The Great Gatsby",
    NF3845UU="A Brief History of Time",
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
print("-------------------------")
print(classify_books(
    ("fiction", "Brave New World"),
    ("fiction", "The Catcher in the Rye"),
    ("fiction", "1984"),
    FICCITRZZ="The Catcher in the Rye",
    FIC1984XX="1984",
    FICBNWYYY="Brave New World"
))




