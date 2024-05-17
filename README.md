# Trello CLI - Add Trello Card

This Python CLI (Command Line Interface) program allows you to connect to the Trello API and create cards with comments and labels.

## Usage

py add_trello_card.py <board_id> <list_name> <card_name> <card_description> <card_comment>

To include multiple words with spaces in the positional arguments (e.g., <list_name>), enclose them in double quotes "".

## Running Instructions

Run the Script:
After running the script with the provided command, the program will prompt you to enter additional information interactively.

Enter Label Information:
After providing the required information for the card, you will be asked to input label information. You can add multiple labels by entering the label name and color one by one. If you do not need to add labels, simply press "q" to exit.

## Example

py add_trello_card.py board123 "To Do" "Implement Feature" "Add a new feature to the application" "This is a comment for the new card"

## Note

### Make sure you have the necessary permissions and API key/token to access your Trello account and boards.
To obtain your API key and token for Trello, follow these steps:

1. Visit the Trello website (https://trello.com/) and log in to your account.
2. Once logged in, go to the (https://trello.com/app-key) in your browser.
3. On the developer page, follow the instructions to generate a new key. 
4. Clicking on the "Token" link next to the API KEY will take you to a new page where you can generate a token. Follow the instructions and grant the necessary permissions. Once done, you'll receive a token.
5. Copy both your API key and token and store them in a .env file.


### To get the board_id from your Trello account, you can follow these steps:

1. Go to the Trello website (https://trello.com/) and log in to your account.
2. Navigate to the board for which you want to obtain the board_id.
3. Look at the URL in your browser's address bar while viewing the board. The URL will look something like this:
   https://trello.com/b/board_id/board_name
4. The board_id is the unique identifier for the board and is part of the URL. It comes after the /b/ segment. For example, if the URL is https://trello.com/b/abc123/board_name, then abc123 is the board_id.


## Future Developments

1. Add functionality to create boards and lists.
2. Add functionality to interact with other features of the card.
3. Manage edge cases for label creation such as identifying duplicates.


## References 

1. What is Trello.com?
2. How to obtain Trello API?
3. What are Power-ups?

Total time spent: 4hrs