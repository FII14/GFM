# GFM
This program allows you to manage files in a GitHub repository using the GitHub API. You can upload a new file or delete an existing file from the repository.
## Setup
1. Install the required libraries:
  - getpass
  - requests
  - base64
2. Obtain a personal access token from GitHub with the necessary permissions to access and modify the repository.
## Usage
1. Run the program with the command `python3 gfm.py`
2. You will be prompted to enter your GitHub username and the repository name.
3. Select an action by entering the corresponding choice number:
  - `1` to upload a new file
  - `2` to delete an existing file
##  Notes
- The program uses the GitHub API to interact with the repository. It requires a valid personal access token with the necessary permissions.
- The access token should be assigned to the `token` variable in the code.
- Make sure to provide the correct username and repository name when prompted.
- When entering the file path, ensure that the file exists and the path is correct.
- The program handles basic errors and provides informative error messages in case of failures.
