$(document).ready(function(){
	
	/* Frontendadmin buttons add, edit, delete */
	$("a.frontendadmin_edit:not(.modal)").hover(		
		function(){
	    	var $base, $link = $(this), $par = $link.parent();
    	
	        if ((typeof(servee) != "undefined") && (typeof(servee.selector) != "undefined")){
    		    $par = $(servee.selector);
    		}
    		else {
    		    $par = $link.parent();
    		}
    		$par.addClass("pre-edit");
    	},
	    function(){
	    	var $base, $link = $(this), $par = $link.parent();
    	
	        if ((typeof(servee) != "undefined") && (typeof(servee.selector) != "undefined")){
    		    $par = $(servee.selector);
    		}
    		else {
    		    $par = $link.parent();
    		}
    		$par.removeClass("pre-edit");
    	}
	);
	$("a.frontendadmin_delete:not(.modal)").hover(
	    function(){
	    	var $base, $link = $(this), $par = $link.parent();
    	
    	    if ((typeof(servee) != "undefined") && (typeof(servee.selector) != "undefined")){
    		    $par = $(servee.selector);
    		}
    		else {
    		    $par = $link.parent();
    		}
    		$par.addClass("pre-delete");
    	},
	    function(){
	    	var $base, $link = $(this), $par = $link.parent();
    	
	        if ((typeof(servee) != "undefined") && (typeof(servee.selector) != "undefined")){
    		    $par = $(servee.selector);
    		}
    		else {
    		    $par = $link.parent();
    		}
    		$par.removeClass("pre-delete");
    	}
	);
	

	$("a.frontendadmin_add").live("click", function(e){
		var $base, $link = $(this);
		
		if ((typeof(servee) != "undefined") && (typeof(servee.selector) != "undefined")){
		    $par = $(servee.selector);
		}
		else {
		    $par = $link.parent();
		}

	    $.ajax({
	        url: this.href,
	        success: function(data, text){
    	        $par.html(data);
	        }
	    });
	    e.preventDefault();
	    return false;
	});
	

	$("a.frontendadmin_list").live("click", function(e){
		var $base, $link = $(this);
		
		if ((typeof(servee) != "undefined") && (typeof(servee.selector) != "undefined")){
		    $par = $(servee.selector);
		}
		else {
		    $par = $link.parent();
		}

	    $.ajax({
	        url: this.href,
	        success: function(data, text){
    	        $par.html(data);
	        }
	    });
	    e.preventDefault();
	    return false;
	});


	$("a.frontendadmin_edit").live("click", function(e){
		var $base, $link = $(this), $par = $link.parent();

        if ((typeof(servee) != "undefined") && (typeof(servee.selector) != "undefined")){
		    $par = $(servee.selector);
		}
		else {
		    $par = $link.parent();
		}

	    $par.css("outline", "");
	    $.ajax({
	        url: this.href,
	        success: function(data, text){
	            $par.html(data);
	        }
	    });
	    e.preventDefault();
	    return false;
	});

	/**************************
	 * Insert Tools 
	 **************************/
	// Clicking of 1st tier, building of 2nd tier
	$(".srv_mediaList li a").live("click", function(e){
		var $link = $(this);
	
	
		//@@ TODO currentInsert is a global object.  This is lame,
		//servee should have only one global object.
		currentInsert = $link.attr("data-slug");
	
		$.ajax({
            url: $link.attr("href"),
            success: function(data, text){
                console.log(data);
                $(".srv_filePane").remove();
                $(".srv_insertOptions").remove();
                $(".srv_mediaList").after(
                    "<div id='srv_"+currentInsert+"_filePane' class='srv_filePane'>"
                    + data
                    + "</div>"
                );
                //Once the dom is rebuilt, slide it in.
                srv_show_adminBox("srv_insertMedia");
            }
        });
		e.preventDefault();
		return false;
	});

	// Clicking of 2nd tier, building of 3rd tier
	$(".srv_filePane li a").live("click", function(e){
		var $link = $(this);
		$.ajax({
            url: $link.attr("href"),
            success: function(data, text){
                $(".srv_insertOptions").remove();
                $(".srv_filePane").after(
                    "<div id='srv_"+ currentInsert +"_insertOptions' class='srv_insertOptions'>"
                    + data
                    + "</div>"
                );
                //Once the dom is rebuilt, slide it in.
                srv_show_adminBox("srv_insertMedia");
            }
        });
		e.preventDefault();
		return false;
	});

});
