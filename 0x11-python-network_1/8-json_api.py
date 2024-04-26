#!/usr/bin/python3

""" Search Api """

import sys
import requests


if __name__ == "__main__":

    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # Send a POST request to the URL with the letter as a parameter
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})
    
    try:
        # Parse the JSON response
        data = response.json()
        
        # Check if the JSON response is properly formatted and not empty
        if data:
            # Display the id and name
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            # Display No result if the JSON is empty
            print("No result")
    except ValueError:
        # Display Not a valid JSON if the JSON is invalid
        print("Not a valid JSON")
