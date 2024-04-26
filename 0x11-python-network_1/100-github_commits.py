#!/usr/bin/python3
"""List recent commits from a GitHub repository"""

import requests
import sys

if __name__ == "__main__":
    # Get repository name and owner name from command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Set up the URL for the GitHub API
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Send a GET request to the GitHub API to retrieve recent commits
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        commits = response.json()
        # Loop through the recent commits and print the SHA and author name
        for commit in commits[:10]:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    else:
        # Display an error message if the request was not successful
        print(f"Error: {response.status_code}")

