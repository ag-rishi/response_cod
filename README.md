# response_code

Uses the Python requests module. <br />

Goes through a list of URLs that you have in a text file, and reads them one-by-one. <br />
Then tries to access the URL and prints out the HTTP response code (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status). <br />
Prints out "failed to connect" if it cannot connect to the URL at all. <br />
<br />
This script is useful, for instance, if you have a list of websites and you want to find out which websites are still accessible and which ones are not. 
