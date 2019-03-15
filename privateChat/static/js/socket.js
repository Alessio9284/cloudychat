var webSocket   = null;

function onDisconnectClick()
{
	webSocket.close();
}

function onConnectClick()
{
	var webSocketURL = "ws://127.0.0.1:5000/WebSocketServer/echo";
	console.log("openWSConnection::Connecting to: " + webSocketURL);
	try
	{
		webSocket = new WebSocket(webSocketURL);
		webSocket.onopen = function(openEvent)
		{
			console.log("WebSocket OPEN: " + JSON.stringify(openEvent, null, 4));
			document.getElementById("btnSend").disabled       = false;
			document.getElementById("btnConnect").disabled    = true;
			document.getElementById("btnDisconnect").disabled = false;
		};
		webSocket.onclose = function (closeEvent)
		{
			console.log("WebSocket CLOSE: " + JSON.stringify(closeEvent, null, 4));
			document.getElementById("btnSend").disabled       = true;
			document.getElementById("btnConnect").disabled    = false;
			document.getElementById("btnDisconnect").disabled = true;
		};
		webSocket.onerror = function (errorEvent)
		{
			console.log("WebSocket ERROR: " + JSON.stringify(errorEvent, null, 4));
		};
		webSocket.onmessage = function (messageEvent)
		{
			var wsMsg = messageEvent.data;
			console.log("WebSocket MESSAGE: " + wsMsg);
			if (wsMsg.indexOf("error") > 0)
			{
				document.getElementById("incomingMsgOutput").value += "error: " + wsMsg.error + "\r\n";
			}
			else
			{
				document.getElementById("incomingMsgOutput").value += "message: " + wsMsg + "\r\n";
			}
		};
	}
	catch (exception)
	{
		console.error(exception);
	}
}

function onSendClick()
{
	if (webSocket.readyState != WebSocket.OPEN)
	{
		console.error("webSocket is not open: " + webSocket.readyState);
		return;
	}
	var msg = document.getElementById("message").value;
	webSocket.send(msg);
}