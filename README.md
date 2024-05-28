# Anthropic FastAPI Service

This is a FastAPI service that provides a RESTful API for the 
Anthropic Claude AI model using [anthropic-sdk-python](https://https://github.com/anthropics/anthropic-sdk-python). For more information on the model, please refer to the [Anthropic Claude AI model](https://docs.anthropic.com/claude/reference)

## Documentation
----------------
The API documentation can be found at [http://localhost:8000/docs](http://localhost:8080/docs)

## Running the Project

### Running the Project Locally
---------------
1. Clone the repository
```bash
git clone https://github.com/furkankyildirim/anthropic-fastapi-service.git
cd anthropic-fastapi-service/
```

2. Create a `.env` file in the root directory and add the following environment variables
```bash
ANTHROPIC_API_KEY=YOUR_API_KEY
```

3. Create a system message file on src/data/system-messages.txt (Optional)
```bash
echo "You are a personal AI assistant" > src/data/system-messages.txt
```


4. Create a virtual environment and install the dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

5. Run the following commands to start the server
```bash
chmod +x runner.sh
./runner.sh
```

### Running the Project with Docker
---------------
1. Clone the repository
```bash
git clone https://github.com/furkankyildirim/anthropic-fastapi-service.git 
cd anthropic-fastapi-service/
```

2. Create a `.env` file in the root directory and add the following environment variables
```bash
ANTHROPIC_API_KEY=YOUR_API_KEY
```

3. Create a system message file on src/data/system-messages.txt (Optional)
```bash
echo "You are a personal AI assistant" > src/data/system-messages.txt
```

4. Build and run the docker container
```bash
docker-compose up --build
```
