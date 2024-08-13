from transformers import pipeline, AutoTokenizer, AutoModelForVision2Seq, AutoImageProcessor

import os
os.environ['HF_HOME'] = 'D:/hf_home'

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

    # Decode the text with clean_up_tokenization_spaces
    # cleaned_text = tokenizer.decode(tokenizer.encode(text, add_special_tokens=False), 
    #                                 clean_up_tokenization_spaces=True, 
    #                                 truncation=True)

    #cleaned_text = tokenizer.decode(tokenizer.encode(text, add_special_tokens=False), clean_up_tokenization_spaces=True)
    #cleaned_text = tokenizer.decode(text, skip_special_tokens=False, clean_up_tokenization_spaces=True)
    
     
    # Print the cleaned-up text
    #print(cleaned_text)


    # # Initialize the pipeline
    # #image_to_text = pipeline("image-to-text", model=model, tokenizer=tokenizer, device=0)
    # result = image_to_text(url)
    # text = result[0]['generated_text']
    # # cleaned_text = tokenizer.decode(tokenizer.encode(result), clean_up_tokenization_spaces=True)
    # # cleaned_text = tokenizer.decode(tokenizer.encode(result), clean_up_tokenization_spaces=True)
    # cleaned_text = tokenizer.decode(tokenizer.encode(result, add_special_tokens=False), clean_up_tokenization_spaces=True)

    # print(cleaned_text)

# text to speech


if __name__ == "__main__":
    print('ok')
    img2text("https://huggingface.co/datasets/Narsil/image_dummy/resolve/main/parrots.png")