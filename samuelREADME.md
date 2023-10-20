It should describe what type of data or behavior your API can accomplish for them
- This API will provide them with the top 20 most popular last names in
America as well as the population of each name

Directions on how to access said data
- In the URL, after /users/, enter the name that you are looking for. This will return
how popular the name is and the population holding the name.

Provide an API key for authenticating their request
python3class

Should have directions for at least two routes
/users/Smith
/users/Thomas


<h1 align="center">
  <br>
  LastNameAPI
  <br>
</h1>
<p align="center">
  <a href="https://cdn.discordapp.com/attachments/1091738497532055573/1161866254999625738/2151c451103fee2ade0bf517ef86123.jpg?ex=6539db45&is=65276645&hm=7a857f418ff0f58e5c750284672ceb6899e397983f433279d097bb4dc779c109&">
    <img src="https://cdn.discordapp.com/attachments/1091738497532055573/1161866254999625738/2151c451103fee2ade0bf517ef86123.jpg?ex=6539db45&is=65276645&hm=7a857f418ff0f58e5c750284672ceb6899e397983f433279d097bb4dc779c109&" width="200">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •

## Key Features

* Name - Gives a list of most popular last names in the US

* Rank - Gives the rank of how popular that particular name is
  


## How To Use

To run this API, you need to have an API key.

Here is the current API key:

- python3class

Then, use that API key to properly load these paths listed below.

Directions for using the API key are included in the Note at the bottom
```
# Get a list of the available last names
/top20-last-names
```
```
# Get the stats of a specific last name from the list
/top20-last-names/{last_name}

# parameter {last_name}: this is where you put your name of choice
```
```
# Get the average IQ of the last name that is passed
/top20-last-names/{last_name}/average_iq

# parameter {last_name}: this is where you put your name of choice
```

## Example:
```
10.6.20.72:8000/top20/rush/average_iq?api_key=1234567890



# Will return with:

{
      "name": "Rush",
      "in_america": "107 thousand"
}
```



‎
> **Note**
> 
>Be sure to end your route with the API key like this: ?api_key={API_KEY}
>* If you do not use one of the API keys provided, the API will not work.


