import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set your API key
client = OpenAI()


def get_response(system_prompt, user_prompt):
    # Assign the role and content for each message
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0
    )

    return response.choices[0].message.content


# Try the function with a system and user prompt of your choice
response = get_response(
    "You are an expert data scientist that explains complex concepts in understandable terms",
    "Define AI",
)
print(response)


# Define the purpose of the chatbot
chatbot_purpose = "You are the customer support chatbot for an e-commerce platform specializing in electronics. Your role is to assist customers with inquiries, order tracking, and troubleshooting common issues related to their purchases. "

# Define audience guidelines
audience_guidelines = "Your primary audience consists of tech-savvy individuals who are interested in purchasing electronic gadgets. "

# Define tone guidelines
tone_guidelines = "Maintain a professional and user-friendly tone in your responses."

base_system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = get_response(
    base_system_prompt, "My new headphones aren't connecting to my device"
)
print(response)


# Define the order number condition
order_number_condition = "If the user is asking about an order, and did not specify the order number, reply by asking for this number. "

# Define the technical issue condition
technical_issue_condition = "If the user is talking about a technical issue, start your response with `I'm sorry to hear about your issue with ...` "

# Create the refined system prompt
refined_system_prompt = (
    base_system_prompt + order_number_condition + technical_issue_condition
)

response_1 = get_response(
    refined_system_prompt, "My laptop screen is flickering. What should I do?"
)
response_2 = get_response(
    refined_system_prompt, "Can you help me track my recent order?"
)

print("Response 1: ", response_1)
print("Response 2: ", response_2)


# Craft the system_prompt using the role-playing approach
system_prompt = "Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options."

user_prompt = "Hello there! I'm a beginner with a marketing background, and I'm really interested in learning about Python, data analytics, and machine learning. Can you recommend some books?"

response = get_response(system_prompt, user_prompt)
print(response)


base_system_prompt = "Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options."

# Define behavior guidelines
behavior_guidelines = "If the user's query does not include details about their background, experience, or goals, kindly ask them to provide the missing information."

# Define response guidelines
response_guidelines = "Don't recommend more than three textbooks in the learning path"

system_prompt = base_system_prompt + behavior_guidelines + response_guidelines
user_prompt = "Hey, I'm looking for courses on Python and data visualization. What do you recommend?"
response = get_response(system_prompt, user_prompt)
print(response)


# Define the system prompt
system_prompt = "You are a customer service chatbot for MyPersonalDelivery, a delivery service that offers a wide range of delivery options for various items. You should respond to user queries in a gentle way."

context_question = "What types of items can be delivered using MyPersonalDelivery?"
context_answer = "We deliver everything from everyday essentials such as groceries, medications, and documents to larger items like electronics, clothing, and furniture. However, please note that we currently do not offer delivery for hazardous materials or extremely fragile items requiring special handling."

# Add the context to the model
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": context_question},
        {"role": "assistant", "content": context_answer},
        {"role": "user", "content": "Do you deliver furniture?"},
    ],
)
response = response.choices[0].message.content
print(response)


# added/edited
service_description = "\nWelcome to MyPersonalDelivery, your trusted and versatile delivery service partner. At MyPersonalDelivery, we are committed to providing you with a seamless and efficient delivery experience for a wide range of items. Whether you need groceries, documents, electronics, or even furniture, we've got you covered.\n\nOur Services:\nWe offer a diverse range of delivery services to cater to your unique needs. From same-day delivery for urgent items to scheduled deliveries that fit your convenience, we have the flexibility to meet your busy lifestyle. Our real-time tracking system ensures that you can monitor the status of your delivery every step of the way.\n\nWhat We Deliver:\nOur service is designed to handle various items, including everyday essentials such as groceries and medications. Need to send important documents? No problem, we'll ensure they reach their destination securely. We also specialize in transporting larger items like electronics, clothing, and even furniture. However, please note that we currently do not offer delivery for hazardous materials or items that are extremely fragile and require special handling.\n\nSafety and Care:\nYour items' safety is our top priority. We take pride in our secure handling practices to ensure that your deliveries arrive intact. Our contactless delivery option minimizes physical contact, adding an extra layer of safety during these times. We understand that each item is valuable, and you can trust us to treat your belongings with the utmost care.\n\nWhy Choose MyPersonalDelivery:\n- Wide variety of items delivered\n- Flexible delivery options\n- Real-time tracking for peace of mind\n- Secure handling and contactless delivery\n- Reliable service with a commitment to excellence\n\nWhether you need a small package delivered across town or a larger item transported across the city, you can rely on MyPersonalDelivery to provide a reliable, secure, and efficient delivery solution. Your satisfaction is our driving force, and we look forward to serving you with our dedicated and customer-centric approach.\n\nFeel free to ask any questions you may have about our services, and we'll be more than happy to assist you.\n\n"

# Define the system prompt
system_prompt = f"""You are a customer service chatbot for MyPersonalDelivery whose service description is delimited by triple backticks. You should respond to user queries in a gentle way.
 ```{service_description}```
"""

user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response(system_prompt, user_prompt)

print(response)