from transformers import pipeline, AutoTokenizer, AutoModelForVision2Seq, AutoImageProcessor

# img2text
def img2text(url):
        
    model_name = "Salesforce/blip-image-captioning-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name, clean_up_tokenization_spaces=True)
    model = AutoModelForVision2Seq.from_pretrained(model_name)
    image_processor = AutoImageProcessor.from_pretrained(model_name)

    # Initialize the pipeline
    image_to_text = pipeline("image-to-text", model=model, tokenizer=tokenizer, feature_extractor=image_processor, device='cuda')
    result = image_to_text(url, max_new_tokens=50)

    # Extract the generated text
    text = result[0]['generated_text']
    print(text)
    

# llm

# text to speech


if __name__ == "__main__":
    print('ok')
    img2text('C:/Users/zhixian/Downloads/parrots.png')

