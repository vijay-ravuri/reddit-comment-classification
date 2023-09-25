# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Web APIs & NLP

### Description

In week four we've learned about a few different classifiers. In week five we'll learn about webscraping, APIs, and Natural Language Processing (NLP). This project will put those skills to the test.

For project 3, your goal is two-fold:
1. Using [PRAW](https://praw.readthedocs.io/en/stable/), you'll collect pairs of __Question and the answer with most votes__ from various subreddits.
2. Next, you will use [OpenAI](https://openai.com/blog/openai-api) API to ask the same question to ChatGPT. You will repeat this process for all the questions from Step 1. You need to ignore any responses where ChatGPT refuses to provide a "straightforward" answer. This kind of responses usually have a pattern and they usually start with something like "As a large language model I do not have the ability to blah blah...". If you receive such a response, move on to the next question. Gather at least 5000 such question-answer pairs and corresponding ChatGPT response.
3. Create a dataset with the data collected in previous two steps. Ideally, the dataset should have at least the following columns:

| row_id | Question | Human_written_answer | ChatGPT_generated_answer |
| ------- | ------- | --------------------- | ------------------------ |
| 1 | abcd | efgh | ijkl |

4. You'll then use NLP to train a classifier on whether a response came from a human being or ChatGPT. This is a binary classification problem.


---
## Checkpoints and Advice

If you aren't familiar with [reddit](https://www.reddit.com/), go check it out and browse different subreddits. Each subreddit is like a forum on a different topic. [Here's a list of subreddits by topic.](https://www.reddit.com/r/ListOfSubreddits/wiki/listofsubreddits)

- What you choose could partly determine how difficult your data cleaning will be and how challenging the classification task will be for your algorithms. In your presentation and executive summary, **tell us what you used**.
- You should aim to have a function built to pull down data from the API by Monday, September 18.
- The more data you can pull the better for your classifier. **You will want data from at least 5000 unique, non-null comments.**

---

### Requirements

- Gather and prepare your data using the appropriate APIs.
- **Create and compare at least two models**. These can be any classifier of your choosing: logistic regression, Naive Bayes, KNN, SVM, Random Forest Classifier, etc.
  - **Bonus**: use a Naive Bayes classifier
- You **must** build a robust commit history on GHE for this project, with the first commit no later than next Monday, 9/18/23.
- A Jupyter Notebook with your analysis for a peer audience of data scientists.
- An executive summary of your results.
- A short presentation outlining your process and findings for a semi-technical audience.

**Pro Tip:** You can find a good example executive summary [here](https://www.proposify.biz/blog/executive-summary).

---

### Necessary Deliverables / Submission

- Code and executive summary must be in a clearly commented Jupyter Notebook.
- You must submit your slide deck.
- Materials must be submitted by **9:00 AM EST on Monday, September 18, 2023**.
- Presentation must be ready by **09:00 AM EST on Monday, September 18, 2023**.

---

## Rubric
You should make sure that you consider and/or follow most if not all of the considerations/recommendations outlined below **while** working through your project.

For Project 3 the evaluation categories are as follows:<br>
**The Data Science Process**
- Problem Statement
- Data Collection
- Data Cleaning & EDA
- Preprocessing & Modeling
- Evaluation and Conceptual Understanding
- Conclusion and Recommendations

**Organization and Professionalism**
- Organization
- Visualizations
- Python Syntax and Control Flow
- Presentation

**Scores will be out of 30 points based on the 10 categories in the rubric.** <br>
*3 points per section*<br>

| Score | Interpretation |
| --- | --- |
| **0** | *Project fails to meet the minimum requirements for this item.* |
| **1** | *Project meets the minimum requirements for this item, but falls significantly short of portfolio-ready expectations.* |
| **2** | *Project exceeds the minimum requirements for this item, but falls short of portfolio-ready expectations.* |
| **3** | *Project meets or exceeds portfolio-ready expectations; demonstrates a thorough understanding of every outlined consideration.* |


### The Data Science Process

**Problem Statement**
- Is it clear what the goal of the project is?
- What type of model will be developed?
- How will success be evaluated?
- Is the scope of the project appropriate?
- Is it clear who cares about this or why this is important to investigate?
- Does the student consider the audience and the primary and secondary stakeholders?

**Data Collection**
- Was enough data gathered to generate a significant result?
- Was data collected that was useful and relevant to the project?
- Was data collection and storage optimized through custom functions, pipelines, and/or automation?
- Was thought given to the server receiving the requests such as considering number of requests per second?

**Data Cleaning and EDA**
- Are missing values imputed/handled appropriately?
- Are distributions examined and described?
- Are outliers identified and addressed?
- Are appropriate summary statistics provided?
- Are steps taken during data cleaning and EDA framed appropriately?
- Does the student address whether or not they are likely to be able to answer their problem statement with the provided data given what they've discovered during EDA?

**Preprocessing and Modeling**
- Is text data successfully converted to a matrix representation?
- Are methods such as stop words, stemming, and lemmatization explored?
- Does the student properly split and/or sample the data for validation/training purposes?
- Does the student test and evaluate a variety of models to identify a production algorithm (**AT MINIMUM:** two classification models, **BONUS:** try a Naive Bayes)?
- Does the student defend their choice of production model relevant to the data at hand and the problem?
- Does the student explain how the model works and evaluate its performance successes/downfalls?

**Evaluation and Conceptual Understanding**
- Does the student accurately identify and explain the baseline score?
- Does the student select and use metrics relevant to the problem objective?
- Does the student interpret the results of their model for purposes of inference?
- Is domain knowledge demonstrated when interpreting results?
- Does the student provide appropriate interpretation with regards to descriptive and inferential statistics?

**Conclusion and Recommendations**
- Does the student provide appropriate context to connect individual steps back to the overall project?
- Is it clear how the final recommendations were reached?
- Are the conclusions/recommendations clearly stated?
- Does the conclusion answer the original problem statement?
- Does the student address how findings of this research can be applied for the benefit of stakeholders?
- Are future steps to move the project forward identified?


### Organization and Professionalism

**Project Organization**
- Are modules imported correctly (using appropriate aliases)?
- Are data imported/saved using relative paths?
- Does the README provide a good executive summary of the project?
- Is markdown formatting used appropriately to structure notebooks?
- Are there an appropriate amount of comments to support the code?
- Are files & directories organized correctly?
- Are there unnecessary files included?
- Do files and directories have well-structured, appropriate, consistent names?
- Is there a robust commit history?

**Visualizations**
- Are sufficient visualizations provided?
- Do plots accurately demonstrate valid relationships?
- Are plots labeled properly?
- Are plots interpreted appropriately?
- Are plots formatted and scaled appropriately for inclusion in a notebook-based technical report?

**Python Syntax and Control Flow**
- Is care taken to write human readable code?
- Is the code syntactically correct (no runtime errors)?
- Does the code generate desired results (logically correct)?
- Does the code follows general best practices and style guidelines?
- Are Pandas functions used appropriately?
- Are `sklearn` and `NLTK` methods used appropriately?

**Presentation**
- Is the problem statement clearly presented?
- Does a strong narrative run through the presentation building toward a final conclusion?
- Are the conclusions/recommendations clearly stated?
- Is the level of technicality appropriate for the intended audience?
- Is the student substantially over or under time?
- Does the student appropriately pace their presentation?
- Does the student deliver their message with clarity and volume?
- Are appropriate visualizations generated for the intended audience?
- Are visualizations necessary and useful for supporting conclusions/explaining findings?


---

### Why did we choose this project for you?
This project covers three of the biggest concepts we cover in the class: Classification Modeling, Natural Language Processing and Data Wrangling/Acquisition.

Part 1 of the project focuses on **Data wrangling/gathering/acquisition**. This is a very important skill as not all the data you will need will be in clean CSVs or a single table in SQL.  There is a good chance that wherever you land you will have to gather some data from some unstructured/semi-structured sources; when possible, requesting information from an API, but sometimes scraping it because they don't have an API (or it's terribly documented).

Part 2 of the project focuses on **Natural Language Processing** and converting standard text data (like Titles and Comments) into a format that allows us to analyze it and use it in modeling.

Part 3 of the project focuses on **Classification Modeling**.  Given that project 2 was a regression focused problem, we needed to give you a classification focused problem to practice the various models, means of assessment and preprocessing associated with classification.   
