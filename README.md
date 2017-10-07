# bulk_onion_link_classifier
Filter out the working TOR URLs from a long list of possible TOR URLs. By default it saves the woring links and thier corresponding page titles in a file named output.csv



Dependencies:

* Beautiful Soup [ For extracting the page title]
* requests [for making the http calls]
* TOR Browser Installed and Running
* A list of newline delimited TOR URLs



To install the dependencies:

`pip install -r requirements.txt`

or

```
pip install requests
pip install bs4
```



Usages:

Modify the `domain_list` and `output_file` varibles in the `onion_classifier.py` file according to your needs.

Check if the SOCKS5 Proxy port matches with the one stated in the TOR Browser Settings.

[ Located at Preferences >> Advanced>> Network>> Settings >>Manual Proxy Configuration>>SOCKS PORT]



To run it locally:

* `git clone https://github.com/amanaryan/bulk_onion_link_classifier.git`
* `cd bulk_onion_link_classifier`
* `python onion_classifier.py`