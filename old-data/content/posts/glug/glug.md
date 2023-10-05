Title: Welcome to the Blog of GLUG NITH 
Date: 2021-01-31 17:47
Tags: glug, nith, welcome
Slug: glug-welcome
Category: glug
Author: glugnith
Summary: This blog uses Pelican Static Site Generator and `reStruxturedText`. ReStructuredText is a lightweight and powerful markup language very similar to `markdown`.

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
        |_static     # CSS and font files
        |_templates  # templates for generating webpages
```

## Contribution Guidelines

### Adding a new Post

* Fork this repository and clone to your system
```bash
    git clone https://github.com/<username>/glugnith.github.io.git
```
* Go to `content/posts` folder and choose a category to start with. We currently have 4 categories. Feel free to [open an issue](https://github.com/glugnith/glugnith.github.io/issues) to recommend new category. 

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
* Add a new `reStructuredText` or `markdown` file. Check for exisiting file names.
```bash
    # reStructuredText
    nano mypost.rst
    # Makrdown
    nano mypost.md
```
* Your file must contain these components in the following format. Put all images in `images` directory only.
* `reStructuredText`
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
* `Markdown`
```md
    Title: Your Post Title 
    Date: YYYY-MM-DD HH:mm
    Modified: YYYY-MM-DD HH:mm (only if existing article is being modified)
    Tags: add, some, tags, here, seperated, by, commas
    Slug: yourfilename-YYYYMMDD
    Category: category-selected-in-previous-steps
    Author: github-username

    <write your post here>
```
* Save and push to GitHub
```shell
    git stage -A
    git commit -m "commit message"
    git push origin master
```

### Improvements

* Fork this repository and clone to your system
```bash
    git clone https://github.com/<username>/glugnith.github.io.git
```
* This blog is based on [Pelican](https://blog.getpelican.com/) SSG. Install required components.
```bash
    cd glugnith.github.io
    sudo pip install -r requirements.txt
```
* Do your changes and test locally (comment `SITEURL` in `pelicanconf.py`)
```bash
    make html # generate html files
    make serve # serve on local host
```
* Push and add a Pull Request (do not forget to un-comment `SITEURL`)

## References

- [Pelican](https://blog.getpelican.com/)
- [Pelican Documentation](https://docs.getpelican.com/en/latest/index.html)
- [reStructuredText reference](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) - Most of them will work with pelican
