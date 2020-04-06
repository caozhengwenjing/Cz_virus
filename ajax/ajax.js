var http = require('http');
var url = require('url');
var querystring = require('querystring');
http.createServer(function(req,res){
    res.setHeader("Access-Control-Allow-Origin","*");
    res.writeHead(200,{"Content-Type":"text/plain;charset=UTF-8"});
    if(req.mehtod == 'GET'){
        var index = req.url.indexOf('?');
        var url = req.url.substring(index+1);
        var str = querystring.parse(url);
        if(str.uname == 'tom' && str.pwd == '123'){
            res.end('欢迎您:'+ str.uname);
        }else{
            res.end('用户名不正确密码错误');
        }
    }else if(req.method == 'POST'){
        var urlStr = '';
        req.on('data',function(data){
            // console.log(data);
            // <Buffer 75 6e 61 6d 65 3d 74 6f 6d 26 70 77 64 3d 31 32 33>
            urlStr += data;
            // console.log(urlStr);
        });
        req.on('end',function(){
            // console.log(urlStr);
            var postUrlJson = querystring.parse(urlStr);
            // console.log(postUrlJson);
            if(postUrlJson.uname == 'tom' && postUrlJson.pwd == '123'){
                res.end('欢迎您:'+ postUrlJson.uname);
            }else{
                res.end('用户名不正确密码错误');
            }
        });
    }
    
}).listen(4003);