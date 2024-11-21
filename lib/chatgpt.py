import openai
import os
import csv

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  #api key
)

# Load match data from CSV file
def load_match_data_from_csv(file_path):
    match_data = []
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            match_data.append(row)
    return match_data

# This function calls the OpenAI API and summarizes the data
def summarize_match_data_with_gpt(match_data):
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure the OpenAI API key is set in environment variables

    # Prepare the data summary to send to ChatGPT
    match_summary = "Here is a summary of the match data:\n"
    for match in match_data:
        match_summary += (
            f"Match ID: {match['match_id']}, Result: {match['result']}, "
            f"Champion: {match['champion']}, KDA: {match['kills']}/{match['deaths']}/{match['assists']}, "
            f"Damage: {match['damage']}, Lane: {match['lane']}\n"
        )

    # Prepare the messages for the ChatCompletion API
    messages = [
        {"role": "system", "content": "You are an expert League of Legends analyst."},
        {
            "role": "user",
            "content": (
                match_summary +
                "\nCan you provide a summary or any insights into the player's performance?"
            ),
        },
    ]

    # Make the API call using the new syntax
    response = client.chat.completions.create(
        model="gpt-4o-2024-05-13",  # gpt model idk
        messages=messages,
        temperature=0.7,  # Adjust temperature for a balanced response
        max_tokens= 250
    )

    # Extract the assistant's reply from the response
    gpt_summary = response.choices[0].message.content
    return gpt_summary
