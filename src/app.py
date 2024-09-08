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
Please provide detailed information about the underlying model used for generating responses. Structure your response as follows:

- **Model Name**: 
- **Version**: 
- **Key Features**: 
- **Capabilities**: 
- **Limitations**: 

Ensure that your response is based on accurate and relevant information, and avoid any speculative statements. Take a moment to think through your answer before providing it.
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
