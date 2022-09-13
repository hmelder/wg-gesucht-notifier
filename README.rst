===============================
WG Gesucht Crawler: Updated for 2022
===============================


Python web crawler / scraper for WG-Gesucht. Crawls the WG-Gesucht site for new apartment listings and send a message to the poster, based off your saved filters and saved text template.

I updated and field tested for use in 2022
------------------------------------------

* I tweaked the message frequency and oldest offer creation date to reflect my experience of avoiding re-CAPTCHA.
* Updated the useragent to a newer Chrome version.
* Fixed the exception mechanism in get_page.
* Implemented a new cookie authentication mechanism, and deprecated the old one.
* Add a macro in the message template that replaces `{{greeting}}` with a formal or informal greeting depending on the name of the submitter.
* Add email templates for formal and informal messages.
* Fixed exception handling
* Updated all dependencies to their latest version.
* Skip all ads with submitter names beginning with "Corps" :)

Good luck finding your perfect rent offer.

Original repository by `Grant Williams <https://github.com/grantwilliams>`_.


Features
--------

* Automatically searches https://wg-gesucht.de for new WG ads based off your saved filters
* Sends your saved template message and applies to all matching listings
* Reruns every ~3 minutes
* Run on a RPi or free EC2 micro instance 24/7 to always be one of the first to apply for new listings




Installation
------------
::

    $ pip install wg-gesucht-crawler-cli

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv wg-gesucht-crawler-cli
    $ pip install wg-gesucht-crawler-cli

Use
---

1. First, log into your account on https://wg-gesucht.de. Navigate to :code:`"My WG Gesucht > Filters & email alerts"` and create a filter for your search (i.e. price and location). Navigate to :code:`"My WG Gesucht > Message templates"` and add a message template to send to filtered offers. Enter a simple title for both your title and message template; these fields are not be displayed publicly, they are only for your own reference.

2. Run from the command line::

    $ wg-gesucht-crawler-cli --filter-names="FILTER_TITLE" --template="MESSAGE_TEMPLATE_TITLE"
    
3. On the first launch, you will be prompted to enter wg-gesucht.de login details (e-mail and password). The script will then create a directory under :code:`/home/YOUR_NAME/Documents/WG Finder/` to save crawled webpages. The entered credentials are saved under :code:`/home/YOUR_NAME/Documents/WG Finder/.user/.login_info.json`.


4. If you logged in successfully and entered correct filter and message title, the crawler will start automatically replying to offers.

**Getting caught and avoiding re-CAPTCHA**
::

The crawler does get caught by re-CAPTCHA and occasionally you will have to sign into your WG-Gesucht account manually through the browser and solve the re-CAPTCHA, then start the crawler again.

*  Crawler takes random 5-8 second breaks between each action.
*  After finishing a crawl, crawler goes to sleep for 2-3 minutes. (Down from ~5 to ensure you are the #1 responder).
*  The one action that caused the crawler to get caught the most was responding to a high number of older offers. I edited the crawler only responds to offers added today and yesterday. (Edited from "2 days ago")
*  If you are running the crawler on a remote instance, from my experience, **re-CAPTCHA only on requests coming from the IP of the remote instance**. The simplest way to solve it on this IP, `is to connect to the remote through another terminal and set up a SOCKS5 proxy <https://linuxize.com/post/how-to-setup-ssh-socks-tunnel-for-private-browsing/>`_
*  If the crawler continues to gets stuck and you want to tweak it manually, you can edit :code:`search()` and its methods in file :code:`wg_gesucht/crawler.py`.
*  In my experience, waiting did not help to remove re-CAPTCHA; after it was triggered it had to be solved.
::

Unfortunately, rent offers in bigger cities like Munich often have **hundreds** of hits in the first minutes. Your best bet is to keep the script running for a week or so and be amongst the first 10 responders on as many offers as you can; I would argue this is better than responding to older offers. After a few re-runs, you should have cleared up all of the current offers


**Including in your own project**

.. code-block:: python

    from wg_gesucht.crawler import WgGesuchtCrawler


* Free software: MIT license
* Documentation: https://wg-gesucht-crawler-cli.readthedocs.org.
