
# Make the virtual environment if it doesn't exist
if [ ! -d "env" ]; then
  python -m venv env
fi

# Go into the virtual environment
source env/Scripts/activate

# Get pre-requisites
pip install -r requirements.txt

# Start local server on port 8000
export PY=python
export PORT=8000

./develop_server.sh restart $PORT
