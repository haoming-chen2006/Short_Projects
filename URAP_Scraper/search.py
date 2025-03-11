import csv

def search_projects(keyword):
    results = []
    with open('URAP_Data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (keyword.lower() in row['Title'].lower() or
                keyword.lower() in row['Professor'].lower() or
                keyword.lower() in row['Weekly Hours'].lower() or
                keyword.lower() in row['Main Text'].lower()):
                results.append(row)
    return results

def display_results(results):
    if results:
        for result in results:
            print(f"Title: {result['Title']}")
            print(f"Professor: {result['Professor']}")
            print(f"Weekly Hours: {result['Weekly Hours']}")
            print(f"Description: {result['Main Text']}")
            print("-" * 40)
    else:
        print("No projects found with the given keyword.")

def main():
    keyword = input("Enter a keyword to search for projects: ")
    results = search_projects(keyword)
    display_results(results)

if __name__ == "__main__":
    main()
search_projects("inequality")