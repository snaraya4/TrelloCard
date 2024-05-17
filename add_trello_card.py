import argparse
import requests

#Constants for the API key and token
API_KEY = 'api_key'
TOKEN = 'token'


def get_lists_from_board(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    query = {
        'key': API_KEY,
        'token': TOKEN
    }

    response = requests.get(url, params=query)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching lists:", response.text)
        return None
    
def main():
    parser = argparse.ArgumentParser(description='Create a Trello card with labels and a comment.')
    parser.add_argument('board_id', type=str, help='The ID of the Trello Board.')
    parser.add_argument('list_name', type=str, help='The name of the list to add the card to.')
    parser.add_argument('card_name', type=str, help='The name of the new card.')
    parser.add_argument('card_desc', type=str, help='The description of the new card.')
    parser.add_argument('comment_text', type=str, help='The comment to add to the new card.')

if __name__ == "__main__":
    main()