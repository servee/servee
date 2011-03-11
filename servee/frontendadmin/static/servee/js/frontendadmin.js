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

	/**************************
	 * Insert Tools 
	 **************************/
	// Clicking of 1st tier, building of 2nd tier
	$(".srv_mediaList li a").live("click", function(e){
		$.ajax({
            url: $(this).attr("href"),
            success: function(data, text){
                console.log(data);
                $(".srv_mediaList").after(data);
                srv_show_adminBox('srv_insertMedia');
            }
        });
		e.preventDefault();
		return false;
	});
	
	// Clicking of 2nd tier, building of 3rd tier
	$(".srv_filePane li a").live("click", function(e){
		$.ajax({
            url: $(this).attr("href"),
            success: function(data, text){
                console.log(data);
                $(".srv_filePane").after(data);
                srv_show_adminBox('srv_insertMedia');
            }
        });
		e.preventDefault();
		return false;
	});
	
});
