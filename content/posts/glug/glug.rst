*********************************************************************
Welcome to Official blog of :abbr:`GLUG NITH (GNU/Linux Users Group)`
*********************************************************************

:date: 2021-01-31 17:47
:tags: glug, nith, welcome
:slug: glug-welcome
:category: glug
:author: glugnith
:summary: This blog uses Pelican Static Site Generator and :code:`reStruxturedText`. ReStructuredText is a lightweight and powerful markup language very similar to :code:`markdown`.

This blog uses Pelican Static Site Generator and :code:`reStruxturedText`. ReStructuredText is a lightweight and powerful markup language very similar to :code:`markdown`.

Directory Structure
===================

.. code-block:: bash

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


Contribution Guidelines
=======================

Adding a new Post
-----------------

1. Fork this repository and clone to your system

.. code-block:: bash

    git clone https://github.com/<username>/glugnith.github.io.git


2. Go to :code:`content/posts` folder and choose a category to start with. We currently have 4 categories. Feel free to `open an issue <https://github.com/glugnith/glugnith.github.io/issues>`_ to recommend new category. 

.. table::
    :align: center

    +-------------+----------------------------------------------------------------------+
    | Category    | Description                                                          |
    +=============+======================================================================+
    | development | web/app/desktop development articles                                 |          
    +-------------+----------------------------------------------------------------------+
    | programming | programming language tips & tricks, competitive programming articles |
    +-------------+----------------------------------------------------------------------+
    | tools       | IDE, editors, other open source development tools articles           |
    +-------------+----------------------------------------------------------------------+
    | experience  | interview, internship, placement experience articles                 |
    +-------------+----------------------------------------------------------------------+
    



.. code-block:: bash

    cd glugnith.github.io/content/posts
    # let us choose development category
    cd development

3. Add a new :code:`reStructuredText` file. Check for exisiting file names.

.. code-block:: bash

    nano mypost.rst

4. Your file must contain these components in the following format. Put all images in `images` directory only.

.. code-block:: rst

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

4. Save and push to GitHub

.. code-block:: bash

    git stage -A
    git commit -m "commit message"
    git push origin master

Improvements
------------

1. Fork this repository and clone to your system

.. code-block:: bash

    git clone https://github.com/<username>/glugnith.github.io.git


2. This blog is based on `Pelican <https://blog.getpelican.com/>`_ SSG. Install required components.

.. code-block:: bash

    cd glugnith.github.io
    sudo pip install -r requirements.txt

3. Do your changes and test locally (comment :code:`SITEURL` in :code:`pelicanconf.py`)

.. code-block:: bash

    make html # generate html files
    make serve # serve on local host

4. Push and add a Pull Request (do not forget to un-comment :code:`SITEURL`)

References
==========

* `Pelican <https://blog.getpelican.com/>`_
* `Pelican Documentation <https://docs.getpelican.com/en/latest/index.html>`_
* `reStructuredText reference <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ - Most of them will work with pelican
