---
permalink: /
title: "Toby Jia-Jun Li is a Ph.D. Student in Human-Computer Interaction at Carnegie Mellon University"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Toby has research interests in human-computer interaction, intelligent user interface, end-user programming, conversational machine learning, and multi-modal mixed-initiative interfaces. His advisor is [Brad A. Myers](http://www.cs.cmu.edu/~bam/). He also works closely with [Tom M. Mitchell](http://www.cs.cmu.edu/~tom/). His research focuses on designing, implementing, and studying new interaction techniques, multi-modal interfaces, dialog systems, and the underlying AI techniques to empower intelligent agents to interactively learn new tasks and concepts from end users.

Toby has published in premier academic venues across HCI, NLP, systems, and software engineering (e.g., CHI, UIST, CSCW, ACL, MobiSys, VL/HCC), including two award-winning papers. Toby’s work is supported by a Yahoo! Fellowship through the [InMind project](http://www.cmu.edu/homepage/computing/2014/winter/project-inmind.shtml), by [J.P. Morgan](https://www.jpmorgan.com/global/technology/artificial-intelligence/awards), and by [NSF](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1814472&HistoricalAwards=false).



News
======
Like many other Jekyll-based GitHub Pages templates, academicpages makes you separate the website's content from its form. The content & metadata of your website are in structured markdown files, while various other files constitute the theme, specifying how to transform that content & metadata into HTML pages. You keep these various markdown (.md), YAML (.yml), HTML, and CSS files in a public GitHub repository. Each time you commit and push an update to the repository, the [GitHub pages](https://pages.github.com/) service creates static HTML pages based on these files, which are hosted on GitHub's servers free of charge.

Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. You can also modify the theme to your heart's content without touching the content of your site. If you get to a point where you've broken something in Jekyll/HTML/CSS beyond repair, your markdown files describing your talks, publications, etc. are safe. You can rollback the changes or even delete the repository and start over -- just be sure to save the markdown files! Finally, you can also write scripts that process the structured data on the site, such as [this one](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb) that analyzes metadata in pages about talks to display [a map of every location you've given a talk](https://academicpages.github.io/talkmap.html).

Publications
======
{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
