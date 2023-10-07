# Welcome to the Blog of GLUG NITH 

<img src="content/images/glug-dark.svg" align=center alt="The GLUG Logo">

This blog uses Pelican Static Site Generator and `reStruxturedText`. ReStructuredText is a lightweight and powerful markup language very similar to `markdown`.

## Directory Structure

```bash
    .
    |_.github       # Workflow Files
    |_content
    |   |_extras    # static files
    |   |_images    # images for posts and website
    |   |_pages     # static pages
    |   |_posts     # post files (add your post here)
    |_themes/alchemy
       |_static     # CSS anf font files
       |_templates  # templates for generating webpages
```

## Contribution Guidelines

### Adding a new Post

1. Fork this repository and clone to your system

```bash
    git clone https://github.com/<username>/glugnith.github.io.git
```

2. Go to `content/posts` folder and choose a category to start with. We currently have 4 categories. Feel free to [open an issue](https://github.com/glugnith/glugnith.github.io/issues) to recommend new category. 

| Category | Description |
| --- | --- |
| development | web/app/desktop development articles |
| programming | programming language tips & tricks, competitive programming articles |
| tools | IDE, editors, other open source development tools articles |
| experience | interview, internship, placement experience articles |

```bash
    cd glugnith.github.io/content/posts
    # let us choose development category
    cd development
```
3. Add a new `reStructuredText` file. Check for exisiting file names.

```bash
    nano mypost.rst
```
4. Your file must contain these components in the following format. Put all images in `images` directory only.

```rst
    *******************************************************
    Your Post Title Surrounded by Asterisks Above and Below
    *******************************************************

    :date: YYYY-MM-DD HH:mm
    :modified: YYYY-MM-DD HH:mm (only if existing article is being modified)
    :tags: add, some, tags, here, seperated, by, commas
    :slug: yourfilename-YYYYMMDD
    :category: category-selected-in-previous-steps
    :author: github-username

    <write your post here>
```

4. Save and push to GitHub

```shell
    git stage -A
    git commit -m "commit message"
    git push origin master
```

### Improvements

1. Fork this repository and clone to your system

```bash
    git clone https://github.com/<username>/glugnith.github.io.git
```

2. This blog is based on [Pelican](https://blog.getpelican.com/) SSG. Install required components.

```bash
    cd glugnith.github.io
    sudo pip install -r requirements.txt
```

3. Do your changes and test locally (comment `SITEURL` in `pelicanconf.py`)

```bash
    make html # generate html files
    make serve # serve on local host
```
4. Push and add a Pull Request (do not forget to un-comment `SITEURL`)

### References

- [Pelican](https://blog.getpelican.com/)
- [Pelican Documentation](https://docs.getpelican.com/en/latest/index.html)
- [reStructuredText reference](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) - Most of them will work with pelican
