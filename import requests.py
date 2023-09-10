import requests

def fetch_startup_news(api_key):
    # Define the News API URL
    url = "https://newsapi.org/v2/top-headlines"
    
    # Define the query parameters
    params = {
        "country": "in",  # India
        "category": "business",
        "q": "startup",
        "apiKey": api_key,
        "pageSize": 5
    }

    try:
        # Send a GET request to the News API
        response = requests.get(url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])

            # Display the headlines
            for index, article in enumerate(articles, start=1):
                print(f"{index}. {article['title']}")
                print(article['description'])
                print(article['url'])
                print("\n")

        else:
            print(f"Failed to fetch news. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    api_key = 'apikey'
    fetch_startup_news(api_key)
