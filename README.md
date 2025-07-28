<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">


# NOTE-TAKING---RECOMMENDATION-SYSTEM

<em>Transform Notes into Personalized Learning Powerhouses</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/last-commit/broy9501/note-taking---recommendation-system?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/broy9501/note-taking---recommendation-system?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/broy9501/note-taking---recommendation-system?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">

</div>
<br>

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
    - [Tech Stack](#tech-stack)
    - [How it works](#how-it-works)
    - [Installation](#installation)
    - [Survey Data Collection](#survey-data-collection)
    - [Future Improvements](#future-improvements)

---

## Overview

note-taking---recommendation-system, a Flask-based web application that allows students to take notes and receive personalized learning material recommendations using Natural Language Processing (NLP). The core features include:

- **🧩** **Database Schema:** Supports persistent storage of user notes, recommendations, and feedback, ensuring data integrity and easy retrieval.
- **🤖** **AI Recommendation System:** Uses Google Cloud NLP API to extract key topics from notes and recommend relevant study materials.
- **🧠** **Content-Based Filtering:** Utilizes TF-IDF and cosine similarity to suggest relevant learning materials tailored to user interests.
- **🔐** **User Authentication:** Manages secure registration, login, and session handling to protect user data and personalize experiences.
- **🌐** **NLP Entity Analysis:** Leverages Google Cloud NLP to extract key concepts from notes, enhancing semantic understanding.
- **📊** **Data Integration:** Aggregates and standardizes educational datasets for efficient search and resource management.
- **🎨** **Interactive UI Components:** Provides user interfaces for profile management, note creation, and viewing personalized suggestions, boosting engagement.
- **✍️** **Note-taking Interface:** Simple and clean UI for students to write and manage notes.

---

## Tech Stack
| Component        | Technology          |
|------------------|---------------------|
| Backend          | Flask (Python)      |
| Recommendation System | Python         |
| Database         | MySQL               |
| Frontend         | HTML, CSS, JavaScript |
| NLP Integration  | Google Cloud Natural Language API |


## How it works

1. Students write notes via the web interface.
2. Notes are sent to the Google NLP API for topic extraction.
3. Extracted topics are matched against a database of curated study resources.
4. Top recommended materials are shown to the student.

## Installation

Build note-taking---recommendation-system from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd note-taking---recommendation-system
    ```

3. **Install the dependencies:**

```sh
❯ pip install -r requirements.txt
```

4. **Set up Google NLP API**
          1. Create a Google Cloud project.
          2. Enable the Natural Language API.
          3. Download your credentials JSON and set the environment variable:
                    
```sh
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
```

5. **Run the app**
```sh
python Registration Process.py
```

### Survey Data Collection
The project is supported by a user survey (built in Microsoft Forms) to gather insights into how students interact with notes and learning resources. The data collected helps improve the recommendation system (see 'Dissertation Bishal Roy.pdf').


### Future Improvements
1. Develop a hybrid recommendation model by combining collaborative and content-based filtering.

2. Broaden the resource pool using open educational content, video tutorials, and research papers via web scraping or APIs.

3. Add user feedback features like rating and commenting on recommendations.

4. Improve UI/UX with features like dark mode, voice search, and better navigation.

5. Allow users to filter content and save preferences for more personalized suggestions.

---

<div align="left"><a href="#top">⬆ Return</a></div>

---
