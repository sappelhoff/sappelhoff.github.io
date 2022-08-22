[![Build and Deploy](https://github.com/sappelhoff/sappelhoff.github.io/actions/workflows/build_and_deploy.yml/badge.svg)](https://github.com/sappelhoff/sappelhoff.github.io/actions/workflows/build_and_deploy.yml)

This repository contains the source code for my
[webpage](https://stefanappelhoff.com), published with the help of:

 - [Sphinx](https://www.sphinx-doc.org/en/master/)
 - [sphinx-bootstrap-theme](https://github.com/ryan-roemer/sphinx-bootstrap-theme)
 - [A "GitHub Action" by JamesIves](https://github.com/JamesIves/github-pages-deploy-action)
 - [GitHub Pages](https://pages.github.com/)

---

# Info

The source of the page is on the `main` branch.
The html files are build from that source and pushed to the `gh-pages` branch,
from where they are deployed.

A `.nojekyll` and a `CNAME` file are created using the [githubpages](https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html)
Sphinx extension.

Switching on the *force HTTPS* option in the GitHub settings was also crucial
for making the website work.
