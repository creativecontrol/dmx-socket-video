var io = require('socket.io').listen(8000);

console.log("started");

io.sockets.on("connection", function(socket){

	socket.on('handshake', function(data){
		socket.emit('vid', {'vid':"Green"});
	});
	
	socket.on('blackout', function(data){
		socket.emit('vid', {'vid':"Black"});
	});

	socket.on('howdy',function(data){
		console.log(data);	//just check when you arrive to the party
	});
	
	socket.on('dmx', function(data){
		console.log(data);
		//forward on messages from python to chrome
		io.sockets.emit('vid',data);
	});
});
