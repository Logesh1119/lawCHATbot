<h1 align="center">LawGPT - RAG based Generative AI Attorney Chatbot</h1>
<h3 align="center">Know Your Rights! Better Citizen, Better Nation!</h1>

<p align="center">
<img  src="https://github.com/user-attachments/assets/98eb5664-0aac-46d0-864e-74bbf31bd525" width="700"/>
</p>

## About The Project
LawGPT is a RAG based generative AI attorney chatbot that is trained using Indian Penal Code data. This project was developed using Streamlit LangChain and TogetherAI API for the LLM. Ask any questions to the attorney and it will give you the right justice as per the IPC. Are you a noob in knowing your rights? then this is for you!
<br>

<div align="center">
  <br>
  <video src="https://github.com/user-attachments/assets/f3158545-7adb-4d28-b8b2-66f9a67b3fdf" width="400" />
  <br>
</div>




 

## Getting Started
 
#### 1. Install necessary packages:
   - ```
     pip install -r requirements.txt
     ```
#### 2. Run the `ingest.py` file, preferably on kaggle or colab for faster embeddings processing and then download the `ipc_vector_db` from the output folder and save it locally.


 ####3. Sign up with Together AI , Whether you choose to use it for a short-term project or opt for a long-term commitment,  You also have the flexibility to explore other Language Models (LLMs) or APIs if you prefer. For a comprehensive list of options, check out this link: [python.langchain.com/docs/integrations/llms](https://python.langchain.com/docs/integrations/llms) . Once signed up, seamlessly integrate Together AI into your Python environment by setting the API Key as an environment variable. 💻✨ 
   - ```
      os.environ["TOGETHER_API_KEY"] = "YOUR_TOGETHER_API_KEY"`
     ```
   - If you are going to host it in streamlit, huggingface or other...
      - Save it in the secrets variable provided by the hosting with the name `TOGETHER_API_KEY` and key as `YOUR_TOGETHER_API_KEY`.


#### 5. To run the `app.py` file, open the CMD Terminal and and type `streamlit run app.py`.

 
