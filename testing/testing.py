from fastapi import APIRouter
from ..APIWrapper import APIWrapper

import google.generativeai as genai


# TODO: Add user feedback

router = APIRouter()

# TODO: INSERT YOUR GEMINI_API_KEY HERE, make sure to sign up for a free one if not using the group one
GEMINI_API_KEY = ""
genai.configure(api_key = GEMINI_API_KEY)
model = genai.GenerativeModel(model_name='gemini-2.0-flash',
                              generation_config={"response_mime_type": "text/plain"})

prompt_middleware = APIWrapper(api_key=GEMINI_API_KEY, model_name='gemini-2.0-flash')

# Generic prompt primer for agricultural chatbot
agroprompt = """You are a chatbot acting as an expert agronomist and agricultural extension officer with deep knowledge of Malawian smallholder farming. Your role is to answer farmer questions related to:

General agricultural practices, Identification and treatment of crop pests and diseases, Context-aware planting and harvesting advice

Your responses must follow these guidelines:

Responsiveness & Clarity:
Only respond to questions asked. Do not introduce new topics unprompted. If the question is missing important details, ask for clarification. Examples: “Which crop are you growing?”, “Can you tell me where you are located?”, “What does the disease look like?” 
If a question is vague, mistyped, or unclear, respond with your best guess, then explicitly ask for clarification.

e.g., “It sounds like you're asking about when to plant maize. Can you confirm or give more details?”

Language:
Respond in English or Chichewa, depending on the farmer’s input. Keep answers simple, respectful, and practical.

Contextual Relevance:
If the farmer’s location is given, tailor advice to that specific region (e.g., Northern, Central, Southern Malawi). If location is unknown, either ask or give the most widely applicable advice.The same applies to weather data or seasonal calendars; use it when available, or explain when you’re generalizing.

Resources:
Include links to guides or documents when useful. All external resources must come from a pre-approved set (to be defined later). Clearly label the links and briefly explain what the farmer can find there.

Avoid:
Overly technical language (unless explained simply). Guessing without signaling uncertainty or seeking confirmation.Providing the same generic advice to all questions. Ask before assuming.

Your goal is to act like a trusted advisor when real extension officers aren't available, ensuring each farmer gets reliable, contextual, and respectful support.

Here is your first prompt:
"""

@router.get("/", tags=["gemini"])
async def gem():
    return {"Hello": "Gemini"}

# FastAPI flag for get requests (HTTP requests which send a prompt and get the response)
@router.get("/testpromptllm", tags=["gemini"])
# asynchronous function for a get request
async def getexample(userprompt: str):
    # modify the given prompt made to api calls here (call the api wrapper function)
    finalprompt = userprompt + "please include the sentence 'inserted additional string' into your response"
    response = prompt_middleware.generate(prompt=userprompt)
    return response

# FastAPI flag for post request (HTTP requests which send a prompt and do not need the response)
@router.post("/postexample", tags=["gemini"])
# asynchronous function for a post request
async def postexample(userprompt: str):
    # modify the given prompt made to api calls here (call the api wrapper function)
    finalprompt = userprompt + "inserted additional string"
    response = model.generate_content(finalprompt)
    return response.text

# Purpose: For use in demos or manual testing
# GET endpoint for single prompt tests running through gemini
@router.get("/test_prompt", tags=["gemini"])
async def testprompt(userprompt: str):
    # TODO: prime model to respond to agriculture qs with prompt here, then follow up with userprompt
    finalprompt = agroprompt + userprompt
    response = prompt_middleware.generate(prompt=finalprompt)
    return response

# Purpose: Run to test active model's response to questions in the testing csv file
# Requires the appropriate testing.csv file which fits the schema, and produces a metrics_log.csv file
# POST endpoint for multiple prompt QA testing from testing csv file
@router.post("/batch_test", tags=["gemini"])
async def postexample(userprompt: str):
    # TODO: modify function to iterate over testing.csv (or call other function) and fill metrics_log.csv with metrics for each
    response = model.generate_content(userprompt)
    return response.text