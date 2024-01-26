## Talk:
https://github.com/bangpypers/meetup-talks/issues/17
Deploying a streamlit app as an executable

I used and modified this starter repo

# Enopios

Install poetry, tested with poetry version `1.2.0rc2`.

```
curl -sSL https://install.python-poetry.org | python - --preview
```

Install dependencies:

```
poetry install
```

If you want to include extra dependencies edit the `pyproject.toml` file.

If you have changed any dependencies run the following:

```
poetry update
poetry export -f requirements.txt --output requirements.txt
```

Update `enopios/app.py` if you want to have a different streamlit script than
the bare-bones hello world.

Build the executable:

```
poetry run pyoxidizer build
```

Run the newly created executable:

```
./build/dist/enopios
```

## Additional Changes done:
To package https://github.com/nagendra-y/streamlit-indictrans2  
- Removed the TF dependency. It was causing a functools32 error similar to https://github.com/python-poetry/poetry/issues/1334
- Update the app.py code
- Change the poetry installation from using a https://github.com/snok/install-poetry workflow(which didn't work) into using `pip install poetry`  
