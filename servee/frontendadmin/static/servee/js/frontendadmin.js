$(document).ready(function(){
	$('a.frontendadmin_edit').hover(
	    function(){$(this).parent().css('outline', '4px solid #eeeeee');},
	    function(){$(this).parent().css('outline', '');}
	);
	$('a.frontendadmin_delete').hover(
	    function(){$(this).parent().css('outline', '4px solid #8C1717');},
	    function(){$(this).parent().css('outline', '');}
	);
	
	
	
	$('a.frontendadmin_add').click(function(){
		var $base, $par = $(this).parent();
	    $par.css('outline', '');
	    $.ajax({
	        url: this.href,
	        success: function(data, text){
	            $par.html(data);
	            $base = $par.find("form.frontendadmin");
	            load_wysiwyg($base);
	        }
	    });
	    return false;
	});
	
	
	$('a.frontendadmin_edit').click(function(){
		var $base, $par = $(this).parent();
	    $par.css('outline', '');
	    $.ajax({
	        url: this.href,
	        success: function(data, text){
	            $par.html(data);
	            $base = $par.find("form.frontendadmin");
	            load_wysiwyg($base);
	        }
	    });
	    return false;
	});
});