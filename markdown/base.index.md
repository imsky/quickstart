<!--
Base Markdown from Quickstart
qkst.io/markdown/base
-->

# Hello World

## Welcome to Markdown

This is a document written in Markdown. It has **bold**, *italic*, and ~~strikethrough~~ text. It's written using [GitHub Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/) features, though most of it will work with other Markdown parsers.

Here's a list of links:

* A link with text to [Markdown](http://daringfireball.net/projects/markdown/)
* A reference-style link to [Markdown][1]
* A link without text to <http://daringfireball.net/projects/markdown/>

[1]: http://daringfireball.net/projects/markdown/

Here's an image:

![General Motors Technical Center, Warren, Michigan, 1945; 1946-56. Administration Building stair](http://cdn.loc.gov/service/pnp/krb/00100/00152r.jpg)

Here's some Scheme code included using GFM syntax:

```scheme
(define (flatten x)
    (cond ((null? x) '())
          ((not (pair? x)) (list x))
          (else (append (flatten (car x))
                        (flatten (cdr x))))))
```

Here's a table using GFM syntax:

Month | Commits
----- | -------
Jan   | 567
Feb   | 345

And here's a table using plain HTML:

<table>
    <thead>
        <tr><th>Month</th><th>Commits</th></tr>
    </thead>
    <tbody>
        <tr><td>Jan</td><td>567</td></tr>
        <tr><td>Feb</td><td>345</td></tr>
    </tbody>
</table>

You can use a small, but useful, subset of HTML in Markdown:

<h3>Markdown Links</h3>

<ul>
    <li><a href="http://daringfireball.net/projects/markdown/syntax">Markdown</a></li>
    <li><a href="https://help.github.com/articles/github-flavored-markdown/">GitHub Flavored Markdown</a></li>
    <li><a href="http://commonmark.org/">CommonMark</a></li>
    <li><a href="http://johnmacfarlane.net/babelmark2">Babelmark 2</a></li>
    <li><a href="http://dillinger.io/">Dillinger</a></li>
</ul>
