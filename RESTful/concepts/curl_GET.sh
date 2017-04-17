curl -X GET \
	-i -H "Accept: application/json" -H "Content-Type: application/json" \
	'https://en.wikipedia.org/w/api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json'
