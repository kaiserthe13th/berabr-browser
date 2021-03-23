import tldextract

# domainexts = [
# 	".com", ".net", ".org", ".dev", ".app", ".inc", ".website", ".xyz", ".club",
# 	".online", ".info", ".store", ".best", ".live", ".tech", ".pro", ".world",
# 	".space",".vip", ".life", ".shop", ".host", ".fun", ".biz", ".icu", ".design",
# 	".art", ".accountant", ".accountant", ".accountants", ".actor", ".adult",
# 	".ae.org", ".africa", ".agency", ".airforce", ".apartments", ".army", "asia",
# 	".associates", ".attorney", ".auction", ".audio", ".auto", ".baby", ".band",
# 	".bar", ".bargains", ".beauty", ".beer", ".berlin", ".bid", ".bike", ".bingo",
# 	".bio", ".black", ".blackfriday", ".blog", ".blue", ".bond", ".boston", ".boutique",
# 	".br.com", ".build", ".builders", ".business", ".buzz", ".cab", ".cafe", ".cam",
# 	".camera", ".camp", ".capital", ".car", ".cards", ".care", ".careers", ".cars", ".casa",
# 	".cash", ".casino", ".catering", ".center", ".ceo", ".chat", ".cheap", ".christmas",
# 	".church", ".city", ".claims", ".cleaning", ".click", ".clinic", ".clothing", ".cloud",
# 	".cn.com", ".co.com", ".coach", ".codes", ".coffee", ".college", ".com.de", ".com.se",
# 	".community", ".company", ".computer", ".condos", ".construction", ".consulting",
# 	".contact", ".contractors", ".cooking", ".cool", ".country", ".coupons", ".courses",
# 	".credit", ".creditcard", ".cricket", ".cruises", ".cymru", ".cyou", ".dance", ".date",
# 	".dating", ".deals", ".degree", ".delivery", ".democrat", ".dental", ".dentist", ".desi",
# 	".diamonds", ".diet", ".digital", ".direct" ,".directory", ".discount", ".doctor", ".dog",
# 	".domains", ".download", ".earth", ".eco", ".education", ".email", ".energy", ".engineer",
# 	".engineering", ".enterprises", ".equipment", ".estate", ".eu.com", ".events", ".exchange",
# 	".expert", ".exposed", ".express", ".fail", ".faith", ".family", ".fans", ".farm",
# 	".fashion", ".feedback", ".film", ".finance", ".financial", ".fish", ".fishing", ".fit",
# 	".fitness", ".flights", ".florist", ".flowers", ".football", .".forsale", ".forum",
# 	".foundation", ".fund", ".furniture", ".futbol", ".fyi", ".gallery", ".game", ".games",
# 	".garden", ".gay", ".gb.net", ".gdn", ".gift", ".gifts", ".gives", ".glass", ".global",
# 	".gmbh", ".gold", ".golf", ".gr.com", ".graphics", ".gratis", ".green", ".gripe",
# 	".group", ".guide", ".guitars", ".guru", ".hair", ".hamburg", ".haus", ".health",
# 	".healthcare", ".help", ".hiphop", ".hockey", ".holdings", ".holiday", ".horse",
# 	".hosting", ".house", ".how", ".hu.net", ".immo", ".immobilien", "in.net",
# 	".industries", ".ink", ".institute", ".insure", ".international", ".investments",
# 	".irish", ".jetzt", "."
# ]

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
