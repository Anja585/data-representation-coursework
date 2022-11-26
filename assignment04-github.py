from github import Github

# access token
token = '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'

# authenticate yourself 
g = Github("Anja585", token)

# find your repository and path of test_file.txt
repo=g.get_user().get_repo("aprivateone")
file = repo.get_contents("test_file.txt")


content = bytes('Andrew','UTF-8')
# find words Andrew in test_file.txt
if content in file.decoded_content:
    content = 'Anja' 
    # replace with new content 
    repo.update_file("test_file.txt", "update", content, file.sha)
