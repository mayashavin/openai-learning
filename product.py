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
Your task is to help marketing team create a short and informative description for a retail store of a product based on the technical details.

Write a product description based on the information provided in the technical specifications delimited by triple \ backticks.

The description is intended for retailer customers who are looking for keychains and stickers, so should be friendly, cute and informative about the product's details.

Technical Specifications: ```{text}```
"""

response = get_completion(prompt)
print(response)