import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description='Create a Trello card with labels and a comment.')
    parser.add_argument('board_id', type=str, help='The ID of the Trello Board.')
    parser.add_argument('list_name', type=str, help='The name of the list to add the card to.')
    parser.add_argument('card_name', type=str, help='The name of the new card.')
    parser.add_argument('card_desc', type=str, help='The description of the new card.')
    parser.add_argument('comment_text', type=str, help='The comment to add to the new card.')

if __name__ == "__main__":
    main()