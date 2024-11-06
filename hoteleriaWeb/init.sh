if ! [ -x "$(command -v python)" ]; then
  echo "Debe instalar python"
  exit 1
fi

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
