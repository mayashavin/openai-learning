from chatGPT import get_completion

text = f"""
My wife and I are planning to buy a house. \ 
We have been saving up for a while now, \ 
and we are finally ready to make the big purchase. \
We have in mind a budget of $500,000.  \ 
And the house we like is listed at $600,000. \ 
We are thinking of getting a loan for the remaining $100,000. \ 
Can we talk to a loan officer about this? \ 
We need an answer as soon as possible. so any time within this week is good for us. \ 
We are available on the morning, and we live in Tel Aviv. \ 
We can come to the office if it is necessary. \ 
"""

text2 = f"""
"time":"10:00","location":"Tel Aviv","loan_amount":"100000","loan_type":"mortgage","date":"2021-10-10","agent":"Mary Jane","instructions":"bring your IDs and income proofs"
"""

prompt2 = f"""
Perform the following actions:
1 - Translate the following JSON formatted text delimited by triple \ backticks into a informative sentence, starting with the following format:
We have found a meeting scheduled for you at..., with ... about .... Please be on time and ...
2 - Ask for a confirmation from the user.

Text:
```{text2}```
"""

meetingTypes = f"""
msfsi_meetingtypeid: d7237666-8b9f-ec11-b400-0022480b8113, msfsi_meetingtypename: House Mortgage
msfsi_meetingtypeid: d7237666-8b9f-ec11-b400-0022480b8130, msfsi_meetingtypename: Open an investment account
msfsi_meetingtypeid: d7237666-8b9f-ec11-b400-0022480b8140, msfsi_meetingtypename: Financial health check-up
"""

prompt3 = f"""
Perform the following actions:
1 - Summarize the following text delimited by triple \ backticks with 1 sentence.
2 - Find the most relevant meeting type from the list below
{meetingTypes}
3 - Prepare a meeting in JSON format with the following keys: loan_amount, time_available, branch_location, loan_type, meeting_id from the matched meeting type found.

Separate your answers with line breaks.

Text:
```{text}```
"""
prompt = f"""
Perform the following actions: 
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Output a json object that contains the following \
keys: loan_amount, time_available, branch_location, loan_type.

Separate your answers with line breaks.

Text:
```{text}```
"""

prompt4 = f"""
Perform the following actions:
1 - Output a time frame for the meeting possible for the user from today 03 May 2023, using the JSON format: start_time, end_time.
2 - Prepare a JSON format from the text and information from Step 1 with the following keys:
loan_amount, start_time, end_time, branch_location, loan_type.

If the loan amount is more than $100,000, ask the user to come to the office for a meeting.
Otherwise, output the following message: You don't need to schedule a meeting. I create for you an online loan application with the following details: you want to borrow ... for ...."

Separate your answers with line breaks.

Text:
```{text}```
"""
response = get_completion(prompt4)
print("Completion for Text 1:")
print(response)
