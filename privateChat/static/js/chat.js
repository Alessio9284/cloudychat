$(document).ready(function()
{
	//console.log("invio");

	var csrftoken = Cookies.get('csrftoken');

	function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});

	chat();

	var i = setInterval(chat(), 2500);

	//console.log("inviato");
});

$(document).on("click", "#invio", function()
{
	console.log("aggiunta del messaggio direttamente sulla pagina");

	var o = new Date();

	var date =
	o.getDate()+"/"+(o.getMonth()+1)+"/"+o.getFullYear()+" "+o.getHours()+":"+o.getMinutes()+":"+o.getSeconds();

	$.ajax(
	{
		type: "POST",
		url: "../../message/",
		data:
		{
			message : $("#messaggio").val(),
			date : date,
			to : nickname
		},
		success: function(data)
		{
			//console.log(data);
			var json = JSON.parse(data);
			//console.log(json);
		},
		error: function(a, b, error)
		{
			//alert("AJAX ERROR");
		}
	});

	$("#messaggio").val("");
});

function chat()
{
	$.ajax(
	{
		type: "POST",
		url: "../../update/" + nickname + "/",
		success: function(data)
		{
			//console.log(data);
			var json = JSON.parse(data);
			//console.log(json);

			$("#scritte").html("");

			for(var i = 0; i < json.length; i++)
			{
				$("#scritte").append(
					"<p>" + json[i].fields.text + "</p>" +
					"<p style='font-size: 10px;'>" + json[i].fields.date +
					"<span>&nbspby " + json[i].fields.io + "</span></p>"
				);
			}
		},
		error: function(a, b, error)
		{
			//alert("AJAX ERROR");
		},
	});
}