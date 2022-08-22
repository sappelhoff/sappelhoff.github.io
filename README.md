[![CircleCI](https://circleci.com/gh/sappelhoff/sappelhoff.github.io.svg?style=shield)](https://circleci.com/gh/sappelhoff/sappelhoff.github.io)

This repository contains the source code for my
[webpage](https://stefanappelhoff.com), published with the help of:

 - [Sphinx](https://www.sphinx-doc.org/en/master/)
 - [sphinx-bootstrap-theme](https://github.com/ryan-roemer/sphinx-bootstrap-theme)
 - [CircleCI](https://circleci.com/blog/deploying-documentation-to-github-pages-with-continuous-integration/) (link to build guide)
 - [GitHub Pages](https://pages.github.com/)

---

# info

GitHub user pages for some reason MUST be served from the `main` branch.
To acommodate this, the present repo uses the `gh-pages` branch as the
*default branch*, to be set in the GitHub options.
The `main` branch is an *orphan branch*, that the
[`gh-pages-npm`](https://www.npmjs.com/package/gh-pages) package pushes
the HTML files to.

A `.nojekyll` and a `CNAME` file are created using the [githubpages](https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html)
sphinx extension.

Switching on the *force HTTPS* option in the GitHub settings was also crucial
for making the website work.

Also, not every combination of URL works :shrug:

| Link                                                         | does not work |
| :----------------------------------------------------------: | :-----------: |
| [https://sappelhoff.github.io](https://sappelhoff.github.io) |               |
| [http://sappelhoff.github.io](http://sappelhoff.github.io)   |               |
| [sappelhoff.github.io](sappelhoff.github.io)                 | x             |
| [https://stefanappelhoff.com](https://stefanappelhoff.com)   |               |
| [http://stefanappelhoff.com](http://stefanappelhoff.com)     |               |
| [stefanappelhoff.com](stefanappelhoff.com)                   | x             |
