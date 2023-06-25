# About

This project aims to allow users to find a good land to invest in taking various factors into account. The code will be easy to read and modify, while the GUI will be even easier to read and interact with.

# Preparing the Environment

Make sure [`Miniconda`](https://docs.conda.io/en/latest/miniconda.html) is installed on your system.

Create or update the conda environment.

```
conda env update --file environment.yaml
```

Activate the conda environment.

```
conda activate real-estate-analysis
```

Run the code.

```
streamlit run main.py
```

# Rules

- Please provide proper type hints to function parameters and global variables whenever possible. Also, turn on the basic type checking on the IDE you are using.
- Use the [Black](https://github.com/psf/black) formatter style.
