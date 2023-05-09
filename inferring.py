from chatGPT import get_completion

review = """
ooooooh my goodness this is the cutest journal! \ 
i'm so excited to start drawing in it! cannot stress \ 
enough how absolutely sweet the seller was as well! \ 
i made a bit of an oopsy when i bought it, \ 
but the seller was so patient and understanding and \ 
even included a few extras in the overall order \ 
(since i ordered some stickers and a cute sticky note \ 
alongside the journal) over something that was my mistake, \ 
but the seller was so nice about it all! absolutely \ 
fantastic customer service, wonderful products, \ 
and i can't wait to buy another journal and stickers \ 
once i fill up this one! :D totally matches the description! \ 
beyond my expectations quite frankly! ^_^
"""

prompt = f"""
What is the sentiment of the following product review, 
which is delimited with triple backticks?

Review text: '''{review}'''
"""

promptEmotions = f"""
Identify a list of emotions that the writer of the \
following review is expressing. Include no more than \
five items in the list. Format your answer as a list of \
lower-case words separated by commas.

Review text: '''{review}'''
"""

promptItem = f"""
Identify the following items from the review text: 
- Items purchased by reviewer
- Sentiment (positive or negative)
- Is the reviewer expressing anger? (true or false)

The review is delimited with triple backticks. \
Format your response as list of JSON objects with \
"Item" as the keys. \
If the information isn't present, use "unknown" \
as the value.
Make your response as short as possible.
  
Review text: '''{review}'''
"""

promptArticle = f"""
Determine the topics that are being discussed in \ 
the following article link, which is delimited with \
triple backticks.

Make each item one or two words long. \

Format your response as a list of lower-case words, separated by commas. \ 

Article link: '''https://dev.to/mayashavin/effortlessly-nuxt-navigation-crafting-dynamic-breadcrumbs-with-storefront-ui-2p32'''
"""

promptTopic = f"""
Determine whether each item in the following list of \
topics is a topic in the article link below, which
is delimited with triple backticks.

Give your answer as list with 0 or 1 for each topic.\

List of topics: "nuxt", "vue", "javascript", "router", "react"

Article link: '''https://dev.to/mayashavin/effortlessly-nuxt-navigation-crafting-dynamic-breadcrumbs-with-storefront-ui-2p32'''
"""

promptTags = f"""
Detect the tags related to product description only that are being used in the following \
product listing link, which is delimited with triple backticks. \

Make each item one or two words long. \

Format your response as a list of lower-case words, separated by commas. \

Product listing link: '''https://www.etsy.com/il-en/listing/1214297580/cute-acrylic-resin-glitter-star-locket'''
"""
print(get_completion(promptTags))