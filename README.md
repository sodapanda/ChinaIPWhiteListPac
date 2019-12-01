# ChinaIPWhiteListPac

基于ipip.net数据库的中国大陆IP段白名单PAC。
使用方法：
将本地socks5代理端口绑定到1080端口。
将PAC地址设置为 https://raw.githubusercontent.com/sodapanda/ChinaIPWhiteListPac/master/IPWhiteListPac.js
DNS污染问题请自行解决。例如使用DoH，可将DNS地址设置为 https://www.233py.com/#dnsservice 的香港地址，具体方法请自行查找。若DNS污染未解决，请不要使用该PAC。

访问大陆IP不走代理直连，国外IP则通过代理连接。