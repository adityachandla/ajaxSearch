$(function(){
	$('#searchInput').focus(function(){
		$.ajax({
			url:'/search',
			data: {'value':''},
			success: function(data){
				$('#searchResult').html(data);
				$('#searchResult .card').fadeOut(0);
				$('#searchResult .card').each(function(index){
					$(this).delay(index*200).fadeIn(1000);
				})
			}
		});
	});
	$("#searchInput").keyup(function(){
		var val = $("#searchInput").val();
		$.ajax({
			url:'/search',
			data: {'value':val},
			success: function(data){
				$('#searchResult').html(data);
				$('#searchResult .card').fadeToggle(0);
				$('#searchResult .card').each(function(index){
					$(this).delay(index*200).fadeToggle(1000);
				})
			}
		});
	});
});