# How to contirbute to this documentation

Clone the docs repo from GitHub:
```console
git clone https://github.com/bird-house/birdhouse-docs.git

cd birdhouse-docs
```

Create conda environment:
```console
conda env create
conda activate birdhouse-docs
```

Build the docs:
```console
mkdocs build

# html output is in folder site/
```

Or serve the docs for your browser:
```console
mkdocs serve
```

### Adding new pages

Please read the docs at [mkdocs](https://www.mkdocs.org/) and also at [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

There is a [user guide](https://www.mkdocs.org/user-guide/writing-your-docs/) on mkdocs describing how to add new pages with markdown.

### Convert rst to markdown

You can convert `rst` files to *markdown* using [pandoc](https://pandoc.org/).

```console
pandoc tutorial.rst -t markdown -o tutorial.md
```

Probably some edits are neccessary after the conversion.

