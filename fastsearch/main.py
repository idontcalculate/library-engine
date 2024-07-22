from query import search_books

def main():
    query_text = "rage of angels, sidney sheldon"
    results = search_books(query_text)
    
    if not results:
        print("No results found")
    else:
        for point in results:
            title = point.payload.get('title', 'Unknown Title')
            description = point.payload.get('description', 'No description available')
            categories = point.payload.get('categories', 'Uncategorized')

            print(f"Title: {title}\nDescription: {description}\nCategories: {categories}\n---")

if __name__ == "__main__":
    main()
