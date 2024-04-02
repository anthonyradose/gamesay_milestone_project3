README:

# GameSay

![GameSay]()

Welcome to GameSay!

Game reviews by gamers for gamers!

This game review app provides people a space to share their experiences, insights, and opinions on their favorite games. Whether you're seeking recommendations or want to contribute your own reviews!

Sign up today to have your say on your favorite (or not so favorite) video games!

The live website can be found [here]()

---

## User Experience

- Purpose of Project
- User Stories
- Web Design
- Wire frames

### Purpose of Project -

Many video game sites often overwhelm users with an abundance of content, including irrelevant information and intrusive promotional pop-ups. This project aims to streamline the video game consumer's experience, by cutting through the noise and focusing on the essential info of a video game, in particular if it's worth playing or not.

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

8. As a user, I want the website to be visually appealing and easy to navigate.

![]() ![]()

### Web Design -

#### Visual Aesthetic:

The app embodies a sleek and incisive design, focusing on a clean, simple, and modern aesthetic that reflects a user-friendly experience. 

#### Color Scheme:

The color palette is vibrant and dynamic, mirroring the energy and excitement synonymous with video games, while also maintaining a sense of user-friendliness.

#### Typography:

The app exclusively uses Roboto. By adopting a clean and accessible font, the design reflects contemporary trends while also ensuring readability.

### Wireframes:

The site's wireframes were made with balsalmiq wireframes.

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

Website Walkthrough -

- **Home Page:**

  - Upon visting the landing page, the user can see the heading and logo of the site along with a view of the three most recent game reviews showcased in a visually appealing card format, offering a snapshot of the latest content.

- **Sign Up Page:**

  - Users can navigate to the sign-up page by selecting the "Sign Up" option from the navbar.
The sign-up page provides a straightforward form where users can input their desired username and password to create a new account.

- **Login Page:**

  - If a user has already registered, they can login by accessing the "Log In" page from the navbar.

- **Profile Page:**

  - After logging in, users are directed to their personalized profile page, where they can access various account-related features and functionalities. The profile page displays the user's username and avatar, along with a summary of their submitted game reviews.

- **Game Reviews:**

  - Users can then choose to explore the current game reviews submitted by users by clicking on the browse link in the navbar, which takes them to the game_reviews page, providing valuable insights and recommendations for a wide range of titles. Each review includes a rating and written feedback, helping users to make informed decisions about their gaming experiences.

- **Search Game:**

  - The user can then choose to search for a game to review themself by clicking on the 'add' link in the navbar, which takes them to the search_game page.
 
- **Search Results:**

  - The user can then view a the results of their query on the search_results page which displays a pagination of the results display as game cards.

- **Adding Reviews:**

  - When the user selects the game they want to review, they are taking to the game_info page which displays a visually appealing covert art of the game along with all the relevant info, and then the ability to at their review and rating of the game with a form.

- **Editing and Deleting Reviews:**

  - The user can then see the games they have reviewed on their profile page and choose to edit or delete the review with a modal form.

- **Deleting Account:**
  - The user can then decide to delete their account if they so wish, which will trigger a modal to verify if the user definitely wants to delete their account, which in turn deletes their reviews from the database.

---

## Made with:

