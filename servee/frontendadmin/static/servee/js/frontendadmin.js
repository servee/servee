$(document).ready(function(){
	
	/* Frontendadmin buttons add, edit, delete */
	$("a.frontendadmin_edit:not(.modal)").hover(
	    function(){$(this).parent().addClass("pre-edit");},
	    function(){$(this).parent().removeClass("pre-edit");}
	);
	$("a.frontendadmin_delete:not(.modal)").hover(
	    function(){$(this).parent().addClass("pre-delete");},
	    function(){$(this).parent().removeClass("pre-delete");}
	);
	

	$("a.frontendadmin_add").live("click", function(e){
		var $base, $link = $(this), $par = $link.parent();

	    $.ajax({
	        url: this.href,
	        success: function(data, text){
	            if ($link.hasClass("modal")){
	                $.fancybox({
	                    content: data,
	                });
	            }
	            else {
    	            $par.html(data);	                
	            }
	        }
	    });
	    e.preventDefault();
	    return false;
	});


	$("a.frontendadmin_edit").live("click", function(e){
		var $base, $link = $(this), $par = $link.parent();

	    $par.css("outline", "");
	    $.ajax({
	        url: this.href,
	        success: function(data, text){
	            if ($link.hasClass("modal")){
	                $.fancybox({
	                    content: data,
	                });
	            }
	            else {
    	            $par.html(data);	                
	            }
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
                console.log(data);
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
	/*---- sticky submit-box ----*/

$(document).ready(function(){


	$(window).scroll(function(){
		if  ($(window).scrollTop() > $(".submit-box").offset({ scroll: false }).top){
		   $(".submit-box").css("position", "fixed");
		   $(".submit-box").css("bottom", "0");
		}
		
		if  ($(window).scrollTop() <= $(".submit-box").offset({ scroll: false }).top){
		   $(".submit-box").css("position", "relative");
		   $(".submit-box").css("bottom", $(".smartBannerIdentifier").offset);
		}
	}); 


});
