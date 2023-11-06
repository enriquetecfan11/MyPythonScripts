"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from newspaper import Article


st.title('Webpage Analyzer')

# Make and input for user to enter a webpage
user_input = st.text_input("Enter a URL to analyze", "https://www.google.com")

# Make a button to submit the input
submit = st.button('Analyze')

# Get all h2 from the webpage
def get_h2(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Putting all h2 in a list
    h2_list = []

    for h2 in soup.find_all('h2'):
        h2_list.append(h2.text)

    return h2_list

# From h2 list, get all links from h2
def get_h2_a(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Putting all h2 in a list
    h2_a_list = []

    for h2 in soup.find_all('h2'):
        h2_a_list.append(h2.a['href'])

    # Filter the list and show only the have http or https
    h2_a_list = [x for x in h2_a_list if "http" in x]

    # Filter the list and show only 5 links
    h2_a_list = h2_a_list[:5]

    return h2_a_list

# Now with newspaper library and h2_a_list we can get the title and summary of the links
def get_title_summary(url):
    article = Article(url)

    article.download()
    article.parse()
    article.nlp()

    articleTitle = article.title
    articleSummary = article.summary
    articleKeywords = article.keywords
    return df, articleTitle, articleSummary, articleKeywords

df = pd.DataFrame()


# Show the details of each link
if submit:
    st.write('Now we are going to get the title and summary of each link')
    
    details = []
    for link in get_h2_a(user_input):
        st.write(f'Here is the title and summary of the link: {link}')
        title_summary = get_title_summary(link)
        st.write(f'Title: {title_summary[1]}')
        st.write(f'Summary: {title_summary[2]}')
        st.write(f'Keywords: {title_summary[3]}')
        st.write('-------------------')
        details.append({'Title': title_summary[1], 'Summary': title_summary[2], 'Keywords': title_summary[3]})

    st.write('Data Frame with details of all links')

    # Create DataFrame from list of dictionaries
    df = pd.DataFrame(details)
    st.write(df)

    # Save the data frame as json utf-8
    df.to_json('details.json', orient='records', lines=True, force_ascii=False)
    st.write('Data Frame saved as details.json')
