What happens when you press enter and a webpage pops up

1. You type maps.google.com into the address bar of your browser

2. Browser checks the cache for a DNS (domain name server) record to find corresponding IP address of maps.google.com. DNS is a list of URLs and their IP address just like how a phone book is a list of names and their corresponding phones numbers. DNS makes accessing webpages human friendly. DNS checks 4 caches: browser, browser checks OS cache, browser checks router cache, last it checks ISP cache.
 3. If the requested URL is not in the cache, ISP’s DNS server initiated a DNS query to find the IP address of the server that hosts the particular webpage you’re trying to access. This is called a recursive search. Root domains > top-level domains > second level domains > third level domains. These requests are sent using small data packets which contain information such as the content of the request and the IP address it is destined for. They travel through multiple networking equipment between the client and the server.
4. Browser initiatives a TCP connection with the server. There are many internet protocols but TCP is by far the most common