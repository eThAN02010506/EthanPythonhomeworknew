import requests as req
# This application uses LastNameAPI created by the luminous Samuel Wu



# It should provide a comment in the code detailing which API server your code consumes
# The application, when run, should give users the ability to access any and all information from the API
# Provide a README explaining what the software does
# Please create a separate repo for this project and submit it along with the link for the API Server you built

list_url = "https://10.6.21.87:8000/lastnames"
# total_url = f"https://10.6.21.87:8000/users/{name}"


start = input("Would you like to: \n"
              "1 - Get a list of the top 20 names\n"
              "2 - Get the stat of people with one of those names\n"
              ">> ")
on = True

while on:
    if start == "1":
        url = "http://10.6.21.87:8000/names?api_key=python3class"
        response = req.get(url=url)
        json_data = response.json()
        print(json_data)
    elif start == "2":
        name = input("Which name would you like to get  the statistic on?\n"
                     ">> ")
        url = f"http://10.6.21.87:8000/lastnames/{name.capitalize()}?api_key=python3class"
        response = req.get(url=url)
        json_data = response.json()
        if "msg" in json_data:
            print(json_data["msg"])
        else:
            print(f"The last name {json_data['name']} is rank {json_data['rank']} with a total of {json_data['total']} people with it.")

    is_done = input("Is that all? yes/no\n"
                    ">> ")
    if is_done == "y" or is_done == "Y":
        on = False
    elif is_done == "n" or is_done == "N":
        pass
