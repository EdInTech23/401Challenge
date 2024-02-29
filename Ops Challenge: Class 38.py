def check_xss(url):
    # test payload
    payload = "<script>document.write('uniqueString')</script>"
    
     params = {'param1': payload}
    # Sending a GET request with the payload. 
    response = requests.get(url, params=params)
    # Using BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Check if the payload is reflected 
    if payload.strip('<script></script>') in soup.text:
        print(f"Potential XSS vulnerability detected in {url}")
    else:
        print(f"No XSS vulnerability detected in {url}")

# uRLs to test
check_xss("https://xss-game.appspot.com/level1/frame")
check_xss("http://dvwa.local/login.php")
