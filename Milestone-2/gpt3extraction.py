import openai
import csv

# Set up OpenAI API credentials
openai.api_key = "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"

# Set the GPT-3 model and parameters
model_engine = "text-davinci-003"
temperature = 0.9
top_p = 1

# Load the prompts from the CSV file
with open("prompts_1.csv", "r") as f:
    reader = csv.reader(f)
    # numP = [row[0][0] for row in reader]
    prompts = [row[0] for row in reader]

# Generate GPT-3 data for each prompt and save in a new CSV file
with open("reddit_davinci_charan2.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for prompt in prompts:
        # Split the prompt into smaller parts
        prompt_parts = [prompt[i:i+2048] for i in range(0, len(prompt), 2048)]

        # Generate GPT-3 data for each prompt part
        generated_data = ""
        while len(generated_data.split()) < 200:  # Generate until at least 500 words are produced
            for part in prompt_parts:
                response = openai.Completion.create(
                    engine=model_engine,
                    prompt=part,
                    max_tokens=475,
                    temperature=temperature,
                    top_p=top_p,
                    n=1,
                    stop=None,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                generated_data += response['choices'][0]['text']
                if len(generated_data.split()) >= 250:
                    break  # Stop generating if at least 500 words have been produced
            if len(generated_data.split()) < 500:
                prompt_parts = [prompt[i:i+2048] for i in range(0, len(prompt), 2048)]  # Reset prompt parts if not enough text has been generated

        # writer.writerow([prompts.index(prompt)+1, prompt, generated_data.strip().replace('\n', ' ')])  # Write the prompt and generated data to the new CSV file
        writer.writerow([prompts.index(prompt), prompt, "['" +generated_data.strip().replace('\n', ' ')+"']"])  # Write the prompt and generated data to the new CSV file
