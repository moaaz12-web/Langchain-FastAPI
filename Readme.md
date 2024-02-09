# FastAPI for interacting with langchain and GPT-3.5 based chatbot, with Redis database as the vector store-backed retriever memory.

## How to run

### Using virtual environment:

1. Set up a virtual environment:
<code>python -m venv myenv</code>

2. Create a .env file and add 'OPENAI_API_KEY', 'REDIS_URL', and 'HUGGINGFACEHUB_API_TOKEN as variables

3. Navigate to the app directory:
<code>cd app</code>

4. Install the required dependencies:
<code>pip install -r requirements.txt</code>

5. Run the FastAPI server with uvicorn:
<code>uvicorn main:app --reload --port=8000 --host=0.0.0.0</code>


### Using Docker Compose:

1. Build the Docker images:
<code>docker-compose build</code>

2. Start the Docker containers:
<code>docker-compose up</code>


## API Documentation

### Changing User for Redis Vector Store

To change the Redis vector store retriever memory to a specific user, send a request to the following endpoint:

<code>localhost:8000/api/{username}</code>

Replace `{username}` with the desired username. This action ensures that the chatbot will only retrieve data from the Redis database specific to that user.


### Accessing API Documentation

For detailed documentation on how to interact with the APIs in the application, visit:
<code>localhost:8000/docs</code>


This endpoint provides comprehensive guidance on utilizing the APIs effectively.

---

You can seamlessly integrate this backend into your existing application, providing your users with access to a dedicated vector-based database chatbot. Remember to generate the repsective API keys.



