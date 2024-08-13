# Overview

An example of using HuggingFace

## Install Pytorch

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118


## Test tht installation is all working 

python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"


##

C:\src\github.com\ongzhixian\HuggingFace\.venv\lib\site-packages\transformers\tokenization_utils_base.py:1601: FutureWarning: `clean_up_tokenization_spaces` was not set. It will be set to `True` by default. This behavior will be depracted in transformers v4.45, and will be then set to `False` by default. 
For more details check this issue: https://github.com/huggingface/transformers/issues/31884
  warnings.warn(

C:\src\github.com\ongzhixian\HuggingFace\.venv\lib\site-packages\transformers\generation\utils.py:1258: UserWarning: Using the model-agnostic default `max_length` (=20) to control the generation length. We recommend setting `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(

[{'generated_text': 'two birds are standing next to each other birds'}]



C:\src\github.com\ongzhixian\HuggingFace\.venv\lib\site-packages\transformers\tokenization_utils_base.py:1601: FutureWarning: `clean_up_tokenization_spaces` was not set. It will be set to `True` by default. This behavior will be depracted in transformers v4.45, and will be then set to `False` by default. For more details check this issue: https://github.com/huggingface/transformers/issues/31884
  warnings.warn(
C:\src\github.com\ongzhixian\HuggingFace\.venv\lib\site-packages\transformers\generation\utils.py:1258: UserWarning: Using the model-agnostic default `max_length` (=20) to control the generation length. We recommend setting `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
[{'generated_text': 'two birds are standing next to each other birds'}]

## Troubleshooting

```
A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.0.1 as it may crash. To support both 1.x and 2.x
versions of NumPy, modules must be compiled with NumPy 2.0.
Some module may need to rebuild instead e.g. with 'pybind11>=2.12'.

If you are a user of the module, the easiest solution will be to
downgrade to 'numpy<2' or try to upgrade the affected module.
We expect that some modules will need time to support NumPy 2.
```

Fix:
pip uninstall numpy       # uninstall existing numpy
pip install "numpy<2.0"