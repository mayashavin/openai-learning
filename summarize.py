from chatGPT import get_completion

text = f"""
Cute Acrylic Blueberry Macaron Keychain Charm | Violet Macaron Charm","Blueberry macaron keychain is the perfect decoration to your keys, tote bag, backpack, etc…..

This keychain comes with a purple red ball chain loop, and a matching 6cmx6cm glossy vinyl sticker!

🌹 DETAILS

- Size: 36mmx40mm(WxH). With the chain loop: 85mm height (length)
- Thickness: 4mm.
- High quality acrylic transparent keychain.
- 2-side full colors printed.
- Comes with a matching purple ball chain loop.

🌹 SHIPPING INFO

- Orders will be shipped within 1-2 days of purchase.
- Europe shipping: 5 - 7 business days (extra delay may subject to Corona situation).
- US and other destinations: 7 - 10 business days (due to Corona per destination)
- Israel: 3-4 business days
- All orders are shipped using standard shipping with tracking, unless it's FREE shipping

🌹 PACKAGING

- Each comes with removable anti-scratch plastic film in the back side that need to be removed before using.
- Color may vary slightly from the photo.
"""

prompt = f"""
Your task is to generate a short summary of the product description based \ 
on the information provided in the technical specifications delimited by triple \ backticks. \ 

Summarize the product description in a most 100 words, and focus on any technical aspects that \ 
are relevant to the product's details. Leave out shipping information. \ 

Technical Specifications: ```{text}```
"""


titlePrompt = f"""
Your task is to generate a title for the product based \ 
on the information provided in the technical specifications delimited by triple \ backticks. \ 

Generate an informative and catchy product title from the technical specifications below in a most 15 words with focus only on the product's details. \ 

Technical Specifications: ```{text}```
"""

response = get_completion(prompt)
print(response)