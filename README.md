# CoolPath

CoolPath is a Cool Command Line Tool that let you interact with your PATH environmental variable in a more fast and easy way.

## Installation

#### UNIX

At the moment you need to clone the repository, and `cd` into it.

With `conda` [installed](https://docs.conda.io/projects/conda/en/latest/user-guide/install/), create an environment from the `environment.yml` file and target the location to a local directory named `env`:

```shell
conda env create -f environment.yml --prefix ./env
```

Now to activate the environment, on the rooth of the `coolpath` cloned repo use:

```shell
conda activate ./env
```

You are ready to use the commands from the **usage** section.

## Usage

To display your path as a numbered list:

```shell
python coolpath.py list
```

## Things to do:

- Figure it out how to change an environment variable from python code.
