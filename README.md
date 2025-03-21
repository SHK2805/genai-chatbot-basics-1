# GENAI ChatBot Basics 1

* Date: 09 Feb

### Environment Setup
* The project uses `conda`
* Set the environment, update the requirements and install the dependencies

### .env
* Create a `.env` file in the root directory
* The required keys are stored in this file
* The keys are loaded using the below code
```python
from config.set_config import Config

config = Config()
if config.set():
    print("Environment variables set")
else:
    print("Environment variables NOT set")
```

### GROQ
* The project uses GROQ to query the data
* Install the GROQ package by adding `langchain-groq` to requirements.txt

