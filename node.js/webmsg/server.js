//The built-in http module provides HTTP service level and client function.
var http = require('http');
var fs = require('fs');
//The built-in pathmodule provides file system path correlation function.
var path = require('path');
var mime = require('mime');
var cache = {};

//Send the file does not exist information.
function send404(response){
	response.writeHead(404, {'Content-Type': 'text/plain'});
	response.write('Error 404:resource not found.');
	response.end();
}

//Send file stream.
function sendFile(response, filePath, fileContents){
	response.writeHead(
		200,
		{"content-type": mime.lookup(path.basename(filePath))}
	);
	response.end(fileContents);
}

//Provide static file service.
function serveStatic(response, cache, absPath){
	//Check if the file exists.
	if(cache[absPath]){
		//Returns a file from memory
		sendFile(response, absPath, cache[absPath]);
	}else{
		fs.exists(absPath, function(exists){
			//Read files from hard disk.
			if(exists){
			  fs.readFile(absPath, function(err, data){
				if(err){
					send404(response);
				}else{
					cache[absPath] = data;
					//Read and returns files from hard disk.
					sendFile(response, absPath, data);
				}
		      });
		}else{
			//Send HTTP 404 error
			send404(response);
		}
	 });
  }
}

//Create HTTP Server
var server = http.createServer(function(request, response){
	var filePath = false;

	if(request.url == '/'){
		filePath = 'public/index.html';
	}else{
		filePath = 'public' + request.url;
	}
	var absPath = './' + filePath;
	serveStatic(response, cache, absPath);
});



//Start server
server.listen(3000,function(){
	console.log("Server listening on port 3000.");
});

var chatServer = require('./lib/chat_server');
chatServer.listen(server);
