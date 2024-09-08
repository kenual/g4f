from g4f.gui import run_gui
from g4f.api import run_api
from g4f.client import Client
from g4f.models import sdxl, sd_3, playground_v2_5, flux, flux_realism, flux_anime, flux_3d, flux_disney, dalle, dalle_mini, emi


def main():
    run_api()


def gui():
    run_gui()


def test_image_models():
    image_models = [sdxl, sd_3, playground_v2_5, flux, flux_realism,
                    flux_anime, flux_3d, flux_disney, dalle, dalle_mini, emi]
    client = Client()
    response = client.images.generate(
        model="gemini",
        prompt="a white siamese cat",
    )
    image_url = response.data[0].url


def test_text_models():
    client = Client()

    text_models = ['gpt-4o', 'gpt-4o-mini', 'llama-3-70b', 'llama-3.1-8b', 'llama-3.1-70b', 'llama-3.1-405b', 'mistral-7b', 'phi-3-mini-4k', 'gemini-pro', 'gemini-flash',
                   'blackbox', 'sparkdesk-v1.1', 'qwen-1.5-14b', 'glm-3-6b', 'glm-4-9b', 'glm-4', 'yi-1.5-9b', 'solar-1-mini', 'samba-coe-v0.1', 'v1olet-merged-7b', 'westlake-7b-v2', 'deepseek']
    unavailable_models = ['gpt-4']
    working_models = []

    for model in text_models:
        print(f'{model}: ')
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": '''
You are an advanced AI language model. Please provide a detailed summary of your capabilities, addressing the following queries:

1. **Model Identification**:
   - State your model name and version (e.g., GPT-4, GPT-3.5).

2. **Advanced Feature Support**:
   - Indicate whether you support the following **advanced LLM features**. For each supported feature, provide a brief explanation:
     1. **Function Calling** (e.g., API invocation for external functions)
     2. **Code Generation and Execution**
     3. **Tool Integration** (e.g., calculator, calendar, or plugin use)
     4. **Memory and Context Retention** (across interactions or sessions)
     5. **Multimodal Input/Output** (e.g., handling text, images, or audio)
     6. **Natural Language API Programming**
     7. **Dynamic Task Handling** (e.g., breaking complex tasks into sub-tasks)
     8. **Extended Text Generation** (e.g., technical reports, creative writing)
     9. **Conversational Memory** (maintaining context in dialogue)
     10. **Task-Specific Fine-Tuning** (e.g., for medical, legal, or financial domains)
     11. **Real-Time Search and Data Retrieval**

### Response Format:
- `Model Number`: [Your Model Name and Version]
- `Advanced LLM Feature Support`: [Yes/No - If yes, list the supported features and give a brief explanation for each.]

### Additional Instructions:
- Provide a structured response in the given format.
- Mention any limitations or uncertainties clearly.
                           '''}]
            )
        except Exception as e:
            print(f'ERROR: {e}')
            unavailable_models.append(model)
            continue

        working_models.append(model)
        print(response.choices[0].message.content)
        print()

    print(f'Unavailable models: {unavailable_models}')
    print(f'Text models: {text_models}')


if __name__ == "__main__":
    test_text_models()
