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
    
def create_card(list_id, card_name, card_desc):
    url = "https://api.trello.com/1/cards"
    query = {
        'key': API_KEY,
        'token': TOKEN, 
        'idList': list_id,
        'name': card_name,
        'desc': card_desc
    }

    response = requests.post(url, data=query)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error creating card:", response.text)
        return None
    
def main():
    parser = argparse.ArgumentParser(description='Create a Trello card with labels and a comment.')
    parser.add_argument('board_id', type=str, help='The ID of the Trello Board.')
    parser.add_argument('list_name', type=str, help='The name of the list to add the card to.')
    parser.add_argument('card_name', type=str, help='The name of the new card.')
    

if __name__ == "__main__":
    main()