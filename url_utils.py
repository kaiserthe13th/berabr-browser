import tldextract

def confUrl(url, urlstr, browser = "http://google.com/search?q=%s"):
	if url.scheme() == "" and (tldextract.extract(urlstr)[2] != "" and tldextract.extract(urlstr)[1] != "" and tldextract.extract(urlstr)[0] == ""): 
		# set url scheme to http 
		urlstr = "http:%s" % urlstr
	elif url.scheme() != "" and tldextract.extract(urlstr)[2] != "":
		return urlstr
	else:
		# search in browser
		urlstr = browser % urlstr
	return urlstr
