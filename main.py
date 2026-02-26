import json
from app import generate_structured_response, StructuredResponse

def main():
    prompt = input("Enter your prompt: ")
    temperature = float(input("Enter temperature (0 - 1.5): "))

    raw_response = generate_structured_response(prompt, temperature)

    try:
        parsed_json = json.loads(raw_response)
        validated = StructuredResponse(**parsed_json)

        print("\nStructured Response:\n")
        print(validated.model_dump_json(indent=4))

    except Exception as e:
        print("\n⚠ Error parsing structured response:")
        print(e)
        print("\nRaw Output:")
        print(raw_response)

if __name__ == "__main__":
    main()