- [HTML5](https://en.wikipedia.org/wiki/HTML) (was used for structuring and presenting content of the website)
- [CSS](https://en.wikipedia.org/wiki/CSS) (used for the styling of the content)
- [JS](https://en.wikipedia.org/wiki/JS) (used for)
- [Google Fonts](https://fonts.google.com/) (used for all the font styling within the project, font used was Roboto, and sans-serif for back-up)
- [Bootstrap](https://www.bootstrapcdn.com/) (used for the responsiveness and additional styling)
- RAWG
- [flaticon](https://www.flaticon.com/) (used for the various custom icons)
- [Chrome](https://www.google.com/intl/en_uk/chrome/) (used to debug and test the source code using HTML5 and to test site responsiveness)
- [GitHub](https://github.com/) (used to create the repository and store the projects code after pushed from Git)
- [Codeanywhere](https://codeanywhere.com/) (used for the editing of code within the project for the site)
- [vscode](https://code.visualstudio.com/) 
- [W3C Markup](https://validator.w3.org/) (used for validating the html5 code)
- [Jigsaw Validator](https://jigsaw.w3.org/css-validator/) (used for validating the CSS code)
- [Webaim Contrast Checker](https://webaim.org/resources/contrastchecker/) (Used for validating color contrast for accessibility)
- [Jshint](https://jshint.com/) (Used for JavaScript validation)
- 
- [Am I Responsive?](https://ui.dev/amiresponsive)(Used for responsiveness testing)

---

## Testing

.

### HTML Validation

.

![HTMLValidation]()

### CSS Validation

No errors were found.

![CSSValidation](https://live.staticflickr.com/65535/53626998416_01ca0dc674_b.jpg)

### JS Validation

No errors were found.

![JSValidation](https://live.staticflickr.com/65535/53627004771_20f0009ce2_b.jpg)

### Python Validation

No errors were found.

![PythonValidation](https://live.staticflickr.com/65535/53626609727_756ee0e3d0_b.jpg)

**Usability Testing:**
.

**Responsiveness Testing:**
.

---

## Functionality Testing: ##

### Homepage Navigation

| Test Case             | Expected Result                            | Outcome |
|-----------------------|--------------------------------------------|---------|
| Click on "Home"       | Should navigate to the homepage           | Pass    |
| Click on "Add"        | Should navigate to the page for adding a new game | Pass    |
| Click on "Browse"     | Should navigate to the page for browsing games | Pass    |
| Click on "Sign Up"    | Should navigate to the sign-up page       | Pass    |
| Click on "Log In"     | Should navigate to the log-in page        | Pass    |
| Click on "Profile"    | Should navigate to the user's profile page | Pass    |
| Click on "Log Out"    | Should log the user out and redirect to the homepage |     |

### Add Game Functionality

| Test Case                    | Expected Result                                   | Outcome |
|------------------------------|---------------------------------------------------|---------|
| Fill out game details form   | Form should be submitted successfully and game should be added | Pass    |
| Submit empty form            | Form submission should be prevented and relevant error messages displayed | Pass    |
| Add duplicate game           | Attempt to add a game with existing name should be prevented and appropriate error message displayed |     |

### Browse Games Functionality

| Test Case                | Expected Result                         | Outcome |
|--------------------------|-----------------------------------------|---------|
| Search for a game        | Search results should display relevant games | Pass    |

### Game Reviews Functionality

| Test Case            | Expected Result                                | Outcome |
|----------------------|------------------------------------------------|---------|
| View game review     | Game details and user reviews should be displayed | Pass    |
| Add game review      | Review should be added successfully to the database | Pass    |
| Edit game review     | Changes to review should be saved successfully | Pass    |
| Delete game review   | Review should be deleted from the database   | Pass    |

### User Profile Functionality

| Test Case          | Expected Result                                      | Outcome |
|--------------------|------------------------------------------------------|---------|
| View user profile  | User profile details and submitted reviews should be displayed | Pass    |
| Delete user account| User account and associated reviews should be deleted | Pass    |



## Deployment

.

**With Heroku:**

.


**Fork and Clone Repository:**

1. Visit the GitHub repository and click on the "Fork" button in the top-right corner. This will create a copy of the repository under your GitHub account.

2. On your forked repository's page, click on the "Code" button and copy the repository's URL.

3. Open your preferred Command Line Interface (e.g., Terminal, Git Bash) and navigate to the directory where you want to clone the repository.

4. Enter the following command in the command line:
   `git clone [repository URL]`

5. Navigate into the Repository: Use the cd command to navigate into the cloned repository:
   `cd [repository name]`

(Replace [repository URL] with the actual URL of your forked repository and [repository name] with the name of the cloned repository on your local machine.)

---

## Credits & Acknowledgements

- [Flaticon](https://www.flaticon.com/) (For custom icons)
- RAWG
- 
- .
- .
- .
- .
- .
- My mentor Marcel for his support, encouragement, advice and guidance throughout the developing of this app.
