def suggest_completions(search_history, partial_query):
    # Filter the search history to find matches that start with the partial query
    suggestions = [item for item in search_history if item.startswith(partial_query)]
    return suggestions

def main():
    search_history = [
        "apple",
        "banana",
        "carrot",
        "pear",
        "pineapple",
        "potato",
        "strawberry"
    ]

    partial_query = input("Enter your partial search query: ")
    suggestions = suggest_completions(search_history, partial_query)

    print("Suggestions:")
    for suggestion in suggestions:
        print(suggestion)

if __name__ == "__main__":
    main()
