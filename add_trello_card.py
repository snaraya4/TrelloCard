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
    
def add_comment_to_card(card_id, comment_text):
    url = f"https://api,trello.com/1/cards/{card_id}/actions/comments"
    query = {
        'key': API_KEY,
        'token': TOKEN,
        'text':comment_text
    }

    response = requests.post(url, data=query)
    if response.status_code == 200:
        print("Comment added successfully.")
    else:
        print("Error adding comment:", response.text)

def create_label(board_id, label_name, label_color):
    url = f"https://api.trello.com/1/boards/{board_id}/labels"
    query = {
        'key': API_KEY,
        'token': TOKEN,
        'name': label_name,
        'color': label_color
    }

    response = requests.post(url, data=query)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error creating label:", response.text)
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