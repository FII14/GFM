import getpass
import requests
import base64

token = '_access_token_'
username = input('Enter GitHub username: ')
repo_name = input('Enter repository name: ')

headers = {
    'Authorization': f'Token {token}'
}

# Menu options
print('\nWelcome to GitHub File Manager\n')
print('Select an action:')
print('1. Upload a new file')
print('2. Delete an existing file\n')

choice = input('Enter the choice number: ')

if choice == '1':
    file_path = input('\nEnter the file path to upload: ')

    upload_url = f'https://api.github.com/repos/{username}/{repo_name}/contents/{file_path}'

    with open(file_path, 'rb') as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode('utf-8')

        data = {
            'message': 'Upload file',
            'content': encoded_content
        }

        response = requests.put(upload_url, headers=headers, json=data)

        if response.status_code == 201:
            print('File successfully uploaded to GitHub.')
          
        else:
            print('Failed to upload file to GitHub.')

elif choice == '2':
    contents_url = f'https://api.github.com/repos/{username}/{repo_name}/contents'

    # Get a list of all files in the repository
    response = requests.get(contents_url, headers=headers)
    if response.status_code == 200:
        content_data = response.json()
        if isinstance(content_data, list):
            if len(content_data) > 0:
                print('\nExisting files in the repository:')
                for file_info in content_data:
                    file_name = file_info.get('name')
                    print(f'- {file_name}')

                file_path = input('\nEnter the file to delete: ')
                delete_url = f'https://api.github.com/repos/{username}/{repo_name}/contents/{file_path}'

                # Check if the file exists in the repository
                response = requests.get(delete_url, headers=headers)
                if response.status_code == 200:
                    delete_data = {
                        'message': 'Delete file',
                        'sha': response.json().get('sha')
                    }

                    delete_response = requests.delete(delete_url, headers=headers, json=delete_data)

                    if delete_response.status_code == 200:
                        print('File successfully deleted from GitHub.')
                    else:
                        print('Failed to delete file from GitHub.')
                else:
                    print('File not found on GitHub.')
            else:
                print('No files found in the repository.')
        else:
            print('Failed to retrieve file information from GitHub.')
    else:
        print('Failed to fetch file information from GitHub.')

else:
    print('Invalid choice')
