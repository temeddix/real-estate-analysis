# About

This project aims to allow users to find a good land to invest in taking various factors into account. The code will be easy to read and modify, while the GUI will be even easier to read and interact with.

As this project is interested in Korean lands, all user interface texts will be written in Korean to fully represent national laws and terminologies.

# Commands

Make sure [`Miniconda`](https://docs.conda.io/en/latest/miniconda.html) is installed on your system. These commands are expected to be executed in the project directory.

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
streamlit run home.py
```

# Rules

- Please provide proper type hints to function parameters and global variables whenever possible. Also, turn on the basic type checking on the IDE you are using.
- Use the [Black](https://github.com/psf/black) formatter.
