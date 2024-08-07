# GameSay

![GameSay](https://live.staticflickr.com/65535/53627602682_e5173a5508_z.jpg)

Welcome to GameSay!

Game reviews by gamers for gamers!

This game review app provides people a space to share their experiences, insights, and opinions on their favorite games. Whether you're seeking recommendations or want to contribute your own reviews!

Sign up today to have your say on your favorite (or not so favorite) video games!

The live website can be found [here](https://gamesay-0e0d80bdb72b.herokuapp.com/)

---

## User Experience

- Purpose of Project
- User Stories
- Web Design
- Wire frames

### Purpose of Project -

Many video game sites often overwhelm users with an abundance of content, including irrelevant information and intrusive promotional pop-ups. This project aims to streamline the video game consumer's experience, by cutting through the noise and focusing on the essential info of a video game, in particular if it's worth playing or not.

Value to Users:
- Community-driven Reviews: Users can read reviews from fellow gamers, offering insight and opinions on different games.
- Streamlined User Experience: The application's clean and modern design ensures a user-friendly experience, minimizing distractions and focusing on essential information.
- Convenient Accessibility: With features like search functionality and detailed game information, users can easily find the games they're interested in and contribute reviews.
- User Engagement: Through functionalities like user profiles and the ability to edit or delete reviews, GameSay encourages user engagement and interaction within the gaming community.

---

### User Stories -

1. As a user, I want to be able to browse a variety of game reviews to discover new games.

![](https://live.staticflickr.com/65535/53627735723_478111bea3_z.jpg) ![](https://live.staticflickr.com/65535/53627865209_4b3cf5022f_z.jpg)

2. As a user, I want to be able to search for specific games.

![](https://live.staticflickr.com/65535/53627536036_196203b983_z.jpg) ![](https://live.staticflickr.com/65535/53627536091_c967500d93_z.jpg)

3. As a user, I want to be able to view detailed information about each game, including screenshots and release date.

![](https://live.staticflickr.com/65535/53626643642_8e7283e1c0_c.jpg) ![](https://live.staticflickr.com/65535/53626643602_fcc7d06b5f.jpg)

4. As a user, I want to be able to add my own reviews for games I've played.

![](https://live.staticflickr.com/65535/53626643567_b4bab65449.jpg)

5. As a user, I want to be able to edit or delete my own reviews.

![](https://live.staticflickr.com/65535/53627865064_301df6c502_z.jpg) ![](https://live.staticflickr.com/65535/53627865074_b23dc909d5_z.jpg)

6. As a user, I want to be able to see reviews from other users to help me decide whether to play a game.

![](https://live.staticflickr.com/65535/53627979010_b3bc2d3b98_z.jpg)

7. As a user, I want to be able to create an account and log in.

![](https://live.staticflickr.com/65535/53627535891_2f4f18fdce_z.jpg) ![](https://live.staticflickr.com/65535/53627893894_0b35e792f9_z.jpg)

---

### Web Design -

#### Visual Aesthetic:

The app embodies a sleek and incisive design, focusing on a clean, simple, and modern aesthetic that reflects a user-friendly experience. 

#### Color Scheme:

The color palette is vibrant and dynamic, mirroring the energy and excitement synonymous with video games, while also maintaining a sense of user-friendliness.

#### Typography:

The app exclusively uses Roboto. By adopting a clean and accessible font, the design reflects contemporary trends while also ensuring readability.

---

### Wireframes:

The site's wireframes were made with balsamiq wireframes.

| Home Page:                  |     |
| --------------------------- | --- |
| ![Home Page](https://live.staticflickr.com/65535/53627339159_fb88714f31_b.jpg) |     |

| Sign Up Page:               |     |
| ------------------------ | --- |
| ![Sign Up Page](https://live.staticflickr.com/65535/53627208918_c2544f1cc7_b.jpg) |     |

| Login Page:               |     |
| ------------------------------- | --- |
| ![Login Page](https://live.staticflickr.com/65535/53627208903_554d9cb9ac_b.jpg) |     |

| Add Review Page:             |     |
| --------------------- | --- |
| ![Add Review Page](https://live.staticflickr.com/65535/53626115127_72bebb6e05_b.jpg) |     |

| Browse Reviews Page:                |     |
| ------------------------- | --- |
| ![Browse Page](https://live.staticflickr.com/65535/53627208893_002ef1d728_b.jpg) |     |

| Profile Page:               |     |
| ---------------------- | --- |
| ![Profile Page](https://live.staticflickr.com/65535/53627339099_2c99260236_b.jpg) |     |

| Search Game Page:               |     |
| ---------------------- | --- |
| ![Search Game Page](https://live.staticflickr.com/65535/53627208888_655478410c_b.jpg) |     |

| Search Results Page:               |     |
| ---------------------- | --- |
| ![Search Results Page](https://live.staticflickr.com/65535/53626115122_3276843fc8_b.jpg) |     |

---

## Website Features

- **User Authentication:**
  - Users can sign up with a username and password.
  - Existing users can log in securely.
  
- **User Profiles:**
  - Each user has a profile page where they can see their reviews.
  - Pagination is implemented for the user's reviews.
  
- **Review System:**
  - Users can add reviews for games.
  - Reviews include a rating and written review.
  
- **Game Information:**
  - Users can search for games.
  - Detailed information about games is fetched from the RAWG API, including description, release date, genres, developers, publishers, platforms, and tags.
  
- **Game Reviews:**
  - Users can view reviews for specific games.
  - Reviews are paginated.
  
- **Editing and Deleting Reviews:**
  - Users can edit and delete their own reviews.
  
- **Account Management:**
  - Users can delete their accounts, which also deletes associated reviews.

---

## Website Walkthrough -

- **Home Page:**

  - Upon visting the landing page, the user can see the heading and logo of the site along with a view of the three most recent game reviews showcased in a visually appealing card format, offering a snapshot of the latest content.

- **Sign Up Page:**

  - Users can navigate to the sign-up page by selecting the "Sign Up" option from the navbar.
The sign-up page provides a straightforward form where users can input their desired username and password to create a new account.

- **Login Page:**

  - If a user has already registered, they can login by accessing the "Log In" page from the navbar.

- **Profile Page:**

  - After logging in, users are directed to their personalized profile page, where they can access various account-related features and functionalities. The profile page displays the user's username, along with a summary of their submitted game reviews.

- **Game Reviews:**

  - Users can then choose to explore the current game reviews submitted by users by clicking on the browse link in the navbar, which takes them to the game_reviews page, providing valuable insights and recommendations for a wide range of titles. Each review includes a rating and written feedback, helping users to make informed decisions about their gaming experiences.

- **Search Game:**

  - The user can then choose to search for a game to review themself by clicking on the 'add' link in the navbar, which takes them to the search_game page.
 
- **Search Results:**

  - The user can then view a the results of their query on the search_results page which displays a pagination of the results display as game cards.

- **Adding Reviews:**

  - When the user selects the game they want to review, they are taking to the game_info page which displays a visually appealing covert art of the game along with all the relevant info, and then the ability to add their review and rating of the game with a form.

- **Editing and Deleting Reviews:**

  - The user can then see the games they have reviewed on their profile page and choose to edit or delete the review with a modal form.

- **Deleting Account:**
  - The user can then decide to delete their account if they so wish, which will trigger a modal to verify if the user definitely wants to delete their account, which in turn deletes their reviews from the database.

---

## Made with:

- [HTML5](https://en.wikipedia.org/wiki/HTML) (was used for structuring and presenting content of the website)
- [CSS](https://en.wikipedia.org/wiki/CSS) (used for the styling of the content)
- [JS](https://en.wikipedia.org/wiki/JavaScript) (used for timeout functionality)
- [Google Fonts](https://fonts.google.com) (used for all the font styling within the project, font used was Roboto, and sans-serif for back-up)
- [Bootstrap](https://getbootstrap.com) (used for the responsiveness and additional styling)
- [RAWG](https://rawg.io/apidocs) (API used for retrieving video game info)
- [flaticon](https://www.flaticon.com) (used for the various custom icons)
- [Chrome](https://www.google.com/intl/en_uk/chrome) (used to debug and test the source code using HTML5 and to test site responsiveness)
- [GitHub](https://github.com) (used to create the repository and store the projects code after pushed from Git)
- [Codeanywhere](https://codeanywhere.com) (used for editing code of project)
- [Gitpod](https://www.gitpod.io/) (used for editing code of project)
- [vscode](https://code.visualstudio.com) (used for editing code of project)
- [W3C Markup](https://validator.w3.org) (used for validating the html5 code)
- [Jigsaw Validator](https://jigsaw.w3.org/css-validator) (used for validating the CSS code)
- [Webaim Contrast Checker](https://webaim.org/resources/contrastchecker) (Used for validating color contrast for accessibility)
- [Jshint](https://jshint.com) (Used for JavaScript validation)
- [Flask](https://flask.palletsprojects.com/en/3.0.x) (used for building of app)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x) (used for html templating)
- [Python](https://www.python.org) (used for app logic)
- [PyMongo](https://pymongo.readthedocs.io/en/stable) (used for interacting with mongodb)
- [Heroku](https://www.heroku.com) (used for deployment of app)
- [MongoDB](https://www.mongodb.com) (used for database)
- [Am I Responsive?](https://ui.dev/amiresponsive) (used for responsiveness testing)

---

## Data Schema

### User Schema

The users collection in MongoDB stores user account information. Each user document has the following fields:

- username (string): A unique identifier for the user. It is stored in lowercase and used for login and profile identification.
- password (string): The hashed password for the user. Stored securely using werkzeug.security.

Example:

```
{
  "username": "johndoe",
  "password": "pbkdf2:sha256:150000$abc123$def456..."
}
```

### Game Review Schema

The game_reviews collection stores user-submitted game reviews. Each review document has the following fields:

- username (string): The username of the reviewer. This links the review to a specific user.
- game_id (string): A unique identifier for the game from the RAWG API.
- name (string): The name of the game.
- background_image (string): URL to the background image of the game.
- description (string): A brief description of the game.
- released (string): The release date of the game.
- genres (array of strings): A list of genres associated with the game.
- developers (array of strings): A list of developers for the game.
- publishers (array of strings): A list of publishers for the game.
- platforms (array of strings): A list of platforms the game is available on.
- tags (array of strings): Tags related to the game, such as gameplay modes (e.g., 'singleplayer', 'multiplayer').
- review (string): The user's review of the game.
- rating (float): The rating given by the user, typically a value between 0 and 10.

  Example:

```
{
  "username": "johndoe",
  "game_id": "12345",
  "name": "Example Game",
  "background_image": "http://example.com/image.jpg",
  "description": "An exciting new game.",
  "released": "2024-01-01",
  "genres": ["Action", "Adventure"],
  "developers": ["Example Developer"],
  "publishers": ["Example Publisher"],
  "platforms": ["PC", "PlayStation 5"],
  "tags": ["multiplayer", "co-op"],
  "review": "This game is fantastic with great gameplay!",
  "rating": 9.0
}
```

### RAWG API Interaction

The application interacts with the RAWG API to fetch game details. While the API data structure is defined by RAWG, key elements include:

- id (string): The unique identifier of the game.
- name (string): The name of the game.
- background_image (string): URL to the background image of the game.
- description (string): A brief description of the game.
- released (string): The release date of the game.
- genres (array of objects): Each genre has a name and slug.
- developers (array of objects): Each developer has a name.
- publishers (array of objects): Each publisher has a name.
- platforms (array of objects): Each platform has a name.
- tags (array of objects): Each tag has a name and slug.

Example:

```
{
  "id": "12345",
  "name": "Example Game",
  "background_image": "http://example.com/image.jpg",
  "description": "An exciting new game.",
  "released": "2024-01-01",
  "genres": [
    {"name": "Action", "slug": "action"},
    {"name": "Adventure", "slug": "adventure"}
  ],
  "developers": [{"name": "Example Developer"}],
  "publishers": [{"name": "Example Publisher"}],
  "platforms": [{"name": "PC"}, {"name": "PlayStation 5"}],
  "tags": [
    {"name": "Multiplayer", "slug": "multiplayer"},
    {"name": "Co-op", "slug": "co-op"}
  ]
}
```

---

## Testing & Validation

### HTML Validation

The only errors found in the templates were seemingly from the HTML Validator's inability to recognize Jinja Templating:

![HTMLValidation](https://live.staticflickr.com/65535/53626872027_d9843c231d_z.jpg) ![](https://live.staticflickr.com/65535/53628105814_4cb17a4c60_z.jpg) ![](https://live.staticflickr.com/65535/53626884062_94ef21cf39_z.jpg)

### CSS Validation

No errors were found.

![CSSValidation](https://live.staticflickr.com/65535/53626998416_01ca0dc674_b.jpg)

### JS Validation

No errors were found.

![JSValidation](https://live.staticflickr.com/65535/53627004771_20f0009ce2_b.jpg)

### Python Validation

No errors were found.

![PythonValidation](https://live.staticflickr.com/65535/53626609727_756ee0e3d0_b.jpg)

### Usability Testing:

#### User Interface Clarity and Intuitiveness

| Test Case                  | Expected Result                                              | Outcome |
|----------------------------|--------------------------------------------------------------|---------|
| Locate and use main features/buttons (e.g., "Add," "Browse")     | Features/buttons should be easily visible and usable.        | Pass        |
| Evaluate the clarity of labels and instructions                     | Labels and instructions should be clear and understandable.   |  Pass       |
| Test the consistency of design elements (color scheme, fonts, layouts) | Design elements should be consistent throughout the application. | Pass        |
| Check for user feedback mechanisms (e.g., flash messages) | Flash messages should be clear and appropriately visible. | Pass |

### Accessibility Testing:

| Test Case                  | Expected Result                                              | Outcome |
|----------------------------|--------------------------------------------------------------|---------|
| Evaluate contrast and color schemes for readability and accessibility | Colors and contrasts should be chosen to ensure readability for users with visual impairments. | Pass        |


### Responsive Testing:

| Test Case                  | Expected Result                                              | Outcome |
|----------------------------|--------------------------------------------------------------|---------|
| Tested the application on various devices and screen sizes | Should be responsive to different breakpoints and devices  |Pass |


### Functionality Testing:

#### Homepage Navigation

| Test Case             | Expected Result                            | Outcome |
|-----------------------|--------------------------------------------|---------|
| Click on "Home"       | Should navigate to the homepage           | Pass    |
| Click on "Add"        | Should navigate to the page for adding a new game | Pass    |
| Click on "Browse"     | Should navigate to the page for browsing games | Pass    |
| Click on "Sign Up"    | Should navigate to the sign-up page       | Pass    |
| Click on "Log In"     | Should navigate to the log-in page        | Pass    |
| Click on "Profile"    | Should navigate to the user's profile page | Pass    |
| Click on "Log Out"    | Should log the user out  | Pass    |

#### Add Game Functionality

| Test Case                    | Expected Result                                   | Outcome |
|------------------------------|---------------------------------------------------|---------|
| Fill out game details form   | Form should be submitted successfully and game should be added | Pass    |
| Submit empty form            | Form submission should be prevented and relevant error messages displayed | Pass    |
| Add duplicate game           | Attempt to add a game with existing name should be prevented and appropriate error message displayed | Pass     |

#### Browse Games Functionality

| Test Case                | Expected Result                         | Outcome |
|--------------------------|-----------------------------------------|---------|
| Search for a game        | Search results should display relevant games | Pass    |

#### Game Reviews Functionality

| Test Case            | Expected Result                                | Outcome |
|----------------------|------------------------------------------------|---------|
| View game review     | Game details and user reviews should be displayed | Pass    |
| Add game review      | Review should be added successfully to the database | Pass    |
| Edit game review     | Changes to review should be saved successfully | Pass    |
| Delete game review   | Review should be deleted from the database   | Pass    |

#### User Profile Functionality

| Test Case          | Expected Result                                      | Outcome |
|--------------------|------------------------------------------------------|---------|
| View user profile  | User profile details and submitted reviews should be displayed | Pass    |
| Delete user account| User account and associated reviews should be deleted | Pass    |


### Database Management Testing:

| Test Case            | Expected Result                                | Outcome |
|----------------------|------------------------------------------------|---------|
| Add game review      | Review should be added successfully to the database | Pass    |
| Edit game review     | Changes to review should be saved successfully to database | Pass    |
| Delete game review   | Review should be deleted from the database   | Pass    |
| View Profile     | Profile of user in database should be viewable | Pass    |
| Sign Up      | User info should be added to database | Pass    |
| Delete Account   | User's info and reviews should be removed from database   | Pass    |


### Deployment Testing:

| Test Case            | Expected Result                                | Outcome |
|----------------------|------------------------------------------------|---------|
| Deployed App matches development version      | The deployed website should mirror the functionality and appearance of the development version. | Pass    |


### Security Testing:

| Test Case            | Expected Result                                | Outcome |
|----------------------|------------------------------------------------|---------|
| Test authentication and authorization      | Unauthorized users should be redirected or blocked from accessing protected content. | Pass    |

### Bug fixes/improvements:

Extensive error handling was added to functions in attempt to handle edge cases. For example:

```
def fetch_api_data(url):
    """
    Utility function to fetch and return data from RAWG API.
    """
    try:
        response = requests.get(url)
        return response.json()
    except HTTPError as http_err:
        # Raise HTTPError to be handled by the caller
        raise RuntimeError(f"HTTP error occurred: {http_err}") from http_err
    except RequestException as req_err:
        # Raise RequestException to be handled by the caller
        raise RuntimeError(f"Request error occurred: {req_err}") from req_err
    except Exception as err:
        # Raise generic Exception to be handled by the caller
        raise RuntimeError(f"An unexpected error occurred: {err}") from err
```

```
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Display user profile and associated reviews.
    """
    current_username = session.get("user")
    try:
        page = request.args.get("page", 1, type=int)
        per_page = 5
        start_index = (page - 1) * per_page
        user_reviews = mongo.db.game_reviews.find(
            {"username": username}
        ).skip(start_index).limit(per_page)
        total_reviews = mongo.db.game_reviews.count_documents(
            {"username": username}
        )
        total_pages = math.ceil(total_reviews / per_page)
        return render_template("profile.html",
                               username=username,
                               current_username=current_username,
                               user_reviews=user_reviews,
                               per_page=per_page,
                               total_reviews=total_reviews,
                               total_pages=total_pages,
                               page=page)
    except PyMongoError:
        flash("A database error occurred while fetching profile data. Please try again later.")
        return redirect(url_for("home"))
    except Exception:
        flash("An unexpected error occurred. Please try again later.")
        return redirect(url_for("home"))
```

```
@app.route("/game_info")
def game_info():
    """
    Fetch detailed information about a specific game.
    """
    # Check if user is logged in to access the page
    if 'user' not in session:
        flash("You need to be logged in to access game details.")
        return redirect(url_for("log_in"))
    game = request.args.get("game")
    if not game:
        flash("No game specified.")
        return redirect(url_for("search_game"))
    try:
        game_dict = eval(game)
        url = f"{RAWG_API_URL}/{game_dict['id']}?key={RAWG_API_KEY}"
        game_data = fetch_api_data(url)
        relevant_tags = [
            tag['name'] for tag in game_data.get('tags', [])
            if 'singleplayer' in tag['slug'] or 'multiplayer' in tag['slug'] or 'co-op' in tag['slug']
        ]
        return render_template("game_info.html", game_data=game_data, relevant_tags=relevant_tags)
    except RuntimeError as err:
        flash(str(err))
        return redirect(url_for("search_game"))
    except Exception:
        flash("An unexpected error occurred. Please try again later.")
        return redirect(url_for("search_game"))
```

---

## Deployment

**With Heroku:**

1. Sign in to your Heroku account or sign up for a new one.
   
2.	Connect your Heroku account to your GitHub account:
    * Navigate to the Heroku Dashboard.
    * Click on the "New" button and select "Create new app."
    * Give your app a unique name and choose the region closest to you.
    * Click "Create app."
    * In the "Deployment method" section, select "GitHub."
      
3. Search for the repository you want to deploy from your GitHub account.
   
4.	Once you've connected your GitHub repository, you can choose to either deploy the app automatically when changes are pushed to GitHub or manually deploy.
   
5. If you choose automatic deploys, select the branch you want to deploy from and enable automatic deploys.
   
6.	If you prefer manual deploys, you can trigger a deployment manually by clicking the "Deploy Branch" button.
   
7. Heroku will build your app using your project's build scripts and dependencies specified in your repository.
   
8. Once the build is complete, you can view your deployed application by clicking the "View" button on the Heroku Dashboard.
   
9.	You can manage your deployed application settings and view logs from the Heroku Dashboard. 
Remember to set up any necessary configuration variables (such as environment variables) on the settings page.

**Fork and Clone Repository:**

1. Visit the GitHub repository and click on the "Fork" button in the top-right corner. This will create a copy of the repository under your GitHub account.

2. On your forked repository's page, click on the "Code" button and copy the repository's URL.

3. Open your preferred Command Line Interface (e.g., Terminal, Git Bash) and navigate to the directory where you want to clone the repository.

4. Enter the following command in the command line:
   `git clone [repository URL]`

5. Navigate into the Repository: Use the cd command to navigate into the cloned repository:
   `cd [repository name]`

(Replace [repository URL] with the actual URL of your forked repository and [repository name] with the name of the cloned repository on your local machine.)

**Run Locally:**

1. Create an .env file in the root directory if it does not exist.

2. Add necessary environment variables. For example:

```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", your_secret_key)
os.environ.setdefault("MONGO_URI", your_mongo_uri)
os.environ.setdefault("MONGO_DBNAME", your_mongo_dbname)
```

3. Run the development server with the command `python3 app.py runserver` and you should see in the terminal a link to the local url such as  `* Running on http://127.0.0.1:5000`

---

## Credits & Acknowledgements

- [Flaticon](https://www.flaticon.com) (For custom icons)
- [Freepik](https://www.freepik.com) (For custom icons)
- [RAWG](https://rawg.io/apidocs) (for amazing api service!)
- [Twitch](https://www.twitch.tv) (for inspiration!)
- [IGDB](https://www.igdb.com) (for inspiration!)
- [Metacritic](https://www.metacritic.com) (for inspiration!)
- Video Games! 
- My mentor Marcel for his support, encouragement, advice and guidance throughout the developing of this app.
